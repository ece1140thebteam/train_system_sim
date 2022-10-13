from ast import parse
import sys
from tkinter import N

from PyQt5.QtGui import QGuiApplication, QStandardItem, QStandardItemModel, QIcon
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, Qt, QModelIndex, QAbstractItemModel, pyqtProperty, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QApplication

import Track
import TrackBlock
import csv
import re
import os


LineRole = Qt.UserRole + 1000
SectionRole = Qt.UserRole + 1001
BlockRole = Qt.UserRole + 1002

BlockInfoTitleRole = Qt.UserRole + 1003
BlockInfoDetailRole = Qt.UserRole + 1004

class Gvars():
    track               = Track.Track()
    track_file          = 'default.csv'
    track_file_binding  = None
    block_list_manager  = None
    block_info_manager  = None
    function_bindings   = None
    displayed_block     = None

def parse_track():
    print(Gvars.track_file)
    with open(Gvars.track_file) as csvfile:
        print('opened')
        reader = csv.reader(csvfile, delimiter=',')
        headers = next(reader, None)
        
        for block in reader:
            line = block[0]
            infra = block[6]

            inf_arr = infra.split(';')
            station = None
            underground = False
            switch = None
            railway_crossing = False
            block_travels_to = []
            
            for i in inf_arr:
                if 'RAILWAY' in i:
                    railway_crossing = True
                elif 'UNDERGROUND' in i:
                    underground = True
                elif 'Station' in i:
                    station = i
                elif 'Switch' in i:
                    # find all switch connections
                    all = [int(x) for x in re.findall(r'\d+', i.lower().replace('yard', '0'))]
                    if len(all) > 2:
                        start = int(max(set(all), key = all.count))
                        print
                        # to = [x for i, x in enumerate(all) if i!=start]
                        to = [x for x in all if x != start]
                        Gvars.track.add_switch(line, start, to)

            connections = block[10]
            connections = connections.split(';')

            # set switch connections within the block
            for c in connections:
                if '*' in c:
                    val = int(c.replace('*',''))
                    if switch is None:
                        switch = [val]
                    else:
                        switch.append(val)
                    block_travels_to.append(val*-1)
                else:
                    block_travels_to.append(int(c))
                    # print(switch)
            
            b = TrackBlock.TrackBlock(
                line = line,
                section = block[1],
                block_number = block[2],
                block_len = block[3],
                block_grade = block[4],
                speed_limit = block[5],
                underground = underground,
                station = station,
                switch = switch,
                elevation = block[8],
                cum_elevation = block[9],
                has_rail_crossing = railway_crossing,
                can_travel_to = block_travels_to
            )

            # b.print()
            # print()

            Gvars.track.add_block(b)
    
    Gvars.track.print()

def fill_block_list():
    for line in Gvars.track.track_lines:
        for section in Gvars.track.track_lines[line].sections:
            for block_num in Gvars.track.track_lines[line].sections[section]:
                Gvars.block_list_manager.add_block(Gvars.track.track_lines[line].blocks[block_num])

def update_properties(engine):
    engine.rootContext().setContextProperty("line_list_manager", Gvars.block_list_manager)
    engine.rootContext().setContextProperty("track_file_binding", Gvars.track_file_binding)
    engine.rootContext().setContextProperty("displayed_block_manager", Gvars.block_info_manager)
    engine.rootContext().setContextProperty("function_bindings", Gvars.function_bindings)

def load_new_track():
    Gvars.track = Track.Track()
    Gvars.track_file_binding.text = Gvars.track_file.replace(os.getcwd(), '').replace('/', '').replace('\\','')
    Gvars.block_list_manager.clear_list()
    parse_track()
    fill_block_list()

def update_block_info():
    block = Gvars.displayed_block
    Gvars.block_info_manager.clear_list()

    Gvars.block_info_manager.add_info_line('Line', block.line)
    Gvars.block_info_manager.add_info_line('Section', block.section)
    Gvars.block_info_manager.add_info_line('Block Number', block.block_number)
    Gvars.block_info_manager.add_info_line('Length (ft)', str(round(block.block_len*3.28084, 2)))
    Gvars.block_info_manager.add_info_line('Grade (%)', block.block_grade)
    Gvars.block_info_manager.add_info_line('Speed Limit (mph)', str(round(block.speed_limit*0.621371,2)))
    Gvars.block_info_manager.add_info_line('Underground', 'Yes' if block.underground else 'No')
    Gvars.block_info_manager.add_info_line('Station', 'None' if block.station is None else block.station)
    Gvars.block_info_manager.add_info_line('Switch Position', "No switch" if block.switch_pos is None else str(block.switch_pos))
    Gvars.block_info_manager.add_info_line('Elevation (ft)', str(round(block.elevation*0.621371,2)))
    Gvars.block_info_manager.add_info_line('Cumulative Elevation (ft)', str(round(block.cum_elevation*0.621371,2)))

    crossing = 'Close'
    if not block.has_rail_crossing: crossing = "None"
    elif block.crossing_open: crossing = "Open"

    Gvars.block_info_manager.add_info_line('Crossing', crossing)
    Gvars.block_info_manager.add_info_line('Track Circuit', "Open" if block.circuit_open else "Closed")
    Gvars.block_info_manager.add_info_line('Signal', block.signal)
    Gvars.block_info_manager.add_info_line('Light', block.light)


