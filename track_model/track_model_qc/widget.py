# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import datetime
import random 
import time
import threading

from os.path import exists
from PyQt6.QtWidgets import QApplication, QWidget, QTreeWidgetItem, QFileDialog
from PyQt6.QtCore import QFile, Qt, QThread, pyqtSignal, QObject
from PyQt6.QtGui import QColor
from PyQt6 import uic
from . import Track
from . import TrackBlock
import re
import csv

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

run_thread = True

class HelperThread(QObject):
    change_color = pyqtSignal()

    def run(self):
        print('starting')
        self.change_color.emit()

class TrackModel(QWidget):
    default_track_file = 'default_track.csv'

    def __init__(self, track=None, parent=None):
        super().__init__(parent)
        self.load_ui()
        self.track = Track.Track()
        self.load_track(TrackModel.default_track_file)
        self.config_temp()
        self.blockTree = self.blockListTreeWidget
        self.uploadTrackButton.clicked.connect(self.open_new_file)

        # self.thread = QThread()
        # self.helper = HelperThread(parent=self)
        # self.helper.moveToThread(self.thread)
        # self.thread.started.connect(self.helper.run)
        # self.helper.change_color.connect(self.update_list_color)
        # # Step 6: Start the thread
        # self.thread.start()

        self.displayed_block = None
        

    def load_block_clicked_info(self, line, section, block):
        line = line.split(' ')[0]
        section = section.split(' ')[1]
        block = int(block.split(' ')[1])

        self.display_block_info(self.track.track_lines[line].blocks[block])

    def display_block_info(self, block=None):
        if block is not None:
            self.displayed_block = block

        block = self.displayed_block

        if block is None: return

        self.blockLineInfo.setText(block.line)
        self.blockNumberInfo.setText(str(block.block_number))
        self.blockSectionInfo.setText(block.section)
        self.blockGradeInfo.setText(str(block.block_grade))
        self.blockSpeedLimitInfo.setText(str(block.speed_limit))
        self.blockLengthInfo.setText(str(block.block_len))
        self.blockStationInfo.setText(block.station)
        self.blockTrackHeaterInfo.setText(block.track_heater)
        self.blockElevationInfo.setText(str(block.elevation))
        self.blockCumulativeElevationInfo.setText(str(block.cum_elevation))
        self.blockRailCrossingInfo.setText(str(block.crossing_open))
        self.blockUndergroundInfo.setText(str(block.underground))
        self.blockAuthorityInfo.setText(str(block.authority))
        self.blockMaintenanceModeInfo.setText(str(block.maintenance_mode))
        self.blockBeaconInfo.setText(str(block.beacon1))
        self.blockFailureModeInfo.setText(str(block.failure_mode))
        self.blockSwitchPositionInfo.setText(str(block.switch_pos))
        self.blockSwitchInfo.setText(str(block.switch))
        self.blockSignalInfo.setText(str(block.signal))
        self.blockTrackCircuitInfo.setText("Open" if block.circuit_open else "Closed")

    def block_list_item_clicked(self, item):
        # if this is a block
        if item.parent() is not None:
            if item.parent().parent() is not None:
                line    = item.parent().parent().text(0)
                section = item.parent().text(0)
                block   = item.text(0)
                self.load_block_clicked_info(line, section, block)

    def open_new_file(self):
        print('opening new file')
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.ExistingFile)
        # dlg.setFilter("csv(*.csv)")
        t = QFileDialog.getOpenFileName(dlg, "hello", os.getcwd(), "csv(*.csv)")
        
        if exists(t[0]):
            track_file = t[0]
            # notify others which track is loaded 
            self.load_track(track_file)

    def load_track(self, track_file):
        tracklines = dict()

        with open(track_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)

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
                            
                            # to = [x for i, x in enumerate(all) if i!=start]
                            to = [x for x in all if x != start]
                            self.track.add_switch(line, start, to)

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
                
                if line not in tracklines:
                    tracklines[line] = dict()
                if block[1] not in tracklines[line]:
                    tracklines[line][block[1]] = []
                if block[2] not in tracklines[line][block[1]]:
                    tracklines[line][block[1]].append(block[2])

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

                self.track.add_block(b)
        
        # parse for display
        items = []
        for line in tracklines:
            lineItem = QTreeWidgetItem([f'{line} line'])
            for section in tracklines[line]:
                sec = QTreeWidgetItem([f'Section {section}'])
                for block in tracklines[line][section]:
                    b = QTreeWidgetItem([f'Block {block}'])
                    sec.addChild(b)
                # sec.expandAll();
                lineItem.addChild(sec)
            items.append(lineItem)
        
        self.blockListTreeWidget.insertTopLevelItems(0, items)
        self.blockListTreeWidget.itemClicked.connect(self.block_list_item_clicked)
        self.blockListTreeWidget.expandAll()

        print(self.blockListTreeWidget)

    def config_temp(self):
        month = datetime.datetime.now().month
        hour = datetime.datetime.now().hour
        avg_month_temp = pittsburgh_weather[month]

        # assume it is hottest at 3:00pm, 15:00
        dev = int(1/abs(hour-15)*24)

        # random pittsburgh temperature based on month
        temp_f = random.randint(avg_month_temp-int(dev/2), avg_month_temp+int(dev/2))

        self.temperatureSpinBox.setValue(temp_f)
        self.temperatureSpinBox.valueChanged.connect(self.update_temp_spin_box)

    def update_temp_spin_box(self):
        if self.track.heater_on:
            if self.temperatureSpinBox.value() > 32:
                print('Turning heater off')
                self.track.turn_heater_off()
                self.display_block_info()

        else:
            if self.temperatureSpinBox.value() <= 32:
                print('Turning heater on')
                self.track.turn_heater_on()
                self.display_block_info()

    def load_ui(self):
#        loader = QUiLoader()
        path = str(Path(__file__).resolve().parent / "form.ui")
        # ui_file = QFile(path)
        # ui_file.open(QFile.ReadOnly)
        uic.loadUi(path, self)
        # ui_file.close()

    def update_list_color(self):
        print('updating')
        num_lines = self.blockListTreeWidget.invisibleRootItem().childCount()

        for line_num in range(0, num_lines):
            line = self.blockListTreeWidget.invisibleRootItem().child(line_num)
            num_sections = line.childCount()

            for section_num in range(0, num_sections):
                section = line.child(section_num)
                num_blocks = section.childCount()

                for block_num in range(0, num_blocks):
                    block = section.child(block_num)
                    print(block.text(0))

                    block.setBackground(0, Qt.green)
                    time.sleep(1)

    def update_commanded_speed(self, line, block, speed):
        pass

    def update_authority(self, line, block, authority):
        pass

    def get_authority(self, line, block):
        pass

    def get_block_info(self, line, block):
        # this will return {next block, block length, beacon, grade, authority, commanded speed}
        pass

    def get_block_occupancy(self, line, block):
        # return true for occupied false for empty
        pass

    def get_route(self, start, end):
        pass

    def update_switch_position(self, line, block, block_target):
        pass

    def set_block_occupancy(self, line, block, occupancy):
        pass

    def set_maintenance_mode(self, line, block, maintenance_mode):
        pass

    def get_ticket_sales(self, line):
        pass

# def make_changes(model):
#     time.sleep(2)
#     model.update_list_color()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TrackModel()
    # helper = HelperThread(parent=widget)
    # helper.change_color.connect(widget.update_list_color)
    # helper.start()

    widget.show()
    run_thread = False
    sys.exit(app.exec())
