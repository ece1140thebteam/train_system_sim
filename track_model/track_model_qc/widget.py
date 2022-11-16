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
from PyQt6 import uic, QtGui
from . import Track
from . import TrackBlock
import re
import csv
from signals import s

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
block_column        = 0
signal_column       = 1
occupancy_column    = 2
numbers_re = re.compile(r'[0-9]+')
class TrackModel(QWidget):
    default_track_file = 'default_track.csv'

    def __init__(self, track=None, parent=None):
        super().__init__(parent)
        self.time_elapsed_s = 0
        self.load_ui()
        self.track = Track.Track()
        self.load_track(TrackModel.default_track_file)
        self.config_temp()
        self.blockTree = self.blockListTreeWidget
        self.uploadTrackButton.clicked.connect(self.open_new_file)
        self.time_elapsed = 0
        self.r = 0
        self.g = 0
        self.b = 0

        self.displayed_block = None
        s.timer_tick.connect(self.handle_time_increment)
        s.send_TrackModel_failure_status.connect(self.update_failures)
        s.send_TrackModel_track_occupancy.connect(self.update_block_occupancy)
        s.get_TrackModel_map_info.connect(self.get_track_info)
        s.send_TrackModel_block_authority.connect(self.update_block_authority)
        s.send_TrackModel_commanded_speed.connect(self.update_commanded_speed)
        s.send_TrackModel_maintenance_status.connect(self.set_maintenance_mode)
        s.send_TrackModel_signal_status.connect(self.update_signal)
        s.send_TrackModel_get_next_block_info.connect(self.get_next_block)
        s.send_TrackModel_switch_position.connect(self.update_switch_position)
        s.send_TrackModel_get_block_info.connect(self.get_block_info)
        s.send_TrackModel_passengers_onboarded.connect(self.passengers_onboarded)

    def get_track_info(self):
        track_dict = dict()

        for line in self.track.track_lines:
            track_dict[line] = dict()
            track_dict[line]['sections'] = dict()
            track_dict[line]['switches'] = dict()

            for section in self.track.track_lines[line].sections:
                track_dict[line]['sections'][section] = list()
                for block in self.track.track_lines[line].sections[section]:
                    track_dict[line]['sections'][section].append(int(block))
                    b = self.track.track_lines[line].blocks[block]
                    if b.switch is not None:
                        track_dict[line]['switches'][b.block_number] = [b.switch.pos1, b.switch.pos2]
        
        s.send_TrackModel_map_info.emit(track_dict)

    def passengers_onboarded(self, line, block):
        onboarded = self.track.track_lines[line].blocks[block].passengers_onboarded()

        self.track.track_lines[line].total_sales += onboarded
        sales = self.track.track_lines[line].total_sales
        time_elapsed_s = self.time_elapsed_s
        time_elapsed_m = time_elapsed_s/60
        time_elapsed_h = time_elapsed_m/60
        tp = sales/time_elapsed_h
        
        print(f'Line {line} onboarded {onboarded} passengers, throughput: {tp}')
        s.send_TrackModel_throughput_signal.emit(line, tp)

    def handle_time_increment(self):
        # timer called every 100ms
        self.time_elapsed_s += .1

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
        if block.switch is not None:
            sw = f'{block.switch.block_num}->{block.switch.curr_pos} ({block.switch.pos1 if block.switch.curr_pos != block.switch.pos1 else block.switch.pos2})'
        else: sw = 'No switch'
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
        self.blockSwitchInfo.setText(sw)
        self.blockSignalInfo.setText(str(block.signal))
        self.blockTrackCircuitInfo.setText("Open" if block.circuit_open else "Closed")
        self.blockCommandedSpeedInfo.setText(str(block.commanded_speed))

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
        dlg.setFileMode(QFileDialog.AnyFile)
        # dlg.setFilter("csv(*.csv)")
        t = QFileDialog.getOpenFileName(dlg, "hello", os.getcwd(), "csv(*.csv)")
        
        if exists(t[0]):
            track_file = t[0]
            # notify others which track is loaded 
            self.load_track(track_file)

    def update_block_color(self, line, block, color, column):
        num_lines = self.blockListTreeWidget.invisibleRootItem().childCount()
        for line_num in range(0, num_lines):
            l = self.blockListTreeWidget.invisibleRootItem().child(line_num)
            num_sections = l.childCount()
            if l.text(0).split(' ')[0].lower() == line.lower():
                for section_num in range(0, num_sections):
                    section = l.child(section_num)
                    num_blocks = section.childCount()

                    for block_num in range(0, num_blocks):
                        b = section.child(block_num)
                        if int(b.text(0).split(' ')[1]) == block:
                            b.setBackground(column, color)

    def update_failures(self, line, block, failure):
        if failure != 'None':
            color = QtGui.QColor(200, 0, 0, 255)
        else:
            color = QtGui.QColor(0, 0, 0, 0)

        self.update_block_color(line, block, color, block_column)
        self.track.track_lines[line].blocks[block].failure_mode = failure
        self.display_block_info()

    def update_block_occupancy(self, line, block, occupancy): 
        if occupancy:
            color = QtGui.QColor(0, 200, 0, 255)
        else:
            color = QtGui.QColor(0, 0, 0, 0)

        self.update_block_color(line, block, color, occupancy_column)
        self.track.track_lines[line].blocks[block].circuit_open = not occupancy
        self.display_block_info()

    def update_block_authority(self, line, block, authority):
        self.track.track_lines[line].blocks[block].authority = authority
        self.display_block_info()

    def load_track(self, track_file):
        tracklines = dict()

        with open(track_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)

            for block in reader:
                line = block[0]
                blocknum = int(block[2])
                infra = block[6]

                inf_arr = infra.split(';')
                station = None
                underground = False
                switch = None
                railway_crossing = False
                block_travels_to = []
                
                for i in inf_arr:
                    i = i.strip()
                    if 'RAILWAY' in i:
                        railway_crossing = True
                    elif 'UNDERGROUND' in i:
                        underground = True
                    elif 'STATION' in i:
                        station = i
                    elif 'SWITCH' in i:
                        # print(i)
                        if 'FROM' in i:
                            print('from yard, adding connection')
                            print(i)
                            self.track.yard.add_connection(line, blocknum)
                        i=i.lower().replace('yard','0')
                        block_matches = re.findall(numbers_re, i)
                        positions = []
                        for b in block_matches:
                            if int(b) != blocknum and int(b) not in positions:
                                positions.append(int(b))

                        if len(positions)!=2:
                            print('switch format incorrect')
                            # if z1 is not blocknum:
                        else:
                            print(positions)
                            switch = TrackBlock.Switch(
                                line=line,
                                section=block[1],
                                block=blocknum,
                                pos1=positions[0],
                                pos2=positions[1],
                            )

                    elif not i.strip().isspace() and len(i.strip())>0:
                        print(i)

                connections = block[10]
                connections = connections.split(';')

                # set switch connections within the block
                for c in connections:
                    if '*' in c:
                        con = c.lower().replace('yard','0')
                        con = con.replace('*','')
                        val = int(con)
                        block_travels_to.append(val*-1)
                    else:
                        block_travels_to.append(int(c))

                # if switch is not None:
                #     if len(switch)>1:
                #         switch = TrackBlock.Switch(
                #             line=line,
                #             section=block[1],
                #             block=block[2],
                #             pos1=switch[0],
                #             pos2=switch[1],
                #         )
                #     else:
                #         switch = None
                if line not in tracklines:
                    tracklines[line] = dict()
                if block[1] not in tracklines[line]:
                    tracklines[line][block[1]] = []
                if block[2] not in tracklines[line][block[1]]:
                    tracklines[line][block[1]].append(block[2])

                b = TrackBlock.TrackBlock(
                    line = line,
                    section = block[1],
                    block_number = blocknum,
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
        
        self.display_track_tree()

        s.send_TrackModel_updated.emit()
        self.blockListTreeWidget.itemClicked.connect(self.block_list_item_clicked)
        self.blockListTreeWidget.expandAll()

    def display_track_tree(self):
        self.blockListTreeWidget.clear()
        items = []
        for line in self.track.track_lines:
            lineItem = QTreeWidgetItem([f'{line} line'])
            for section in self.track.track_lines[line].sections:
                sec = QTreeWidgetItem([f'Section {section}'])
                for block in self.track.track_lines[line].sections[section]:
                    blk = self.track.track_lines[line].blocks[block]
                    if blk.switch is not None:
                        pass
                    b = QTreeWidgetItem([f'Block {block}'])
                    sec.addChild(b)
                # sec.expandAll();
                lineItem.addChild(sec)
            items.append(lineItem)
        self.blockListTreeWidget.insertTopLevelItems(0, items)

    def get_railroad_crossing_blocks(self):
        pass

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
        path = str(Path(__file__).resolve().parent / "form.ui")
        # ui_file = QFile(path)
        # ui_file.open(QFile.ReadOnly)
        uic.loadUi(path, self)
        # ui_file.close()

    def update_list_color(self, column):
        num_lines = self.blockListTreeWidget.invisibleRootItem().childCount()
        # if self.i is None: self.i = 0
        self.b += 10
        if self.b > 255:
            self.g += 10
            self.b = 0
        if self.g > 255:
            self.g = 0
            self.r += 10
            self.r = self.r % 255

        for line_num in range(0, num_lines):
            line = self.blockListTreeWidget.invisibleRootItem().child(line_num)
            num_sections = line.childCount()

            for section_num in range(0, num_sections):
                section = line.child(section_num)
                num_blocks = section.childCount()

                for block_num in range(0, num_blocks):
                    block = section.child(block_num)

                    block.setBackground(column, QtGui.QColor(self.r, self.g, self.b, 255))

    def handle_timestep(self, ts):
        self.time_elapsed += 1
        print(f'Elapsed time: {self.time_elapsed}')

    def update_commanded_speed(self, line, block, speed):
        self.track.track_lines[line].blocks[block].commanded_speed = speed
        self.display_block_info()

    def update_signal(self, line, block, sig):
        if sig == 'Green':
            color = QtGui.QColor(0, 255, 0, 255)
        else:
            color = QtGui.QColor(255, 0, 0, 255)

        self.track.track_lines[line].blocks[block].signal = sig
        self.display_block_info()
        self.update_block_color(line, block, color, signal_column)

    def get_authority(self, line, block):
        pass
    

    def get_next_block(self, line, current_block_num, previous_block_num, train_num):   
        print('get next block')
        print(f'{current_block_num} {previous_block_num} {train_num}')
        next_block_num = -1
        if current_block_num == 0:  #dispatching from the yard
            next_block_num = 1
            print(self.track.yard.get_connections(line))
            for block in self.track.yard.get_connections(line):
                print(block)
                switch = self.track.track_lines[line].blocks[block].switch
                print(switch.curr_pos)
                next_block_num = block

                # switch is in the right position
                if switch.curr_pos != 0:
                    print('switch is not in the right position')

        else:
            if self.track.track_lines[line].blocks[current_block_num].switch is None:
                next_block_num = self.track.track_lines[line].blocks[current_block_num].can_travel_to
                print(next_block_num)

                if len(next_block_num) > 1:
                    for block in next_block_num:
                        if previous_block_num != abs(block): 
                            next_block_num = abs(block)
                else:
                    next_block_num = next_block_num[0]
                
                # accessed through a switch
                if next_block_num < 0:
                    b = abs(next_block_num)
                    sw = self.track.track_lines[line].blocks[b].switch
                    if sw.curr_pos != b:
                        print('switch position not correct, train derailed')
                    else:
                        next_block_num = b


            else:
                curr_b = self.track.track_lines[line].blocks[current_block_num]
                if len(curr_b.can_travel_to) > 2:
                    for block in curr_b.can_travel_to:
                        if previous_block_num != abs(block) and block>0:
                            print(block)
                            next_block_num = block
                            break
                if next_block_num<0:
                    print(curr_b.switch.curr_pos)
                    next_block_num = self.track.track_lines[line].blocks[current_block_num].switch.curr_pos
        
        block = self.track.track_lines[line].blocks[next_block_num]
        block_info = dict()

        # the block the train will enter
        block_info['block_num']          = block.block_number
        block_info['grade']              = block.block_grade
        block_info['beacon']             = {'station_name' : block.station, 'station_side' : 'right'}
        block_info['length']             = block.block_len
        block_info['commanded_speed']    = block.commanded_speed
        block_info['authority']          = block.authority
        block_info['underground']        = block.underground
        block_info['speed_limit']        = block.speed_limit

        block_info['passengers_waiting'] = block.passengers_waiting

        print(block_info)
        s.send_TrackModel_next_block_info.emit(train_num, block_info)

    def get_block_info(self, line, block, train_num):
        block = self.track.track_lines[line].blocks[block]
        block_info = dict()

        # the block the train will enter
        block_info['block_num']          = block.block_number
        block_info['grade']              = block.block_grade
        block_info['beacon']             = {'station_name' : block.station, 'station_side' : 'right'}
        block_info['length']             = block.block_len
        block_info['commanded_speed']    = block.commanded_speed
        block_info['authority']          = block.authority
        block_info['underground']        = block.underground
        block_info['speed_limit']        = block.speed_limit

        s.send_TrackModel_block_info.emit(train_num, block_info)

    # def get_block)_(self, line, block):
    #     # return true for occupied false for empty
    #     pass

    def get_route(self, start, end):
        pass

    def update_switch_position(self, line, block, position):
        self.track.track_lines[line].blocks[block].switch.update_switch_position(position)
        self.display_block_info()

    def set_maintenance_mode(self, line, block, in_maintenance):
        if in_maintenance:
            color = QtGui.QColor(204, 204, 0, 255)
        else:
            color = QtGui.QColor(0, 0, 0, 0)

        self.update_block_color(line, block, color, block_column)
        self.track.track_lines[line].blocks[block].maintenance_mode = in_maintenance
        self.display_block_info()

    def get_ticket_sales(self, line):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TrackModel()

    widget.show()
    run_thread = False
    sys.exit(app.exec())
