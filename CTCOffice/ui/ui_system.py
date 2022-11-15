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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(631, 395)
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

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 631, 22))
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
    # retranslateUi

