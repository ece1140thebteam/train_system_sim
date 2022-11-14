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
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(898, 713)
        self.actionCTC_Office = QAction(MainWindow)
        self.actionCTC_Office.setObjectName(u"actionCTC_Office")
        self.actionTest = QAction(MainWindow)
        self.actionTest.setObjectName(u"actionTest")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 841, 668))
        self.horizontalLayout_19 = QHBoxLayout(self.widget)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton_manualMode = QPushButton(self.widget)
        self.pushButton_manualMode.setObjectName(u"pushButton_manualMode")
        self.pushButton_manualMode.setCheckable(True)
        self.pushButton_manualMode.setAutoDefault(False)

        self.verticalLayout_10.addWidget(self.pushButton_manualMode)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_10.setFont(font)

        self.verticalLayout_2.addWidget(self.label_10)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.comboBox_controlSwitch_Line = QComboBox(self.widget)
        self.comboBox_controlSwitch_Line.addItem("")
        self.comboBox_controlSwitch_Line.addItem("")
        self.comboBox_controlSwitch_Line.setObjectName(u"comboBox_controlSwitch_Line")

        self.horizontalLayout_6.addWidget(self.comboBox_controlSwitch_Line)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_7.addWidget(self.label_13)

        self.comboBox_controlSwitch_switch = QComboBox(self.widget)
        self.comboBox_controlSwitch_switch.setObjectName(u"comboBox_controlSwitch_switch")

        self.horizontalLayout_7.addWidget(self.comboBox_controlSwitch_switch)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_8.addWidget(self.label_14)

        self.comboBox_controlSwitch_switchPosition = QComboBox(self.widget)
        self.comboBox_controlSwitch_switchPosition.addItem("")
        self.comboBox_controlSwitch_switchPosition.addItem("")
        self.comboBox_controlSwitch_switchPosition.setObjectName(u"comboBox_controlSwitch_switchPosition")

        self.horizontalLayout_8.addWidget(self.comboBox_controlSwitch_switchPosition)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.pushButton_controlSwitch = QPushButton(self.widget)
        self.pushButton_controlSwitch.setObjectName(u"pushButton_controlSwitch")

        self.verticalLayout_2.addWidget(self.pushButton_controlSwitch)


        self.verticalLayout_10.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.comboBox_trackMaintenance_line = QComboBox(self.widget)
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
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.comboBox_trackMaintenance_blockNumber = QComboBox(self.widget)
        self.comboBox_trackMaintenance_blockNumber.setObjectName(u"comboBox_trackMaintenance_blockNumber")

        self.horizontalLayout_3.addWidget(self.comboBox_trackMaintenance_blockNumber)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.comboBox_trackMaintenance_trackStatus = QComboBox(self.widget)
        self.comboBox_trackMaintenance_trackStatus.addItem("")
        self.comboBox_trackMaintenance_trackStatus.addItem("")
        self.comboBox_trackMaintenance_trackStatus.setObjectName(u"comboBox_trackMaintenance_trackStatus")

        self.horizontalLayout_4.addWidget(self.comboBox_trackMaintenance_trackStatus)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.pushButton_trackMaintenance = QPushButton(self.widget)
        self.pushButton_trackMaintenance.setObjectName(u"pushButton_trackMaintenance")

        self.verticalLayout.addWidget(self.pushButton_trackMaintenance)


        self.verticalLayout_10.addLayout(self.verticalLayout)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_27 = QLabel(self.widget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)

        self.verticalLayout_9.addWidget(self.label_27)

        self.label_28 = QLabel(self.widget)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_9.addWidget(self.label_28)

        self.comboBox_dispatchTrain_line = QComboBox(self.widget)
        self.comboBox_dispatchTrain_line.addItem("")
        self.comboBox_dispatchTrain_line.addItem("")
        self.comboBox_dispatchTrain_line.setObjectName(u"comboBox_dispatchTrain_line")

        self.verticalLayout_9.addWidget(self.comboBox_dispatchTrain_line)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 349, 214))
        self.horizontalLayout_18 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.columnView = QColumnView(self.scrollAreaWidgetContents)
        self.columnView.setObjectName(u"columnView")

        self.horizontalLayout_18.addWidget(self.columnView)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_9.addWidget(self.scrollArea)

        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_9.addWidget(self.pushButton_8)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)


        self.horizontalLayout_19.addLayout(self.verticalLayout_10)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_3.addWidget(self.pushButton_5)


        self.horizontalLayout_17.addLayout(self.verticalLayout_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_7.addWidget(self.label_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 0, 0, 1, 1)

        self.RedThroughput = QLabel(self.widget)
        self.RedThroughput.setObjectName(u"RedThroughput")

        self.gridLayout.addWidget(self.RedThroughput, 0, 1, 1, 1)

        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout.addWidget(self.label_25, 1, 0, 1, 1)

        self.GreenThroughput = QLabel(self.widget)
        self.GreenThroughput.setObjectName(u"GreenThroughput")

        self.gridLayout.addWidget(self.GreenThroughput, 1, 1, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout)


        self.horizontalLayout_17.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_17)

        self.columnView_2 = QColumnView(self.widget)
        self.columnView_2.setObjectName(u"columnView_2")

        self.verticalLayout_8.addWidget(self.columnView_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.horizontalLayout_19.addLayout(self.verticalLayout_8)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.verticalLayout_4.addWidget(self.label_11)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_9.addWidget(self.label_15)

        self.comboBox_changeSpeed_line = QComboBox(self.widget)
        self.comboBox_changeSpeed_line.addItem("")
        self.comboBox_changeSpeed_line.addItem("")
        self.comboBox_changeSpeed_line.setObjectName(u"comboBox_changeSpeed_line")

        self.horizontalLayout_9.addWidget(self.comboBox_changeSpeed_line)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_10.addWidget(self.label_16)

        self.comboBox_changeSpeed_train = QComboBox(self.widget)
        self.comboBox_changeSpeed_train.setObjectName(u"comboBox_changeSpeed_train")

        self.horizontalLayout_10.addWidget(self.comboBox_changeSpeed_train)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_11.addWidget(self.label_17)

        self.spinBox_changeSpeed_speed = QSpinBox(self.widget)
        self.spinBox_changeSpeed_speed.setObjectName(u"spinBox_changeSpeed_speed")

        self.horizontalLayout_11.addWidget(self.spinBox_changeSpeed_speed)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.pushButton_changeSpeed = QPushButton(self.widget)
        self.pushButton_changeSpeed.setObjectName(u"pushButton_changeSpeed")

        self.verticalLayout_4.addWidget(self.pushButton_changeSpeed)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.verticalLayout_5.addWidget(self.label_18)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_19 = QLabel(self.widget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_12.addWidget(self.label_19)

        self.comboBox_editStations_line = QComboBox(self.widget)
        self.comboBox_editStations_line.addItem("")
        self.comboBox_editStations_line.addItem("")
        self.comboBox_editStations_line.setObjectName(u"comboBox_editStations_line")

        self.horizontalLayout_12.addWidget(self.comboBox_editStations_line)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_20 = QLabel(self.widget)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_13.addWidget(self.label_20)

        self.comboBox_editStations_train = QComboBox(self.widget)
        self.comboBox_editStations_train.setObjectName(u"comboBox_editStations_train")

        self.horizontalLayout_13.addWidget(self.comboBox_editStations_train)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_21 = QLabel(self.widget)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_14.addWidget(self.label_21)

        self.comboBox_editStations_station = QComboBox(self.widget)
        self.comboBox_editStations_station.setObjectName(u"comboBox_editStations_station")

        self.horizontalLayout_14.addWidget(self.comboBox_editStations_station)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_15.addWidget(self.label_22)

        self.comboBox_editStations_action = QComboBox(self.widget)
        self.comboBox_editStations_action.addItem("")
        self.comboBox_editStations_action.addItem("")
        self.comboBox_editStations_action.setObjectName(u"comboBox_editStations_action")

        self.horizontalLayout_15.addWidget(self.comboBox_editStations_action)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_16.addWidget(self.label_3)

        self.spinBox = QSpinBox(self.widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(23)

        self.horizontalLayout_16.addWidget(self.spinBox)

        self.spinBox_editStations_time = QSpinBox(self.widget)
        self.spinBox_editStations_time.setObjectName(u"spinBox_editStations_time")
        self.spinBox_editStations_time.setMaximum(59)

        self.horizontalLayout_16.addWidget(self.spinBox_editStations_time)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.pushButton_editStations = QPushButton(self.widget)
        self.pushButton_editStations.setObjectName(u"pushButton_editStations")

        self.verticalLayout_5.addWidget(self.pushButton_editStations)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.horizontalLayout_19.addLayout(self.verticalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 898, 22))
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

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Switch", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.comboBox_controlSwitch_switchPosition.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.comboBox_controlSwitch_switchPosition.setItemText(1, QCoreApplication.translate("MainWindow", u"Reverse", None))

        self.pushButton_controlSwitch.setText(QCoreApplication.translate("MainWindow", u"Set Switch", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Track Maintenance", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.comboBox_trackMaintenance_line.setItemText(0, QCoreApplication.translate("MainWindow", u"Red", None))
        self.comboBox_trackMaintenance_line.setItemText(1, QCoreApplication.translate("MainWindow", u"Green", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Block Number", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Track Status", None))
        self.comboBox_trackMaintenance_trackStatus.setItemText(0, QCoreApplication.translate("MainWindow", u"In Maintenance", None))
        self.comboBox_trackMaintenance_trackStatus.setItemText(1, QCoreApplication.translate("MainWindow", u"Out of Maintenance", None))

        self.pushButton_trackMaintenance.setText(QCoreApplication.translate("MainWindow", u"Set Status", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Dispatch Trains", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.comboBox_dispatchTrain_line.setItemText(0, QCoreApplication.translate("MainWindow", u"Red", None))
        self.comboBox_dispatchTrain_line.setItemText(1, QCoreApplication.translate("MainWindow", u"Green", None))

        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Dispatch Train", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Schedule Trains", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Choose File", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"No File Selected", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Throughput", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Red Line", None))
        self.RedThroughput.setText(QCoreApplication.translate("MainWindow", u"Throughput", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.GreenThroughput.setText(QCoreApplication.translate("MainWindow", u"Throughput", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Change Speed", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.comboBox_changeSpeed_line.setItemText(0, QCoreApplication.translate("MainWindow", u"Red", None))
        self.comboBox_changeSpeed_line.setItemText(1, QCoreApplication.translate("MainWindow", u"Green", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Speed (mph)", None))
        self.pushButton_changeSpeed.setText(QCoreApplication.translate("MainWindow", u"Set Speed", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Edit Stations", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.comboBox_editStations_line.setItemText(0, QCoreApplication.translate("MainWindow", u"Red", None))
        self.comboBox_editStations_line.setItemText(1, QCoreApplication.translate("MainWindow", u"Green", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Station", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Action", None))
        self.comboBox_editStations_action.setItemText(0, QCoreApplication.translate("MainWindow", u"Stop", None))
        self.comboBox_editStations_action.setItemText(1, QCoreApplication.translate("MainWindow", u"Skip", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.pushButton_editStations.setText(QCoreApplication.translate("MainWindow", u"Update Station", None))
        self.menuMain.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
    # retranslateUi

