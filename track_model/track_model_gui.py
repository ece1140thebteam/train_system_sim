from ast import parse
from audioop import avg
from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE
import sys
from tkinter import N
from tracemalloc import start

from PyQt5.QtGui import QGuiApplication, QStandardItem, QStandardItemModel, QIcon
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, Qt, QModelIndex, QAbstractItemModel, pyqtProperty, pyqtSlot, pyqtSignal, QRunnable, QThreadPool, QThread
from PyQt5.QtWidgets import QFileDialog, QApplication

import Track
import TrackBlock
import csv
import re
import os
from os.path import exists
import datetime
import random
import time
import _md5

LineRole = Qt.UserRole + 1000
SectionRole = Qt.UserRole + 1001
BlockRole = Qt.UserRole + 1002

BlockInfoTitleRole = Qt.UserRole + 1003
BlockInfoDetailRole = Qt.UserRole + 1004
pittsburgh_weather = {
    1: 30,
    2: 32,
    3: 41,
    4: 53,
    5: 62,
    6: 70,
    7: 74,
    8: 73,
    9: 66,
    10: 54,
    11: 44,
    12: 29
}

class Gvars():
    track               = Track.Track()
    track_file          = 'blueline.csv'
    track_file_binding  = None
    block_list_manager  = None
    block_info_manager  = None
    function_bindings   = None
    displayed_block     = None
    temperature_f       = 30
    run_bkgd            = True
    bkgd_monitor        = None

def get_temperature():
    month = datetime.datetime.now().month
    hour = datetime.datetime.now().hour
    avg_month_temp = pittsburgh_weather[month]

    # assume it is hottest at 3:00pm, 15:00
    dev = int(1/abs(hour-15)*7)

    # random pittsburgh temperature based on month
    Gvars.temperature_f = random.randint(avg_month_temp-dev, avg_month_temp+dev)

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
    Gvars.block_list_manager.clear_list()

    with open('loaded_track', 'w') as f:
        f.write(Gvars.track_file)
    Gvars.track = Track.Track()
    Gvars.track_file_binding.text = Gvars.track_file.replace(os.getcwd(), '').replace('/', '').replace('\\','')
    Gvars.block_list_manager.clear_list()
    parse_track()
    fill_block_list()

def update_block_info():
    block = Gvars.displayed_block
    block.print()
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
    Gvars.block_info_manager.add_info_line('Track Heater', block.track_heater)
    Gvars.block_info_manager.add_info_line('Failure Mode', block.failure_mode)
    Gvars.block_info_manager.add_info_line('Maintenance Mode', block.maintenance_mode)

def create_failure(block, type):
    block.update_failure(type)

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
    blockChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.m_model = QStandardItemModel(self)

        roles = {BlockInfoTitleRole: b"title", BlockInfoDetailRole: b"detail"}

        self.m_model.setItemRoleNames(roles)

    @pyqtProperty(QObject, notify=blockChanged)
    def model(self):
        return self.m_model

    @pyqtSlot(str, str)
    def add_info_line(self, title, detail):
        it = QStandardItem()
        it.setData(title, BlockInfoTitleRole)
        it.setData(detail, BlockInfoDetailRole)
        self.model.appendRow(it)
        self.blockChanged.emit()

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

class QFunctions(QObject):
    def __init__(self):
        QObject.__init__(self)

    @pyqtSlot(str, int)
    def select_block(self, line, block_num):
        print(f'{line}: {block_num}')
        block = Gvars.track.track_lines[line].get_block(block_num)
        Gvars.displayed_block = block
        update_block_info()
        # block.print()

    @pyqtSlot()
    def open_new_file(self):
        print('opening new file')
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.ExistingFile)
        # dlg.setFilter("csv(*.csv)")
        t = QFileDialog.getOpenFileName(dlg, "hello", os.getcwd(), "csv(*.csv)")
        
        if exists(t[0]):
            Gvars.track_file = t[0]
            # notify others which track is loaded 
            load_new_track()

    @pyqtSlot(str)
    def create_failure(self, failure_type):
        print('creating failure')
        create_failure(Gvars.displayed_block, failure_type)
        update_block_info()

def init_globals():
    # managers
    Gvars.track_file_binding  = TextBinding()
    Gvars.block_list_manager  = LineListManager()
    Gvars.block_info_manager  = BlockInfoListManager()
    Gvars.function_bindings   = QFunctions()
    
    Gvars.track_file_binding.text = Gvars.track_file


def handle_communication():
    # try:
        with open('test_communications', 'r') as f:
            comm = f.read()
            array = comm.split(':')
            type = array[0]
            target = array[1]
            value = array[2]
            line = list(Gvars.track.track_lines.values())[0] # TODO update this 

            if type == "Authority":
                print(f'OUTPUT COMMUNICATION')
                print(f'Train {target} authority {float(value)*0.3048} m')
            elif type == "Commanded Speed":
                print(f'OUTPUT COMMUNICATION')
                print(f'Train {target} speed {value*1.60934} km/h')
            elif type == "Switch Position":
                print(f'updating switch position')
                if line.blocks.get_block(int(target)).update_switch_pos(int(value)):
                    print(f'updated switch position')
                else:
                    print('invalid switch position')

            elif type == "Railway Crossing":
                if line.get_block(int(target)).has_rail_crossing:
                    line.get_block(target).rail_crossing = value
                else:
                    print('error in railway submission')
            elif type == "Signal":
                line.get_block(int(target)).signal = value

            elif type == "Track Maintenance":
                line.set_maintenance_mode(value.lower()=="yes")

            elif type == "Track Heater":
                line.get_block(int(target)).track_heater = value
            elif type == "Track Failure":
                line.get_block(int(target)).track_failure = value

            elif type == "Lights":
                line.get_block(int(target)).light = value

            elif type == "Track Circuit":
                line.get_block(int(target)).circuit_open = value.lower()=='open'
        update_block_info()
        update_block_info()
    # except:
    #     print('error with update')


class BkgdMonitor(QObject):
    bkgd_info_update = pyqtSignal()

    @pyqtSlot()
    def monitor_images(self):
        # I'm guessing this is an infinite while loop that monitors files
        t = os.stat('test_communications')[8]
        while True:
            time.sleep(.2)
            if os.stat('test_communications')[8] != t:
                t = os.stat('test_communications')[8]
                handle_communication()
                print('file changed!')
                update_block_info()
                Gvars.block_info_manager.blockChanged.emit()

                


def main():
    init_globals()
    load_new_track()
    get_temperature()
    Gvars.bkgd_monitor = BkgdMonitor()


    Gvars.displayed_block = list(Gvars.track.track_lines.values())[0].get_block(1)
    update_block_info()

    app = QApplication(sys.argv)
    background_thread = QThread(app)
    Gvars.bkgd_monitor.moveToThread(background_thread)
    background_thread.started.connect(Gvars.bkgd_monitor.monitor_images)
    background_thread.start()

    app.setWindowIcon(QIcon("folder.png"))
    # using_runnable(app)

    t = Track.Track()


    engine = QQmlApplicationEngine()
    update_properties(engine)
    # fill_block_list()

    engine.quit.connect(app.quit)
    engine.load('./main.qml')

    sys.exit(app.exec())
    

    
if __name__ == "__main__":
    main()
