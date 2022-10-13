# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDial, QLabel,
    QPushButton, QSizePolicy, QSlider, QTextEdit,
    QWidget)

class Ui_TrainCTRLTestUI(object):
    def setupUi(self, TrainCTRLTestUI):
        if not TrainCTRLTestUI.objectName():
            TrainCTRLTestUI.setObjectName(u"TrainCTRLTestUI")
        TrainCTRLTestUI.resize(967, 616)
        self.speedLabel = QLabel(TrainCTRLTestUI)
        self.speedLabel.setObjectName(u"speedLabel")
        self.speedLabel.setGeometry(QRect(770, 210, 151, 51))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush)
        brush1 = QBrush(QColor(127, 127, 127, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        brush2 = QBrush(QColor(170, 170, 170, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush3)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        brush4 = QBrush(QColor(240, 240, 240, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        brush5 = QBrush(QColor(227, 227, 227, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush5)
        brush6 = QBrush(QColor(160, 160, 160, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        brush7 = QBrush(QColor(105, 105, 105, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(245, 245, 245, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        self.speedLabel.setPalette(palette)
        font = QFont()
        font.setPointSize(18)
        self.speedLabel.setFont(font)
        self.ldoorBtn = QPushButton(TrainCTRLTestUI)
        self.ldoorBtn.setObjectName(u"ldoorBtn")
        self.ldoorBtn.setGeometry(QRect(780, 470, 121, 51))
        font1 = QFont()
        font1.setPointSize(14)
        self.ldoorBtn.setFont(font1)
        self.sBrakeBtn = QPushButton(TrainCTRLTestUI)
        self.sBrakeBtn.setObjectName(u"sBrakeBtn")
        self.sBrakeBtn.setGeometry(QRect(630, 250, 131, 191))
        palette1 = QPalette()
        brush9 = QBrush(QColor(255, 0, 0, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush)
        brush10 = QBrush(QColor(255, 95, 89, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        brush11 = QBrush(QColor(255, 80, 80, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush11)
        self.sBrakeBtn.setPalette(palette1)
        font2 = QFont()
        font2.setPointSize(16)
        self.sBrakeBtn.setFont(font2)
        self.speedSlider = QSlider(TrainCTRLTestUI)
        self.speedSlider.setObjectName(u"speedSlider")
        self.speedSlider.setGeometry(QRect(790, 270, 22, 160))
        self.speedSlider.setMaximum(40)
        self.speedSlider.setOrientation(Qt.Vertical)
        self.speedSlider.setTickPosition(QSlider.TicksBothSides)
        self.speedSlider.setTickInterval(1)
        self.tempDial = QDial(TrainCTRLTestUI)
        self.tempDial.setObjectName(u"tempDial")
        self.tempDial.setGeometry(QRect(190, 120, 50, 64))
        self.tempDial.setMinimum(55)
        self.tempDial.setMaximum(90)
        self.rdoorBtn = QPushButton(TrainCTRLTestUI)
        self.rdoorBtn.setObjectName(u"rdoorBtn")
        self.rdoorBtn.setGeometry(QRect(780, 530, 121, 51))
        self.rdoorBtn.setFont(font1)
        self.trackSigStatus = QLabel(TrainCTRLTestUI)
        self.trackSigStatus.setObjectName(u"trackSigStatus")
        self.trackSigStatus.setGeometry(QRect(290, 260, 171, 31))
        self.curTempLabel = QLabel(TrainCTRLTestUI)
        self.curTempLabel.setObjectName(u"curTempLabel")
        self.curTempLabel.setGeometry(QRect(40, 140, 161, 21))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush3)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        self.curTempLabel.setPalette(palette2)
        font3 = QFont()
        font3.setPointSize(12)
        self.curTempLabel.setFont(font3)
        self.manModeBtn = QPushButton(TrainCTRLTestUI)
        self.manModeBtn.setObjectName(u"manModeBtn")
        self.manModeBtn.setGeometry(QRect(640, 140, 261, 61))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush11)
        self.manModeBtn.setPalette(palette3)
        self.manModeBtn.setFont(font2)
        self.curSpd = QLabel(TrainCTRLTestUI)
        self.curSpd.setObjectName(u"curSpd")
        self.curSpd.setGeometry(QRect(600, 20, 261, 51))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush3)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        self.curSpd.setPalette(palette4)
        self.curSpd.setFont(font)
        self.engFailStatus = QLabel(TrainCTRLTestUI)
        self.engFailStatus.setObjectName(u"engFailStatus")
        self.engFailStatus.setGeometry(QRect(290, 160, 191, 41))
        self.ilightBtn = QPushButton(TrainCTRLTestUI)
        self.ilightBtn.setObjectName(u"ilightBtn")
        self.ilightBtn.setGeometry(QRect(630, 470, 131, 51))
        palette5 = QPalette()
        brush12 = QBrush(QColor(255, 255, 0, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush)
        self.ilightBtn.setPalette(palette5)
        self.ilightBtn.setFont(font1)
        self.faultLabel = QLabel(TrainCTRLTestUI)
        self.faultLabel.setObjectName(u"faultLabel")
        self.faultLabel.setGeometry(QRect(280, 110, 201, 51))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Button, brush)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush3)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        self.faultLabel.setPalette(palette6)
        self.faultLabel.setFont(font)
        self.brakeFailStatus = QLabel(TrainCTRLTestUI)
        self.brakeFailStatus.setObjectName(u"brakeFailStatus")
        self.brakeFailStatus.setGeometry(QRect(290, 210, 191, 41))
        self.eBrakeBtn = QPushButton(TrainCTRLTestUI)
        self.eBrakeBtn.setObjectName(u"eBrakeBtn")
        self.eBrakeBtn.setGeometry(QRect(270, 310, 261, 91))
        palette7 = QPalette()
        brush13 = QBrush(QColor(240, 0, 0, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush9)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush)
        self.eBrakeBtn.setPalette(palette7)
        font4 = QFont()
        font4.setPointSize(20)
        self.eBrakeBtn.setFont(font4)
        self.eBrakeBtn.setCheckable(False)
        self.tempLabel = QLabel(TrainCTRLTestUI)
        self.tempLabel.setObjectName(u"tempLabel")
        self.tempLabel.setGeometry(QRect(30, 70, 231, 51))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Button, brush)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush)
        palette8.setBrush(QPalette.Active, QPalette.Shadow, brush3)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Shadow, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        self.tempLabel.setPalette(palette8)
        self.tempLabel.setFont(font)
        self.intercomBtn = QPushButton(TrainCTRLTestUI)
        self.intercomBtn.setObjectName(u"intercomBtn")
        self.intercomBtn.setGeometry(QRect(60, 230, 141, 121))
        palette9 = QPalette()
        brush14 = QBrush(QColor(170, 170, 127, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush14)
        brush15 = QBrush(QColor(255, 255, 190, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.Light, brush15)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Light, brush)
        self.intercomBtn.setPalette(palette9)
        self.intercomBtn.setFont(font4)
        self.intercomBtn.setCheckable(False)
        self.cmdSpd = QLabel(TrainCTRLTestUI)
        self.cmdSpd.setObjectName(u"cmdSpd")
        self.cmdSpd.setGeometry(QRect(540, 60, 331, 51))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.Button, brush)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush2)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush)
        palette10.setBrush(QPalette.Active, QPalette.Shadow, brush3)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Shadow, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        self.cmdSpd.setPalette(palette10)
        self.cmdSpd.setFont(font)
        self.elightBtn = QPushButton(TrainCTRLTestUI)
        self.elightBtn.setObjectName(u"elightBtn")
        self.elightBtn.setGeometry(QRect(630, 530, 131, 51))
        self.elightBtn.setFont(font1)
        self.driverSpd = QLabel(TrainCTRLTestUI)
        self.driverSpd.setObjectName(u"driverSpd")
        self.driverSpd.setGeometry(QRect(830, 330, 101, 51))
        self.driverSpd.setFont(font4)
        self.activateEFault = QPushButton(TrainCTRLTestUI)
        self.activateEFault.setObjectName(u"activateEFault")
        self.activateEFault.setGeometry(QRect(40, 450, 151, 41))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette11.setBrush(QPalette.Active, QPalette.Light, brush9)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Light, brush)
        self.activateEFault.setPalette(palette11)
        self.activateEFault.setFont(font3)
        self.activateEFault.setCheckable(False)
        self.faultLabel_2 = QLabel(TrainCTRLTestUI)
        self.faultLabel_2.setObjectName(u"faultLabel_2")
        self.faultLabel_2.setGeometry(QRect(50, 390, 201, 51))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.Button, brush)
        palette12.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette12.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Mid, brush2)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush)
        palette12.setBrush(QPalette.Active, QPalette.Shadow, brush3)
        palette12.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Midlight, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.Dark, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Mid, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette12.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Mid, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Shadow, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        self.faultLabel_2.setPalette(palette12)
        self.faultLabel_2.setFont(font)
        self.activateBFault = QPushButton(TrainCTRLTestUI)
        self.activateBFault.setObjectName(u"activateBFault")
        self.activateBFault.setGeometry(QRect(40, 500, 151, 41))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette13.setBrush(QPalette.Active, QPalette.Light, brush9)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Light, brush)
        self.activateBFault.setPalette(palette13)
        self.activateBFault.setFont(font3)
        self.activateBFault.setCheckable(False)
        self.activateSFault = QPushButton(TrainCTRLTestUI)
        self.activateSFault.setObjectName(u"activateSFault")
        self.activateSFault.setGeometry(QRect(40, 550, 151, 41))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette14.setBrush(QPalette.Active, QPalette.Light, brush9)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Light, brush)
        self.activateSFault.setPalette(palette14)
        self.activateSFault.setFont(font3)
        self.activateSFault.setCheckable(False)
        self.cmdSpdInput = QTextEdit(TrainCTRLTestUI)
        self.cmdSpdInput.setObjectName(u"cmdSpdInput")
        self.cmdSpdInput.setGeometry(QRect(390, 470, 91, 21))
        self.cmdSpdInput.setReadOnly(False)
        self.iolabel = QLabel(TrainCTRLTestUI)
        self.iolabel.setObjectName(u"iolabel")
        self.iolabel.setGeometry(QRect(300, 410, 201, 51))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.Button, brush)
        palette15.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette15.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Mid, brush2)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush)
        palette15.setBrush(QPalette.Active, QPalette.Shadow, brush3)
        palette15.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Midlight, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.Dark, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.Mid, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette15.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette15.setBrush(QPalette.Disabled, QPalette.Mid, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Shadow, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        self.iolabel.setPalette(palette15)
        self.iolabel.setFont(font)
        self.brakeFailStatus_2 = QLabel(TrainCTRLTestUI)
        self.brakeFailStatus_2.setObjectName(u"brakeFailStatus_2")
        self.brakeFailStatus_2.setGeometry(QRect(280, 460, 111, 41))
        self.brakeFailStatus_3 = QLabel(TrainCTRLTestUI)
        self.brakeFailStatus_3.setObjectName(u"brakeFailStatus_3")
        self.brakeFailStatus_3.setGeometry(QRect(300, 490, 81, 41))
        self.curSpdInput = QTextEdit(TrainCTRLTestUI)
        self.curSpdInput.setObjectName(u"curSpdInput")
        self.curSpdInput.setGeometry(QRect(390, 500, 91, 21))
        self.checkBox = QCheckBox(TrainCTRLTestUI)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(330, 560, 76, 20))
        self.checkBox.setChecked(True)
        self.speedLimInput = QTextEdit(TrainCTRLTestUI)
        self.speedLimInput.setObjectName(u"speedLimInput")
        self.speedLimInput.setGeometry(QRect(390, 530, 91, 21))
        self.brakeFailStatus_4 = QLabel(TrainCTRLTestUI)
        self.brakeFailStatus_4.setObjectName(u"brakeFailStatus_4")
        self.brakeFailStatus_4.setGeometry(QRect(310, 520, 81, 41))
        self.curSpd_2 = QLabel(TrainCTRLTestUI)
        self.curSpd_2.setObjectName(u"curSpd_2")
        self.curSpd_2.setGeometry(QRect(210, 20, 291, 51))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.Button, brush)
        palette16.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette16.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Mid, brush2)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush)
        palette16.setBrush(QPalette.Active, QPalette.Shadow, brush3)
        palette16.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette16.setBrush(QPalette.Inactive, QPalette.Midlight, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.Dark, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.Mid, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette16.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette16.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette16.setBrush(QPalette.Disabled, QPalette.Mid, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Shadow, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        self.curSpd_2.setPalette(palette16)
        self.curSpd_2.setFont(font)

        self.retranslateUi(TrainCTRLTestUI)

        QMetaObject.connectSlotsByName(TrainCTRLTestUI)
    # setupUi

    def retranslateUi(self, TrainCTRLTestUI):
        TrainCTRLTestUI.setWindowTitle(QCoreApplication.translate("TrainCTRLTestUI", u"TrainCTRLTestUI", None))
        self.speedLabel.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Speed Control", None))
        self.ldoorBtn.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Left Doors", None))
        self.sBrakeBtn.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Service Brake", None))
        self.rdoorBtn.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Right Doors", None))
        self.trackSigStatus.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Track Signal Status: ", None))
        self.curTempLabel.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Current Temp:", None))
        self.manModeBtn.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Manual Mode", None))
        self.curSpd.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Current Speed:", None))
        self.engFailStatus.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Engine Status:", None))
        self.ilightBtn.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Interior Lights", None))
        self.faultLabel.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Fault Information", None))
        self.brakeFailStatus.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Brake Status: ", None))
        self.eBrakeBtn.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Emergency Brake", None))
        self.tempLabel.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Temperature Control", None))
        self.intercomBtn.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Intercom", None))
        self.cmdSpd.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Commanded Speed:", None))
        self.elightBtn.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Exterior Lights", None))
        self.driverSpd.setText("")
        self.activateEFault.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Engine Fault ", None))
        self.faultLabel_2.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Fault Modes", None))
        self.activateBFault.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Brake Fault", None))
        self.activateSFault.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Track Signal Fault", None))
        self.iolabel.setText(QCoreApplication.translate("TrainCTRLTestUI", u"I/O Settings", None))
        self.brakeFailStatus_2.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Commanded Speed:", None))
        self.brakeFailStatus_3.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Current Speed", None))
        self.checkBox.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Authority", None))
        self.brakeFailStatus_4.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Speed Limit", None))
        self.curSpd_2.setText(QCoreApplication.translate("TrainCTRLTestUI", u"Current Power Output:", None))
    # retranslateUi

