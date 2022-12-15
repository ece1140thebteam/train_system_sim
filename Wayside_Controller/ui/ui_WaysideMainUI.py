# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WaysideMainUI.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1010, 625)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(15)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.gridLayout_3 = QGridLayout(self.tab1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tab1Frame = QFrame(self.tab1)
        self.tab1Frame.setObjectName(u"tab1Frame")
        self.tab1Frame.setFrameShape(QFrame.StyledPanel)
        self.tab1Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.tab1Frame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.suggestedSpeedFrame1 = QFrame(self.tab1Frame)
        self.suggestedSpeedFrame1.setObjectName(u"suggestedSpeedFrame1")
        self.suggestedSpeedFrame1.setAutoFillBackground(True)
        self.suggestedSpeedFrame1.setFrameShape(QFrame.Box)
        self.suggestedSpeedFrame1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.suggestedSpeedFrame1)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.suggestedSpeedLabel1 = QLabel(self.suggestedSpeedFrame1)
        self.suggestedSpeedLabel1.setObjectName(u"suggestedSpeedLabel1")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.suggestedSpeedLabel1.setFont(font1)
        self.suggestedSpeedLabel1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.suggestedSpeedLabel1)

        self.suggestedSpeedValue1 = QLabel(self.suggestedSpeedFrame1)
        self.suggestedSpeedValue1.setObjectName(u"suggestedSpeedValue1")
        self.suggestedSpeedValue1.setFont(font1)
        self.suggestedSpeedValue1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.suggestedSpeedValue1)


        self.gridLayout_11.addWidget(self.suggestedSpeedFrame1, 1, 3, 1, 1)

        self.blockLabel1 = QLabel(self.tab1Frame)
        self.blockLabel1.setObjectName(u"blockLabel1")
        self.blockLabel1.setFont(font1)
        self.blockLabel1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.blockLabel1, 0, 3, 1, 1)

        self.blockSelect1 = QComboBox(self.tab1Frame)
        self.blockSelect1.addItem("")
        self.blockSelect1.setObjectName(u"blockSelect1")
        self.blockSelect1.setEnabled(True)
        self.blockSelect1.setFont(font1)
        self.blockSelect1.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout_11.addWidget(self.blockSelect1, 0, 4, 1, 1)

        self.authorityFrame1 = QFrame(self.tab1Frame)
        self.authorityFrame1.setObjectName(u"authorityFrame1")
        self.authorityFrame1.setAutoFillBackground(True)
        self.authorityFrame1.setFrameShape(QFrame.Box)
        self.authorityFrame1.setFrameShadow(QFrame.Raised)
        self.authorityFrame1.setLineWidth(1)
        self.authorityFrame1.setMidLineWidth(0)
        self.verticalLayout_28 = QVBoxLayout(self.authorityFrame1)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.authorityLabel1 = QLabel(self.authorityFrame1)
        self.authorityLabel1.setObjectName(u"authorityLabel1")
        self.authorityLabel1.setFont(font1)
        self.authorityLabel1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.authorityLabel1)

        self.authorityValue1 = QLabel(self.authorityFrame1)
        self.authorityValue1.setObjectName(u"authorityValue1")
        self.authorityValue1.setFont(font1)
        self.authorityValue1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.authorityValue1)


        self.gridLayout_11.addWidget(self.authorityFrame1, 1, 2, 1, 1)

        self.switchPositionFrame1 = QFrame(self.tab1Frame)
        self.switchPositionFrame1.setObjectName(u"switchPositionFrame1")
        self.switchPositionFrame1.setAutoFillBackground(True)
        self.switchPositionFrame1.setFrameShape(QFrame.Box)
        self.switchPositionFrame1.setFrameShadow(QFrame.Raised)
        self.switchPositionFrame1.setLineWidth(1)
        self.switchPositionFrame1.setMidLineWidth(0)
        self.gridLayout_10 = QGridLayout(self.switchPositionFrame1)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.switchPositionLabel1 = QLabel(self.switchPositionFrame1)
        self.switchPositionLabel1.setObjectName(u"switchPositionLabel1")
        self.switchPositionLabel1.setFont(font1)
        self.switchPositionLabel1.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.switchPositionLabel1, 0, 0, 1, 3)

        self.switchArrowLabel1 = QLabel(self.switchPositionFrame1)
        self.switchArrowLabel1.setObjectName(u"switchArrowLabel1")
        self.switchArrowLabel1.setFont(font1)
        self.switchArrowLabel1.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.switchArrowLabel1, 1, 1, 1, 1)

        self.switchFromValue1 = QLabel(self.switchPositionFrame1)
        self.switchFromValue1.setObjectName(u"switchFromValue1")
        self.switchFromValue1.setFont(font1)
        self.switchFromValue1.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.switchFromValue1, 1, 0, 1, 1)

        self.switchToValue1 = QLabel(self.switchPositionFrame1)
        self.switchToValue1.setObjectName(u"switchToValue1")
        self.switchToValue1.setFont(font1)
        self.switchToValue1.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.switchToValue1, 1, 2, 1, 1)


        self.gridLayout_11.addWidget(self.switchPositionFrame1, 1, 1, 1, 1)

        self.uploadPLC1 = QPushButton(self.tab1Frame)
        self.uploadPLC1.setObjectName(u"uploadPLC1")
        self.uploadPLC1.setEnabled(False)
        self.uploadPLC1.setFont(font1)

        self.gridLayout_11.addWidget(self.uploadPLC1, 4, 4, 1, 1)

        self.statusFrame1 = QFrame(self.tab1Frame)
        self.statusFrame1.setObjectName(u"statusFrame1")
        self.statusFrame1.setAutoFillBackground(True)
        self.statusFrame1.setFrameShape(QFrame.Box)
        self.statusFrame1.setFrameShadow(QFrame.Raised)
        self.statusFrame1.setLineWidth(1)
        self.statusFrame1.setMidLineWidth(0)
        self.verticalLayout_26 = QVBoxLayout(self.statusFrame1)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.statusLabel1 = QLabel(self.statusFrame1)
        self.statusLabel1.setObjectName(u"statusLabel1")
        self.statusLabel1.setFont(font1)
        self.statusLabel1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.statusLabel1)

        self.statusValue1 = QLabel(self.statusFrame1)
        self.statusValue1.setObjectName(u"statusValue1")
        self.statusValue1.setFont(font1)
        self.statusValue1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.statusValue1)


        self.gridLayout_11.addWidget(self.statusFrame1, 1, 4, 1, 1)

        self.trafficLightFrame1 = QFrame(self.tab1Frame)
        self.trafficLightFrame1.setObjectName(u"trafficLightFrame1")
        self.trafficLightFrame1.setAutoFillBackground(True)
        self.trafficLightFrame1.setFrameShape(QFrame.Box)
        self.trafficLightFrame1.setFrameShadow(QFrame.Raised)
        self.trafficLightFrame1.setLineWidth(1)
        self.trafficLightFrame1.setMidLineWidth(0)
        self.verticalLayout_27 = QVBoxLayout(self.trafficLightFrame1)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.trafficLightLabel1 = QLabel(self.trafficLightFrame1)
        self.trafficLightLabel1.setObjectName(u"trafficLightLabel1")
        self.trafficLightLabel1.setFont(font1)
        self.trafficLightLabel1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.trafficLightLabel1)

        self.trafficLightValue1 = QLabel(self.trafficLightFrame1)
        self.trafficLightValue1.setObjectName(u"trafficLightValue1")
        self.trafficLightValue1.setFont(font1)
        self.trafficLightValue1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.trafficLightValue1)


        self.gridLayout_11.addWidget(self.trafficLightFrame1, 2, 1, 1, 1)

        self.trackLabel1 = QLabel(self.tab1Frame)
        self.trackLabel1.setObjectName(u"trackLabel1")
        self.trackLabel1.setFont(font1)
        self.trackLabel1.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.trackLabel1, 0, 0, 1, 1)

        self.occupancyFrame1 = QFrame(self.tab1Frame)
        self.occupancyFrame1.setObjectName(u"occupancyFrame1")
        self.occupancyFrame1.setAutoFillBackground(True)
        self.occupancyFrame1.setFrameShape(QFrame.Box)
        self.occupancyFrame1.setFrameShadow(QFrame.Raised)
        self.occupancyFrame1.setLineWidth(1)
        self.occupancyFrame1.setMidLineWidth(0)
        self.verticalLayout_23 = QVBoxLayout(self.occupancyFrame1)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.occupancyLabel1 = QLabel(self.occupancyFrame1)
        self.occupancyLabel1.setObjectName(u"occupancyLabel1")
        self.occupancyLabel1.setFont(font1)
        self.occupancyLabel1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.occupancyLabel1)

        self.occupancyValue1 = QLabel(self.occupancyFrame1)
        self.occupancyValue1.setObjectName(u"occupancyValue1")
        self.occupancyValue1.setFont(font1)
        self.occupancyValue1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.occupancyValue1)


        self.gridLayout_11.addWidget(self.occupancyFrame1, 2, 2, 1, 1)

        self.displayPLC1 = QTextBrowser(self.tab1Frame)
        self.displayPLC1.setObjectName(u"displayPLC1")
        font2 = QFont()
        font2.setPointSize(12)
        self.displayPLC1.setFont(font2)

        self.gridLayout_11.addWidget(self.displayPLC1, 3, 0, 1, 5)

        self.commandedSpeedFrame1 = QFrame(self.tab1Frame)
        self.commandedSpeedFrame1.setObjectName(u"commandedSpeedFrame1")
        self.commandedSpeedFrame1.setAutoFillBackground(True)
        self.commandedSpeedFrame1.setFrameShape(QFrame.Box)
        self.commandedSpeedFrame1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.commandedSpeedFrame1)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.commandedSpeedLabel1 = QLabel(self.commandedSpeedFrame1)
        self.commandedSpeedLabel1.setObjectName(u"commandedSpeedLabel1")
        self.commandedSpeedLabel1.setFont(font1)
        self.commandedSpeedLabel1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.commandedSpeedLabel1)

        self.commandedSpeedValue1 = QLabel(self.commandedSpeedFrame1)
        self.commandedSpeedValue1.setObjectName(u"commandedSpeedValue1")
        self.commandedSpeedValue1.setFont(font1)
        self.commandedSpeedValue1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.commandedSpeedValue1)


        self.gridLayout_11.addWidget(self.commandedSpeedFrame1, 2, 3, 1, 1)

        self.maintenanceFrame1 = QFrame(self.tab1Frame)
        self.maintenanceFrame1.setObjectName(u"maintenanceFrame1")
        self.maintenanceFrame1.setAutoFillBackground(True)
        self.maintenanceFrame1.setFrameShape(QFrame.Box)
        self.maintenanceFrame1.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.maintenanceFrame1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.maintenanceLabel1 = QLabel(self.maintenanceFrame1)
        self.maintenanceLabel1.setObjectName(u"maintenanceLabel1")
        font3 = QFont()
        font3.setPointSize(10)
        self.maintenanceLabel1.setFont(font3)
        self.maintenanceLabel1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.maintenanceLabel1)

        self.maintenanceValue1 = QLabel(self.maintenanceFrame1)
        self.maintenanceValue1.setObjectName(u"maintenanceValue1")
        self.maintenanceValue1.setFont(font3)
        self.maintenanceValue1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.maintenanceValue1)


        self.gridLayout_11.addWidget(self.maintenanceFrame1, 2, 4, 1, 1)

        self.railwayCrossingFrame1 = QFrame(self.tab1Frame)
        self.railwayCrossingFrame1.setObjectName(u"railwayCrossingFrame1")
        self.railwayCrossingFrame1.setEnabled(True)
        self.railwayCrossingFrame1.setAutoFillBackground(True)
        self.railwayCrossingFrame1.setFrameShape(QFrame.Box)
        self.railwayCrossingFrame1.setFrameShadow(QFrame.Raised)
        self.railwayCrossingFrame1.setLineWidth(1)
        self.railwayCrossingFrame1.setMidLineWidth(0)
        self.gridLayout_5 = QGridLayout(self.railwayCrossingFrame1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.railwayCrossingLabel1 = QLabel(self.railwayCrossingFrame1)
        self.railwayCrossingLabel1.setObjectName(u"railwayCrossingLabel1")
        self.railwayCrossingLabel1.setFont(font1)
        self.railwayCrossingLabel1.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.railwayCrossingLabel1, 0, 0, 1, 2)

        self.railwayGateLabel1 = QLabel(self.railwayCrossingFrame1)
        self.railwayGateLabel1.setObjectName(u"railwayGateLabel1")
        self.railwayGateLabel1.setFont(font3)

        self.gridLayout_5.addWidget(self.railwayGateLabel1, 1, 0, 1, 1)

        self.railwayGateValue1 = QLabel(self.railwayCrossingFrame1)
        self.railwayGateValue1.setObjectName(u"railwayGateValue1")
        self.railwayGateValue1.setFont(font1)
        self.railwayGateValue1.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.railwayGateValue1, 1, 1, 1, 1)

        self.railwayLightsLabel1 = QLabel(self.railwayCrossingFrame1)
        self.railwayLightsLabel1.setObjectName(u"railwayLightsLabel1")
        self.railwayLightsLabel1.setFont(font3)

        self.gridLayout_5.addWidget(self.railwayLightsLabel1, 2, 0, 1, 1)

        self.railwayLightsValue1 = QLabel(self.railwayCrossingFrame1)
        self.railwayLightsValue1.setObjectName(u"railwayLightsValue1")
        self.railwayLightsValue1.setFont(font1)
        self.railwayLightsValue1.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.railwayLightsValue1, 2, 1, 1, 1)


        self.gridLayout_11.addWidget(self.railwayCrossingFrame1, 1, 0, 2, 1)


        self.gridLayout_3.addWidget(self.tab1Frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.gridLayout_4 = QGridLayout(self.tab2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tab2Frame = QFrame(self.tab2)
        self.tab2Frame.setObjectName(u"tab2Frame")
        self.tab2Frame.setFrameShape(QFrame.StyledPanel)
        self.tab2Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.tab2Frame)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.blockLabel2 = QLabel(self.tab2Frame)
        self.blockLabel2.setObjectName(u"blockLabel2")
        self.blockLabel2.setFont(font1)
        self.blockLabel2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.blockLabel2, 0, 3, 1, 1)

        self.occupancyFrame2 = QFrame(self.tab2Frame)
        self.occupancyFrame2.setObjectName(u"occupancyFrame2")
        self.occupancyFrame2.setAutoFillBackground(True)
        self.occupancyFrame2.setFrameShape(QFrame.Box)
        self.occupancyFrame2.setFrameShadow(QFrame.Raised)
        self.occupancyFrame2.setLineWidth(1)
        self.occupancyFrame2.setMidLineWidth(0)
        self.verticalLayout_32 = QVBoxLayout(self.occupancyFrame2)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.occupancyLabel2 = QLabel(self.occupancyFrame2)
        self.occupancyLabel2.setObjectName(u"occupancyLabel2")
        self.occupancyLabel2.setFont(font1)
        self.occupancyLabel2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.occupancyLabel2)

        self.occupancyValue2 = QLabel(self.occupancyFrame2)
        self.occupancyValue2.setObjectName(u"occupancyValue2")
        self.occupancyValue2.setFont(font1)
        self.occupancyValue2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.occupancyValue2)


        self.gridLayout_12.addWidget(self.occupancyFrame2, 2, 2, 1, 1)

        self.authorityFrame2 = QFrame(self.tab2Frame)
        self.authorityFrame2.setObjectName(u"authorityFrame2")
        self.authorityFrame2.setAutoFillBackground(True)
        self.authorityFrame2.setFrameShape(QFrame.Box)
        self.authorityFrame2.setFrameShadow(QFrame.Raised)
        self.authorityFrame2.setLineWidth(1)
        self.authorityFrame2.setMidLineWidth(0)
        self.verticalLayout_33 = QVBoxLayout(self.authorityFrame2)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.authorityLabel2 = QLabel(self.authorityFrame2)
        self.authorityLabel2.setObjectName(u"authorityLabel2")
        self.authorityLabel2.setFont(font1)
        self.authorityLabel2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.authorityLabel2)

        self.authorityValue2 = QLabel(self.authorityFrame2)
        self.authorityValue2.setObjectName(u"authorityValue2")
        self.authorityValue2.setFont(font1)
        self.authorityValue2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.authorityValue2)


        self.gridLayout_12.addWidget(self.authorityFrame2, 1, 2, 1, 1)

        self.uploadPLC2 = QPushButton(self.tab2Frame)
        self.uploadPLC2.setObjectName(u"uploadPLC2")
        self.uploadPLC2.setEnabled(False)
        self.uploadPLC2.setFont(font1)

        self.gridLayout_12.addWidget(self.uploadPLC2, 4, 4, 1, 1)

        self.suggestedSpeedFrame2 = QFrame(self.tab2Frame)
        self.suggestedSpeedFrame2.setObjectName(u"suggestedSpeedFrame2")
        self.suggestedSpeedFrame2.setAutoFillBackground(True)
        self.suggestedSpeedFrame2.setFrameShape(QFrame.Box)
        self.suggestedSpeedFrame2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.suggestedSpeedFrame2)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.suggestedSpeedLabel2 = QLabel(self.suggestedSpeedFrame2)
        self.suggestedSpeedLabel2.setObjectName(u"suggestedSpeedLabel2")
        self.suggestedSpeedLabel2.setFont(font1)
        self.suggestedSpeedLabel2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.suggestedSpeedLabel2)

        self.suggestedSpeedValue2 = QLabel(self.suggestedSpeedFrame2)
        self.suggestedSpeedValue2.setObjectName(u"suggestedSpeedValue2")
        self.suggestedSpeedValue2.setFont(font1)
        self.suggestedSpeedValue2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.suggestedSpeedValue2)


        self.gridLayout_12.addWidget(self.suggestedSpeedFrame2, 1, 3, 1, 1)

        self.trackLabel2 = QLabel(self.tab2Frame)
        self.trackLabel2.setObjectName(u"trackLabel2")
        self.trackLabel2.setFont(font1)
        self.trackLabel2.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.trackLabel2, 0, 0, 1, 1)

        self.blockSelect2 = QComboBox(self.tab2Frame)
        self.blockSelect2.addItem("")
        self.blockSelect2.setObjectName(u"blockSelect2")
        self.blockSelect2.setEnabled(True)
        self.blockSelect2.setFont(font1)
        self.blockSelect2.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout_12.addWidget(self.blockSelect2, 0, 4, 1, 1)

        self.railwayCrossingFrame2 = QFrame(self.tab2Frame)
        self.railwayCrossingFrame2.setObjectName(u"railwayCrossingFrame2")
        self.railwayCrossingFrame2.setAutoFillBackground(True)
        self.railwayCrossingFrame2.setFrameShape(QFrame.Box)
        self.railwayCrossingFrame2.setFrameShadow(QFrame.Raised)
        self.railwayCrossingFrame2.setLineWidth(1)
        self.railwayCrossingFrame2.setMidLineWidth(0)
        self.gridLayout_14 = QGridLayout(self.railwayCrossingFrame2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.railwayCrossingLabel2 = QLabel(self.railwayCrossingFrame2)
        self.railwayCrossingLabel2.setObjectName(u"railwayCrossingLabel2")
        self.railwayCrossingLabel2.setFont(font1)
        self.railwayCrossingLabel2.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.railwayCrossingLabel2, 0, 0, 1, 2)

        self.railwayGateLabel2 = QLabel(self.railwayCrossingFrame2)
        self.railwayGateLabel2.setObjectName(u"railwayGateLabel2")
        self.railwayGateLabel2.setFont(font3)

        self.gridLayout_14.addWidget(self.railwayGateLabel2, 1, 0, 1, 1)

        self.railwayGateValue2 = QLabel(self.railwayCrossingFrame2)
        self.railwayGateValue2.setObjectName(u"railwayGateValue2")
        self.railwayGateValue2.setFont(font1)
        self.railwayGateValue2.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.railwayGateValue2, 1, 1, 1, 1)

        self.railwayLightsLabel2 = QLabel(self.railwayCrossingFrame2)
        self.railwayLightsLabel2.setObjectName(u"railwayLightsLabel2")
        self.railwayLightsLabel2.setFont(font3)

        self.gridLayout_14.addWidget(self.railwayLightsLabel2, 2, 0, 1, 1)

        self.railwayLightsValue2 = QLabel(self.railwayCrossingFrame2)
        self.railwayLightsValue2.setObjectName(u"railwayLightsValue2")
        self.railwayLightsValue2.setFont(font1)
        self.railwayLightsValue2.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.railwayLightsValue2, 2, 1, 1, 1)


        self.gridLayout_12.addWidget(self.railwayCrossingFrame2, 1, 0, 2, 1)

        self.displayPLC2 = QTextBrowser(self.tab2Frame)
        self.displayPLC2.setObjectName(u"displayPLC2")
        self.displayPLC2.setFont(font2)

        self.gridLayout_12.addWidget(self.displayPLC2, 3, 0, 1, 5)

        self.commandedSpeedFrame2 = QFrame(self.tab2Frame)
        self.commandedSpeedFrame2.setObjectName(u"commandedSpeedFrame2")
        self.commandedSpeedFrame2.setAutoFillBackground(True)
        self.commandedSpeedFrame2.setFrameShape(QFrame.Box)
        self.commandedSpeedFrame2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.commandedSpeedFrame2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.commandedSpeedLabel2 = QLabel(self.commandedSpeedFrame2)
        self.commandedSpeedLabel2.setObjectName(u"commandedSpeedLabel2")
        self.commandedSpeedLabel2.setFont(font1)
        self.commandedSpeedLabel2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.commandedSpeedLabel2)

        self.commandedSpeedValue2 = QLabel(self.commandedSpeedFrame2)
        self.commandedSpeedValue2.setObjectName(u"commandedSpeedValue2")
        self.commandedSpeedValue2.setFont(font1)
        self.commandedSpeedValue2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.commandedSpeedValue2)


        self.gridLayout_12.addWidget(self.commandedSpeedFrame2, 2, 3, 1, 1)

        self.statusFrame2 = QFrame(self.tab2Frame)
        self.statusFrame2.setObjectName(u"statusFrame2")
        self.statusFrame2.setAutoFillBackground(True)
        self.statusFrame2.setFrameShape(QFrame.Box)
        self.statusFrame2.setFrameShadow(QFrame.Raised)
        self.statusFrame2.setLineWidth(1)
        self.statusFrame2.setMidLineWidth(0)
        self.verticalLayout_36 = QVBoxLayout(self.statusFrame2)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.statusLabel2 = QLabel(self.statusFrame2)
        self.statusLabel2.setObjectName(u"statusLabel2")
        self.statusLabel2.setFont(font1)
        self.statusLabel2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.statusLabel2)

        self.statusValue2 = QLabel(self.statusFrame2)
        self.statusValue2.setObjectName(u"statusValue2")
        self.statusValue2.setFont(font1)
        self.statusValue2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.statusValue2)


        self.gridLayout_12.addWidget(self.statusFrame2, 1, 4, 1, 1)

        self.switchPositionFrame2 = QFrame(self.tab2Frame)
        self.switchPositionFrame2.setObjectName(u"switchPositionFrame2")
        self.switchPositionFrame2.setAutoFillBackground(True)
        self.switchPositionFrame2.setFrameShape(QFrame.Box)
        self.switchPositionFrame2.setFrameShadow(QFrame.Raised)
        self.switchPositionFrame2.setLineWidth(1)
        self.switchPositionFrame2.setMidLineWidth(0)
        self.gridLayout_13 = QGridLayout(self.switchPositionFrame2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.switchPositionLabel2 = QLabel(self.switchPositionFrame2)
        self.switchPositionLabel2.setObjectName(u"switchPositionLabel2")
        self.switchPositionLabel2.setFont(font1)
        self.switchPositionLabel2.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.switchPositionLabel2, 0, 0, 1, 3)

        self.switchToValue2 = QLabel(self.switchPositionFrame2)
        self.switchToValue2.setObjectName(u"switchToValue2")
        self.switchToValue2.setFont(font1)
        self.switchToValue2.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.switchToValue2, 1, 2, 1, 1)

        self.switchArrowLabel2 = QLabel(self.switchPositionFrame2)
        self.switchArrowLabel2.setObjectName(u"switchArrowLabel2")
        self.switchArrowLabel2.setFont(font1)
        self.switchArrowLabel2.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.switchArrowLabel2, 1, 1, 1, 1)

        self.switchFromValue2 = QLabel(self.switchPositionFrame2)
        self.switchFromValue2.setObjectName(u"switchFromValue2")
        self.switchFromValue2.setFont(font1)
        self.switchFromValue2.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.switchFromValue2, 1, 0, 1, 1)


        self.gridLayout_12.addWidget(self.switchPositionFrame2, 1, 1, 1, 1)

        self.trafficLightFrame2 = QFrame(self.tab2Frame)
        self.trafficLightFrame2.setObjectName(u"trafficLightFrame2")
        self.trafficLightFrame2.setAutoFillBackground(True)
        self.trafficLightFrame2.setFrameShape(QFrame.Box)
        self.trafficLightFrame2.setFrameShadow(QFrame.Raised)
        self.trafficLightFrame2.setLineWidth(1)
        self.trafficLightFrame2.setMidLineWidth(0)
        self.verticalLayout_34 = QVBoxLayout(self.trafficLightFrame2)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.trafficLightLabel2 = QLabel(self.trafficLightFrame2)
        self.trafficLightLabel2.setObjectName(u"trafficLightLabel2")
        self.trafficLightLabel2.setFont(font1)
        self.trafficLightLabel2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.trafficLightLabel2)

        self.trafficLightValue2 = QLabel(self.trafficLightFrame2)
        self.trafficLightValue2.setObjectName(u"trafficLightValue2")
        self.trafficLightValue2.setFont(font1)
        self.trafficLightValue2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.trafficLightValue2)


        self.gridLayout_12.addWidget(self.trafficLightFrame2, 2, 1, 1, 1)

        self.maintenanceFrame2 = QFrame(self.tab2Frame)
        self.maintenanceFrame2.setObjectName(u"maintenanceFrame2")
        self.maintenanceFrame2.setAutoFillBackground(True)
        self.maintenanceFrame2.setFrameShape(QFrame.Box)
        self.maintenanceFrame2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.maintenanceFrame2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.maintenanceLabel2 = QLabel(self.maintenanceFrame2)
        self.maintenanceLabel2.setObjectName(u"maintenanceLabel2")
        self.maintenanceLabel2.setFont(font3)
        self.maintenanceLabel2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.maintenanceLabel2)

        self.maintenanceValue2 = QLabel(self.maintenanceFrame2)
        self.maintenanceValue2.setObjectName(u"maintenanceValue2")
        self.maintenanceValue2.setFont(font3)
        self.maintenanceValue2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.maintenanceValue2)


        self.gridLayout_12.addWidget(self.maintenanceFrame2, 2, 4, 1, 1)


        self.gridLayout_4.addWidget(self.tab2Frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.gridLayout_18 = QGridLayout(self.tab3)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.tab3Frame = QFrame(self.tab3)
        self.tab3Frame.setObjectName(u"tab3Frame")
        self.tab3Frame.setFrameShape(QFrame.StyledPanel)
        self.tab3Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.tab3Frame)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.blockLabel3 = QLabel(self.tab3Frame)
        self.blockLabel3.setObjectName(u"blockLabel3")
        self.blockLabel3.setFont(font1)
        self.blockLabel3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.blockLabel3, 0, 3, 1, 1)

        self.occupancyFrame3 = QFrame(self.tab3Frame)
        self.occupancyFrame3.setObjectName(u"occupancyFrame3")
        self.occupancyFrame3.setAutoFillBackground(True)
        self.occupancyFrame3.setFrameShape(QFrame.Box)
        self.occupancyFrame3.setFrameShadow(QFrame.Raised)
        self.occupancyFrame3.setLineWidth(1)
        self.occupancyFrame3.setMidLineWidth(0)
        self.verticalLayout_39 = QVBoxLayout(self.occupancyFrame3)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.occupancyLabel3 = QLabel(self.occupancyFrame3)
        self.occupancyLabel3.setObjectName(u"occupancyLabel3")
        self.occupancyLabel3.setFont(font1)
        self.occupancyLabel3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.occupancyLabel3)

        self.occupancyValue3 = QLabel(self.occupancyFrame3)
        self.occupancyValue3.setObjectName(u"occupancyValue3")
        self.occupancyValue3.setFont(font1)
        self.occupancyValue3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.occupancyValue3)


        self.gridLayout_15.addWidget(self.occupancyFrame3, 2, 2, 1, 1)

        self.authorityFrame3 = QFrame(self.tab3Frame)
        self.authorityFrame3.setObjectName(u"authorityFrame3")
        self.authorityFrame3.setAutoFillBackground(True)
        self.authorityFrame3.setFrameShape(QFrame.Box)
        self.authorityFrame3.setFrameShadow(QFrame.Raised)
        self.authorityFrame3.setLineWidth(1)
        self.authorityFrame3.setMidLineWidth(0)
        self.verticalLayout_40 = QVBoxLayout(self.authorityFrame3)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.authorityLabel3 = QLabel(self.authorityFrame3)
        self.authorityLabel3.setObjectName(u"authorityLabel3")
        self.authorityLabel3.setFont(font1)
        self.authorityLabel3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.authorityLabel3)

        self.authorityValue3 = QLabel(self.authorityFrame3)
        self.authorityValue3.setObjectName(u"authorityValue3")
        self.authorityValue3.setFont(font1)
        self.authorityValue3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.authorityValue3)


        self.gridLayout_15.addWidget(self.authorityFrame3, 1, 2, 1, 1)

        self.uploadPLC3 = QPushButton(self.tab3Frame)
        self.uploadPLC3.setObjectName(u"uploadPLC3")
        self.uploadPLC3.setEnabled(False)
        self.uploadPLC3.setFont(font1)

        self.gridLayout_15.addWidget(self.uploadPLC3, 4, 4, 1, 1)

        self.suggestedSpeedFrame3 = QFrame(self.tab3Frame)
        self.suggestedSpeedFrame3.setObjectName(u"suggestedSpeedFrame3")
        self.suggestedSpeedFrame3.setAutoFillBackground(True)
        self.suggestedSpeedFrame3.setFrameShape(QFrame.Box)
        self.suggestedSpeedFrame3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.suggestedSpeedFrame3)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.suggestedSpeedLabel3 = QLabel(self.suggestedSpeedFrame3)
        self.suggestedSpeedLabel3.setObjectName(u"suggestedSpeedLabel3")
        self.suggestedSpeedLabel3.setFont(font1)
        self.suggestedSpeedLabel3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_42.addWidget(self.suggestedSpeedLabel3)

        self.suggestedSpeedValue3 = QLabel(self.suggestedSpeedFrame3)
        self.suggestedSpeedValue3.setObjectName(u"suggestedSpeedValue3")
        self.suggestedSpeedValue3.setFont(font1)
        self.suggestedSpeedValue3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_42.addWidget(self.suggestedSpeedValue3)


        self.gridLayout_15.addWidget(self.suggestedSpeedFrame3, 1, 3, 1, 1)

        self.trackLabel3 = QLabel(self.tab3Frame)
        self.trackLabel3.setObjectName(u"trackLabel3")
        self.trackLabel3.setFont(font1)
        self.trackLabel3.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.trackLabel3, 0, 0, 1, 1)

        self.blockSelect3 = QComboBox(self.tab3Frame)
        self.blockSelect3.addItem("")
        self.blockSelect3.setObjectName(u"blockSelect3")
        self.blockSelect3.setEnabled(True)
        self.blockSelect3.setFont(font1)
        self.blockSelect3.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout_15.addWidget(self.blockSelect3, 0, 4, 1, 1)

        self.railwayCrossingFrame3 = QFrame(self.tab3Frame)
        self.railwayCrossingFrame3.setObjectName(u"railwayCrossingFrame3")
        self.railwayCrossingFrame3.setAutoFillBackground(True)
        self.railwayCrossingFrame3.setFrameShape(QFrame.Box)
        self.railwayCrossingFrame3.setFrameShadow(QFrame.Raised)
        self.railwayCrossingFrame3.setLineWidth(1)
        self.railwayCrossingFrame3.setMidLineWidth(0)
        self.gridLayout_17 = QGridLayout(self.railwayCrossingFrame3)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.railwayCrossingLabel3 = QLabel(self.railwayCrossingFrame3)
        self.railwayCrossingLabel3.setObjectName(u"railwayCrossingLabel3")
        self.railwayCrossingLabel3.setFont(font1)
        self.railwayCrossingLabel3.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.railwayCrossingLabel3, 0, 0, 1, 2)

        self.railwayGateLabel3 = QLabel(self.railwayCrossingFrame3)
        self.railwayGateLabel3.setObjectName(u"railwayGateLabel3")
        self.railwayGateLabel3.setFont(font3)

        self.gridLayout_17.addWidget(self.railwayGateLabel3, 1, 0, 1, 1)

        self.railwayGateValue3 = QLabel(self.railwayCrossingFrame3)
        self.railwayGateValue3.setObjectName(u"railwayGateValue3")
        self.railwayGateValue3.setFont(font1)
        self.railwayGateValue3.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.railwayGateValue3, 1, 1, 1, 1)

        self.railwayLightsLabel3 = QLabel(self.railwayCrossingFrame3)
        self.railwayLightsLabel3.setObjectName(u"railwayLightsLabel3")
        self.railwayLightsLabel3.setFont(font3)

        self.gridLayout_17.addWidget(self.railwayLightsLabel3, 2, 0, 1, 1)

        self.railwayLightsValue3 = QLabel(self.railwayCrossingFrame3)
        self.railwayLightsValue3.setObjectName(u"railwayLightsValue3")
        self.railwayLightsValue3.setFont(font1)
        self.railwayLightsValue3.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.railwayLightsValue3, 2, 1, 1, 1)


        self.gridLayout_15.addWidget(self.railwayCrossingFrame3, 1, 0, 2, 1)

        self.displayPLC3 = QTextBrowser(self.tab3Frame)
        self.displayPLC3.setObjectName(u"displayPLC3")
        self.displayPLC3.setFont(font2)

        self.gridLayout_15.addWidget(self.displayPLC3, 3, 0, 1, 5)

        self.commandedSpeedFrame3 = QFrame(self.tab3Frame)
        self.commandedSpeedFrame3.setObjectName(u"commandedSpeedFrame3")
        self.commandedSpeedFrame3.setAutoFillBackground(True)
        self.commandedSpeedFrame3.setFrameShape(QFrame.Box)
        self.commandedSpeedFrame3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.commandedSpeedFrame3)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.commandedSpeedLabel3 = QLabel(self.commandedSpeedFrame3)
        self.commandedSpeedLabel3.setObjectName(u"commandedSpeedLabel3")
        self.commandedSpeedLabel3.setFont(font1)
        self.commandedSpeedLabel3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.commandedSpeedLabel3)

        self.commandedSpeedValue3 = QLabel(self.commandedSpeedFrame3)
        self.commandedSpeedValue3.setObjectName(u"commandedSpeedValue3")
        self.commandedSpeedValue3.setFont(font1)
        self.commandedSpeedValue3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.commandedSpeedValue3)


        self.gridLayout_15.addWidget(self.commandedSpeedFrame3, 2, 3, 1, 1)

        self.statusFrame3 = QFrame(self.tab3Frame)
        self.statusFrame3.setObjectName(u"statusFrame3")
        self.statusFrame3.setAutoFillBackground(True)
        self.statusFrame3.setFrameShape(QFrame.Box)
        self.statusFrame3.setFrameShadow(QFrame.Raised)
        self.statusFrame3.setLineWidth(1)
        self.statusFrame3.setMidLineWidth(0)
        self.verticalLayout_43 = QVBoxLayout(self.statusFrame3)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.statusLabel3 = QLabel(self.statusFrame3)
        self.statusLabel3.setObjectName(u"statusLabel3")
        self.statusLabel3.setFont(font1)
        self.statusLabel3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.statusLabel3)

        self.statusValue3 = QLabel(self.statusFrame3)
        self.statusValue3.setObjectName(u"statusValue3")
        self.statusValue3.setFont(font1)
        self.statusValue3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.statusValue3)


        self.gridLayout_15.addWidget(self.statusFrame3, 1, 4, 1, 1)

        self.switchPositionFrame3 = QFrame(self.tab3Frame)
        self.switchPositionFrame3.setObjectName(u"switchPositionFrame3")
        self.switchPositionFrame3.setAutoFillBackground(True)
        self.switchPositionFrame3.setFrameShape(QFrame.Box)
        self.switchPositionFrame3.setFrameShadow(QFrame.Raised)
        self.switchPositionFrame3.setLineWidth(1)
        self.switchPositionFrame3.setMidLineWidth(0)
        self.gridLayout_16 = QGridLayout(self.switchPositionFrame3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.switchPositionLabel3 = QLabel(self.switchPositionFrame3)
        self.switchPositionLabel3.setObjectName(u"switchPositionLabel3")
        self.switchPositionLabel3.setFont(font1)
        self.switchPositionLabel3.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.switchPositionLabel3, 0, 0, 1, 3)

        self.switchFromValue3 = QLabel(self.switchPositionFrame3)
        self.switchFromValue3.setObjectName(u"switchFromValue3")
        self.switchFromValue3.setFont(font1)
        self.switchFromValue3.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.switchFromValue3, 1, 0, 1, 1)

        self.switchToValue3 = QLabel(self.switchPositionFrame3)
        self.switchToValue3.setObjectName(u"switchToValue3")
        self.switchToValue3.setFont(font1)
        self.switchToValue3.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.switchToValue3, 1, 2, 1, 1)

        self.switchArrowLabel3 = QLabel(self.switchPositionFrame3)
        self.switchArrowLabel3.setObjectName(u"switchArrowLabel3")
        self.switchArrowLabel3.setFont(font1)
        self.switchArrowLabel3.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.switchArrowLabel3, 1, 1, 1, 1)


        self.gridLayout_15.addWidget(self.switchPositionFrame3, 1, 1, 1, 1)

        self.trafficLightFrame3 = QFrame(self.tab3Frame)
        self.trafficLightFrame3.setObjectName(u"trafficLightFrame3")
        self.trafficLightFrame3.setAutoFillBackground(True)
        self.trafficLightFrame3.setFrameShape(QFrame.Box)
        self.trafficLightFrame3.setFrameShadow(QFrame.Raised)
        self.trafficLightFrame3.setLineWidth(1)
        self.trafficLightFrame3.setMidLineWidth(0)
        self.verticalLayout_41 = QVBoxLayout(self.trafficLightFrame3)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.trafficLightLabel3 = QLabel(self.trafficLightFrame3)
        self.trafficLightLabel3.setObjectName(u"trafficLightLabel3")
        self.trafficLightLabel3.setFont(font1)
        self.trafficLightLabel3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.trafficLightLabel3)

        self.trafficLightValue3 = QLabel(self.trafficLightFrame3)
        self.trafficLightValue3.setObjectName(u"trafficLightValue3")
        self.trafficLightValue3.setFont(font1)
        self.trafficLightValue3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.trafficLightValue3)


        self.gridLayout_15.addWidget(self.trafficLightFrame3, 2, 1, 1, 1)

        self.maintenanceFrame3 = QFrame(self.tab3Frame)
        self.maintenanceFrame3.setObjectName(u"maintenanceFrame3")
        self.maintenanceFrame3.setAutoFillBackground(True)
        self.maintenanceFrame3.setFrameShape(QFrame.Box)
        self.maintenanceFrame3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.maintenanceFrame3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.maintenanceLabel3 = QLabel(self.maintenanceFrame3)
        self.maintenanceLabel3.setObjectName(u"maintenanceLabel3")
        self.maintenanceLabel3.setFont(font3)
        self.maintenanceLabel3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.maintenanceLabel3)

        self.maintenanceValue3 = QLabel(self.maintenanceFrame3)
        self.maintenanceValue3.setObjectName(u"maintenanceValue3")
        self.maintenanceValue3.setFont(font3)
        self.maintenanceValue3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.maintenanceValue3)


        self.gridLayout_15.addWidget(self.maintenanceFrame3, 2, 4, 1, 1)


        self.gridLayout_18.addWidget(self.tab3Frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab3, "")
        self.tab4 = QWidget()
        self.tab4.setObjectName(u"tab4")
        self.gridLayout_22 = QGridLayout(self.tab4)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.tab4Frame = QFrame(self.tab4)
        self.tab4Frame.setObjectName(u"tab4Frame")
        self.tab4Frame.setFrameShape(QFrame.StyledPanel)
        self.tab4Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.tab4Frame)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.blockLabel4 = QLabel(self.tab4Frame)
        self.blockLabel4.setObjectName(u"blockLabel4")
        self.blockLabel4.setFont(font1)
        self.blockLabel4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.blockLabel4, 0, 3, 1, 1)

        self.occupancyFrame4 = QFrame(self.tab4Frame)
        self.occupancyFrame4.setObjectName(u"occupancyFrame4")
        self.occupancyFrame4.setAutoFillBackground(True)
        self.occupancyFrame4.setFrameShape(QFrame.Box)
        self.occupancyFrame4.setFrameShadow(QFrame.Raised)
        self.occupancyFrame4.setLineWidth(1)
        self.occupancyFrame4.setMidLineWidth(0)
        self.verticalLayout_46 = QVBoxLayout(self.occupancyFrame4)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.occupancyLabel4 = QLabel(self.occupancyFrame4)
        self.occupancyLabel4.setObjectName(u"occupancyLabel4")
        self.occupancyLabel4.setFont(font1)
        self.occupancyLabel4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_46.addWidget(self.occupancyLabel4)

        self.occupancyValue4 = QLabel(self.occupancyFrame4)
        self.occupancyValue4.setObjectName(u"occupancyValue4")
        self.occupancyValue4.setFont(font1)
        self.occupancyValue4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_46.addWidget(self.occupancyValue4)


        self.gridLayout_19.addWidget(self.occupancyFrame4, 2, 2, 1, 1)

        self.authorityFrame4 = QFrame(self.tab4Frame)
        self.authorityFrame4.setObjectName(u"authorityFrame4")
        self.authorityFrame4.setAutoFillBackground(True)
        self.authorityFrame4.setFrameShape(QFrame.Box)
        self.authorityFrame4.setFrameShadow(QFrame.Raised)
        self.authorityFrame4.setLineWidth(1)
        self.authorityFrame4.setMidLineWidth(0)
        self.verticalLayout_47 = QVBoxLayout(self.authorityFrame4)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.authorityLabel4 = QLabel(self.authorityFrame4)
        self.authorityLabel4.setObjectName(u"authorityLabel4")
        self.authorityLabel4.setFont(font1)
        self.authorityLabel4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.authorityLabel4)

        self.authorityValue4 = QLabel(self.authorityFrame4)
        self.authorityValue4.setObjectName(u"authorityValue4")
        self.authorityValue4.setFont(font1)
        self.authorityValue4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.authorityValue4)


        self.gridLayout_19.addWidget(self.authorityFrame4, 1, 2, 1, 1)

        self.uploadPLC4 = QPushButton(self.tab4Frame)
        self.uploadPLC4.setObjectName(u"uploadPLC4")
        self.uploadPLC4.setEnabled(False)
        self.uploadPLC4.setFont(font1)

        self.gridLayout_19.addWidget(self.uploadPLC4, 4, 4, 1, 1)

        self.suggestedSpeedFrame4 = QFrame(self.tab4Frame)
        self.suggestedSpeedFrame4.setObjectName(u"suggestedSpeedFrame4")
        self.suggestedSpeedFrame4.setAutoFillBackground(True)
        self.suggestedSpeedFrame4.setFrameShape(QFrame.Box)
        self.suggestedSpeedFrame4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.suggestedSpeedFrame4)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.suggestedSpeedLabel4 = QLabel(self.suggestedSpeedFrame4)
        self.suggestedSpeedLabel4.setObjectName(u"suggestedSpeedLabel4")
        self.suggestedSpeedLabel4.setFont(font1)
        self.suggestedSpeedLabel4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_49.addWidget(self.suggestedSpeedLabel4)

        self.suggestedSpeedValue4 = QLabel(self.suggestedSpeedFrame4)
        self.suggestedSpeedValue4.setObjectName(u"suggestedSpeedValue4")
        self.suggestedSpeedValue4.setFont(font1)
        self.suggestedSpeedValue4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_49.addWidget(self.suggestedSpeedValue4)


        self.gridLayout_19.addWidget(self.suggestedSpeedFrame4, 1, 3, 1, 1)

        self.trackLabel4 = QLabel(self.tab4Frame)
        self.trackLabel4.setObjectName(u"trackLabel4")
        self.trackLabel4.setFont(font1)
        self.trackLabel4.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.trackLabel4, 0, 0, 1, 1)

        self.blockSelect4 = QComboBox(self.tab4Frame)
        self.blockSelect4.addItem("")
        self.blockSelect4.setObjectName(u"blockSelect4")
        self.blockSelect4.setEnabled(True)
        self.blockSelect4.setFont(font1)
        self.blockSelect4.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout_19.addWidget(self.blockSelect4, 0, 4, 1, 1)

        self.railwayCrossingFrame4 = QFrame(self.tab4Frame)
        self.railwayCrossingFrame4.setObjectName(u"railwayCrossingFrame4")
        self.railwayCrossingFrame4.setAutoFillBackground(True)
        self.railwayCrossingFrame4.setFrameShape(QFrame.Box)
        self.railwayCrossingFrame4.setFrameShadow(QFrame.Raised)
        self.railwayCrossingFrame4.setLineWidth(1)
        self.railwayCrossingFrame4.setMidLineWidth(0)
        self.gridLayout_21 = QGridLayout(self.railwayCrossingFrame4)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.railwayCrossingLabel4 = QLabel(self.railwayCrossingFrame4)
        self.railwayCrossingLabel4.setObjectName(u"railwayCrossingLabel4")
        self.railwayCrossingLabel4.setFont(font1)
        self.railwayCrossingLabel4.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.railwayCrossingLabel4, 0, 0, 1, 2)

        self.railwayGateLabel4 = QLabel(self.railwayCrossingFrame4)
        self.railwayGateLabel4.setObjectName(u"railwayGateLabel4")
        self.railwayGateLabel4.setFont(font3)

        self.gridLayout_21.addWidget(self.railwayGateLabel4, 1, 0, 1, 1)

        self.railwayGateValue4 = QLabel(self.railwayCrossingFrame4)
        self.railwayGateValue4.setObjectName(u"railwayGateValue4")
        self.railwayGateValue4.setFont(font1)
        self.railwayGateValue4.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.railwayGateValue4, 1, 1, 1, 1)

        self.railwayLightsLabel4 = QLabel(self.railwayCrossingFrame4)
        self.railwayLightsLabel4.setObjectName(u"railwayLightsLabel4")
        self.railwayLightsLabel4.setFont(font3)

        self.gridLayout_21.addWidget(self.railwayLightsLabel4, 2, 0, 1, 1)

        self.railwayLightsValue4 = QLabel(self.railwayCrossingFrame4)
        self.railwayLightsValue4.setObjectName(u"railwayLightsValue4")
        self.railwayLightsValue4.setFont(font1)
        self.railwayLightsValue4.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.railwayLightsValue4, 2, 1, 1, 1)


        self.gridLayout_19.addWidget(self.railwayCrossingFrame4, 1, 0, 2, 1)

        self.displayPLC4 = QTextBrowser(self.tab4Frame)
        self.displayPLC4.setObjectName(u"displayPLC4")
        self.displayPLC4.setFont(font2)

        self.gridLayout_19.addWidget(self.displayPLC4, 3, 0, 1, 5)

        self.commandedSpeedFrame4 = QFrame(self.tab4Frame)
        self.commandedSpeedFrame4.setObjectName(u"commandedSpeedFrame4")
        self.commandedSpeedFrame4.setAutoFillBackground(True)
        self.commandedSpeedFrame4.setFrameShape(QFrame.Box)
        self.commandedSpeedFrame4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.commandedSpeedFrame4)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.commandedSpeedLabel4 = QLabel(self.commandedSpeedFrame4)
        self.commandedSpeedLabel4.setObjectName(u"commandedSpeedLabel4")
        self.commandedSpeedLabel4.setFont(font1)
        self.commandedSpeedLabel4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.commandedSpeedLabel4)

        self.commandedSpeedValue4 = QLabel(self.commandedSpeedFrame4)
        self.commandedSpeedValue4.setObjectName(u"commandedSpeedValue4")
        self.commandedSpeedValue4.setFont(font1)
        self.commandedSpeedValue4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.commandedSpeedValue4)


        self.gridLayout_19.addWidget(self.commandedSpeedFrame4, 2, 3, 1, 1)

        self.statusFrame4 = QFrame(self.tab4Frame)
        self.statusFrame4.setObjectName(u"statusFrame4")
        self.statusFrame4.setAutoFillBackground(True)
        self.statusFrame4.setFrameShape(QFrame.Box)
        self.statusFrame4.setFrameShadow(QFrame.Raised)
        self.statusFrame4.setLineWidth(1)
        self.statusFrame4.setMidLineWidth(0)
        self.verticalLayout_50 = QVBoxLayout(self.statusFrame4)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.statusLabel4 = QLabel(self.statusFrame4)
        self.statusLabel4.setObjectName(u"statusLabel4")
        self.statusLabel4.setFont(font1)
        self.statusLabel4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_50.addWidget(self.statusLabel4)

        self.statusValue4 = QLabel(self.statusFrame4)
        self.statusValue4.setObjectName(u"statusValue4")
        self.statusValue4.setFont(font1)
        self.statusValue4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_50.addWidget(self.statusValue4)


        self.gridLayout_19.addWidget(self.statusFrame4, 1, 4, 1, 1)

        self.switchPositionFrame4 = QFrame(self.tab4Frame)
        self.switchPositionFrame4.setObjectName(u"switchPositionFrame4")
        self.switchPositionFrame4.setAutoFillBackground(True)
        self.switchPositionFrame4.setFrameShape(QFrame.Box)
        self.switchPositionFrame4.setFrameShadow(QFrame.Raised)
        self.switchPositionFrame4.setLineWidth(1)
        self.switchPositionFrame4.setMidLineWidth(0)
        self.gridLayout_20 = QGridLayout(self.switchPositionFrame4)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.switchToValue4 = QLabel(self.switchPositionFrame4)
        self.switchToValue4.setObjectName(u"switchToValue4")
        self.switchToValue4.setFont(font1)
        self.switchToValue4.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.switchToValue4, 1, 2, 1, 1)

        self.switchPositionLabel4 = QLabel(self.switchPositionFrame4)
        self.switchPositionLabel4.setObjectName(u"switchPositionLabel4")
        self.switchPositionLabel4.setFont(font1)
        self.switchPositionLabel4.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.switchPositionLabel4, 0, 0, 1, 3)

        self.switchFromValue4 = QLabel(self.switchPositionFrame4)
        self.switchFromValue4.setObjectName(u"switchFromValue4")
        self.switchFromValue4.setFont(font1)
        self.switchFromValue4.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.switchFromValue4, 1, 0, 1, 1)

        self.switchArrowLabel4 = QLabel(self.switchPositionFrame4)
        self.switchArrowLabel4.setObjectName(u"switchArrowLabel4")
        self.switchArrowLabel4.setFont(font1)
        self.switchArrowLabel4.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.switchArrowLabel4, 1, 1, 1, 1)


        self.gridLayout_19.addWidget(self.switchPositionFrame4, 1, 1, 1, 1)

        self.trafficLightFrame4 = QFrame(self.tab4Frame)
        self.trafficLightFrame4.setObjectName(u"trafficLightFrame4")
        self.trafficLightFrame4.setAutoFillBackground(True)
        self.trafficLightFrame4.setFrameShape(QFrame.Box)
        self.trafficLightFrame4.setFrameShadow(QFrame.Raised)
        self.trafficLightFrame4.setLineWidth(1)
        self.trafficLightFrame4.setMidLineWidth(0)
        self.verticalLayout_48 = QVBoxLayout(self.trafficLightFrame4)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.trafficLightLabel4 = QLabel(self.trafficLightFrame4)
        self.trafficLightLabel4.setObjectName(u"trafficLightLabel4")
        self.trafficLightLabel4.setFont(font1)
        self.trafficLightLabel4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_48.addWidget(self.trafficLightLabel4)

        self.trafficLightValue4 = QLabel(self.trafficLightFrame4)
        self.trafficLightValue4.setObjectName(u"trafficLightValue4")
        self.trafficLightValue4.setFont(font1)
        self.trafficLightValue4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_48.addWidget(self.trafficLightValue4)


        self.gridLayout_19.addWidget(self.trafficLightFrame4, 2, 1, 1, 1)

        self.maintenanceFrame4 = QFrame(self.tab4Frame)
        self.maintenanceFrame4.setObjectName(u"maintenanceFrame4")
        self.maintenanceFrame4.setAutoFillBackground(True)
        self.maintenanceFrame4.setFrameShape(QFrame.Box)
        self.maintenanceFrame4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.maintenanceFrame4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.maintenanceLabel4 = QLabel(self.maintenanceFrame4)
        self.maintenanceLabel4.setObjectName(u"maintenanceLabel4")
        self.maintenanceLabel4.setFont(font3)
        self.maintenanceLabel4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.maintenanceLabel4)

        self.maintenanceValue4 = QLabel(self.maintenanceFrame4)
        self.maintenanceValue4.setObjectName(u"maintenanceValue4")
        self.maintenanceValue4.setFont(font3)
        self.maintenanceValue4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.maintenanceValue4)


        self.gridLayout_19.addWidget(self.maintenanceFrame4, 2, 4, 1, 1)


        self.gridLayout_22.addWidget(self.tab4Frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab4, "")
        self.tab5 = QWidget()
        self.tab5.setObjectName(u"tab5")
        self.gridLayout_26 = QGridLayout(self.tab5)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.tab5Frame = QFrame(self.tab5)
        self.tab5Frame.setObjectName(u"tab5Frame")
        self.tab5Frame.setFrameShape(QFrame.StyledPanel)
        self.tab5Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.tab5Frame)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.blockLabel5 = QLabel(self.tab5Frame)
        self.blockLabel5.setObjectName(u"blockLabel5")
        self.blockLabel5.setFont(font1)
        self.blockLabel5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_23.addWidget(self.blockLabel5, 0, 3, 1, 1)

        self.occupancyFrame5 = QFrame(self.tab5Frame)
        self.occupancyFrame5.setObjectName(u"occupancyFrame5")
        self.occupancyFrame5.setAutoFillBackground(True)
        self.occupancyFrame5.setFrameShape(QFrame.Box)
        self.occupancyFrame5.setFrameShadow(QFrame.Raised)
        self.occupancyFrame5.setLineWidth(1)
        self.occupancyFrame5.setMidLineWidth(0)
        self.verticalLayout_53 = QVBoxLayout(self.occupancyFrame5)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.occupancyLabel5 = QLabel(self.occupancyFrame5)
        self.occupancyLabel5.setObjectName(u"occupancyLabel5")
        self.occupancyLabel5.setFont(font1)
        self.occupancyLabel5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.occupancyLabel5)

        self.occupancyValue5 = QLabel(self.occupancyFrame5)
        self.occupancyValue5.setObjectName(u"occupancyValue5")
        self.occupancyValue5.setFont(font1)
        self.occupancyValue5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.occupancyValue5)


        self.gridLayout_23.addWidget(self.occupancyFrame5, 2, 2, 1, 1)

        self.authorityFrame5 = QFrame(self.tab5Frame)
        self.authorityFrame5.setObjectName(u"authorityFrame5")
        self.authorityFrame5.setAutoFillBackground(True)
        self.authorityFrame5.setFrameShape(QFrame.Box)
        self.authorityFrame5.setFrameShadow(QFrame.Raised)
        self.authorityFrame5.setLineWidth(1)
        self.authorityFrame5.setMidLineWidth(0)
        self.verticalLayout_54 = QVBoxLayout(self.authorityFrame5)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.authorityLabel5 = QLabel(self.authorityFrame5)
        self.authorityLabel5.setObjectName(u"authorityLabel5")
        self.authorityLabel5.setFont(font1)
        self.authorityLabel5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.authorityLabel5)

        self.authorityValue5 = QLabel(self.authorityFrame5)
        self.authorityValue5.setObjectName(u"authorityValue5")
        self.authorityValue5.setFont(font1)
        self.authorityValue5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.authorityValue5)


        self.gridLayout_23.addWidget(self.authorityFrame5, 1, 2, 1, 1)

        self.uploadPLC5 = QPushButton(self.tab5Frame)
        self.uploadPLC5.setObjectName(u"uploadPLC5")
        self.uploadPLC5.setEnabled(False)
        self.uploadPLC5.setFont(font1)

        self.gridLayout_23.addWidget(self.uploadPLC5, 4, 4, 1, 1)

        self.suggestedSpeedFrame5 = QFrame(self.tab5Frame)
        self.suggestedSpeedFrame5.setObjectName(u"suggestedSpeedFrame5")
        self.suggestedSpeedFrame5.setAutoFillBackground(True)
        self.suggestedSpeedFrame5.setFrameShape(QFrame.Box)
        self.suggestedSpeedFrame5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.suggestedSpeedFrame5)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.suggestedSpeedLabel5 = QLabel(self.suggestedSpeedFrame5)
        self.suggestedSpeedLabel5.setObjectName(u"suggestedSpeedLabel5")
        self.suggestedSpeedLabel5.setFont(font1)
        self.suggestedSpeedLabel5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_56.addWidget(self.suggestedSpeedLabel5)

        self.suggestedSpeedValue5 = QLabel(self.suggestedSpeedFrame5)
        self.suggestedSpeedValue5.setObjectName(u"suggestedSpeedValue5")
        self.suggestedSpeedValue5.setFont(font1)
        self.suggestedSpeedValue5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_56.addWidget(self.suggestedSpeedValue5)


        self.gridLayout_23.addWidget(self.suggestedSpeedFrame5, 1, 3, 1, 1)

        self.trackLabel5 = QLabel(self.tab5Frame)
        self.trackLabel5.setObjectName(u"trackLabel5")
        self.trackLabel5.setFont(font1)
        self.trackLabel5.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.trackLabel5, 0, 0, 1, 1)

        self.blockSelect5 = QComboBox(self.tab5Frame)
        self.blockSelect5.addItem("")
        self.blockSelect5.setObjectName(u"blockSelect5")
        self.blockSelect5.setEnabled(True)
        self.blockSelect5.setFont(font1)
        self.blockSelect5.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout_23.addWidget(self.blockSelect5, 0, 4, 1, 1)

        self.railwayCrossingFrame5 = QFrame(self.tab5Frame)
        self.railwayCrossingFrame5.setObjectName(u"railwayCrossingFrame5")
        self.railwayCrossingFrame5.setAutoFillBackground(True)
        self.railwayCrossingFrame5.setFrameShape(QFrame.Box)
        self.railwayCrossingFrame5.setFrameShadow(QFrame.Raised)
        self.railwayCrossingFrame5.setLineWidth(1)
        self.railwayCrossingFrame5.setMidLineWidth(0)
        self.gridLayout_25 = QGridLayout(self.railwayCrossingFrame5)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.railwayCrossingLabel5 = QLabel(self.railwayCrossingFrame5)
        self.railwayCrossingLabel5.setObjectName(u"railwayCrossingLabel5")
        self.railwayCrossingLabel5.setFont(font1)
        self.railwayCrossingLabel5.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.railwayCrossingLabel5, 0, 0, 1, 2)

        self.railwayGateLabel5 = QLabel(self.railwayCrossingFrame5)
        self.railwayGateLabel5.setObjectName(u"railwayGateLabel5")
        self.railwayGateLabel5.setFont(font3)

        self.gridLayout_25.addWidget(self.railwayGateLabel5, 1, 0, 1, 1)

        self.railwayGateValue5 = QLabel(self.railwayCrossingFrame5)
        self.railwayGateValue5.setObjectName(u"railwayGateValue5")
        self.railwayGateValue5.setFont(font1)
        self.railwayGateValue5.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.railwayGateValue5, 1, 1, 1, 1)

        self.railwayLightsLabel5 = QLabel(self.railwayCrossingFrame5)
        self.railwayLightsLabel5.setObjectName(u"railwayLightsLabel5")
        self.railwayLightsLabel5.setFont(font3)

        self.gridLayout_25.addWidget(self.railwayLightsLabel5, 2, 0, 1, 1)

        self.railwayLightsValue5 = QLabel(self.railwayCrossingFrame5)
        self.railwayLightsValue5.setObjectName(u"railwayLightsValue5")
        self.railwayLightsValue5.setFont(font1)
        self.railwayLightsValue5.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.railwayLightsValue5, 2, 1, 1, 1)


        self.gridLayout_23.addWidget(self.railwayCrossingFrame5, 1, 0, 2, 1)

        self.displayPLC5 = QTextBrowser(self.tab5Frame)
        self.displayPLC5.setObjectName(u"displayPLC5")
        self.displayPLC5.setFont(font2)

        self.gridLayout_23.addWidget(self.displayPLC5, 3, 0, 1, 5)

        self.commandedSpeedFrame5 = QFrame(self.tab5Frame)
        self.commandedSpeedFrame5.setObjectName(u"commandedSpeedFrame5")
        self.commandedSpeedFrame5.setAutoFillBackground(True)
        self.commandedSpeedFrame5.setFrameShape(QFrame.Box)
        self.commandedSpeedFrame5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.commandedSpeedFrame5)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.commandedSpeedLabel5 = QLabel(self.commandedSpeedFrame5)
        self.commandedSpeedLabel5.setObjectName(u"commandedSpeedLabel5")
        self.commandedSpeedLabel5.setFont(font1)
        self.commandedSpeedLabel5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_51.addWidget(self.commandedSpeedLabel5)

        self.commandedSpeedValue5 = QLabel(self.commandedSpeedFrame5)
        self.commandedSpeedValue5.setObjectName(u"commandedSpeedValue5")
        self.commandedSpeedValue5.setFont(font1)
        self.commandedSpeedValue5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_51.addWidget(self.commandedSpeedValue5)


        self.gridLayout_23.addWidget(self.commandedSpeedFrame5, 2, 3, 1, 1)

        self.statusFrame5 = QFrame(self.tab5Frame)
        self.statusFrame5.setObjectName(u"statusFrame5")
        self.statusFrame5.setAutoFillBackground(True)
        self.statusFrame5.setFrameShape(QFrame.Box)
        self.statusFrame5.setFrameShadow(QFrame.Raised)
        self.statusFrame5.setLineWidth(1)
        self.statusFrame5.setMidLineWidth(0)
        self.verticalLayout_57 = QVBoxLayout(self.statusFrame5)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.statusLabel5 = QLabel(self.statusFrame5)
        self.statusLabel5.setObjectName(u"statusLabel5")
        self.statusLabel5.setFont(font1)
        self.statusLabel5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_57.addWidget(self.statusLabel5)

        self.statusValue5 = QLabel(self.statusFrame5)
        self.statusValue5.setObjectName(u"statusValue5")
        self.statusValue5.setFont(font1)
        self.statusValue5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_57.addWidget(self.statusValue5)


        self.gridLayout_23.addWidget(self.statusFrame5, 1, 4, 1, 1)

        self.switchPositionFrame5 = QFrame(self.tab5Frame)
        self.switchPositionFrame5.setObjectName(u"switchPositionFrame5")
        self.switchPositionFrame5.setAutoFillBackground(True)
        self.switchPositionFrame5.setFrameShape(QFrame.Box)
        self.switchPositionFrame5.setFrameShadow(QFrame.Raised)
        self.switchPositionFrame5.setLineWidth(1)
        self.switchPositionFrame5.setMidLineWidth(0)
        self.gridLayout_24 = QGridLayout(self.switchPositionFrame5)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.switchPositionLabel5 = QLabel(self.switchPositionFrame5)
        self.switchPositionLabel5.setObjectName(u"switchPositionLabel5")
        self.switchPositionLabel5.setFont(font1)
        self.switchPositionLabel5.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.switchPositionLabel5, 0, 0, 1, 3)

        self.switchArrowLabel5 = QLabel(self.switchPositionFrame5)
        self.switchArrowLabel5.setObjectName(u"switchArrowLabel5")
        self.switchArrowLabel5.setFont(font1)
        self.switchArrowLabel5.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.switchArrowLabel5, 1, 1, 1, 1)

        self.switchFromValue5 = QLabel(self.switchPositionFrame5)
        self.switchFromValue5.setObjectName(u"switchFromValue5")
        self.switchFromValue5.setFont(font1)
        self.switchFromValue5.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.switchFromValue5, 1, 0, 1, 1)

        self.switchToValue5 = QLabel(self.switchPositionFrame5)
        self.switchToValue5.setObjectName(u"switchToValue5")
        self.switchToValue5.setFont(font1)
        self.switchToValue5.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.switchToValue5, 1, 2, 1, 1)


        self.gridLayout_23.addWidget(self.switchPositionFrame5, 1, 1, 1, 1)

        self.trafficLightFrame5 = QFrame(self.tab5Frame)
        self.trafficLightFrame5.setObjectName(u"trafficLightFrame5")
        self.trafficLightFrame5.setAutoFillBackground(True)
        self.trafficLightFrame5.setFrameShape(QFrame.Box)
        self.trafficLightFrame5.setFrameShadow(QFrame.Raised)
        self.trafficLightFrame5.setLineWidth(1)
        self.trafficLightFrame5.setMidLineWidth(0)
        self.verticalLayout_55 = QVBoxLayout(self.trafficLightFrame5)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.trafficLightLabel5 = QLabel(self.trafficLightFrame5)
        self.trafficLightLabel5.setObjectName(u"trafficLightLabel5")
        self.trafficLightLabel5.setFont(font1)
        self.trafficLightLabel5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_55.addWidget(self.trafficLightLabel5)

        self.trafficLightValue5 = QLabel(self.trafficLightFrame5)
        self.trafficLightValue5.setObjectName(u"trafficLightValue5")
        self.trafficLightValue5.setFont(font1)
        self.trafficLightValue5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_55.addWidget(self.trafficLightValue5)


        self.gridLayout_23.addWidget(self.trafficLightFrame5, 2, 1, 1, 1)

        self.maintenanceFrame5 = QFrame(self.tab5Frame)
        self.maintenanceFrame5.setObjectName(u"maintenanceFrame5")
        self.maintenanceFrame5.setAutoFillBackground(True)
        self.maintenanceFrame5.setFrameShape(QFrame.Box)
        self.maintenanceFrame5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.maintenanceFrame5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.maintenanceLabel5 = QLabel(self.maintenanceFrame5)
        self.maintenanceLabel5.setObjectName(u"maintenanceLabel5")
        self.maintenanceLabel5.setFont(font3)
        self.maintenanceLabel5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.maintenanceLabel5)

        self.maintenanceValue5 = QLabel(self.maintenanceFrame5)
        self.maintenanceValue5.setObjectName(u"maintenanceValue5")
        self.maintenanceValue5.setFont(font3)
        self.maintenanceValue5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.maintenanceValue5)


        self.gridLayout_23.addWidget(self.maintenanceFrame5, 2, 4, 1, 1)


        self.gridLayout_26.addWidget(self.tab5Frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab5, "")
        self.tab6 = QWidget()
        self.tab6.setObjectName(u"tab6")
        self.gridLayout_30 = QGridLayout(self.tab6)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.tab6Frame = QFrame(self.tab6)
        self.tab6Frame.setObjectName(u"tab6Frame")
        self.tab6Frame.setFrameShape(QFrame.StyledPanel)
        self.tab6Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.tab6Frame)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.trafficLightFrame6 = QFrame(self.tab6Frame)
        self.trafficLightFrame6.setObjectName(u"trafficLightFrame6")
        self.trafficLightFrame6.setAutoFillBackground(True)
        self.trafficLightFrame6.setFrameShape(QFrame.Box)
        self.trafficLightFrame6.setFrameShadow(QFrame.Raised)
        self.trafficLightFrame6.setLineWidth(1)
        self.trafficLightFrame6.setMidLineWidth(0)
        self.verticalLayout_62 = QVBoxLayout(self.trafficLightFrame6)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.trafficLightLabel6 = QLabel(self.trafficLightFrame6)
        self.trafficLightLabel6.setObjectName(u"trafficLightLabel6")
        self.trafficLightLabel6.setFont(font1)
        self.trafficLightLabel6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_62.addWidget(self.trafficLightLabel6)

        self.trafficLightValue6 = QLabel(self.trafficLightFrame6)
        self.trafficLightValue6.setObjectName(u"trafficLightValue6")
        self.trafficLightValue6.setFont(font1)
        self.trafficLightValue6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_62.addWidget(self.trafficLightValue6)


        self.gridLayout_27.addWidget(self.trafficLightFrame6, 2, 1, 1, 1)

        self.suggestedSpeedFrame6 = QFrame(self.tab6Frame)
        self.suggestedSpeedFrame6.setObjectName(u"suggestedSpeedFrame6")
        self.suggestedSpeedFrame6.setAutoFillBackground(True)
        self.suggestedSpeedFrame6.setFrameShape(QFrame.Box)
        self.suggestedSpeedFrame6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.suggestedSpeedFrame6)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.suggestedSpeedLabel6 = QLabel(self.suggestedSpeedFrame6)
        self.suggestedSpeedLabel6.setObjectName(u"suggestedSpeedLabel6")
        self.suggestedSpeedLabel6.setFont(font1)
        self.suggestedSpeedLabel6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_63.addWidget(self.suggestedSpeedLabel6)

        self.suggestedSpeedValue6 = QLabel(self.suggestedSpeedFrame6)
        self.suggestedSpeedValue6.setObjectName(u"suggestedSpeedValue6")
        self.suggestedSpeedValue6.setFont(font1)
        self.suggestedSpeedValue6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_63.addWidget(self.suggestedSpeedValue6)


        self.gridLayout_27.addWidget(self.suggestedSpeedFrame6, 1, 3, 1, 1)

        self.uploadPLC6 = QPushButton(self.tab6Frame)
        self.uploadPLC6.setObjectName(u"uploadPLC6")
        self.uploadPLC6.setEnabled(False)
        self.uploadPLC6.setFont(font1)

        self.gridLayout_27.addWidget(self.uploadPLC6, 4, 4, 1, 1)

        self.trackLabel6 = QLabel(self.tab6Frame)
        self.trackLabel6.setObjectName(u"trackLabel6")
        self.trackLabel6.setFont(font1)
        self.trackLabel6.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.trackLabel6, 0, 0, 1, 1)

        self.occupancyFrame6 = QFrame(self.tab6Frame)
        self.occupancyFrame6.setObjectName(u"occupancyFrame6")
        self.occupancyFrame6.setAutoFillBackground(True)
        self.occupancyFrame6.setFrameShape(QFrame.Box)
        self.occupancyFrame6.setFrameShadow(QFrame.Raised)
        self.occupancyFrame6.setLineWidth(1)
        self.occupancyFrame6.setMidLineWidth(0)
        self.verticalLayout_60 = QVBoxLayout(self.occupancyFrame6)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.occupancyLabel6 = QLabel(self.occupancyFrame6)
        self.occupancyLabel6.setObjectName(u"occupancyLabel6")
        self.occupancyLabel6.setFont(font1)
        self.occupancyLabel6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_60.addWidget(self.occupancyLabel6)

        self.occupancyValue6 = QLabel(self.occupancyFrame6)
        self.occupancyValue6.setObjectName(u"occupancyValue6")
        self.occupancyValue6.setFont(font1)
        self.occupancyValue6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_60.addWidget(self.occupancyValue6)


        self.gridLayout_27.addWidget(self.occupancyFrame6, 2, 2, 1, 1)

        self.authorityFrame6 = QFrame(self.tab6Frame)
        self.authorityFrame6.setObjectName(u"authorityFrame6")
        self.authorityFrame6.setAutoFillBackground(True)
        self.authorityFrame6.setFrameShape(QFrame.Box)
        self.authorityFrame6.setFrameShadow(QFrame.Raised)
        self.authorityFrame6.setLineWidth(1)
        self.authorityFrame6.setMidLineWidth(0)
        self.verticalLayout_61 = QVBoxLayout(self.authorityFrame6)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.authorityLabel6 = QLabel(self.authorityFrame6)
        self.authorityLabel6.setObjectName(u"authorityLabel6")
        self.authorityLabel6.setFont(font1)
        self.authorityLabel6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_61.addWidget(self.authorityLabel6)

        self.authorityValue6 = QLabel(self.authorityFrame6)
        self.authorityValue6.setObjectName(u"authorityValue6")
        self.authorityValue6.setFont(font1)
        self.authorityValue6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_61.addWidget(self.authorityValue6)


        self.gridLayout_27.addWidget(self.authorityFrame6, 1, 2, 1, 1)

        self.commandedSpeedFrame6 = QFrame(self.tab6Frame)
        self.commandedSpeedFrame6.setObjectName(u"commandedSpeedFrame6")
        self.commandedSpeedFrame6.setAutoFillBackground(True)
        self.commandedSpeedFrame6.setFrameShape(QFrame.Box)
        self.commandedSpeedFrame6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.commandedSpeedFrame6)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.commandedSpeedLabel6 = QLabel(self.commandedSpeedFrame6)
        self.commandedSpeedLabel6.setObjectName(u"commandedSpeedLabel6")
        self.commandedSpeedLabel6.setFont(font1)
        self.commandedSpeedLabel6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_58.addWidget(self.commandedSpeedLabel6)

        self.commandedSpeedValue6 = QLabel(self.commandedSpeedFrame6)
        self.commandedSpeedValue6.setObjectName(u"commandedSpeedValue6")
        self.commandedSpeedValue6.setFont(font1)
        self.commandedSpeedValue6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_58.addWidget(self.commandedSpeedValue6)


        self.gridLayout_27.addWidget(self.commandedSpeedFrame6, 2, 3, 1, 1)

        self.switchPositionFrame6 = QFrame(self.tab6Frame)
        self.switchPositionFrame6.setObjectName(u"switchPositionFrame6")
        self.switchPositionFrame6.setAutoFillBackground(True)
        self.switchPositionFrame6.setFrameShape(QFrame.Box)
        self.switchPositionFrame6.setFrameShadow(QFrame.Raised)
        self.switchPositionFrame6.setLineWidth(1)
        self.switchPositionFrame6.setMidLineWidth(0)
        self.gridLayout_28 = QGridLayout(self.switchPositionFrame6)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.switchToValue6 = QLabel(self.switchPositionFrame6)
        self.switchToValue6.setObjectName(u"switchToValue6")
        self.switchToValue6.setFont(font1)
        self.switchToValue6.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.switchToValue6, 1, 2, 1, 1)

        self.switchPositionLabel6 = QLabel(self.switchPositionFrame6)
        self.switchPositionLabel6.setObjectName(u"switchPositionLabel6")
        self.switchPositionLabel6.setFont(font1)
        self.switchPositionLabel6.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.switchPositionLabel6, 0, 0, 1, 3)

        self.switchFromValue6 = QLabel(self.switchPositionFrame6)
        self.switchFromValue6.setObjectName(u"switchFromValue6")
        self.switchFromValue6.setFont(font1)
        self.switchFromValue6.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.switchFromValue6, 1, 0, 1, 1)

        self.switchArrowLabel6 = QLabel(self.switchPositionFrame6)
        self.switchArrowLabel6.setObjectName(u"switchArrowLabel6")
        self.switchArrowLabel6.setFont(font1)
        self.switchArrowLabel6.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.switchArrowLabel6, 1, 1, 1, 1)


        self.gridLayout_27.addWidget(self.switchPositionFrame6, 1, 1, 1, 1)

        self.statusFrame6 = QFrame(self.tab6Frame)
        self.statusFrame6.setObjectName(u"statusFrame6")
        self.statusFrame6.setAutoFillBackground(True)
        self.statusFrame6.setFrameShape(QFrame.Box)
        self.statusFrame6.setFrameShadow(QFrame.Raised)
        self.statusFrame6.setLineWidth(1)
        self.statusFrame6.setMidLineWidth(0)
        self.verticalLayout_64 = QVBoxLayout(self.statusFrame6)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.statusLabel6 = QLabel(self.statusFrame6)
        self.statusLabel6.setObjectName(u"statusLabel6")
        self.statusLabel6.setFont(font1)
        self.statusLabel6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_64.addWidget(self.statusLabel6)

        self.statusValue6 = QLabel(self.statusFrame6)
        self.statusValue6.setObjectName(u"statusValue6")
        self.statusValue6.setFont(font1)
        self.statusValue6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_64.addWidget(self.statusValue6)


        self.gridLayout_27.addWidget(self.statusFrame6, 1, 4, 1, 1)

        self.displayPLC6 = QTextBrowser(self.tab6Frame)
        self.displayPLC6.setObjectName(u"displayPLC6")
        self.displayPLC6.setFont(font2)

        self.gridLayout_27.addWidget(self.displayPLC6, 3, 0, 1, 5)

        self.blockLabel6 = QLabel(self.tab6Frame)
        self.blockLabel6.setObjectName(u"blockLabel6")
        self.blockLabel6.setFont(font1)
        self.blockLabel6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.blockLabel6, 0, 3, 1, 1)

        self.blockSelect6 = QComboBox(self.tab6Frame)
        self.blockSelect6.addItem("")
        self.blockSelect6.setObjectName(u"blockSelect6")
        self.blockSelect6.setEnabled(True)
        self.blockSelect6.setFont(font1)
        self.blockSelect6.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout_27.addWidget(self.blockSelect6, 0, 4, 1, 1)

        self.railwayCrossingFrame6 = QFrame(self.tab6Frame)
        self.railwayCrossingFrame6.setObjectName(u"railwayCrossingFrame6")
        self.railwayCrossingFrame6.setAutoFillBackground(True)
        self.railwayCrossingFrame6.setFrameShape(QFrame.Box)
        self.railwayCrossingFrame6.setFrameShadow(QFrame.Raised)
        self.railwayCrossingFrame6.setLineWidth(1)
        self.railwayCrossingFrame6.setMidLineWidth(0)
        self.gridLayout_29 = QGridLayout(self.railwayCrossingFrame6)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.railwayCrossingLabel6 = QLabel(self.railwayCrossingFrame6)
        self.railwayCrossingLabel6.setObjectName(u"railwayCrossingLabel6")
        self.railwayCrossingLabel6.setFont(font1)
        self.railwayCrossingLabel6.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.railwayCrossingLabel6, 0, 0, 1, 2)

        self.railwayGateLabel6 = QLabel(self.railwayCrossingFrame6)
        self.railwayGateLabel6.setObjectName(u"railwayGateLabel6")
        self.railwayGateLabel6.setFont(font3)

        self.gridLayout_29.addWidget(self.railwayGateLabel6, 1, 0, 1, 1)

        self.railwayGateValue6 = QLabel(self.railwayCrossingFrame6)
        self.railwayGateValue6.setObjectName(u"railwayGateValue6")
        self.railwayGateValue6.setFont(font1)
        self.railwayGateValue6.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.railwayGateValue6, 1, 1, 1, 1)

        self.railwayLightsLabel6 = QLabel(self.railwayCrossingFrame6)
        self.railwayLightsLabel6.setObjectName(u"railwayLightsLabel6")
        self.railwayLightsLabel6.setFont(font3)

        self.gridLayout_29.addWidget(self.railwayLightsLabel6, 2, 0, 1, 1)

        self.railwayLightsValue6 = QLabel(self.railwayCrossingFrame6)
        self.railwayLightsValue6.setObjectName(u"railwayLightsValue6")
        self.railwayLightsValue6.setFont(font1)
        self.railwayLightsValue6.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.railwayLightsValue6, 2, 1, 1, 1)


        self.gridLayout_27.addWidget(self.railwayCrossingFrame6, 1, 0, 2, 1)

        self.maintenanceFrame6 = QFrame(self.tab6Frame)
        self.maintenanceFrame6.setObjectName(u"maintenanceFrame6")
        self.maintenanceFrame6.setAutoFillBackground(True)
        self.maintenanceFrame6.setFrameShape(QFrame.Box)
        self.maintenanceFrame6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.maintenanceFrame6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.maintenanceLabel6 = QLabel(self.maintenanceFrame6)
        self.maintenanceLabel6.setObjectName(u"maintenanceLabel6")
        self.maintenanceLabel6.setFont(font3)
        self.maintenanceLabel6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.maintenanceLabel6)

        self.maintenanceValue6 = QLabel(self.maintenanceFrame6)
        self.maintenanceValue6.setObjectName(u"maintenanceValue6")
        self.maintenanceValue6.setFont(font3)
        self.maintenanceValue6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.maintenanceValue6)


        self.gridLayout_27.addWidget(self.maintenanceFrame6, 2, 4, 1, 1)


        self.gridLayout_30.addWidget(self.tab6Frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab6, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wayside Controller", None))
        self.suggestedSpeedLabel1.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.suggestedSpeedValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.blockLabel1.setText(QCoreApplication.translate("MainWindow", u"Block:", None))
        self.blockSelect1.setItemText(0, "")

        self.blockSelect1.setCurrentText("")
        self.authorityLabel1.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.authorityValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchPositionLabel1.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchArrowLabel1.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.switchFromValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchToValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.uploadPLC1.setText(QCoreApplication.translate("MainWindow", u"Upload PLC", None))
        self.statusLabel1.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trafficLightLabel1.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trackLabel1.setText(QCoreApplication.translate("MainWindow", u"Track Line: Green", None))
        self.occupancyLabel1.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.occupancyValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel1.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.maintenanceLabel1.setText(QCoreApplication.translate("MainWindow", u"Maintenance", None))
        self.maintenanceValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayCrossingLabel1.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel1.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel1.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Wayside 1", None))
        self.blockLabel2.setText(QCoreApplication.translate("MainWindow", u"Block:", None))
        self.occupancyLabel2.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.occupancyValue2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.authorityLabel2.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.authorityValue2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.uploadPLC2.setText(QCoreApplication.translate("MainWindow", u"Upload PLC", None))
        self.suggestedSpeedLabel2.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.suggestedSpeedValue2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trackLabel2.setText(QCoreApplication.translate("MainWindow", u"Track Line: Green", None))
        self.blockSelect2.setItemText(0, "")

        self.blockSelect2.setCurrentText("")
        self.railwayCrossingLabel2.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel2.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel2.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel2.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel2.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchPositionLabel2.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchToValue2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchArrowLabel2.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.switchFromValue2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trafficLightLabel2.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.maintenanceLabel2.setText(QCoreApplication.translate("MainWindow", u"Maintenance", None))
        self.maintenanceValue2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"Wayside 2", None))
        self.blockLabel3.setText(QCoreApplication.translate("MainWindow", u"Block:", None))
        self.occupancyLabel3.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.occupancyValue3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.authorityLabel3.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.authorityValue3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.uploadPLC3.setText(QCoreApplication.translate("MainWindow", u"Upload PLC", None))
        self.suggestedSpeedLabel3.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.suggestedSpeedValue3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trackLabel3.setText(QCoreApplication.translate("MainWindow", u"Track Line: Green", None))
        self.blockSelect3.setItemText(0, "")

        self.blockSelect3.setCurrentText("")
        self.railwayCrossingLabel3.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel3.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel3.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel3.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel3.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchPositionLabel3.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchFromValue3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchToValue3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchArrowLabel3.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.trafficLightLabel3.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.maintenanceLabel3.setText(QCoreApplication.translate("MainWindow", u"Maintenance", None))
        self.maintenanceValue3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QCoreApplication.translate("MainWindow", u"Wayside 3", None))
        self.blockLabel4.setText(QCoreApplication.translate("MainWindow", u"Block:", None))
        self.occupancyLabel4.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.occupancyValue4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.authorityLabel4.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.authorityValue4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.uploadPLC4.setText(QCoreApplication.translate("MainWindow", u"Upload PLC", None))
        self.suggestedSpeedLabel4.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.suggestedSpeedValue4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trackLabel4.setText(QCoreApplication.translate("MainWindow", u"Track Line: Red", None))
        self.blockSelect4.setItemText(0, "")

        self.blockSelect4.setCurrentText("")
        self.railwayCrossingLabel4.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel4.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel4.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel4.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel4.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchToValue4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchPositionLabel4.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchFromValue4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchArrowLabel4.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.trafficLightLabel4.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.maintenanceLabel4.setText(QCoreApplication.translate("MainWindow", u"Maintenance", None))
        self.maintenanceValue4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), QCoreApplication.translate("MainWindow", u"Wayside 4", None))
        self.blockLabel5.setText(QCoreApplication.translate("MainWindow", u"Block:", None))
        self.occupancyLabel5.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.occupancyValue5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.authorityLabel5.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.authorityValue5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.uploadPLC5.setText(QCoreApplication.translate("MainWindow", u"Upload PLC", None))
        self.suggestedSpeedLabel5.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.suggestedSpeedValue5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trackLabel5.setText(QCoreApplication.translate("MainWindow", u"Track Line: Red", None))
        self.blockSelect5.setItemText(0, "")

        self.blockSelect5.setCurrentText("")
        self.railwayCrossingLabel5.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel5.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel5.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel5.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel5.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchPositionLabel5.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchArrowLabel5.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.switchFromValue5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchToValue5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trafficLightLabel5.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.maintenanceLabel5.setText(QCoreApplication.translate("MainWindow", u"Maintenance", None))
        self.maintenanceValue5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), QCoreApplication.translate("MainWindow", u"Wayside 5", None))
        self.trafficLightLabel6.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.suggestedSpeedLabel6.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.suggestedSpeedValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.uploadPLC6.setText(QCoreApplication.translate("MainWindow", u"Upload PLC", None))
        self.trackLabel6.setText(QCoreApplication.translate("MainWindow", u"Track Line: Red", None))
        self.occupancyLabel6.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.occupancyValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.authorityLabel6.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.authorityValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel6.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchToValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchPositionLabel6.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchFromValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchArrowLabel6.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.statusLabel6.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.blockLabel6.setText(QCoreApplication.translate("MainWindow", u"Block:", None))
        self.blockSelect6.setItemText(0, "")

        self.blockSelect6.setCurrentText("")
        self.railwayCrossingLabel6.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel6.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel6.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.maintenanceLabel6.setText(QCoreApplication.translate("MainWindow", u"Maintenance", None))
        self.maintenanceValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab6), QCoreApplication.translate("MainWindow", u"Wayside 6", None))
    # retranslateUi

