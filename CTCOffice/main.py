from PyQt6 import QtGui

import CTCOffice.ui.ctcOfficeLayout as ctcOfficeLayout
from PyQt6.QtCore import * 
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys
# import sqlite3
# import time
from signals import s
import CTCOffice.Train as Train

from CTCOffice.testUiMain import MainTestWindow

import CTCOffice.InitData as InitData

# mydb = sqlite3.connect("CTCOffice/ctcOffice.db")
# cursor = mydb.cursor()

class MainWindow(QMainWindow, ctcOfficeLayout.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        init_data = InitData.InitData()
        self.throughputs = init_data.get_throughput()
        self.lines = init_data.get_blocks()

        self.startTime = 0
        self.elapsedTime = 0
        self.simRunning = 0
        self.simReset = 1

        # Initialize Static Data
        self.redBlocks = []
        self.greenBlocks = []
        self.blueBlocks = []

        self.red_authority = [0]
        self.green_authority = [0]

        self.redSwitches = []
        self.greenSwitches = []
        self.blueSwitches = []

        self.redCrossings = []
        self.greenCrossings = []
        self.blueCrossings = []

        self.redStations = []
        self.redStationBlocks = [7, 16, 21, 25, 35, 45, 48, 60]
        self.greenStations = []
        self.greenStationBlocks = [2, 9, 16, 22, 31, 39, 48, 57, 65, 73, 77, 88, 96, 105, 114, 123, 132, 141]
        self.blueStations = []

        self.redTrains = []
        self.greenTrains = []
        self.blueTrains = []

        self.init_get_blocks()
        self.init_get_switches()
        self.init_get_crossings()
        self.init_get_stations()

        self.init_switch_positions()
        self.init_crossings()

        # Initialize Components
        self.set_manual_mode()
        self.update_maintenance_combobox()
        self.update_switches_combobox()
        self.update_stations_combobox()
        self.update_dispatch_stations_combobox()
        self.update_stations_trains_combobox()
        self.update_speed_trains_combobox()

        self.get_line_data()

        # Button Connections
        self.pushButton_manualMode.clicked.connect(self.set_manual_mode)
        self.pushButton_controlSwitch.clicked.connect(self.set_switch)
        self.pushButton_trackMaintenance.clicked.connect(self.set_maintenance)
        self.pushButton_changeSpeed.clicked.connect(self.change_speed)
        self.pushButton_editStations.clicked.connect(self.edit_stations)
        self.pushButton_2.clicked.connect(self.open_file)
        self.pushButton_dispatchTrains.clicked.connect(self.dispatch_train)
        self.pushButton_scheduleTrains.clicked.connect(self.schedule_trains)

        # ComboBox Connections
        self.comboBox_trackMaintenance_line.currentTextChanged.connect(self.update_maintenance_combobox)
        self.comboBox_controlSwitch_Line.currentTextChanged.connect(self.update_switches_combobox)
        self.comboBox_editStations_line.currentTextChanged.connect(self.update_stations_combobox)
        self.comboBox_dispatchTrain_line.currentTextChanged.connect(self.update_dispatch_stations_combobox)
        self.comboBox_changeSpeed_line.currentTextChanged.connect(self.update_speed_trains_combobox)
        self.comboBox_editStations_line.currentTextChanged.connect(self.update_stations_trains_combobox)

        # Signal Connections
        # Test Signals
        s.send_CTC_test_throughput_signal.connect(self.update_throughput)
        s.send_CTC_test_failure.connect(self.update_failure)
        s.send_CTC_test_crossing.connect(self.update_crossing)
        s.send_CTC_test_track_occupancy.connect(self.set_occupancy)

        # Wayside Signals
        s.send_CTC_authority.connect(self.set_authorities)

        # Track Signals
        s.send_TrackModel_throughput_signal.connect(self.update_throughput)

    # Enables the actions only available in manual mode
    # Called when the manual mode button is clicked
    def set_manual_mode(self):
        if self.pushButton_manualMode.isChecked() is True:
            self.pushButton_controlSwitch.setDisabled(False)
            self.pushButton_trackMaintenance.setDisabled(False)
            self.pushButton_dispatchTrains.setDisabled(False)
        else:
            self.pushButton_controlSwitch.setDisabled(True)
            self.pushButton_trackMaintenance.setDisabled(True)
            self.pushButton_dispatchTrains.setDisabled(True)

    def schedule_trains(self):
        fileName = self.label.text();
        self.outputLabel.setText("Scheduling Trains from file: " + fileName)

    # Set the switch position for given line and block and store in database
    # Called when the set switch button is clicked
    def set_switch(self):
        line = self.comboBox_controlSwitch_Line.currentText()
        switch = self.comboBox_controlSwitch_switch.currentText()
        position = self.comboBox_controlSwitch_switchPosition.currentText()

        print("Setting Line " + line + " switch #: " + switch + " to position: " + position)
        self.outputLabel.setText("Setting Line " + line + " switch #: " + switch + " to position: " + position)
        if position == "Normal":
            state = 0
        else:
            state = 1
        
        if line == "Red":
            self.lines[0].get(int(switch)).switch_position = state
            positions = []
            for block in self.lines[0]:
                positions.append(self.lines[0].get(block).switch_position)

            s.send_CTC_switch_position_signal.emit(line, positions) # Emit signal to set positions
        elif line == "Green":
            self.lines[1].get(int(switch)).switch_position = state
            positions = []
            for block in self.lines[1]:
                positions.append(self.lines[1].get(block).switch_position)

            s.send_CTC_switch_position_signal.emit(line, positions) # Emit signal to set positions

        self.get_line_data() # Update displayed tables

    # Set the maintenance for given line and block and store in database
    # Called when the set maintenance button is clicked
    def set_maintenance(self):
        line = self.comboBox_trackMaintenance_line.currentText()
        block = self.comboBox_trackMaintenance_blockNumber.currentText()
        status = self.comboBox_trackMaintenance_trackStatus.currentText()

        print("Setting Line " + line + " block #: " + block + " to status: " + status)
        self.outputLabel.setText("Setting Line " + line + " block #: " + block + " to status: " + status)
        if status == "In Maintenance":
            state = 1
        else:
            state = 0

        if line == "Red":
            self.lines[0].get(int(block)).maintenance_mode = state
            modes = []
            for block in self.lines[0]:
                modes.append(self.lines[0].get(block).maintenance_mode)

            s.send_CTC_maintenance_mode_signal.emit(line, modes) # Emit signal to set maintenance 
        elif line == "Green":
            self.lines[1].get(int(block)).maintenance_mode = state
            modes = []
            for block in self.lines[1]:
                modes.append(self.lines[1].get(block).maintenance_mode)

            s.send_CTC_maintenance_mode_signal.emit(line, modes) # Emit signal to set maintenance

        self.get_line_data() # Update displayed tables

    def change_speed(self):
        line = self.comboBox_changeSpeed_line.currentText()
        train = self.comboBox_changeSpeed_train.currentText()
        speed = self.spinBox_changeSpeed_speed.value()

        print("Setting Line " + line + " train #: " + train + " to speed: " + str(speed) + "mph")
        self.outputLabel.setText("Setting Line " + line + " train #: " + train + " to speed: " + str(speed) + "mph")

        s.send_CTC_suggested_speed.emit(line, int(train), int(speed))

    def edit_stations(self):
        line = self.comboBox_editStations_line.currentText()
        train = self.comboBox_editStations_train.currentText()
        station = self.comboBox_editStations_station.currentText()
        action = self.comboBox_editStations_action.currentText()
        hour = self.spinBox_editStations_hour.value()
        minute = self.spinBox_editStations_minute.value()
        print("Setting Line " + line + " train #: " + train + " to " + action + " at station " + station + " at: " + str(
            hour) + ":" + str(minute))
        self.outputLabel.setText("Setting Line " + line + " train #: " + train + " to " + action + " at station " + station + " at: " + str(
            hour) + ":" + str(minute))

    def dispatch_train(self):
        line = self.comboBox_dispatchTrain_line.currentText()
        stations = []
        stationBlocks = []

        for row in range(0, self.tableWidget_dispatch.rowCount()):
            time = self.tableWidget_dispatch.item(row, 1).text()
            if time != '':
                if line == "Green":
                    block = self.greenStationBlocks[row]
                else:
                    block = self.redStationBlocks[row]
                
                stations.append((block, time))
                stationBlocks.append(block)

        print(str(stations))

        Train.trains.create_train('Green', stationBlocks)
        


    # Update the comboBox of track_blocks
    # Called when the line is changed for maintenance
    def update_maintenance_combobox(self):
        block_box = self.comboBox_trackMaintenance_blockNumber
        block_box.clear()
        if self.comboBox_trackMaintenance_line.currentText() == "Red":
            block_box.addItems(self.redBlocks)
        elif self.comboBox_trackMaintenance_line.currentText() == "Green":
            block_box.addItems(self.greenBlocks)
        elif self.comboBox_trackMaintenance_line.currentText() == "Blue":
            block_box.addItems(self.blueBlocks)

    # Update the comboBox of switches
    # Called when the line is changed for switch control
    def update_switches_combobox(self):
        switch_box = self.comboBox_controlSwitch_switch
        switch_box.clear()
        if self.comboBox_controlSwitch_Line.currentText() == "Red":
            switch_box.addItems(self.redSwitches)
        elif self.comboBox_controlSwitch_Line.currentText() == "Green":
            switch_box.addItems(self.greenSwitches)
        elif self.comboBox_controlSwitch_Line.currentText() == "Blue":
            switch_box.addItems(self.blueSwitches)

    # Update the comboBox of stations
    # Called when the line is changed for edit stations
    def update_stations_combobox(self):
        station_box = self.comboBox_editStations_station
        station_box.clear()
        if self.comboBox_editStations_line.currentText() == "Red":
            station_box.addItems(self.redStations)
        elif self.comboBox_editStations_line.currentText() == "Green":
            station_box.addItems(self.greenStations)
        elif self.comboBox_editStations_line.currentText() == "Blue":
            station_box.addItems(self.blueStations)

    # Update the comboBox of trains
    # Called when the line is changed for edit stations
    def update_stations_trains_combobox(self):
        train_box = self.comboBox_editStations_train
        train_box.clear()
        if self.comboBox_editStations_line.currentText() == "Red":
            train_box.addItems(self.redTrains)
        elif self.comboBox_editStations_line.currentText() == "Green":
            train_box.addItems(self.greenTrains)
        elif self.comboBox_editStations_line.currentText() == "Blue":
            train_box.addItems(self.blueTrains)

    # Update the comboBox of trains
    # Called when the line is changed for change speed
    def update_speed_trains_combobox(self):
        train_box = self.comboBox_changeSpeed_train
        train_box.clear()
        if self.comboBox_changeSpeed_line.currentText() == "Red":
            train_box.addItems(self.redTrains)
        elif self.comboBox_changeSpeed_line.currentText() == "Green":
            train_box.addItems(self.greenTrains)
        elif self.comboBox_changeSpeed_line.currentText() == "Blue":
            train_box.addItems(self.blueTrains)

    # Update the comboBox of stations for dispatch
    # Called when the line is changed for edit stations
    def update_dispatch_stations_combobox(self):
        if self.comboBox_dispatchTrain_line.currentText() == "Red":
            self.tableWidget_dispatch.setRowCount(len(self.redStations))
            for row in range(0, len(self.redStations)):
                station = self.redStations[row]
                self.tableWidget_dispatch.setItem(row, 0, QTableWidgetItem(station))
                self.tableWidget_dispatch.setItem(row, 1, QTableWidgetItem())

        elif self.comboBox_dispatchTrain_line.currentText() == "Green":
            self.tableWidget_dispatch.setRowCount(len(self.greenStations))
            for row in range(0, len(self.greenStations)):
                station = self.greenStations[row]
                self.tableWidget_dispatch.setItem(row, 0, QTableWidgetItem(station))
                self.tableWidget_dispatch.setItem(row, 1, QTableWidgetItem())

    # Get all blocks for a line
    # Called once on init of window
    def init_get_blocks(self):
        for line in self.lines:
            for block in line:
                if line.get(block).line == 'Red':
                    self.redBlocks.append(str(block))
                    self.red_authority.append(0)
                if line.get(block).line == 'Green':
                    self.greenBlocks.append(str(block))
                    self.green_authority.append(0)
                if line.get(block).line == 'Blue':
                    self.blueBlocks.append(str(block))

    # Get all switches for a line by filtering on Infrastructure substring
    # Called once on init of window
    def init_get_switches(self):
        for line in self.lines:
            for block in line:
                if line.get(block).line == 'Red':
                    if line.get(block).infrastructure[0:6] == "SWITCH":
                        self.redSwitches.append(str(block))
                if line.get(block).line == 'Green':
                    if line.get(block).infrastructure[0:6] == "SWITCH":
                        self.greenSwitches.append(str(block))
                if line.get(block).line == 'Blue':
                    if line.get(block).infrastructure[0:6] == "SWITCH":
                        self.blueSwitches.append(str(block))      

    # Get all stations for a line by filtering on Infrastructure substring
    # Called once on init of window
    def init_get_stations(self): 
        for line in self.lines:
            for block in line:
                if line.get(block).line == 'Red':
                    if line.get(block).infrastructure[0:7].upper() == "STATION":
                        self.redStations.append(str(line.get(block).infrastructure))
                if line.get(block).line == 'Green':
                    if line.get(block).infrastructure[0:7].upper() == "STATION":
                        self.greenStations.append(str(line.get(block).infrastructure))
                if line.get(block).line == 'Blue':
                    if line.get(block).infrastructure[0:7].upper() == "STATION":
                        self.blueStations.append(str(line.get(block).infrastructure))

    # Get all crossings for a line by filtering on Infrastructure match
    # Called once on init of window
    def init_get_crossings(self):
        for line in self.lines:
            for block in line:
                if line.get(block).line == 'Red':
                    if line.get(block).infrastructure == "RAILWAY CROSSING":
                        self.redCrossings.append(str(block))
                if line.get(block).line == 'Green':
                    if line.get(block).infrastructure == "RAILWAY CROSSING":
                        self.greenCrossings.append(str(block))
                if line.get(block).line == 'Blue':
                    if line.get(block).infrastructure == "RAILWAY CROSSING":
                        self.blueCrossings.append(str(block))

    # Update all switches to have a position of 0
    def init_switch_positions(self):
        for c in self.redSwitches:
            self.lines[0].get(int(c)).switch_position = 0
        for c in self.greenSwitches:
            self.lines[1].get(int(c)).switch_position = 0
        for c in self.blueSwitches:
            self.lines[2].get(int(c)).switch_position = 0

    # Update all crossings to have a status of 0
    def init_crossings(self):
        for c in self.redCrossings:
            self.lines[0].get(int(c)).crossing = 0
        for c in self.greenCrossings:
            self.lines[1].get(int(c)).crossing = 0
        for c in self.blueCrossings:
            self.lines[2].get(int(c)).crossing = 0

    # Get all data for a line and update table
    # Table is colored depending on value returned
    def get_line_data(self):
        self.tableWidget_2.setRowCount(70)
        for row in range(0, 70):
            block = self.lines[0].get(row+1)
            self.tableWidget_2.setItem(row, 0, QTableWidgetItem(str(block.block_number)))
            self.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(block.line)))
            self.tableWidget_2.setItem(row, 2, QTableWidgetItem(str(block.occupancy)))
            self.tableWidget_2.setItem(row, 3, QTableWidgetItem(str(block.authority)))
            self.tableWidget_2.setItem(row, 4, QTableWidgetItem(str(block.switch_position)))
            self.tableWidget_2.setItem(row, 5, QTableWidgetItem(str(block.failure)))
            self.tableWidget_2.setItem(row, 6, QTableWidgetItem(str(block.crossing)))
            self.tableWidget_2.setItem(row, 7, QTableWidgetItem(str(block.section)))
            self.tableWidget_2.setItem(row, 8, QTableWidgetItem(str(block.maintenance_mode)))
            self.tableWidget_2.setItem(row, 9, QTableWidgetItem(str(block.infrastructure)))  
            self.tableWidget_2.setItem(row, 10, QTableWidgetItem(str(block.signal_state)))  
            self.tableWidget_2.setItem(row, 11, QTableWidgetItem(str(block.suggested_speed)))

            # Failure
            if block.failure != '':
                self.tableWidget_2.item(row, 5).setBackground(QtGui.QColor(255, 0, 0))
            else:
                self.tableWidget_2.item(row, 5).setBackground(QtGui.QColor(255, 255, 255))

            if block.authority != 0:
                self.tableWidget_2.item(row, 3).setBackground(QtGui.QColor(189, 252, 194))
            else:
                self.tableWidget_2.item(row, 3).setBackground(QtGui.QColor(255, 255, 255))

            # Maintenance
            if block.maintenance_mode != 0:
                self.tableWidget_2.item(row, 8).setBackground(QtGui.QColor(255, 255, 51))
            else:
                self.tableWidget_2.item(row, 8).setBackground(QtGui.QColor(255, 255, 255))

            # Switch
            if block.switch_position is None:
                self.tableWidget_2.item(row, 4).setBackground(QtGui.QColor(255, 255, 255))
            elif block.switch_position == 0:
                self.tableWidget_2.item(row, 4).setBackground(QtGui.QColor(102, 255, 255))
            else:
                self.tableWidget_2.item(row, 4).setBackground(QtGui.QColor(255, 255, 102))

            # Occupancy
            if block.occupancy != 0:
                self.tableWidget_2.item(row, 2).setBackground(QtGui.QColor(51, 255, 51))
            else:
                self.tableWidget_2.item(row, 2).setBackground(QtGui.QColor(255, 255, 255))

            # Crossing
            if block.crossing is None:
                self.tableWidget_2.item(row, 6).setBackground(QtGui.QColor(255, 255, 255))
            elif block.crossing == 0:
                self.tableWidget_2.item(row, 6).setBackground(QtGui.QColor(255, 255, 255))
            else:
                self.tableWidget_2.item(row, 6).setBackground(QtGui.QColor(255, 153, 51))

        self.tableWidget.setRowCount(150)
        for row in range(0, 150):
            block = self.lines[1].get(row+1)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(block.block_number)))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(block.line)))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(block.occupancy)))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(block.authority)))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(block.switch_position)))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(str(block.failure)))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(str(block.crossing)))
            self.tableWidget.setItem(row, 7, QTableWidgetItem(str(block.section)))
            self.tableWidget.setItem(row, 8, QTableWidgetItem(str(block.maintenance_mode)))
            self.tableWidget.setItem(row, 9, QTableWidgetItem(str(block.infrastructure)))  
            self.tableWidget.setItem(row, 10, QTableWidgetItem(str(block.signal_state)))  
            self.tableWidget.setItem(row, 11, QTableWidgetItem(str(block.suggested_speed)))

            # Failure
            if block.failure != '':
                self.tableWidget.item(row, 5).setBackground(QtGui.QColor(255, 0, 0))
            else:
                self.tableWidget.item(row, 5).setBackground(QtGui.QColor(255, 255, 255))

            # Maintenance
            if block.maintenance_mode != 0:
                self.tableWidget.item(row, 8).setBackground(QtGui.QColor(255, 255, 51))
            else:
                self.tableWidget.item(row, 8).setBackground(QtGui.QColor(255, 255, 255))

            # Authority
            if block.authority != 0:
                self.tableWidget.item(row, 3).setBackground(QtGui.QColor(189, 252, 194))
            else:
                self.tableWidget.item(row, 3).setBackground(QtGui.QColor(255, 255, 255))

            # Switch
            if block.switch_position is None:
                self.tableWidget.item(row, 4).setBackground(QtGui.QColor(255, 255, 255))
            elif block.switch_position == 0:
                self.tableWidget.item(row, 4).setBackground(QtGui.QColor(102, 255, 255))
            else:
                self.tableWidget.item(row, 4).setBackground(QtGui.QColor(255, 255, 102))

            # Occupancy
            if block.occupancy != 0:
                self.tableWidget.item(row, 2).setBackground(QtGui.QColor(51, 255, 51))
            else:
                self.tableWidget.item(row, 2).setBackground(QtGui.QColor(255, 255, 255))

            # Crossing
            if block.crossing is None:
                self.tableWidget.item(row, 6).setBackground(QtGui.QColor(255, 255, 255))
            elif block.crossing == 0:
                self.tableWidget.item(row, 6).setBackground(QtGui.QColor(255, 255, 255))
            else:
                self.tableWidget.item(row, 6).setBackground(QtGui.QColor(255, 153, 51))

    def open_file(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File')
        print(filename)
        self.label.setText(str(filename[0]))
        self.outputLabel.setText(("Opened file: " + str(filename[0])))

    # Connected to signal from CTC Test
    def update_failure(self, line, block_number, failure):
        if line == "Red":
            self.lines[0].get(block_number).failure = failure
        elif line == "Green":
            self.lines[1].get(block_number).failure = failure

        self.get_line_data()

        print("Update Failure: " + line, str(block_number), failure)

    # Connected to signal from CTC Test
    def update_crossing(self, line, block_number, crossing):
        if line == "Red":
            self.lines[0].get(block_number).set_crossing(crossing)
        elif line == "Green":
            self.lines[1].get(block_number).set_crossing(crossing)

        self.get_line_data()

        print("Update Crossing: " + line + str(block_number) + str(crossing))

    # Connected to signal from CTC Test and Track Model
    def update_throughput(self, line_name: str, throughput):
        if line_name == 'Red':
            self.throughputs[0].setThroughput(throughput)
            self.RedThroughput.setText(str(self.throughputs[0].get_throughput()))
        elif line_name == "Green":
            self.throughputs[1].setThroughput(throughput)
            self.GreenThroughput.setText(str(self.throughputs[1].get_throughput()))
        elif line_name == "Blue":
            self.throughputs[2].setThroughput(throughput)
            self.BlueThroughput.setText(str(self.throughputs[2].get_throughput()))
        
        print("Update throughput: " + line_name + str(throughput))
    
    # Connected to signal from CTC Test
    def set_occupancy(self, occupancies):
        for occupancy in occupancies:
            if occupancy['line'] == 'Red':
                if occupancy['block'] != 0:
                    self.lines[0].get(occupancy['block']).occupancy = occupancy['occupancy']
            if occupancy['line'] == 'Green':
                if occupancy['block'] != 0:
                    self.lines[1].get(occupancy['block']).occupancy = occupancy['occupancy']

        # if line == "Red":
        #     self.lines[0].get(block_number).occupancy = occupancy
        # elif line == "Green":
        #     self.lines[1].get(block_number).occupancy = occupancy

        self.get_line_data()
        
        # print("Update Occupancy: " + line, str(block_number), str(occupancy))

    # Connected to signal from CTC Office
    def set_authorities(self, authorities):
        for authority in authorities:
            if authority['line'] == 'Red':
                if authority['block'] != 0:
                    self.lines[0].get(authority['block']).authority = authority['authority']
            if authority['line'] == 'Green':
                if authority['block'] != 0:
                    self.lines[1].get(authority['block']).authority = authority['authority']

        self.get_line_data()

    # Conncted to signal from Wayside
    def set_occupancies(self, line, occupancies):


        if line == "Red":
            for block in range(0, len(occupancies)):
                self.lines[0].get(block + 1).occupancy = occupancies[block]
        if line == "Green":
            for block in range(0, len(occupancies)):
                self.lines[1].get(block + 1).occupancy = occupancies[block]

        self.get_line_data()


    def open_test_ui(self):
        self.testUi = MainTestWindow()
        self.testUi.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())