class LineListManager(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.m_model = QStandardItemModel(self)

        roles = {LineRole: b"line", SectionRole: b"section", BlockRole: b"block"}

        self.m_model.setItemRoleNames(roles)

    @pyqtProperty(QObject, constant=True)
    def model(self):
        return self.m_model

    @pyqtSlot(float, float, float)
    def add_block(self, block):
        it = QStandardItem()
        it.setData(block.block_number, BlockRole)
        it.setData(block.line, LineRole)
        it.setData(block.section, SectionRole)
        self.model.appendRow(it)

    @pyqtSlot()
    def clear_list(self):
        self.model.clear()

class BlockInfoListManager(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.m_model = QStandardItemModel(self)

        roles = {BlockInfoTitleRole: b"title", BlockInfoDetailRole: b"detail"}

        self.m_model.setItemRoleNames(roles)

    @pyqtProperty(QObject, constant=True)
    def model(self):
        return self.m_model

    @pyqtSlot(str, str)
    def add_info_line(self, title, detail):
        it = QStandardItem()
        it.setData(title, BlockInfoTitleRole)
        it.setData(detail, BlockInfoDetailRole)
        self.model.appendRow(it)

    @pyqtSlot()
    def clear_list(self):
        self.model.clear()

class TextBinding(QObject):
    textChanged = pyqtSignal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self._text = ""

    @pyqtProperty(str, notify=textChanged)
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if self._text == value:
            return
        self._text = value
        self.textChanged.emit()

# class DisplayedBlockBinding(QObject):
#     blockChanged = pyqtSignal()

#     def __init__(self, parent=None):
#         QObject.__init__(self, parent)
#         self._block = None

#     @pyqtProperty(str, notify=blockChanged)
#     def block(self):
#         return self._block

#     @pyqtProperty(str, notify=blockChanged)
#     def line(self):
#         return self._block.line
    
#     @pyqtProperty(str, notify=blockChanged)
#     def section(self):
#         return self._block.section
    
#     @pyqtProperty(int, notify=blockChanged)
#     def block_number(self):
#         return self._block.block_number

#     @pyqtProperty(float, notify=blockChanged)
#     def len_ft(self):
#         return self._block.block_len*3.28084
    
#     @pyqtProperty(float, notify=blockChanged)
#     def grade(self):
#         return self._block.grade

#     @pyqtProperty(float, notify=blockChanged)
#     def speed_limit_mph(self):
#         return self._block.speed_limit*0.621371

#     @pyqtProperty(bool, notify=blockChanged)
#     def underground(self):
#         return self._block.underground
    
#     @pyqtProperty(str, notify=blockChanged)
#     def station(self):
#         return self._block.station

#     @pyqtProperty(str, notify=blockChanged)
#     def switch_pos(self):
#         return str(self._block.switch_pos) if self._block.switch_pos is not None else "No switch"

#     @pyqtProperty(float, notify=blockChanged)
#     def elevation_ft(self):
#         return self._block.elevation*0.621371

#     @pyqtProperty(bool, notify=blockChanged)
#     def has_rail_crossing(self):
#         return self._block.has_rail_crossing
    
#     @pyqtProperty(float, notify=blockChanged)
#     def cum_elevation_ft(self):
#         return self._block.cum_elevation*0.621371

#     @pyqtProperty(str, notify=blockChanged)
#     def crossing(self):
#         if not self._block.has_rail_crossing: return "None"
#         elif self._block.crossing_open: return "Open"
#         return "Closed"

#     @pyqtProperty(str, notify=blockChanged)
#     def circuit(self):
#         return "Open" if self._block.circuit_open else "Closed"
    
#     @pyqtProperty(str, notify=blockChanged)
#     def signal(self):
#         return self._block.signal

#     @pyqtProperty(str, notify=blockChanged)
#     def light(self):
#         return self._block.light

#     @block.setter
#     def block(self, block):
#         if self._block == block:
#             return
#         self._block = block
#         self.blockChanged.emit()

class QFunctions(QObject):
    def __init__(self):
        QObject.__init__(self)

    @pyqtSlot(str, int)
    def select_block(self, line, block_num):
        print(f'{line}: {block_num}')
        block = Gvars.track.track_lines[line].get_block(block_num)
        Gvars.displayed_block = block
        update_block_info()
        block.print()

    @pyqtSlot()
    def open_new_file(self):
        print('opening new file')
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.ExistingFile)
        # dlg.setFilter("csv(*.csv)")
        t = QFileDialog.getOpenFileName(dlg, "hello", os.getcwd(), "csv(*.csv)")
        Gvars.track_file = t[0]
        load_new_track()

def init_globals():
    # managers
    Gvars.track_file_binding  = TextBinding()
    Gvars.block_list_manager  = LineListManager()
    Gvars.block_info_manager  = BlockInfoListManager()
    Gvars.function_bindings   = QFunctions()

    Gvars.track_file_binding.text = Gvars.track_file


def main():
    init_globals()
    parse_track()

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("folder.png"))
    t = Track.Track()


    engine = QQmlApplicationEngine()
    update_properties(engine)
    fill_block_list()

    engine.quit.connect(app.quit)
    engine.load('./main.qml')

    sys.exit(app.exec())

    
if __name__ == "__main__":
    main()
