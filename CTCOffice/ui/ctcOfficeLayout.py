# Form implementation generated from reading ui file 'ctcOfficeLayout.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1187, 719)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_manualMode = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_manualMode.setStyleSheet("QPushButton:checked {background-color: red;}")
        self.pushButton_manualMode.setCheckable(True)
        self.pushButton_manualMode.setAutoDefault(False)
        self.pushButton_manualMode.setFlat(False)
        self.pushButton_manualMode.setObjectName("pushButton_manualMode")
        self.verticalLayout_10.addWidget(self.pushButton_manualMode)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.comboBox_controlSwitch_Line = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_controlSwitch_Line.setObjectName("comboBox_controlSwitch_Line")
        self.comboBox_controlSwitch_Line.addItem("")
        self.comboBox_controlSwitch_Line.addItem("")
        self.comboBox_controlSwitch_Line.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_controlSwitch_Line)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.comboBox_controlSwitch_switch = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_controlSwitch_switch.setObjectName("comboBox_controlSwitch_switch")
        self.horizontalLayout_7.addWidget(self.comboBox_controlSwitch_switch)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_8.addWidget(self.label_14)
        self.comboBox_controlSwitch_switchPosition = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_controlSwitch_switchPosition.setObjectName("comboBox_controlSwitch_switchPosition")
        self.comboBox_controlSwitch_switchPosition.addItem("")
        self.comboBox_controlSwitch_switchPosition.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_controlSwitch_switchPosition)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.pushButton_controlSwitch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_controlSwitch.setObjectName("pushButton_controlSwitch")
        self.verticalLayout_2.addWidget(self.pushButton_controlSwitch)
        self.verticalLayout_10.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.comboBox_trackMaintenance_line = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_trackMaintenance_line.setObjectName("comboBox_trackMaintenance_line")
        self.comboBox_trackMaintenance_line.addItem("")
        self.comboBox_trackMaintenance_line.addItem("")
        self.comboBox_trackMaintenance_line.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_trackMaintenance_line)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.comboBox_trackMaintenance_blockNumber = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_trackMaintenance_blockNumber.setObjectName("comboBox_trackMaintenance_blockNumber")
        self.horizontalLayout_3.addWidget(self.comboBox_trackMaintenance_blockNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.comboBox_trackMaintenance_trackStatus = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_trackMaintenance_trackStatus.setObjectName("comboBox_trackMaintenance_trackStatus")
        self.comboBox_trackMaintenance_trackStatus.addItem("")
        self.comboBox_trackMaintenance_trackStatus.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_trackMaintenance_trackStatus)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.pushButton_trackMaintenance = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_trackMaintenance.setObjectName("pushButton_trackMaintenance")
        self.verticalLayout.addWidget(self.pushButton_trackMaintenance)
        self.verticalLayout_10.addLayout(self.verticalLayout)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_9.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_9.addWidget(self.label_28)
        self.comboBox_dispatchTrain_line = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_dispatchTrain_line.setObjectName("comboBox_dispatchTrain_line")
        self.comboBox_dispatchTrain_line.addItem("")
        self.comboBox_dispatchTrain_line.addItem("")
        self.comboBox_dispatchTrain_line.addItem("")
        self.verticalLayout_9.addWidget(self.comboBox_dispatchTrain_line)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_9.addLayout(self.horizontalLayout_19)
        self.tableWidget_dispatch = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_dispatch.setObjectName("tableWidget_dispatch")
        self.tableWidget_dispatch.setColumnCount(2)
        self.tableWidget_dispatch.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dispatch.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dispatch.setHorizontalHeaderItem(1, item)
        self.verticalLayout_9.addWidget(self.tableWidget_dispatch)
        self.pushButton_dispatchTrains = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dispatchTrains.setObjectName("pushButton_dispatchTrains")
        self.verticalLayout_9.addWidget(self.pushButton_dispatchTrains)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.horizontalLayout_20.addLayout(self.verticalLayout_10)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.pushButton_scheduleTrains = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_scheduleTrains.setObjectName("pushButton_scheduleTrains")
        self.verticalLayout_3.addWidget(self.pushButton_scheduleTrains)
        self.horizontalLayout_17.addLayout(self.verticalLayout_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.RedThroughput = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.RedThroughput.setFont(font)
        self.RedThroughput.setObjectName("RedThroughput")
        self.gridLayout.addWidget(self.RedThroughput, 1, 1, 1, 1)
        self.GreenThroughput = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.GreenThroughput.setFont(font)
        self.GreenThroughput.setObjectName("GreenThroughput")
        self.gridLayout.addWidget(self.GreenThroughput, 2, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 1, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.BlueThroughput = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.BlueThroughput.setFont(font)
        self.BlueThroughput.setObjectName("BlueThroughput")
        self.gridLayout.addWidget(self.BlueThroughput, 0, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout)
        self.horizontalLayout_17.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_17)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setToolTipDuration(-1)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(12)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(11, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.verticalLayout_8.addWidget(self.tableWidget_2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_8.addWidget(self.tableWidget)
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(9)
        self.outputLabel.setFont(font)
        self.outputLabel.setObjectName("outputLabel")
        self.verticalLayout_8.addWidget(self.outputLabel)
        self.horizontalLayout_20.addLayout(self.verticalLayout_8)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_9.addWidget(self.label_15)
        self.comboBox_changeSpeed_line = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_changeSpeed_line.setObjectName("comboBox_changeSpeed_line")
        self.comboBox_changeSpeed_line.addItem("")
        self.comboBox_changeSpeed_line.addItem("")
        self.comboBox_changeSpeed_line.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_changeSpeed_line)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_10.addWidget(self.label_16)
        self.comboBox_changeSpeed_train = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_changeSpeed_train.setObjectName("comboBox_changeSpeed_train")
        self.horizontalLayout_10.addWidget(self.comboBox_changeSpeed_train)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_11.addWidget(self.label_17)
        self.spinBox_changeSpeed_speed = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_changeSpeed_speed.setObjectName("spinBox_changeSpeed_speed")
        self.horizontalLayout_11.addWidget(self.spinBox_changeSpeed_speed)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.pushButton_changeSpeed = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_changeSpeed.setObjectName("pushButton_changeSpeed")
        self.verticalLayout_4.addWidget(self.pushButton_changeSpeed)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_5.addWidget(self.label_18)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_12.addWidget(self.label_19)
        self.comboBox_editStations_line = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_editStations_line.setObjectName("comboBox_editStations_line")
        self.comboBox_editStations_line.addItem("")
        self.comboBox_editStations_line.addItem("")
        self.comboBox_editStations_line.addItem("")
        self.horizontalLayout_12.addWidget(self.comboBox_editStations_line)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_13.addWidget(self.label_20)
        self.comboBox_editStations_train = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_editStations_train.setObjectName("comboBox_editStations_train")
        self.horizontalLayout_13.addWidget(self.comboBox_editStations_train)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_14.addWidget(self.label_21)
        self.comboBox_editStations_station = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_editStations_station.setToolTipDuration(100)
        self.comboBox_editStations_station.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.comboBox_editStations_station.setObjectName("comboBox_editStations_station")
        self.horizontalLayout_14.addWidget(self.comboBox_editStations_station)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_15.addWidget(self.label_22)
        self.comboBox_editStations_action = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_editStations_action.setObjectName("comboBox_editStations_action")
        self.comboBox_editStations_action.addItem("")
        self.comboBox_editStations_action.addItem("")
        self.horizontalLayout_15.addWidget(self.comboBox_editStations_action)
        self.verticalLayout_5.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_16.addWidget(self.label_3)
        self.spinBox_editStations_hour = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_editStations_hour.setMaximum(23)
        self.spinBox_editStations_hour.setObjectName("spinBox_editStations_hour")
        self.horizontalLayout_16.addWidget(self.spinBox_editStations_hour)
        self.spinBox_editStations_minute = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_editStations_minute.setMaximum(59)
        self.spinBox_editStations_minute.setObjectName("spinBox_editStations_minute")
        self.horizontalLayout_16.addWidget(self.spinBox_editStations_minute)
        self.verticalLayout_5.addLayout(self.horizontalLayout_16)
        self.pushButton_editStations = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_editStations.setObjectName("pushButton_editStations")
        self.verticalLayout_5.addWidget(self.pushButton_editStations)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_5.addWidget(self.label_24)
        self.comboBox_dispatch_line = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_dispatch_line.setObjectName("comboBox_dispatch_line")
        self.comboBox_dispatch_line.addItem("")
        self.comboBox_dispatch_line.addItem("")
        self.verticalLayout_5.addWidget(self.comboBox_dispatch_line)
        self.comboBox_dispatch_block = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_dispatch_block.setObjectName("comboBox_dispatch_block")
        self.verticalLayout_5.addWidget(self.comboBox_dispatch_block)
        self.pushButton_dispatch_block = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dispatch_block.setObjectName("pushButton_dispatch_block")
        self.verticalLayout_5.addWidget(self.pushButton_dispatch_block)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_6.addWidget(self.pushButton)
        self.horizontalLayout_20.addLayout(self.verticalLayout_6)
        self.horizontalLayout_20.setStretch(0, 4)
        self.horizontalLayout_20.setStretch(1, 10)
        self.horizontalLayout_20.setStretch(2, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1187, 21))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCTC_Office = QtGui.QAction(MainWindow)
        self.actionCTC_Office.setObjectName("actionCTC_Office")
        self.actionTest = QtGui.QAction(MainWindow)
        self.actionTest.setObjectName("actionTest")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMain.addAction(self.actionCTC_Office)
        self.menuMain.addAction(self.actionTest)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionExit)
        self.menubar.addAction(self.menuMain.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_manualMode.setText(_translate("MainWindow", "Manual Mode"))
        self.label_10.setText(_translate("MainWindow", "Control Switch"))
        self.label_12.setText(_translate("MainWindow", "Line"))
        self.comboBox_controlSwitch_Line.setItemText(0, _translate("MainWindow", "Red"))
        self.comboBox_controlSwitch_Line.setItemText(1, _translate("MainWindow", "Green"))
        self.comboBox_controlSwitch_Line.setItemText(2, _translate("MainWindow", "Blue"))
        self.label_13.setText(_translate("MainWindow", "Switch"))
        self.label_14.setText(_translate("MainWindow", "Switch Position"))
        self.comboBox_controlSwitch_switchPosition.setItemText(0, _translate("MainWindow", "Normal"))
        self.comboBox_controlSwitch_switchPosition.setItemText(1, _translate("MainWindow", "Reverse"))
        self.pushButton_controlSwitch.setText(_translate("MainWindow", "Set Switch"))
        self.label_5.setText(_translate("MainWindow", "Track Maintenance"))
        self.label_6.setText(_translate("MainWindow", "Line"))
        self.comboBox_trackMaintenance_line.setItemText(0, _translate("MainWindow", "Red"))
        self.comboBox_trackMaintenance_line.setItemText(1, _translate("MainWindow", "Green"))
        self.comboBox_trackMaintenance_line.setItemText(2, _translate("MainWindow", "Blue"))
        self.label_8.setText(_translate("MainWindow", "Block Number"))
        self.label_9.setText(_translate("MainWindow", "Track Status"))
        self.comboBox_trackMaintenance_trackStatus.setItemText(0, _translate("MainWindow", "In Maintenance"))
        self.comboBox_trackMaintenance_trackStatus.setItemText(1, _translate("MainWindow", "Out of Maintenance"))
        self.pushButton_trackMaintenance.setText(_translate("MainWindow", "Set Status"))
        self.label_27.setText(_translate("MainWindow", "Dispatch Trains"))
        self.label_28.setText(_translate("MainWindow", "Line"))
        self.comboBox_dispatchTrain_line.setItemText(0, _translate("MainWindow", "Red"))
        self.comboBox_dispatchTrain_line.setItemText(1, _translate("MainWindow", "Green"))
        self.comboBox_dispatchTrain_line.setItemText(2, _translate("MainWindow", "Blue"))
        item = self.tableWidget_dispatch.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Station"))
        item = self.tableWidget_dispatch.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time"))
        self.pushButton_dispatchTrains.setText(_translate("MainWindow", "Dispatch Train"))
        self.label_2.setText(_translate("MainWindow", "Schedule Trains"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Red Line"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Green Line"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Blue Line"))
        self.pushButton_2.setText(_translate("MainWindow", "Choose File"))
        self.label.setText(_translate("MainWindow", "No File Selected"))
        self.pushButton_scheduleTrains.setText(_translate("MainWindow", "Schedule"))
        self.label_4.setText(_translate("MainWindow", "Throughput"))
        self.RedThroughput.setText(_translate("MainWindow", "0"))
        self.GreenThroughput.setText(_translate("MainWindow", "0"))
        self.label_23.setText(_translate("MainWindow", "Red Line"))
        self.label_25.setText(_translate("MainWindow", "Green Line"))
        self.label_7.setText(_translate("MainWindow", "Blue Line"))
        self.BlueThroughput.setText(_translate("MainWindow", "0"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Block Number"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Line"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Occupancy"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Authority"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Switch Position"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Failure"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Crossing"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Section"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Maintenance Mode"))
        item = self.tableWidget_2.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Infrastructure"))
        item = self.tableWidget_2.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Signal"))
        item = self.tableWidget_2.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Suggested Speed"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Block"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Line"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Occupancy"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Authority"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Switch Position"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Failure"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Crossing"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Section"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Maintenance Mode"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Infrastructure"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Signal"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Suggested Speed"))
        self.outputLabel.setText(_translate("MainWindow", "Output"))
        self.label_11.setText(_translate("MainWindow", "Change Speed"))
        self.label_15.setText(_translate("MainWindow", "Line"))
        self.comboBox_changeSpeed_line.setItemText(0, _translate("MainWindow", "Red"))
        self.comboBox_changeSpeed_line.setItemText(1, _translate("MainWindow", "Green"))
        self.comboBox_changeSpeed_line.setItemText(2, _translate("MainWindow", "Blue"))
        self.label_16.setText(_translate("MainWindow", "Train"))
        self.label_17.setText(_translate("MainWindow", "Speed (mph)"))
        self.pushButton_changeSpeed.setText(_translate("MainWindow", "Set Speed"))
        self.label_18.setText(_translate("MainWindow", "Edit Stations"))
        self.label_19.setText(_translate("MainWindow", "Line"))
        self.comboBox_editStations_line.setItemText(0, _translate("MainWindow", "Red"))
        self.comboBox_editStations_line.setItemText(1, _translate("MainWindow", "Green"))
        self.comboBox_editStations_line.setItemText(2, _translate("MainWindow", "Blue"))
        self.label_20.setText(_translate("MainWindow", "Train"))
        self.label_21.setText(_translate("MainWindow", "Station"))
        self.label_22.setText(_translate("MainWindow", "Action"))
        self.comboBox_editStations_action.setItemText(0, _translate("MainWindow", "Stop"))
        self.comboBox_editStations_action.setItemText(1, _translate("MainWindow", "Skip"))
        self.label_3.setText(_translate("MainWindow", "Time"))
        self.pushButton_editStations.setText(_translate("MainWindow", "Update Station"))
        self.label_24.setText(_translate("MainWindow", "Dispatch to Block"))
        self.comboBox_dispatch_line.setItemText(0, _translate("MainWindow", "Red"))
        self.comboBox_dispatch_line.setItemText(1, _translate("MainWindow", "Green"))
        self.pushButton_dispatch_block.setText(_translate("MainWindow", "Dispatch"))
        self.pushButton.setText(_translate("MainWindow", "Refresh Data"))
        self.menuMain.setTitle(_translate("MainWindow", "Window"))
        self.actionCTC_Office.setText(_translate("MainWindow", "CTC Office"))
        self.actionTest.setText(_translate("MainWindow", "Test"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
