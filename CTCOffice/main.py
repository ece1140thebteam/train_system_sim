from PyQt6 import QtGui

import CTCOffice.ui.ctcOfficeLayout as ctcOfficeLayout
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys
import sqlite3
import time
from signals import s

from CTCOffice.testUiMain import MainTestWindow

import CTCOffice.InitData as InitData

mydb = sqlite3.connect("CTCOffice/ctcOffice.db")
cursor = mydb.cursor()

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

        self.redSwitches = []
        self.greenSwitches = []
        self.blueSwitches = []

        self.redCrossings = []
        self.greenCrossings = []
        self.blueCrossings = []

        self.redStations = []
        self.greenStations = []
        self.blueStations = []

        self.redTrains = []
        self.greenTrains = []
        self.blueTrains = []

        self.get_blocks()
        self.get_switches()
        self.get_crossings()
        self.get_stations()

        self.init_switch_positions()
        self.init_crossings()

        # self.get_throughput()
        self.get_trains()

        # Initialize Components
        self.set_manual_mode()
        self.update_maintenance()
        self.update_switches()
        self.update_stations()
        self.update_dispatch_stations()
        self.update_stations_trains()
        self.update_speed_trains()

        self.get_line_data()

        # Button Connections
        self.pushButton_manualMode.clicked.connect(self.set_manual_mode)
        self.pushButton_controlSwitch.clicked.connect(self.set_switch)
        self.pushButton_trackMaintenance.clicked.connect(self.set_maintenance)
        self.pushButton_changeSpeed.clicked.connect(self.change_speed)
        self.pushButton_editStations.clicked.connect(self.edit_stations)
        self.pushButton.clicked.connect(self.get_line_data)
        self.pushButton_2.clicked.connect(self.open_file)
        self.pushButton_dispatchTrains.clicked.connect(self.dispatch_train)
        self.pushButton_scheduleTrains.clicked.connect(self.schedule_trains)
        self.pushButton_startSim.clicked.connect(self.start_simulation)
        self.pushButton_stopSim.clicked.connect(self.stop_simulation)
        self.pushButton_resetSim.clicked.connect(self.reset_simulation)

        self.pushButton_openTestUi.clicked.connect(self.open_test_ui)

        # ComboBox Connections
        self.comboBox_trackMaintenance_line.currentTextChanged.connect(self.update_maintenance)
        self.comboBox_controlSwitch_Line.currentTextChanged.connect(self.update_switches)
        self.comboBox_editStations_line.currentTextChanged.connect(self.update_stations)
        self.comboBox_dispatchTrain_line.currentTextChanged.connect(self.update_dispatch_stations)
        self.comboBox_changeSpeed_line.currentTextChanged.connect(self.update_speed_trains)
        self.comboBox_editStations_line.currentTextChanged.connect(self.update_stations_trains)

        s.send_TrackModel_throughput_signal.connect(self.update_throughput)
        s.send_TrackController_failure.connect(self.update_failure)
        s.send_TrackController_crossing.connect(self.update_crossing)
        s.send_TrackController_track_occupancy.connect(self.set_occupancy)
        s.send_CTC_switch_position_signal.connect(self.set_switch_position)
        s.send_CTC_maintenance_mode_signal.connect(self.set_maintenance_mode)

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

        s.send_CTC_switch_position_signal.emit(line, int(switch), int(state))

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

        s.send_CTC_maintenance_mode_signal.emit(line, int(block), int(state))

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
        station = self.comboBox_dispatchTrain_station.currentText()
        hour = self.spinBox_dispatchTrain_hour.value()
        minute = self.spinBox_dispatchTrain_minute.value()
        print("Dispatching train on " + line + " line to " + station + " at " + str(hour) + ":" + str(minute))
        self.outputLabel.setText("Dispatching train on " + line + " line to " + station + " at " + str(hour) + ":" + str(minute))

        query = "INSERT INTO trains VALUES (?, ?, ?, ?, ?)"
        values = (None, line, 0,0,0)
        cursor.execute(query, values)
        mydb.commit()

        self.get_trains()

    # Update the comboBox of track_blocks
    # Called when the line is changed for maintenance
    def update_maintenance(self):
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
    def update_switches(self):
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
    def update_stations(self):
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
    def update_stations_trains(self):
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
    def update_speed_trains(self):
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
    def update_dispatch_stations(self):
        station_box = self.comboBox_dispatchTrain_station
        station_box.clear()
        if self.comboBox_dispatchTrain_line.currentText() == "Red":
            station_box.addItems(self.redStations)
        elif self.comboBox_dispatchTrain_line.currentText() == "Green":
            station_box.addItems(self.greenStations)
        elif self.comboBox_dispatchTrain_line.currentText() == "Blue":
            station_box.addItems(self.blueStations)


    # Get all blocks for a line
    # Called once on init of window
    def get_blocks(self):
        for line in self.lines:
            for block in line:
                if line.get(block).line == 'Red':
                    self.redBlocks.append(str(block))
                if line.get(block).line == 'Green':
                    self.greenBlocks.append(str(block))
                if line.get(block).line == 'Blue':
                    self.blueBlocks.append(str(block))

    # Get all switches for a line be filtering on Infrastructure substring
    # Called once on init of window
    def get_switches(self):
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
        

    # Get all stations for a line be filtering on Infrastructure substring
    # Called once on init of window
    def get_stations(self): 
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

    # Get all stations for a line be filtering on Infrastructure match
    # Called once on init of window
    def get_crossings(self):
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

        if self.comboBox_selectLineGraph.currentText() == "Blue Line":
            self.tableWidget.setRowCount(15)
            cursor.execute("SELECT * FROM track_blocks WHERE line = 'Blue'")
            data = cursor.fetchall()

            for row in range(0, 15):
                for col in range(0, 9):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(data[row][col])))

                # Color Failure
                if str(data[row][5]) != '':
                    self.tableWidget.item(row, 5).setBackground(QtGui.QColor(255, 0, 0))
                else:
                    self.tableWidget.item(row, 5).setBackground(QtGui.QColor(255, 255, 255))

                # Color Maintenance
                if str(data[row][3]) != '0':
                    self.tableWidget.item(row, 3).setBackground(QtGui.QColor(255, 255, 51))
                else:
                    self.tableWidget.item(row, 3).setBackground(QtGui.QColor(255, 255, 255))

                # Switch
                if data[row][6] is None:
                    self.tableWidget.item(row, 6).setBackground(QtGui.QColor(255, 255, 255))
                elif str(data[row][6]) == '0':
                    self.tableWidget.item(row, 6).setBackground(QtGui.QColor(102, 255, 255))
                else:
                    self.tableWidget.item(row, 6).setBackground(QtGui.QColor(255, 255, 102))

                # Color Occupancy
                if str(data[row][7]) != '0':
                    self.tableWidget.item(row, 7).setBackground(QtGui.QColor(51, 255, 51))
                else:
                    self.tableWidget.item(row, 7).setBackground(QtGui.QColor(255, 255, 255))

                # Color Crossing
                if data[row][8] is None:
                    self.tableWidget.item(row, 8).setBackground(QtGui.QColor(255, 255, 255))
                elif str(data[row][8]) == '0':
                    self.tableWidget.item(row, 8).setBackground(QtGui.QColor(255, 255, 255))
                else:
                    self.tableWidget.item(row, 8).setBackground(QtGui.QColor(255, 153, 51))
        elif self.comboBox_selectLineGraph.currentText() == "Green Line":
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

    def get_trains(self):
        cursor.execute("SELECT Train_ID FROM trains WHERE line = 'Red'")
        trains = cursor.fetchall()
        for train in trains:
            self.redTrains.append(str(train[0]))

        cursor.execute("SELECT Train_ID FROM trains WHERE line = 'Green'")
        trains = cursor.fetchall()
        for train in trains:
            self.greenTrains.append(str(train[0]))

        cursor.execute("SELECT Train_ID FROM trains WHERE line = 'Blue'")
        trains = cursor.fetchall()
        for train in trains:
            self.blueTrains.append(str(train[0]))

        self.update_speed_trains()
        self.update_stations_trains()

    # Helper method to call get_line_data and get_throughput
    # These methods are called every time the timer expires
    def update_data(self):
        self.get_line_data()
        mydb.commit()

        if self.simRunning == 1:
            self.elapsedTime = time.time() - self.startTime
            self.label_currentTime.setText(time.strftime("%H:%M:%S", time.gmtime(self.elapsedTime)))
        else:
            self.label_currentTime.setText(time.strftime("%H:%M:%S", time.gmtime(0)))

    def open_file(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File')
        print(filename)
        self.label.setText(str(filename[0]))
        self.outputLabel.setText(("Opened file: " + str(filename[0])))

    # Function calls for Class Objects
    def update_failure(self, line, block_number, failure):
        if line == "Red":
            self.lines[0].get(block_number).failure = failure
        elif line == "Green":
            self.lines[1].get(block_number).failure = failure

        self.get_line_data()

        print("Update Failure: " + line, str(block_number), failure)

    def update_crossing(self, line, block_number, crossing):
        if line == "Red":
            self.lines[0].get(block_number).set_crossing(crossing)
        elif line == "Green":
            self.lines[1].get(block_number).set_crossing(crossing)

        self.get_line_data()

        print("Update Crossing: " + line + str(block_number) + str(crossing))

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

    def set_occupancy(self, line, block_number, occupancy):
        if line == "Red":
            self.lines[0].get(block_number).occupancy = occupancy
        elif line == "Green":
            self.lines[1].get(block_number).occupancy = occupancy

        self.get_line_data()
        
        print("Update Occupancy: " + line, str(block_number), str(occupancy))

    def set_switch_position(self, line, block_number, position):
        if line == "Red":
            self.lines[0].get(block_number).switch_position = position
        elif line == "Green":
            self.lines[1].get(block_number).switch_position = position

        self.get_line_data()
        
        print("Update crossing: " + line, str(block_number), str(position))
    
    def set_maintenance_mode(self, line, block_number, mode):
        if line == "Red":
            self.lines[0].get(block_number).maintenance_mode = mode
        elif line == "Green":
            self.lines[1].get(block_number).maintenance_mode = mode

        self.get_line_data()
        
        print("Update crossing: " + line, str(block_number), str(mode))

    # Simulation Timing Control
    def start_simulation(self): 
        self.startTime = time.time()
        self.elapsedTime = time.time()
        self.outputLabel.setText("Starting Simulation")
        self.label_simStatus.setText("Running")
        self.elapsedTime = 1

    def stop_simulation(self):
        self.outputLabel.setText("Stopping Simulation")
        self.label_simStatus.setText("Stopped")
        self.elapsedTime = 0

    def reset_simulation(self):
        self.outputLabel.setText("Resetting Simulation")
        self.label_simStatus.setText("Stopped")
        self.elapsedTime = 0
    
    def open_test_ui(self):
        self.testUi = MainTestWindow()
        self.testUi.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    timer = QTimer()
    timer.timeout.connect(window.update_data)
    timer.start(1000)

    sys.exit(app.exec())