# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QWidget)

class Ui_TestTrainModel(object):
    def setupUi(self, TestTrainModel):
        if not TestTrainModel.objectName():
            TestTrainModel.setObjectName(u"TestTrainModel")
        TestTrainModel.resize(800, 600)
        self.centralwidget = QWidget(TestTrainModel)
        self.centralwidget.setObjectName(u"centralwidget")
        self.speedcmd = QLabel(self.centralwidget)
        self.speedcmd.setObjectName(u"speedcmd")
        self.speedcmd.setGeometry(QRect(250, 210, 101, 16))
        self.speedlmt = QLabel(self.centralwidget)
        self.speedlmt.setObjectName(u"speedlmt")
        self.speedlmt.setGeometry(QRect(450, 210, 71, 16))
        self.signalfailure = QLabel(self.centralwidget)
        self.signalfailure.setObjectName(u"signalfailure")
        self.signalfailure.setGeometry(QRect(30, 270, 181, 16))
        self.temp = QLabel(self.centralwidget)
        self.temp.setObjectName(u"temp")
        self.temp.setGeometry(QRect(450, 120, 161, 16))
        self.brakefailure = QLabel(self.centralwidget)
        self.brakefailure.setObjectName(u"brakefailure")
        self.brakefailure.setGeometry(QRect(450, 240, 131, 16))
        self.length = QLabel(self.centralwidget)
        self.length.setObjectName(u"length")
        self.length.setGeometry(QRect(30, 90, 181, 16))
        self.rdoors = QLabel(self.centralwidget)
        self.rdoors.setObjectName(u"rdoors")
        self.rdoors.setGeometry(QRect(30, 120, 191, 16))
        self.ldoors = QLabel(self.centralwidget)
        self.ldoors.setObjectName(u"ldoors")
        self.ldoors.setGeometry(QRect(250, 120, 161, 16))
        self.eBrake = QPushButton(self.centralwidget)
        self.eBrake.setObjectName(u"eBrake")
        self.eBrake.setGeometry(QRect(200, 380, 201, 111))
        self.eBrake.setCheckable(True)
        self.eBrake.setChecked(False)
        self.mass = QLabel(self.centralwidget)
        self.mass.setObjectName(u"mass")
        self.mass.setGeometry(QRect(250, 90, 161, 16))
        self.grade = QLabel(self.centralwidget)
        self.grade.setObjectName(u"grade")
        self.grade.setGeometry(QRect(30, 240, 41, 16))
        self.brakefail = QPushButton(self.centralwidget)
        self.brakefail.setObjectName(u"brakefail")
        self.brakefail.setGeometry(QRect(560, 360, 201, 51))
        self.brakefail.setCheckable(True)
        self.width = QLabel(self.centralwidget)
        self.width.setObjectName(u"width")
        self.width.setGeometry(QRect(30, 60, 181, 16))
        self.height = QLabel(self.centralwidget)
        self.height.setObjectName(u"height")
        self.height.setGeometry(QRect(30, 30, 151, 16))
        self.tempcmd = QLabel(self.centralwidget)
        self.tempcmd.setObjectName(u"tempcmd")
        self.tempcmd.setGeometry(QRect(30, 210, 101, 16))
        self.light = QLabel(self.centralwidget)
        self.light.setObjectName(u"light")
        self.light.setGeometry(QRect(450, 90, 171, 16))
        self.powercmd = QLabel(self.centralwidget)
        self.powercmd.setObjectName(u"powercmd")
        self.powercmd.setGeometry(QRect(450, 180, 101, 16))
        self.accel = QLabel(self.centralwidget)
        self.accel.setObjectName(u"accel")
        self.accel.setGeometry(QRect(450, 60, 171, 16))
        self.enginefailure = QLabel(self.centralwidget)
        self.enginefailure.setObjectName(u"enginefailure")
        self.enginefailure.setGeometry(QRect(250, 240, 141, 16))
        self.crew = QLabel(self.centralwidget)
        self.crew.setObjectName(u"crew")
        self.crew.setGeometry(QRect(250, 60, 161, 16))
        self.signalfail = QPushButton(self.centralwidget)
        self.signalfail.setObjectName(u"signalfail")
        self.signalfail.setGeometry(QRect(560, 430, 201, 51))
        self.signalfail.setCheckable(True)
        self.speed = QLabel(self.centralwidget)
        self.speed.setObjectName(u"speed")
        self.speed.setGeometry(QRect(450, 30, 161, 16))
        self.enginefail = QPushButton(self.centralwidget)
        self.enginefail.setObjectName(u"enginefail")
        self.enginefail.setGeometry(QRect(560, 290, 201, 51))
        self.enginefail.setCheckable(True)
        self.passenger = QLabel(self.centralwidget)
        self.passenger.setObjectName(u"passenger")
        self.passenger.setGeometry(QRect(250, 30, 161, 16))
        self.gradebox = QSpinBox(self.centralwidget)
        self.gradebox.setObjectName(u"gradebox")
        self.gradebox.setGeometry(QRect(70, 240, 42, 25))
        self.gradebox.setMaximum(30)
        self.speedlmtbox = QSpinBox(self.centralwidget)
        self.speedlmtbox.setObjectName(u"speedlmtbox")
        self.speedlmtbox.setGeometry(QRect(530, 210, 42, 25))
        self.speedlmtbox.setMaximum(40)
        self.speedlmtbox.setValue(40)
        self.speedcmdbox = QSpinBox(self.centralwidget)
        self.speedcmdbox.setObjectName(u"speedcmdbox")
        self.speedcmdbox.setGeometry(QRect(350, 210, 42, 25))
        self.speedcmdbox.setMaximum(40)
        self.speedcmdbox.setValue(35)
        self.tempbox = QSpinBox(self.centralwidget)
        self.tempbox.setObjectName(u"tempbox")
        self.tempbox.setGeometry(QRect(130, 210, 42, 25))
        self.tempbox.setMinimum(55)
        self.tempbox.setMaximum(90)
        self.tempbox.setValue(70)
        self.powerbox = QSpinBox(self.centralwidget)
        self.powerbox.setObjectName(u"powerbox")
        self.powerbox.setGeometry(QRect(560, 180, 42, 25))
        self.powerbox.setMaximum(120)
        self.powerbox.setValue(0)
        self.sbrakecmd = QPushButton(self.centralwidget)
        self.sbrakecmd.setObjectName(u"sbrakecmd")
        self.sbrakecmd.setGeometry(QRect(220, 180, 141, 24))
        self.ebrakecmd = QPushButton(self.centralwidget)
        self.ebrakecmd.setObjectName(u"ebrakecmd")
        self.ebrakecmd.setGeometry(QRect(30, 180, 141, 24))
        self.lightcmd = QPushButton(self.centralwidget)
        self.lightcmd.setObjectName(u"lightcmd")
        self.lightcmd.setGeometry(QRect(430, 150, 141, 24))
        self.ldoorcmd = QPushButton(self.centralwidget)
        self.ldoorcmd.setObjectName(u"ldoorcmd")
        self.ldoorcmd.setGeometry(QRect(220, 150, 141, 24))
        self.rdoorcmd = QPushButton(self.centralwidget)
        self.rdoorcmd.setObjectName(u"rdoorcmd")
        self.rdoorcmd.setGeometry(QRect(30, 150, 141, 24))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 240, 49, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 210, 49, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 210, 49, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(580, 210, 49, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(610, 180, 49, 16))
        TestTrainModel.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TestTrainModel)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        TestTrainModel.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TestTrainModel)
        self.statusbar.setObjectName(u"statusbar")
        TestTrainModel.setStatusBar(self.statusbar)

        self.retranslateUi(TestTrainModel)

        QMetaObject.connectSlotsByName(TestTrainModel)
    # setupUi

    def retranslateUi(self, TestTrainModel):
        TestTrainModel.setWindowTitle(QCoreApplication.translate("TestTrainModel", u"TestTrainModel", None))
        self.speedcmd.setText(QCoreApplication.translate("TestTrainModel", u"Speed Command:", None))
        self.speedlmt.setText(QCoreApplication.translate("TestTrainModel", u"Speed Limit:", None))
        self.signalfailure.setText(QCoreApplication.translate("TestTrainModel", u"TextLabel", None))
        self.temp.setText(QCoreApplication.translate("TestTrainModel", u"TextLabel", None))
        self.brakefailure.setText(QCoreApplication.translate("TestTrainModel", u"TextLabel", None))
        self.length.setText(QCoreApplication.translate("TestTrainModel", u"TextLabel", None))
        self.rdoors.setText(QCoreApplication.translate("TestTrainModel", u"TextLabel", None))
        self.ldoors.setText(QCoreApplication.translate("TestTrainModel", u"TextLabel", None))
        self.eBrake.setText(QCoreApplication.translate("TestTrainModel", u"Emergency Brake", None))
        self.mass.setText(QCoreApplication.translate("TestTrainModel", u"TextLabel", None))
        self.grade.setText(QCoreApplication.translate("TestTrainModel", u"Grade: ", None))
        self.brakefail.setText(QCoreApplication.translate("TestTrainModel", u"Train Brake Failure", None))
        self.width.setText(QCoreApplication.translate("TestTrainModel", u"TextLabel", None))
        self.height.setText(QCoreApplication.translate("TestTrainModel", u"TextLabel", None))
        self.tempcmd.setText(QCoreApplication.translate("TestTrainModel", u"Temperature Cmd:", None))
        self.light.setText(QCoreApplication.translate("TestTrainModel", u"TextLabel", None))
        self.powercmd.setText(QCoreApplication.translate("TestTrainModel", u"Power Command:", None))
        self.accel.setText(QCoreApplication.translate("TestTrainModel", u"TextLabel", None))
        self.enginefailure.setText(QCoreApplication.translate("TestTrainModel", u"TextLabel", None))
        self.crew.setText(QCoreApplication.translate("TestTrainModel", u"TextLabel", None))
        self.signalfail.setText(QCoreApplication.translate("TestTrainModel", u"Signal Pickup Failure", None))
        self.speed.setText(QCoreApplication.translate("TestTrainModel", u"TextLabel", None))
        self.enginefail.setText(QCoreApplication.translate("TestTrainModel", u"Train Engine Failure", None))
        self.passenger.setText(QCoreApplication.translate("TestTrainModel", u"TextLabel", None))
        self.sbrakecmd.setText(QCoreApplication.translate("TestTrainModel", u"Service Brake Cmd", None))
        self.ebrakecmd.setText(QCoreApplication.translate("TestTrainModel", u"E Brake Cmd", None))
        self.lightcmd.setText(QCoreApplication.translate("TestTrainModel", u"Light Command", None))
        self.ldoorcmd.setText(QCoreApplication.translate("TestTrainModel", u"Left Door Cmd", None))
        self.rdoorcmd.setText(QCoreApplication.translate("TestTrainModel", u"Right Door Cmd", None))
        self.label.setText(QCoreApplication.translate("TestTrainModel", u"deg", None))
        self.label_2.setText(QCoreApplication.translate("TestTrainModel", u"F", None))
        self.label_3.setText(QCoreApplication.translate("TestTrainModel", u"mph", None))
        self.label_4.setText(QCoreApplication.translate("TestTrainModel", u"mph", None))
        self.label_5.setText(QCoreApplication.translate("TestTrainModel", u"kW", None))
    # retranslateUi

