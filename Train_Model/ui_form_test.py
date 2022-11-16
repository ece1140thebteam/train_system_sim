# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testTrainModel.ui'
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

class Ui_testTrainModel(object):
    def setupUi(self, testTrainModel):
        if not testTrainModel.objectName():
            testTrainModel.setObjectName(u"testTrainModel")
        testTrainModel.resize(800, 300)
        self.centralwidget = QWidget(testTrainModel)
        self.centralwidget.setObjectName(u"centralwidget")
        self.powerbox = QSpinBox(self.centralwidget)
        self.powerbox.setObjectName(u"powerbox")
        self.powerbox.setGeometry(QRect(130, 180, 42, 25))
        self.powerbox.setMaximum(120)
        self.powerbox.setValue(0)
        self.gradebox = QSpinBox(self.centralwidget)
        self.gradebox.setObjectName(u"gradebox")
        self.gradebox.setGeometry(QRect(80, 110, 42, 25))
        self.gradebox.setMaximum(30)
        self.lightcmd = QPushButton(self.centralwidget)
        self.lightcmd.setObjectName(u"lightcmd")
        self.lightcmd.setGeometry(QRect(330, 40, 141, 24))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 110, 49, 16))
        self.sbrakecmd = QPushButton(self.centralwidget)
        self.sbrakecmd.setObjectName(u"sbrakecmd")
        self.sbrakecmd.setGeometry(QRect(480, 40, 141, 24))
        self.ldoorcmd = QPushButton(self.centralwidget)
        self.ldoorcmd.setObjectName(u"ldoorcmd")
        self.ldoorcmd.setGeometry(QRect(180, 40, 141, 24))
        self.speedcmd = QLabel(self.centralwidget)
        self.speedcmd.setObjectName(u"speedcmd")
        self.speedcmd.setGeometry(QRect(30, 150, 101, 16))
        self.powercmd = QLabel(self.centralwidget)
        self.powercmd.setObjectName(u"powercmd")
        self.powercmd.setGeometry(QRect(30, 180, 101, 16))
        self.tempbox = QSpinBox(self.centralwidget)
        self.tempbox.setObjectName(u"tempbox")
        self.tempbox.setGeometry(QRect(130, 80, 42, 25))
        self.tempbox.setMinimum(55)
        self.tempbox.setMaximum(90)
        self.tempbox.setValue(70)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 220, 49, 16))
        self.speedlmt = QLabel(self.centralwidget)
        self.speedlmt.setObjectName(u"speedlmt")
        self.speedlmt.setGeometry(QRect(30, 220, 71, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 80, 49, 16))
        self.speedcmdbox = QSpinBox(self.centralwidget)
        self.speedcmdbox.setObjectName(u"speedcmdbox")
        self.speedcmdbox.setGeometry(QRect(130, 140, 42, 25))
        self.speedcmdbox.setMaximum(40)
        self.speedcmdbox.setValue(35)
        self.grade = QLabel(self.centralwidget)
        self.grade.setObjectName(u"grade")
        self.grade.setGeometry(QRect(30, 120, 41, 16))
        self.tempcmd = QLabel(self.centralwidget)
        self.tempcmd.setObjectName(u"tempcmd")
        self.tempcmd.setGeometry(QRect(30, 90, 101, 16))
        self.rdoorcmd = QPushButton(self.centralwidget)
        self.rdoorcmd.setObjectName(u"rdoorcmd")
        self.rdoorcmd.setGeometry(QRect(30, 40, 141, 24))
        self.speedlmtbox = QSpinBox(self.centralwidget)
        self.speedlmtbox.setObjectName(u"speedlmtbox")
        self.speedlmtbox.setGeometry(QRect(110, 220, 42, 25))
        self.speedlmtbox.setMaximum(40)
        self.speedlmtbox.setValue(40)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 150, 49, 16))
        self.ebrakecmd = QPushButton(self.centralwidget)
        self.ebrakecmd.setObjectName(u"ebrakecmd")
        self.ebrakecmd.setGeometry(QRect(630, 40, 141, 24))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 180, 49, 16))
        testTrainModel.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(testTrainModel)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        testTrainModel.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(testTrainModel)
        self.statusbar.setObjectName(u"statusbar")
        testTrainModel.setStatusBar(self.statusbar)

        self.retranslateUi(testTrainModel)

        QMetaObject.connectSlotsByName(testTrainModel)
    # setupUi

    def retranslateUi(self, testTrainModel):
        testTrainModel.setWindowTitle(QCoreApplication.translate("testTrainModel", u"testTrainModel", None))
        self.lightcmd.setText(QCoreApplication.translate("testTrainModel", u"Light Command", None))
        self.label.setText(QCoreApplication.translate("testTrainModel", u"deg", None))
        self.sbrakecmd.setText(QCoreApplication.translate("testTrainModel", u"Service Brake Cmd", None))
        self.ldoorcmd.setText(QCoreApplication.translate("testTrainModel", u"Left Door Cmd", None))
        self.speedcmd.setText(QCoreApplication.translate("testTrainModel", u"Speed Command:", None))
        self.powercmd.setText(QCoreApplication.translate("testTrainModel", u"Power Command:", None))
        self.label_4.setText(QCoreApplication.translate("testTrainModel", u"mph", None))
        self.speedlmt.setText(QCoreApplication.translate("testTrainModel", u"Speed Limit:", None))
        self.label_2.setText(QCoreApplication.translate("testTrainModel", u"F", None))
        self.grade.setText(QCoreApplication.translate("testTrainModel", u"Grade: ", None))
        self.tempcmd.setText(QCoreApplication.translate("testTrainModel", u"Temperature Cmd:", None))
        self.rdoorcmd.setText(QCoreApplication.translate("testTrainModel", u"Right Door Cmd", None))
        self.label_3.setText(QCoreApplication.translate("testTrainModel", u"mph", None))
        self.ebrakecmd.setText(QCoreApplication.translate("testTrainModel", u"E Brake Cmd", None))
        self.label_5.setText(QCoreApplication.translate("testTrainModel", u"kW", None))
    # retranslateUi

