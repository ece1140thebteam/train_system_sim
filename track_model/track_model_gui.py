import sys
from tkinter import N

from PyQt5.QtGui import QGuiApplication, QStandardItem, QStandardItemModel
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, Qt, QModelIndex, QAbstractItemModel, pyqtProperty, pyqtSlot

import Track
import TrackBlock
import csv
import pprint
import re

class Gvars():
    track           = Track.Track()
    default_track   = 'default.csv'

LineRole = Qt.UserRole + 1000
SectionRole = Qt.UserRole + 1001
BlockRole = Qt.UserRole + 1002

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
    def clear_lines(self):
        self.model.clear()

def parse_default_track():
    with open(Gvars.default_track) as csvfile:
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



parse_default_track()

manager = LineListManager()

for line in Gvars.track.track_lines:
    for section in Gvars.track.track_lines[line].sections:
        for block_num in Gvars.track.track_lines[line].sections[section]:
            print(f'{line} {section} {block_num}')
            Gvars.track.track_lines[line].blocks[block_num].print()

            manager.add_block(Gvars.track.track_lines[line].blocks[block_num])

app = QGuiApplication(sys.argv)

t = Track.Track()

engine = QQmlApplicationEngine()
engine.rootContext().setContextProperty("line_list_manager", manager)

engine.quit.connect(app.quit)
engine.load('./main.qml')

sys.exit(app.exec())