# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'system.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(325, 245)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_ctc = QPushButton(self.centralwidget)
        self.pushButton_ctc.setObjectName(u"pushButton_ctc")

        self.verticalLayout.addWidget(self.pushButton_ctc)

        self.pushButton_trackcontrol = QPushButton(self.centralwidget)
        self.pushButton_trackcontrol.setObjectName(u"pushButton_trackcontrol")

        self.verticalLayout.addWidget(self.pushButton_trackcontrol)

        self.pushButton_trackmodel = QPushButton(self.centralwidget)
        self.pushButton_trackmodel.setObjectName(u"pushButton_trackmodel")

        self.verticalLayout.addWidget(self.pushButton_trackmodel)

        self.pushButton_trainmodel = QPushButton(self.centralwidget)
        self.pushButton_trainmodel.setObjectName(u"pushButton_trainmodel")

        self.verticalLayout.addWidget(self.pushButton_trainmodel)

        self.pushButton_traincontrol = QPushButton(self.centralwidget)
        self.pushButton_traincontrol.setObjectName(u"pushButton_traincontrol")

        self.verticalLayout.addWidget(self.pushButton_traincontrol)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_ctc_test = QPushButton(self.centralwidget)
        self.pushButton_ctc_test.setObjectName(u"pushButton_ctc_test")

        self.verticalLayout_2.addWidget(self.pushButton_ctc_test)

        self.pushButton_trackcontrol_test = QPushButton(self.centralwidget)
        self.pushButton_trackcontrol_test.setObjectName(u"pushButton_trackcontrol_test")

        self.verticalLayout_2.addWidget(self.pushButton_trackcontrol_test)

        self.pushButton_trackmodel_test = QPushButton(self.centralwidget)
        self.pushButton_trackmodel_test.setObjectName(u"pushButton_trackmodel_test")

        self.verticalLayout_2.addWidget(self.pushButton_trackmodel_test)

        self.pushButton_trainmodel_test = QPushButton(self.centralwidget)
        self.pushButton_trainmodel_test.setObjectName(u"pushButton_trainmodel_test")

        self.verticalLayout_2.addWidget(self.pushButton_trainmodel_test)

        self.pushButton_traincontrol_test = QPushButton(self.centralwidget)
        self.pushButton_traincontrol_test.setObjectName(u"pushButton_traincontrol_test")

        self.verticalLayout_2.addWidget(self.pushButton_traincontrol_test)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)

        self.label_time = QLabel(self.centralwidget)
        self.label_time.setObjectName(u"label_time")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_time.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_time)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setSingleStep(5)
        self.horizontalSlider.setValue(1)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(1)

        self.verticalLayout_3.addWidget(self.horizontalSlider)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_speed = QLabel(self.centralwidget)
        self.label_speed.setObjectName(u"label_speed")

        self.horizontalLayout_2.addWidget(self.label_speed)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.pushButton_start = QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_start)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 325, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_ctc.setText(QCoreApplication.translate("MainWindow", u"CTC", None))
        self.pushButton_trackcontrol.setText(QCoreApplication.translate("MainWindow", u"Track Control", None))
        self.pushButton_trackmodel.setText(QCoreApplication.translate("MainWindow", u"Track Model", None))
        self.pushButton_trainmodel.setText(QCoreApplication.translate("MainWindow", u"Train Model", None))
        self.pushButton_traincontrol.setText(QCoreApplication.translate("MainWindow", u"Train Control", None))
        self.pushButton_ctc_test.setText(QCoreApplication.translate("MainWindow", u"CTC Test", None))
        self.pushButton_trackcontrol_test.setText(QCoreApplication.translate("MainWindow", u"Track Control Test", None))
        self.pushButton_trackmodel_test.setText(QCoreApplication.translate("MainWindow", u"Track Model Test", None))
        self.pushButton_trainmodel_test.setText(QCoreApplication.translate("MainWindow", u"Train Model Test", None))
        self.pushButton_traincontrol_test.setText(QCoreApplication.translate("MainWindow", u"Train Control Test", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Simulation", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Speed:", None))
        self.label_speed.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"Start/Stop", None))
    # retranslateUi

