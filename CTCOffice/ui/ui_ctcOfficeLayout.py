# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ctcOfficeLayout.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QColumnView, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1195, 739)
        MainWindow.setStyleSheet(u"")
        self.actionCTC_Office = QAction(MainWindow)
        self.actionCTC_Office.setObjectName(u"actionCTC_Office")
        self.actionTest = QAction(MainWindow)
        self.actionTest.setObjectName(u"actionTest")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_20 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton_manualMode = QPushButton(self.centralwidget)
        self.pushButton_manualMode.setObjectName(u"pushButton_manualMode")
        self.pushButton_manualMode.setStyleSheet(u"QPushButton:checked {background-color: red;}")
        self.pushButton_manualMode.setCheckable(True)
        self.pushButton_manualMode.setAutoDefault(False)
        self.pushButton_manualMode.setFlat(False)

        self.verticalLayout_10.addWidget(self.pushButton_manualMode)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_10.setFont(font)

        self.verticalLayout_2.addWidget(self.label_10)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.comboBox_controlSwitch_Line = QComboBox(self.centralwidget)
        self.comboBox_controlSwitch_Line.addItem("")
        self.comboBox_controlSwitch_Line.addItem("")
        self.comboBox_controlSwitch_Line.addItem("")
        self.comboBox_controlSwitch_Line.setObjectName(u"comboBox_controlSwitch_Line")

        self.horizontalLayout_6.addWidget(self.comboBox_controlSwitch_Line)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_7.addWidget(self.label_13)

        self.comboBox_controlSwitch_switch = QComboBox(self.centralwidget)
        self.comboBox_controlSwitch_switch.setObjectName(u"comboBox_controlSwitch_switch")

        self.horizontalLayout_7.addWidget(self.comboBox_controlSwitch_switch)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_8.addWidget(self.label_14)

        self.comboBox_controlSwitch_switchPosition = QComboBox(self.centralwidget)
        self.comboBox_controlSwitch_switchPosition.addItem("")
        self.comboBox_controlSwitch_switchPosition.addItem("")
        self.comboBox_controlSwitch_switchPosition.setObjectName(u"comboBox_controlSwitch_switchPosition")

        self.horizontalLayout_8.addWidget(self.comboBox_controlSwitch_switchPosition)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.pushButton_controlSwitch = QPushButton(self.centralwidget)
        self.pushButton_controlSwitch.setObjectName(u"pushButton_controlSwitch")

        self.verticalLayout_2.addWidget(self.pushButton_controlSwitch)


        self.verticalLayout_10.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.comboBox_trackMaintenance_line = QComboBox(self.centralwidget)
        self.comboBox_trackMaintenance_line.addItem("")
        self.comboBox_trackMaintenance_line.addItem("")
        self.comboBox_trackMaintenance_line.addItem("")
        self.comboBox_trackMaintenance_line.setObjectName(u"comboBox_trackMaintenance_line")

        self.horizontalLayout.addWidget(self.comboBox_trackMaintenance_line)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.comboBox_trackMaintenance_blockNumber = QComboBox(self.centralwidget)
        self.comboBox_trackMaintenance_blockNumber.setObjectName(u"comboBox_trackMaintenance_blockNumber")

        self.horizontalLayout_3.addWidget(self.comboBox_trackMaintenance_blockNumber)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.comboBox_trackMaintenance_trackStatus = QComboBox(self.centralwidget)
        self.comboBox_trackMaintenance_trackStatus.addItem("")
        self.comboBox_trackMaintenance_trackStatus.addItem("")
        self.comboBox_trackMaintenance_trackStatus.setObjectName(u"comboBox_trackMaintenance_trackStatus")

        self.horizontalLayout_4.addWidget(self.comboBox_trackMaintenance_trackStatus)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.pushButton_trackMaintenance = QPushButton(self.centralwidget)
        self.pushButton_trackMaintenance.setObjectName(u"pushButton_trackMaintenance")

        self.verticalLayout.addWidget(self.pushButton_trackMaintenance)


        self.verticalLayout_10.addLayout(self.verticalLayout)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)

        self.verticalLayout_9.addWidget(self.label_27)

        self.label_28 = QLabel(self.centralwidget)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_9.addWidget(self.label_28)

        self.comboBox_dispatchTrain_line = QComboBox(self.centralwidget)
        self.comboBox_dispatchTrain_line.addItem("")
        self.comboBox_dispatchTrain_line.addItem("")
        self.comboBox_dispatchTrain_line.addItem("")
        self.comboBox_dispatchTrain_line.setObjectName(u"comboBox_dispatchTrain_line")

        self.verticalLayout_9.addWidget(self.comboBox_dispatchTrain_line)

        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_9.addWidget(self.label_24)

        self.comboBox_dispatchTrain_station = QComboBox(self.centralwidget)
        self.comboBox_dispatchTrain_station.setObjectName(u"comboBox_dispatchTrain_station")

        self.verticalLayout_9.addWidget(self.comboBox_dispatchTrain_station)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_29 = QLabel(self.centralwidget)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_19.addWidget(self.label_29)

        self.spinBox_dispatchTrain_hour = QSpinBox(self.centralwidget)
        self.spinBox_dispatchTrain_hour.setObjectName(u"spinBox_dispatchTrain_hour")
        self.spinBox_dispatchTrain_hour.setMaximum(23)

        self.horizontalLayout_19.addWidget(self.spinBox_dispatchTrain_hour)

        self.spinBox_dispatchTrain_minute = QSpinBox(self.centralwidget)
        self.spinBox_dispatchTrain_minute.setObjectName(u"spinBox_dispatchTrain_minute")
        self.spinBox_dispatchTrain_minute.setMaximum(59)

        self.horizontalLayout_19.addWidget(self.spinBox_dispatchTrain_minute)


        self.verticalLayout_9.addLayout(self.horizontalLayout_19)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 200, 155))
        self.horizontalLayout_18 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.columnView = QColumnView(self.scrollAreaWidgetContents)
        self.columnView.setObjectName(u"columnView")

        self.horizontalLayout_18.addWidget(self.columnView)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_9.addWidget(self.scrollArea)

        self.pushButton_dispatchTrains = QPushButton(self.centralwidget)
        self.pushButton_dispatchTrains.setObjectName(u"pushButton_dispatchTrains")

        self.verticalLayout_9.addWidget(self.pushButton_dispatchTrains)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)


        self.horizontalLayout_20.addLayout(self.verticalLayout_10)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_3.addWidget(self.comboBox)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.pushButton_scheduleTrains = QPushButton(self.centralwidget)
        self.pushButton_scheduleTrains.setObjectName(u"pushButton_scheduleTrains")

        self.verticalLayout_3.addWidget(self.pushButton_scheduleTrains)


        self.horizontalLayout_17.addLayout(self.verticalLayout_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_7.addWidget(self.label_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.RedThroughput = QLabel(self.centralwidget)
        self.RedThroughput.setObjectName(u"RedThroughput")
        self.RedThroughput.setFont(font)

        self.gridLayout.addWidget(self.RedThroughput, 1, 1, 1, 1)

        self.GreenThroughput = QLabel(self.centralwidget)
        self.GreenThroughput.setObjectName(u"GreenThroughput")
        self.GreenThroughput.setFont(font)

        self.gridLayout.addWidget(self.GreenThroughput, 2, 1, 1, 1)

        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 1, 0, 1, 1)

        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout.addWidget(self.label_25, 2, 0, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.BlueThroughput = QLabel(self.centralwidget)
        self.BlueThroughput.setObjectName(u"BlueThroughput")
        self.BlueThroughput.setFont(font)

        self.gridLayout.addWidget(self.BlueThroughput, 0, 1, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout)


        self.horizontalLayout_17.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_17)

        self.tableWidget_2 = QTableWidget(self.centralwidget)
        if (self.tableWidget_2.columnCount() < 12):
            self.tableWidget_2.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy1)
        self.tableWidget_2.setToolTipDuration(-1)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.tableWidget_2)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 12):
            self.tableWidget.setColumnCount(12)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.tableWidget)

        self.outputLabel = QLabel(self.centralwidget)
        self.outputLabel.setObjectName(u"outputLabel")
        font1 = QFont()
        font1.setFamilies([u"Terminal"])
        font1.setPointSize(9)
        self.outputLabel.setFont(font1)

        self.verticalLayout_8.addWidget(self.outputLabel)


        self.horizontalLayout_20.addLayout(self.verticalLayout_8)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.verticalLayout_4.addWidget(self.label_11)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_9.addWidget(self.label_15)

        self.comboBox_changeSpeed_line = QComboBox(self.centralwidget)
        self.comboBox_changeSpeed_line.addItem("")
        self.comboBox_changeSpeed_line.addItem("")
        self.comboBox_changeSpeed_line.addItem("")
        self.comboBox_changeSpeed_line.setObjectName(u"comboBox_changeSpeed_line")

        self.horizontalLayout_9.addWidget(self.comboBox_changeSpeed_line)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_10.addWidget(self.label_16)

        self.comboBox_changeSpeed_train = QComboBox(self.centralwidget)
        self.comboBox_changeSpeed_train.setObjectName(u"comboBox_changeSpeed_train")

        self.horizontalLayout_10.addWidget(self.comboBox_changeSpeed_train)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_11.addWidget(self.label_17)

        self.spinBox_changeSpeed_speed = QSpinBox(self.centralwidget)
        self.spinBox_changeSpeed_speed.setObjectName(u"spinBox_changeSpeed_speed")

        self.horizontalLayout_11.addWidget(self.spinBox_changeSpeed_speed)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.pushButton_changeSpeed = QPushButton(self.centralwidget)
        self.pushButton_changeSpeed.setObjectName(u"pushButton_changeSpeed")

        self.verticalLayout_4.addWidget(self.pushButton_changeSpeed)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.verticalLayout_5.addWidget(self.label_18)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_12.addWidget(self.label_19)

        self.comboBox_editStations_line = QComboBox(self.centralwidget)
        self.comboBox_editStations_line.addItem("")
        self.comboBox_editStations_line.addItem("")
        self.comboBox_editStations_line.addItem("")
        self.comboBox_editStations_line.setObjectName(u"comboBox_editStations_line")

        self.horizontalLayout_12.addWidget(self.comboBox_editStations_line)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_13.addWidget(self.label_20)

        self.comboBox_editStations_train = QComboBox(self.centralwidget)
        self.comboBox_editStations_train.setObjectName(u"comboBox_editStations_train")

        self.horizontalLayout_13.addWidget(self.comboBox_editStations_train)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_14.addWidget(self.label_21)

        self.comboBox_editStations_station = QComboBox(self.centralwidget)
        self.comboBox_editStations_station.setObjectName(u"comboBox_editStations_station")
        self.comboBox_editStations_station.setToolTipDuration(100)
        self.comboBox_editStations_station.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_14.addWidget(self.comboBox_editStations_station)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_15.addWidget(self.label_22)

        self.comboBox_editStations_action = QComboBox(self.centralwidget)
        self.comboBox_editStations_action.addItem("")
        self.comboBox_editStations_action.addItem("")
        self.comboBox_editStations_action.setObjectName(u"comboBox_editStations_action")

        self.horizontalLayout_15.addWidget(self.comboBox_editStations_action)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_16.addWidget(self.label_3)

        self.spinBox_editStations_hour = QSpinBox(self.centralwidget)
        self.spinBox_editStations_hour.setObjectName(u"spinBox_editStations_hour")
        self.spinBox_editStations_hour.setMaximum(23)

        self.horizontalLayout_16.addWidget(self.spinBox_editStations_hour)

        self.spinBox_editStations_minute = QSpinBox(self.centralwidget)
        self.spinBox_editStations_minute.setObjectName(u"spinBox_editStations_minute")
        self.spinBox_editStations_minute.setMaximum(59)

        self.horizontalLayout_16.addWidget(self.spinBox_editStations_minute)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.pushButton_editStations = QPushButton(self.centralwidget)
        self.pushButton_editStations.setObjectName(u"pushButton_editStations")

        self.verticalLayout_5.addWidget(self.pushButton_editStations)

        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)

        self.verticalLayout_5.addWidget(self.label_26)

        self.pushButton_startSim = QPushButton(self.centralwidget)
        self.pushButton_startSim.setObjectName(u"pushButton_startSim")

        self.verticalLayout_5.addWidget(self.pushButton_startSim)

        self.pushButton_stopSim = QPushButton(self.centralwidget)
        self.pushButton_stopSim.setObjectName(u"pushButton_stopSim")

        self.verticalLayout_5.addWidget(self.pushButton_stopSim)

        self.pushButton_resetSim = QPushButton(self.centralwidget)
        self.pushButton_resetSim.setObjectName(u"pushButton_resetSim")

        self.verticalLayout_5.addWidget(self.pushButton_resetSim)

        self.label_simStatus = QLabel(self.centralwidget)
        self.label_simStatus.setObjectName(u"label_simStatus")

        self.verticalLayout_5.addWidget(self.label_simStatus)

        self.label_31 = QLabel(self.centralwidget)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_5.addWidget(self.label_31)

        self.label_currentTime = QLabel(self.centralwidget)
        self.label_currentTime.setObjectName(u"label_currentTime")

        self.verticalLayout_5.addWidget(self.label_currentTime)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.comboBox_selectLineGraph = QComboBox(self.centralwidget)
        self.comboBox_selectLineGraph.addItem("")
        self.comboBox_selectLineGraph.addItem("")
        self.comboBox_selectLineGraph.setObjectName(u"comboBox_selectLineGraph")

        self.verticalLayout_6.addWidget(self.comboBox_selectLineGraph)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_6.addWidget(self.pushButton)

        self.pushButton_openTestUi = QPushButton(self.centralwidget)
        self.pushButton_openTestUi.setObjectName(u"pushButton_openTestUi")

        self.verticalLayout_6.addWidget(self.pushButton_openTestUi)


        self.horizontalLayout_20.addLayout(self.verticalLayout_6)

        self.horizontalLayout_20.setStretch(0, 1)
        self.horizontalLayout_20.setStretch(1, 10)
        self.horizontalLayout_20.setStretch(2, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1195, 22))
        self.menuMain = QMenu(self.menubar)
        self.menuMain.setObjectName(u"menuMain")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMain.menuAction())
        self.menuMain.addAction(self.actionCTC_Office)
        self.menuMain.addAction(self.actionTest)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionCTC_Office.setText(QCoreApplication.translate("MainWindow", u"CTC Office", None))
        self.actionTest.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton_manualMode.setText(QCoreApplication.translate("MainWindow", u"Manual Mode", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Control Switch", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.comboBox_controlSwitch_Line.setItemText(0, QCoreApplication.translate("MainWindow", u"Red", None))
        self.comboBox_controlSwitch_Line.setItemText(1, QCoreApplication.translate("MainWindow", u"Green", None))
        self.comboBox_controlSwitch_Line.setItemText(2, QCoreApplication.translate("MainWindow", u"Blue", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Switch", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.comboBox_controlSwitch_switchPosition.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.comboBox_controlSwitch_switchPosition.setItemText(1, QCoreApplication.translate("MainWindow", u"Reverse", None))

        self.pushButton_controlSwitch.setText(QCoreApplication.translate("MainWindow", u"Set Switch", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Track Maintenance", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.comboBox_trackMaintenance_line.setItemText(0, QCoreApplication.translate("MainWindow", u"Red", None))
        self.comboBox_trackMaintenance_line.setItemText(1, QCoreApplication.translate("MainWindow", u"Green", None))
        self.comboBox_trackMaintenance_line.setItemText(2, QCoreApplication.translate("MainWindow", u"Blue", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Block Number", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Track Status", None))
        self.comboBox_trackMaintenance_trackStatus.setItemText(0, QCoreApplication.translate("MainWindow", u"In Maintenance", None))
        self.comboBox_trackMaintenance_trackStatus.setItemText(1, QCoreApplication.translate("MainWindow", u"Out of Maintenance", None))

        self.pushButton_trackMaintenance.setText(QCoreApplication.translate("MainWindow", u"Set Status", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Dispatch Trains", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.comboBox_dispatchTrain_line.setItemText(0, QCoreApplication.translate("MainWindow", u"Red", None))
        self.comboBox_dispatchTrain_line.setItemText(1, QCoreApplication.translate("MainWindow", u"Green", None))
        self.comboBox_dispatchTrain_line.setItemText(2, QCoreApplication.translate("MainWindow", u"Blue", None))

        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Station", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.pushButton_dispatchTrains.setText(QCoreApplication.translate("MainWindow", u"Dispatch Train", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Schedule Trains", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Red Line", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Blue Line", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Choose File", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"No File Selected", None))
        self.pushButton_scheduleTrains.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Throughput", None))
        self.RedThroughput.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.GreenThroughput.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Red Line", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Blue Line", None))
        self.BlueThroughput.setText(QCoreApplication.translate("MainWindow", u"0", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Block Number", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Authority", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Failure", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Crossing", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Section", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Maintenance Mode", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Infrastructure", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Signal", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Block", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Authority", None));
        ___qtablewidgetitem16 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None));
        ___qtablewidgetitem17 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Failure", None));
        ___qtablewidgetitem18 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Crossing", None));
        ___qtablewidgetitem19 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Section", None));
        ___qtablewidgetitem20 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Maintenance Mode", None));
        ___qtablewidgetitem21 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Infrastructure", None));
        ___qtablewidgetitem22 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Signal", None));
        ___qtablewidgetitem23 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None));
        self.outputLabel.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Change Speed", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.comboBox_changeSpeed_line.setItemText(0, QCoreApplication.translate("MainWindow", u"Red", None))
        self.comboBox_changeSpeed_line.setItemText(1, QCoreApplication.translate("MainWindow", u"Green", None))
        self.comboBox_changeSpeed_line.setItemText(2, QCoreApplication.translate("MainWindow", u"Blue", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Speed (mph)", None))
        self.pushButton_changeSpeed.setText(QCoreApplication.translate("MainWindow", u"Set Speed", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Edit Stations", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.comboBox_editStations_line.setItemText(0, QCoreApplication.translate("MainWindow", u"Red", None))
        self.comboBox_editStations_line.setItemText(1, QCoreApplication.translate("MainWindow", u"Green", None))
        self.comboBox_editStations_line.setItemText(2, QCoreApplication.translate("MainWindow", u"Blue", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Station", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Action", None))
        self.comboBox_editStations_action.setItemText(0, QCoreApplication.translate("MainWindow", u"Stop", None))
        self.comboBox_editStations_action.setItemText(1, QCoreApplication.translate("MainWindow", u"Skip", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.pushButton_editStations.setText(QCoreApplication.translate("MainWindow", u"Update Station", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Simulation Timing", None))
        self.pushButton_startSim.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_stopSim.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton_resetSim.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_simStatus.setText(QCoreApplication.translate("MainWindow", u"Stopped", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Current Time: ", None))
        self.label_currentTime.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.comboBox_selectLineGraph.setItemText(0, QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.comboBox_selectLineGraph.setItemText(1, QCoreApplication.translate("MainWindow", u"Blue Line", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Refresh Data", None))
        self.pushButton_openTestUi.setText(QCoreApplication.translate("MainWindow", u"OPEN TEST UI", None))
        self.menuMain.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
    # retranslateUi

