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
    default_track_file = str(Path(__file__).resolve().parent / default_track_file)
    
    def __init__(self, track=None, parent=None):
        super().__init__(parent)
        self.displayed_block = None
        self.time_elapsed_s = 0
        self.load_ui()
        self.track = Track.Track()
        self.load_track(TrackModel.default_track_file)
        self.blockTree = self.blockListTreeWidget
        self.uploadTrackButton.clicked.connect(self.open_new_file)
        self.time_elapsed = 0
        self.r = 0
        self.g = 0
        self.b = 0
        self.config_temp()

        # connect UI
        self.failureDropDown.currentTextChanged.connect(self.handle_failure_dropdown)

        # connect communication signals
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
        s.send_TrackModel_railway_crossing_status.connect(self.update_crossing_position)
        # self.print_track_info_dict()

        #from track controller
        s.send_TrackController_switch_pos.connect(self.tc_set_switch_pos)



    def print_track_info_dict(self):
        track_dict = dict()

        for line in self.track.track_lines:
            track_dict[line] = dict()

            for block in self.track.track_lines[line].blocks:
                b = self.track.track_lines[line].blocks[block]
                track_dict[line][block] = {
                    'authority': 0,
                    'switch_pos': None if b.switch is None else 0,
                    'failure': 0,
                    'suggested_speed': 0,
                    'track_crossing': None if not b.has_rail_crossing else 0,
                    'traffic_light': 0,
                    'commanded_speed': 0,
                    'maintenance': 0,
                    'occupancy': 0
                }

               
        print(track_dict)

    def get_track_info(self):
        track_dict = dict()

        for line in self.track.track_lines:
            track_dict[line] = dict()
            track_dict[line]['sections']    = dict()
            track_dict[line]['switches']    = dict()
            track_dict[line]['crossings']   = dict()

            for section in self.track.track_lines[line].sections:
                track_dict[line]['sections'][section] = list()
                for block in self.track.track_lines[line].sections[section]:
                    track_dict[line]['sections'][section].append(int(block))
                    b = self.track.track_lines[line].blocks[block]
                    if b.switch is not None:
                        track_dict[line]['switches'][b.block_number] = [b.switch.pos1, b.switch.pos2]
                    if b.has_rail_crossing:
                        track_dict[line]['crossings'][b.block_number] = True
        
        s.send_TrackModel_map_info.emit(track_dict)

    def passengers_onboarded(self, line, block, deboarded):
        onboarded = self.track.track_lines[line].blocks[block].passengers_onboarded(deboarded)

        self.track.track_lines[line].total_sales += onboarded
        sales = self.track.track_lines[line].total_sales
        time_elapsed_s = self.time_elapsed_s
        time_elapsed_m = time_elapsed_s/60
        time_elapsed_h = time_elapsed_m/60
        tp = sales/time_elapsed_h
        
        print(f'Line {line} onboarded {onboarded} passengers, throughput: {tp}')
        s.send_TrackModel_throughput_signal.emit(line, int(tp))
        self.update_station_tree(line, block)

    def tc_set_switch_pos(self, line, block, pos):
        sw = -1
        if pos == 0:
            sw = self.track.track_lines[line].blocks[block].switch.pos1
        elif pos == 1:
            sw = self.track.track_lines[line].blocks[block].switch.pos2

        else:
            print('ERROR')
        self.update_switch_position(line, block, sw)
    
    def update_crossing_position(self, line, block, pos):
        # if pos is true, crossing is open
        self.track.track_lines[line].blocks[block].crossing_open = pos
        if self.displayed_block is None: return
        if block == self.displayed_block.block_number: self.display_block_info()

    def handle_time_increment(self):
        # timer called every 100ms
        self.time_elapsed_s += .1

    def handle_failure_dropdown(self):
        failure_type = self.failureDropDown.currentText()
        block = self.displayed_block
        
        self.update_failures(block.line, block.block_number, failure_type)
        

    def load_block_clicked_info(self, line, section, block):
        line = line.split(' ')[0]
        # block = int(block.split(' ')[1])

        self.display_block_info(self.track.track_lines[line].blocks[block])

    def display_block_info(self, block=None):
        if block is not None:
            self.displayed_block = block
        
        block = self.displayed_block

        if block is None: return
        if block.switch is not None:
            sw = f'{block.switch.block_num}->{block.switch.curr_pos} ({block.switch.pos1 if block.switch.curr_pos != block.switch.pos1 else block.switch.pos2})'
        else: sw = 'No switch'

        crossing_info = 'None'

        if block.has_rail_crossing:
            if block.crossing_open:
                crossing_info = 'Open'
            else: crossing_info = 'Closed'

        self.failureDropDown.setEnabled(True)
        self.failureDropDown.setCurrentText(block.failure_mode)
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
        self.blockRailCrossingInfo.setText(crossing_info)
        self.blockUndergroundInfo.setText(str(block.underground))
        self.blockAuthorityInfo.setText(str(block.authority))
        self.blockMaintenanceModeInfo.setText(str(block.maintenance_mode))
        # self.blockBeaconInfo.setText(str(block.beacon1) + )
        self.blockSwitchPositionInfo.setText(str(block.switch_pos))
        self.blockSwitchInfo.setText(sw)
        self.blockSignalInfo.setText(str(block.signal))
        self.blockTrackCircuitInfo.setText("Open" if block.circuit_open else "Closed")
        self.blockCommandedSpeedInfo.setText(str(block.commanded_speed))

        travstr = ''
        for val in block.can_travel_to:
            if val > 0:
                travstr += str(val)
                travstr += ', '
            if val == 0:
                travstr += '*YARD, '

        for val in block.can_travel_to:
            if val < 0:
                travstr += f'*{val}, '
        
        travstr = travstr.strip().strip(',')
                
        self.blockDirectionsOfTravel.setText(travstr)

    def block_list_item_clicked(self, item):
        # if this is the yard block
        if 'Yard' in item.text(0):
            line  = item.parent().text(0)
            self.load_block_clicked_info(line, '', 0)

        # if this is a block
        elif item.parent() is not None:
            if item.parent().parent() is not None:
                line    = item.parent().parent().text(0)
                section = item.parent().text(0)
                block   = item.text(0)
                block   = int(block.split(' ')[1])
                self.load_block_clicked_info(line, section, block)

    def open_new_file(self):
        print('opening new file')
        dlg = QFileDialog()
        # dlg.setFileMode(QFileDialog.AnyFile)
        # dlg.setFilter("csv(*.csv)")
        t = QFileDialog.getOpenFileName(dlg, "hello", os.getcwd(), "csv(*.csv)")
        
        if exists(t[0]):
            track_file = t[0]
            # notify others which track is loaded 
            self.load_track(track_file)

    def update_block_color(self, line, block, color, column):
        if block != 0:
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
        
        else:
            num_lines = self.blockListTreeWidget.invisibleRootItem().childCount()
            for line_num in range(0, num_lines):
                l = self.blockListTreeWidget.invisibleRootItem().child(line_num)
                num_sections = l.childCount()
                if l.text(0).split(' ')[0].lower() == line.lower():
                    for section_num in range(0, num_sections):
                        yard = l.child(section_num)
                        if '0' in yard.text(0):
                            yard.setBackground(column, color)


    def update_switch_tree_pos_color(self, line, block):
        # print('updating station tree')
        block = self.track.track_lines[line].blocks[block]
        num_lines = self.switchPosTree.invisibleRootItem().childCount()
        for line_num in range(0, num_lines):
            l = self.switchPosTree.invisibleRootItem().child(line_num)
            num_switches = l.childCount()
            if l.text(0).split(' ')[0].lower() == line.lower():
                for switch_num in range(0, num_switches):
                    sw = l.child(switch_num)
                    if int(sw.text(0)) == block.block_number:
                        pos1Color = None
                        pos2Color = None

                        if block.switch.pos1 == block.switch.curr_pos:
                            pos1Color = QtGui.QColor(0,170, 0, 255)
                            pos2Color = QtGui.QColor(0,0, 0, 0)
                        else:
                            pos1Color = QtGui.QColor(0,0, 0, 0)
                            pos2Color = QtGui.QColor(0,170, 0, 255)
                        sw.setBackground(1, pos1Color)
                        sw.setBackground(2, pos2Color)

    def update_failures(self, line, block, failure):
        if failure != 'None':
            color = QtGui.QColor(200, 0, 0, 255)
        else:
            color = QtGui.QColor(0, 0, 0, 0)

        self.update_block_color(line, block, color, block_column)
        self.track.track_lines[line].blocks[block].failure_mode = failure
        self.display_block_info()
        s.send_TrackModel_tc_track_failure.emit(line, block, failure)

    def update_block_occupancy(self, line, block, occupancy):
        if block in self.track.track_lines[line].blocks:
            if occupancy:
                color = QtGui.QColor(0, 200, 0, 255)
            else:
                color = QtGui.QColor(0, 0, 0, 0)

            self.update_block_color(line, block, color, occupancy_column)
            self.track.track_lines[line].blocks[block].circuit_open = not occupancy
            self.display_block_info()

    def update_block_authority(self, line, block, authority):
        if block in self.track.track_lines[line].blocks:
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
                station_side = block[11] if block[11] != '' else None

                for i in inf_arr:
                    i = i.strip()
                    if 'RAILWAY' in i:
                        railway_crossing = True
                    elif 'UNDERGROUND' in i:
                        underground = True
                    elif 'STATION' in i:
                        station = i.replace('STATION','').replace(':','').strip()
                    elif 'SWITCH' in i:
                        # print(i)
                        if 'FROM' in i:
                            # print('from yard, adding connection')
                            # print(i)
                            self.track.yard.add_connection(line, blocknum)
                            self.track.track_lines[line].blocks[0].can_travel_to.append(blocknum)
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
                            switch = TrackBlock.Switch(
                                line=line,
                                section=block[1],
                                block=blocknum,
                                pos1=min(positions[0], positions[1]),
                                pos2=max(positions[1], positions[0]),
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
                    can_travel_to = block_travels_to,
                    station_side = station_side
                )

                self.track.add_block(b)
        
        self.display_track_tree()
        self.display_station_tree()
        self.display_switch_tree()

        s.send_TrackModel_updated.emit()
        self.blockListTreeWidget.expandAll()
        self.stationTree.expandAll()


    def display_track_tree(self):
        self.blockListTreeWidget.clear()
        items = []
        for line in self.track.track_lines:
            lineItem = QTreeWidgetItem([f'{line} line'])
            lineyard = QTreeWidgetItem(['Yard: Block 0'])
            lineItem.addChild(lineyard)

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
        self.blockListTreeWidget.itemClicked.connect(self.block_list_item_clicked)
        self.blockListTreeWidget.header().resizeSection(0, 175)
        self.blockListTreeWidget.header().resizeSection(1, 50)
        self.blockListTreeWidget.header().resizeSection(2, 50)

    def update_station_tree(self, line, block):
        # print('updating station tree')
        block = self.track.track_lines[line].blocks[block]
        num_lines = self.stationTree.invisibleRootItem().childCount()
        for line_num in range(0, num_lines):
            l = self.stationTree.invisibleRootItem().child(line_num)
            num_stations = l.childCount()
            if l.text(0).split(' ')[0].lower() == line.lower():
                for station_num in range(0, num_stations):
                    station = l.child(station_num)
                    if station.text(0) == block.station:
                        station.setText(1, str(block.passengers_waiting))
                        station.setText(2, str(block.passengers_deboarded))
      
    def display_station_tree(self):
        self.stationTree.clear()
        items = []
        for line in self.track.track_lines:
            lineItem = QTreeWidgetItem([f'{line} line'])
            for section in self.track.track_lines[line].sections:
                # sec = QTreeWidgetItem([f'Section {section}'])
                for block in self.track.track_lines[line].sections[section]:
                    blk = self.track.track_lines[line].blocks[block]
                    if blk.station is not None:
                        b = QTreeWidgetItem([str(blk.station), str(blk.passengers_waiting), str(blk.passengers_deboarded)])
                        lineItem.addChild(b)
            items.append(lineItem)
        self.stationTree.insertTopLevelItems(0, items)
        self.stationTree.header().resizeSection(0, 145)
        self.stationTree.header().resizeSection(1, 50)
        self.stationTree.header().resizeSection(2, 70)

    def display_switch_tree(self):
        self.switchPosTree.clear()
        items = []
        for line in self.track.track_lines:
            lineItem = QTreeWidgetItem([f'{line} line'])
            for section in self.track.track_lines[line].sections:
                # sec = QTreeWidgetItem([f'Section {section}'])
                for block in self.track.track_lines[line].sections[section]:
                    blk = self.track.track_lines[line].blocks[block]
                    if blk.switch is not None:
                        b = QTreeWidgetItem([str(blk.block_number), str(blk.switch.pos1), str(blk.switch.pos2)])
                        pos1Color = None
                        pos2Color = None

                        if blk.switch.pos1 == blk.switch.curr_pos:
                            pos1Color = QtGui.QColor(0,170, 0, 255)
                            pos2Color = QtGui.QColor(0,0, 0, 0)
                        else:
                            pos1Color = QtGui.QColor(0,0, 0, 0)
                            pos2Color = QtGui.QColor(0,170, 0, 255)
                        b.setBackground(1, pos1Color)
                        b.setBackground(2, pos2Color)
                        lineItem.addChild(b)

            items.append(lineItem)

        self.switchPosTree.insertTopLevelItems(0, items)
        self.switchPosTree.header().resizeSection(0, 145)
        self.switchPosTree.header().resizeSection(1, 50)
        self.switchPosTree.header().resizeSection(2, 70)

    def get_railroad_crossing_blocks(self):
        pass

    def config_temp(self):
        month = datetime.datetime.now().month
        hour = datetime.datetime.now().hour
        avg_month_temp = pittsburgh_weather[month]

        # assume it is hottest at 3:00pm, 15:00
        dev = int(1/(1+abs(hour-15))*24)

        # random pittsburgh temperature based on month
        temp_f = random.randint(avg_month_temp-int(dev/2), avg_month_temp+int(dev/2))

        self.temperatureSpinBox.setValue(temp_f)
        self.temperatureSpinBox.valueChanged.connect(self.update_temp_spin_box)
        self.update_temp_spin_box()

    def update_temp_spin_box(self):
        if self.track.heater_on:
            if self.temperatureSpinBox.value() > 32:
                # print('Turning heater off')
                self.track.turn_heater_off()
                self.display_block_info()

        else:
            if self.temperatureSpinBox.value() <= 32:
                # print('Turning heater on')
                self.track.turn_heater_on()
                self.display_block_info()

    def load_ui(self):
        path = str(Path(__file__).resolve().parent / "form.ui")
        # ui_file = QFile(path)
        # ui_file.open(QFile.ReadOnly)
        uic.loadUi(path, self)
        # ui_file.close()

    def update_commanded_speed(self, line, block, speed):
        if block in self.track.track_lines[line].blocks:
            self.track.track_lines[line].blocks[block].commanded_speed = speed
            self.display_block_info()

    def update_signal_tc(self, line, block, sig):
        self.update_signal(line, block, 'Green' if sig == 1 else 'Red')

    def update_signal(self, line, block, sig):
        if sig == 'Green':
            color = QtGui.QColor(0,255, 0, 255)
        else:
            color = QtGui.QColor(255, 0, 0, 255)

        self.track.track_lines[line].blocks[block].signal = sig
        self.display_block_info()
        self.update_block_color(line, block, color, signal_column)

    def get_authority(self, line, block):
        pass
    

    def get_next_block(self, line, current_block_num, previous_block_num, train_num):   
        # print('get next block')
        print(f'{current_block_num} {previous_block_num} {train_num}')
        next_block_num = -1
        dispatching = False
        if current_block_num == 0: # connections from the yard
            # next_block_num = 1
            # print(self.track.yard.get_connections(line))
            for block in self.track.yard.get_connections(line):
                # print(block)
                switch = self.track.track_lines[line].blocks[block].switch
                # print(switch.curr_pos)
                next_block_num = block

                # switch is in the right position
                if switch.curr_pos != 0:
                    print('switch is not in the right position')
        elif current_block_num == -1:   #dispatching now 
            next_block_num = 0
            dispatching = True
        else:
            if self.track.track_lines[line].blocks[current_block_num].switch is None:
                next_block_num = self.track.track_lines[line].blocks[current_block_num].can_travel_to
                print(next_block_num)

                if len(next_block_num) > 1:
                    for block in next_block_num:
                        if previous_block_num != abs(block): 
                            next_block_num = block
                else:
                    next_block_num = next_block_num[0]
                
                # accessed through a switch
                if next_block_num < 0:
                    b = abs(next_block_num)
                    sw = self.track.track_lines[line].blocks[b].switch
                    print('checking if switch position is correct')
                    print(sw.curr_pos)
                    if sw.curr_pos != b and sw.curr_pos != current_block_num:
                        print('switch position not correct, train derailed')
                        s.send_TrackModel_next_block_info.emit(train_num, {'block_num':-1})
                        return
                    else:
                        next_block_num = b

            else:
                curr_b = self.track.track_lines[line].blocks[current_block_num]
                block_options = [b for b in curr_b.can_travel_to if abs(b) != previous_block_num]
                print(block_options)
                # bidirectional block that can travel to both of the switches
                if len(block_options) > 1:
                    found = False
                    for block in block_options:
                        if block>0:
                            next_block_num = block
                            found = True

                    # all options are through switch
                    if not found:
                        curr_pos = self.track.track_lines[line].blocks[current_block_num].switch.curr_pos 
                        if -1*curr_pos not in block_options:
                            print('TRAIN DERAILED')
                            s.send_TrackModel_next_block_info.emit(train_num, {'block_num':-1})
                            return
                        else:
                            next_block_num = curr_pos 

                elif len(block_options) == 1:
                    next_block_num = block_options[0]

                # block is traveling through the switch to the current position of the switch
                if next_block_num<0:
                    print(curr_b.switch.curr_pos)
                    pos = self.track.track_lines[line].blocks[current_block_num].switch.curr_pos
                    if abs(next_block_num) == pos:
                        next_block_num = pos
                    else:
                        s.send_TrackModel_next_block_info.emit(train_num, {'block_num':-1})
                        return 
        
        if next_block_num == 0 and not dispatching:
            block_info = dict()
            block_info['block_num'] = 0
            block_info['yard'] = True
            s.send_TrackModel_next_block_info.emit(train_num, block_info)
            return

        block = self.track.track_lines[line].blocks[next_block_num]
        block.print()
        block_info = dict()
        block_info['beacon'] = None

        # if the train is leaving a block w a station
        if current_block_num > 0:
            curr_block = self.track.track_lines[line].blocks[current_block_num]
            if curr_block.station is not None:
                if next_block_num > current_block_num:
                    block_info['beacon'] = curr_block.beacon2
                else:
                    block_info['beacon'] = curr_block.beacon1

        # if the train is entering a block with a station
        if block.station is not None:
            if next_block_num > current_block_num:
                block_info['beacon'] = block.beacon1
            else:
                block_info['beacon'] = block.beacon2
            


        # the block the train will enter
        block_info['block_num']          = block.block_number
        block_info['grade']              = block.block_grade
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
        block_info['beacon'] = block.beacon1

        # # if the train is leaving a block w a station
        # block.beacon1
        # if current_block_num > 0:
        #     curr_block = self.track.track_lines[line].blocks[current_block_num]
        #     if curr_block.station is not None:
        #         if next_block_num > current_block_num:
        #             block_info['beacon'] = curr_block.beacon2
        #         else:
        #             block_info['beacon'] = curr_block.beacon1

        # # if the train is entering a block with a station
        # if block.station is not None:
        #     if next_block_num > current_block_num:
        #         block_info['beacon'] = curr_block.beacon1
        #     else:
        #         block_info['beacon'] = curr_block.beacon2
        # the block the train will enter
        block_info['block_num']          = block.block_number
        block_info['grade']              = block.block_grade
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
        self.update_switch_tree_pos_color(line, block)

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
