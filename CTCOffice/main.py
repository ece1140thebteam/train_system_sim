from PyQt6 import QtGui, QtWidgets

import ui.ctcOfficeLayout as ctcOfficeLayout
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys
import sqlite3

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="P1ttsburgh",
#     database="ctcoffice"
# )

mydb = sqlite3.connect("ctcOffice.db")

cursor = mydb.cursor()


class MainWindow(QMainWindow, ctcOfficeLayout.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

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

        self.get_throughput()
        self.get_trains()

        # Initialize Components
        self.set_manual_mode()
        self.update_maintenance()
        self.update_switches()
        self.update_stations()
        self.update_dispatch_stations()
        self.update_stations_trains()
        self.update_speed_trains()

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

        # ComboBox Connections
        self.comboBox_trackMaintenance_line.currentTextChanged.connect(self.update_maintenance)
        self.comboBox_controlSwitch_Line.currentTextChanged.connect(self.update_switches)
        self.comboBox_editStations_line.currentTextChanged.connect(self.update_stations)
        self.comboBox_dispatchTrain_line.currentTextChanged.connect(self.update_dispatch_stations)
        self.comboBox_changeSpeed_line.currentTextChanged.connect(self.update_speed_trains)
        self.comboBox_editStations_line.currentTextChanged.connect(self.update_stations_trains)

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
        self.outputLabel.setText("Scheduling Trains from file: " + fileName);

    # Set the switch position for given line and block and store in database
    # Called when the set switch button is clicked
    def set_switch(self):
        line = self.comboBox_controlSwitch_Line.currentText()
        switch = self.comboBox_controlSwitch_switch.currentText()
        position = self.comboBox_controlSwitch_switchPosition.currentText()
        print("Setting Line " + line + " switch #: " + switch + " to position: " + position)
        self.outputLabel.setText("Setting Line " + line + " switch #: " + switch + " to position: " + position)
        if position == "Normal":
            values = (0, line, switch)
        else:
            values = (1, line, switch)
        # query = "UPDATE track_blocks SET Switch_Position = (%s) WHERE Line = (%s) and Block_Number = (%s)"
        query = "UPDATE track_blocks SET Switch_Position = ? WHERE Line = ? and Block_Number = ?"

        cursor.execute(query, values)
        mydb.commit()

    # Set the maintenance for given line and block and store in database
    # Called when the set maintenance button is clicked
    def set_maintenance(self):
        line = self.comboBox_trackMaintenance_line.currentText()
        block = self.comboBox_trackMaintenance_blockNumber.currentText()
        status = self.comboBox_trackMaintenance_trackStatus.currentText()
        print("Setting Line " + line + " block #: " + block + " to status: " + status)
        self.outputLabel.setText("Setting Line " + line + " block #: " + block + " to status: " + status)
        if status == "In Maintenance":
            values = (1, line, block)
        else:
            values = (0, line, block)
        # query = "UPDATE track_blocks SET Maintenance = (%s) WHERE Line = (%s) and Block_Number = (%s)"
        query = "UPDATE track_blocks SET Maintenance = ? WHERE Line = ? and Block_Number = ?"

        cursor.execute(query, values)
        mydb.commit()

    def change_speed(self):
        line = self.comboBox_changeSpeed_line.currentText()
        train = self.comboBox_changeSpeed_train.currentText()
        speed = self.spinBox_changeSpeed_speed.value()
        print("Setting Line " + line + " train #: " + train + " to speed: " + str(speed) + "mph")
        self.outputLabel.setText("Setting Line " + line + " train #: " + train + " to speed: " + str(speed) + "mph")

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
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT Block_Number FROM track_blocks WHERE line = 'Red'")
        blocks = my_cursor.fetchall()
        for block in blocks:
            self.redBlocks.append(str(block[0]))

        my_cursor.execute("SELECT Block_Number FROM track_blocks WHERE line = 'Green'")
        blocks = my_cursor.fetchall()
        for block in blocks:
            self.greenBlocks.append(str(block[0]))

        my_cursor.execute("SELECT Block_Number FROM track_blocks WHERE line = 'Blue'")
        blocks = my_cursor.fetchall()
        for block in blocks:
            self.blueBlocks.append(str(block[0]))

    # Get all switches for a line be filtering on Infrastructure substring
    # Called once on init of window
    def get_switches(self):
        cursor.execute(
            "SELECT Block_Number FROM track_blocks WHERE line = 'Red' AND SUBSTR(Infrastructure, 1, 6) = 'SWITCH'")
            # "SELECT Block_Number FROM track_blocks WHERE line = 'Red' AND SUBSTRING(Infrastructure, 1, 6) = 'SWITCH'")
        blocks = cursor.fetchall()
        for block in blocks:
            self.redSwitches.append(str(block[0]))

        cursor.execute(
            "SELECT Block_Number FROM track_blocks WHERE line = 'Green' AND SUBSTR(Infrastructure, 1, 6) = 'SWITCH'")
            # "SELECT Block_Number FROM track_blocks WHERE line = 'Green' AND SUBSTRING(Infrastructure, 1, 6) = 'SWITCH'")
        blocks = cursor.fetchall()
        for block in blocks:
            self.greenSwitches.append(str(block[0]))

        cursor.execute(
            "SELECT Block_Number FROM track_blocks WHERE line = 'Blue' AND SUBSTR(Infrastructure, 1, 6) = 'SWITCH'")
        # "SELECT Block_Number FROM track_blocks WHERE line = 'Green' AND SUBSTRING(Infrastructure, 1, 6) = 'SWITCH'")
        blocks = cursor.fetchall()
        for block in blocks:
            self.blueSwitches.append(str(block[0]))

    # Get all stations for a line be filtering on Infrastructure substring
    # Called once on init of window
    def get_stations(self):
        cursor.execute(
            "SELECT Infrastructure FROM track_blocks WHERE line = 'Red' AND SUBSTR(UPPER(Infrastructure), 1, 7) = 'STATION'")
        blocks = cursor.fetchall()
        for block in blocks:
            self.redStations.append(str(block[0]))

        cursor.execute(
            "SELECT Infrastructure FROM track_blocks WHERE line = 'Green' AND SUBSTR(UPPER(Infrastructure), 1, 7) = 'STATION'")
        blocks = cursor.fetchall()
        for block in blocks:
            self.greenStations.append(str(block[0]))

        cursor.execute(
            "SELECT Infrastructure FROM track_blocks WHERE line = 'Blue' AND SUBSTR(UPPER(Infrastructure), 1, 7) = 'STATION'")
        blocks = cursor.fetchall()
        for block in blocks:
            self.blueStations.append(str(block[0]))

    # Get all stations for a line be filtering on Infrastructure match
    # Called once on init of window
    def get_crossings(self):
        cursor.execute(
            "SELECT Block_Number FROM track_blocks WHERE line = 'Red' AND Infrastructure = 'RAILWAY CROSSING'")
        blocks = cursor.fetchall()
        for block in blocks:
            self.redCrossings.append(str(block[0]))

        cursor.execute(
            "SELECT Block_Number FROM track_blocks WHERE line = 'Green' AND Infrastructure = 'RAILWAY CROSSING'")
        blocks = cursor.fetchall()
        for block in blocks:
            self.greenCrossings.append(str(block[0]))

        cursor.execute(
            "SELECT Block_Number FROM track_blocks WHERE line = 'Blue' AND Infrastructure = 'RAILWAY CROSSING'")
        blocks = cursor.fetchall()
        for block in blocks:
            self.blueCrossings.append(str(block[0]))

    # Update all switches to have a position of 0
    def init_switch_positions(self):
        # query = "UPDATE track_blocks SET Switch_Position = (%s) WHERE line = (%s) and Block_Number = (%s)"
        query = "UPDATE track_blocks SET Switch_Position = ? WHERE line = ? and Block_Number = ?"
        for c in self.redSwitches:
            values = (0, 'Red', c)
            cursor.execute(query, values)
        for c in self.greenSwitches:
            values = (0, 'Green', c)
            cursor.execute(query, values)
        for c in self.blueSwitches:
            values = (0, 'Blue', c)
            cursor.execute(query, values)
        mydb.commit()

    # Update all crossings to have a status of 0
    def init_crossings(self):
        # query = "UPDATE track_blocks SET Crossing = (%s) WHERE line = (%s) and Block_Number = (%s)"
        query = "UPDATE track_blocks SET Crossing = ? WHERE line = ? and Block_Number = ?"
        for c in self.redCrossings:
            values = (0, 'Red', c)
            cursor.execute(query, values)
        for c in self.greenCrossings:
            values = (0, 'Green', c)
            cursor.execute(query, values)
        for c in self.blueCrossings:
            values = (0, 'Blue', c)
            cursor.execute(query, values)
        mydb.commit()

    # Get all data for a line and update table
    # Table is colored depending on value returned
    def get_line_data(self):
        self.tableWidget_2.setRowCount(70)

        cursor.execute("SELECT * FROM track_blocks WHERE line = 'Red'")
        data = cursor.fetchall()
        for row in range(0, 70):
            for col in range(0, 9):
                self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(data[row][col])))

            # Failure
            if str(data[row][5]) != '':
                self.tableWidget_2.item(row, 5).setBackground(QtGui.QColor(255, 0, 0))
            else:
                self.tableWidget_2.item(row, 5).setBackground(QtGui.QColor(255, 255, 255))

            # Maintenance
            if str(data[row][3]) != '0':
                self.tableWidget_2.item(row, 3).setBackground(QtGui.QColor(255, 255, 51))
            else:
                self.tableWidget_2.item(row, 3).setBackground(QtGui.QColor(255, 255, 255))

            # Switch
            if data[row][6] is None:
                self.tableWidget_2.item(row, 6).setBackground(QtGui.QColor(255, 255, 255))
            elif str(data[row][6]) == '0':
                self.tableWidget_2.item(row, 6).setBackground(QtGui.QColor(102, 255, 255))
            else:
                self.tableWidget_2.item(row, 6).setBackground(QtGui.QColor(255, 255, 102))

            # Occupancy
            if str(data[row][7]) != '0':
                self.tableWidget_2.item(row, 7).setBackground(QtGui.QColor(51, 255, 51))
            else:
                self.tableWidget_2.item(row, 7).setBackground(QtGui.QColor(255, 255, 255))

            # Crossing
            if data[row][8] is None:
                self.tableWidget_2.item(row, 8).setBackground(QtGui.QColor(255, 255, 255))
            elif str(data[row][8]) == '0':
                self.tableWidget_2.item(row, 8).setBackground(QtGui.QColor(255, 255, 255))
            else:
                self.tableWidget_2.item(row, 8).setBackground(QtGui.QColor(255, 153, 51))

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
            cursor.execute("SELECT * FROM track_blocks WHERE line = 'Green'")
            data = cursor.fetchall()

            for row in range(0, 150):
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

    # Fetch the throughput for each line from the database
    def get_throughput(self):
        cursor.execute("SELECT throughput FROM throughput WHERE line = 'Red'")
        data = cursor.fetchone()
        self.RedThroughput.setText(str(data[0]))

        cursor.execute("SELECT throughput FROM throughput WHERE line = 'Green'")
        data = cursor.fetchone()
        self.GreenThroughput.setText(str(data[0]))

        cursor.execute("SELECT throughput FROM throughput WHERE line = 'Blue'")
        data = cursor.fetchone()
        self.BlueThroughput.setText(str(data[0]))

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
        self.get_throughput()
        mydb.commit()

    def open_file(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File')
        print(filename)
        self.label.setText(str(filename[0]))
        self.outputLabel.setText(("Opened file: " + str(filename[0])))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    timer = QTimer()
    timer.timeout.connect(window.update_data)
    timer.start(1000)

    sys.exit(app.exec())
