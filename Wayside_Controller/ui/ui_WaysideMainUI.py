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
        MainWindow.resize(1012, 632)
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
        self.trackLabel1 = QLabel(self.tab1Frame)
        self.trackLabel1.setObjectName(u"trackLabel1")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.trackLabel1.setFont(font1)
        self.trackLabel1.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.trackLabel1, 0, 0, 1, 1)

        self.uploadPLC1 = QPushButton(self.tab1Frame)
        self.uploadPLC1.setObjectName(u"uploadPLC1")
        self.uploadPLC1.setFont(font1)

        self.gridLayout_11.addWidget(self.uploadPLC1, 4, 4, 1, 1)

        self.railwayCrossingFrame1 = QFrame(self.tab1Frame)
        self.railwayCrossingFrame1.setObjectName(u"railwayCrossingFrame1")
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
        font2 = QFont()
        font2.setPointSize(10)
        self.railwayGateLabel1.setFont(font2)

        self.gridLayout_5.addWidget(self.railwayGateLabel1, 1, 0, 1, 1)

        self.railwayGateValue1 = QLabel(self.railwayCrossingFrame1)
        self.railwayGateValue1.setObjectName(u"railwayGateValue1")
        self.railwayGateValue1.setFont(font1)
        self.railwayGateValue1.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.railwayGateValue1, 1, 1, 1, 1)

        self.railwayLightsLabel1 = QLabel(self.railwayCrossingFrame1)
        self.railwayLightsLabel1.setObjectName(u"railwayLightsLabel1")
        self.railwayLightsLabel1.setFont(font2)

        self.gridLayout_5.addWidget(self.railwayLightsLabel1, 2, 0, 1, 1)

        self.railwayLightsValue1 = QLabel(self.railwayCrossingFrame1)
        self.railwayLightsValue1.setObjectName(u"railwayLightsValue1")
        self.railwayLightsValue1.setFont(font1)
        self.railwayLightsValue1.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.railwayLightsValue1, 2, 1, 1, 1)


        self.gridLayout_11.addWidget(self.railwayCrossingFrame1, 1, 0, 2, 1)

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

        self.suggestedSpeedFrame1 = QFrame(self.tab1Frame)
        self.suggestedSpeedFrame1.setObjectName(u"suggestedSpeedFrame1")
        self.suggestedSpeedFrame1.setAutoFillBackground(True)
        self.suggestedSpeedFrame1.setFrameShape(QFrame.Box)
        self.suggestedSpeedFrame1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.suggestedSpeedFrame1)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.suggestedSpeedLabel1 = QLabel(self.suggestedSpeedFrame1)
        self.suggestedSpeedLabel1.setObjectName(u"suggestedSpeedLabel1")
        self.suggestedSpeedLabel1.setFont(font1)
        self.suggestedSpeedLabel1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.suggestedSpeedLabel1)

        self.suggestedSpeedValue1 = QLabel(self.suggestedSpeedFrame1)
        self.suggestedSpeedValue1.setObjectName(u"suggestedSpeedValue1")
        self.suggestedSpeedValue1.setFont(font1)
        self.suggestedSpeedValue1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.suggestedSpeedValue1)


        self.gridLayout_11.addWidget(self.suggestedSpeedFrame1, 1, 3, 1, 1)

        self.displayPLC1 = QTextBrowser(self.tab1Frame)
        self.displayPLC1.setObjectName(u"displayPLC1")
        font3 = QFont()
        font3.setPointSize(12)
        self.displayPLC1.setFont(font3)

        self.gridLayout_11.addWidget(self.displayPLC1, 3, 0, 1, 5)

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


        self.gridLayout_11.addWidget(self.trafficLightFrame1, 2, 4, 1, 1)

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

        self.switchPositionFrame1 = QFrame(self.tab1Frame)
        self.switchPositionFrame1.setObjectName(u"switchPositionFrame1")
        self.switchPositionFrame1.setAutoFillBackground(True)
        self.switchPositionFrame1.setFrameShape(QFrame.Box)
        self.switchPositionFrame1.setFrameShadow(QFrame.Raised)
        self.switchPositionFrame1.setLineWidth(1)
        self.switchPositionFrame1.setMidLineWidth(0)
        self.gridLayout_10 = QGridLayout(self.switchPositionFrame1)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
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

        self.switchButton1 = QPushButton(self.switchPositionFrame1)
        self.switchButton1.setObjectName(u"switchButton1")
        self.switchButton1.setEnabled(False)
        self.switchButton1.setFont(font2)
        self.switchButton1.setAutoDefault(False)

        self.gridLayout_10.addWidget(self.switchButton1, 2, 1, 1, 1)


        self.gridLayout_11.addWidget(self.switchPositionFrame1, 1, 1, 2, 1)


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
        self.railwayGateLabel2.setFont(font2)

        self.gridLayout_14.addWidget(self.railwayGateLabel2, 1, 0, 1, 1)

        self.railwayGateValue2 = QLabel(self.railwayCrossingFrame2)
        self.railwayGateValue2.setObjectName(u"railwayGateValue2")
        self.railwayGateValue2.setFont(font1)
        self.railwayGateValue2.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.railwayGateValue2, 1, 1, 1, 1)

        self.railwayLightsLabel2 = QLabel(self.railwayCrossingFrame2)
        self.railwayLightsLabel2.setObjectName(u"railwayLightsLabel2")
        self.railwayLightsLabel2.setFont(font2)

        self.gridLayout_14.addWidget(self.railwayLightsLabel2, 2, 0, 1, 1)

        self.railwayLightsValue2 = QLabel(self.railwayCrossingFrame2)
        self.railwayLightsValue2.setObjectName(u"railwayLightsValue2")
        self.railwayLightsValue2.setFont(font1)
        self.railwayLightsValue2.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.railwayLightsValue2, 2, 1, 1, 1)


        self.gridLayout_12.addWidget(self.railwayCrossingFrame2, 1, 0, 2, 1)

        self.displayPLC2 = QTextBrowser(self.tab2Frame)
        self.displayPLC2.setObjectName(u"displayPLC2")
        self.displayPLC2.setFont(font3)

        self.gridLayout_12.addWidget(self.displayPLC2, 3, 0, 1, 5)

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


        self.gridLayout_12.addWidget(self.trafficLightFrame2, 2, 4, 1, 1)

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

        self.switchArrowLabel2 = QLabel(self.switchPositionFrame2)
        self.switchArrowLabel2.setObjectName(u"switchArrowLabel2")
        self.switchArrowLabel2.setFont(font1)
        self.switchArrowLabel2.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.switchArrowLabel2, 1, 1, 1, 1)

        self.switchToValue2 = QLabel(self.switchPositionFrame2)
        self.switchToValue2.setObjectName(u"switchToValue2")
        self.switchToValue2.setFont(font1)
        self.switchToValue2.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.switchToValue2, 1, 2, 1, 1)

        self.switchFromValue2 = QLabel(self.switchPositionFrame2)
        self.switchFromValue2.setObjectName(u"switchFromValue2")
        self.switchFromValue2.setFont(font1)
        self.switchFromValue2.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.switchFromValue2, 1, 0, 1, 1)

        self.switchButton2 = QPushButton(self.switchPositionFrame2)
        self.switchButton2.setObjectName(u"switchButton2")
        self.switchButton2.setEnabled(False)
        self.switchButton2.setFont(font2)

        self.gridLayout_13.addWidget(self.switchButton2, 2, 1, 1, 1)


        self.gridLayout_12.addWidget(self.switchPositionFrame2, 1, 1, 2, 1)


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
        self.railwayGateLabel3.setFont(font2)

        self.gridLayout_17.addWidget(self.railwayGateLabel3, 1, 0, 1, 1)

        self.railwayGateValue3 = QLabel(self.railwayCrossingFrame3)
        self.railwayGateValue3.setObjectName(u"railwayGateValue3")
        self.railwayGateValue3.setFont(font1)
        self.railwayGateValue3.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.railwayGateValue3, 1, 1, 1, 1)

        self.railwayLightsLabel3 = QLabel(self.railwayCrossingFrame3)
        self.railwayLightsLabel3.setObjectName(u"railwayLightsLabel3")
        self.railwayLightsLabel3.setFont(font2)

        self.gridLayout_17.addWidget(self.railwayLightsLabel3, 2, 0, 1, 1)

        self.railwayLightsValue3 = QLabel(self.railwayCrossingFrame3)
        self.railwayLightsValue3.setObjectName(u"railwayLightsValue3")
        self.railwayLightsValue3.setFont(font1)
        self.railwayLightsValue3.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.railwayLightsValue3, 2, 1, 1, 1)


        self.gridLayout_15.addWidget(self.railwayCrossingFrame3, 1, 0, 2, 1)

        self.displayPLC3 = QTextBrowser(self.tab3Frame)
        self.displayPLC3.setObjectName(u"displayPLC3")
        self.displayPLC3.setFont(font3)

        self.gridLayout_15.addWidget(self.displayPLC3, 3, 0, 1, 5)

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


        self.gridLayout_15.addWidget(self.trafficLightFrame3, 2, 4, 1, 1)

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
        self.switchFromValue3 = QLabel(self.switchPositionFrame3)
        self.switchFromValue3.setObjectName(u"switchFromValue3")
        self.switchFromValue3.setFont(font1)
        self.switchFromValue3.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.switchFromValue3, 1, 0, 1, 1)

        self.switchArrowLabel3 = QLabel(self.switchPositionFrame3)
        self.switchArrowLabel3.setObjectName(u"switchArrowLabel3")
        self.switchArrowLabel3.setFont(font1)
        self.switchArrowLabel3.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.switchArrowLabel3, 1, 1, 1, 1)

        self.switchToValue3 = QLabel(self.switchPositionFrame3)
        self.switchToValue3.setObjectName(u"switchToValue3")
        self.switchToValue3.setFont(font1)
        self.switchToValue3.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.switchToValue3, 1, 2, 1, 1)

        self.switchPositionLabel3 = QLabel(self.switchPositionFrame3)
        self.switchPositionLabel3.setObjectName(u"switchPositionLabel3")
        self.switchPositionLabel3.setFont(font1)
        self.switchPositionLabel3.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.switchPositionLabel3, 0, 0, 1, 3)

        self.switchButton3 = QPushButton(self.switchPositionFrame3)
        self.switchButton3.setObjectName(u"switchButton3")
        self.switchButton3.setEnabled(False)
        self.switchButton3.setFont(font2)

        self.gridLayout_16.addWidget(self.switchButton3, 2, 1, 1, 1)


        self.gridLayout_15.addWidget(self.switchPositionFrame3, 1, 1, 2, 1)


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
        self.railwayGateLabel4.setFont(font2)

        self.gridLayout_21.addWidget(self.railwayGateLabel4, 1, 0, 1, 1)

        self.railwayGateValue4 = QLabel(self.railwayCrossingFrame4)
        self.railwayGateValue4.setObjectName(u"railwayGateValue4")
        self.railwayGateValue4.setFont(font1)
        self.railwayGateValue4.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.railwayGateValue4, 1, 1, 1, 1)

        self.railwayLightsLabel4 = QLabel(self.railwayCrossingFrame4)
        self.railwayLightsLabel4.setObjectName(u"railwayLightsLabel4")
        self.railwayLightsLabel4.setFont(font2)

        self.gridLayout_21.addWidget(self.railwayLightsLabel4, 2, 0, 1, 1)

        self.railwayLightsValue4 = QLabel(self.railwayCrossingFrame4)
        self.railwayLightsValue4.setObjectName(u"railwayLightsValue4")
        self.railwayLightsValue4.setFont(font1)
        self.railwayLightsValue4.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.railwayLightsValue4, 2, 1, 1, 1)


        self.gridLayout_19.addWidget(self.railwayCrossingFrame4, 1, 0, 2, 1)

        self.displayPLC4 = QTextBrowser(self.tab4Frame)
        self.displayPLC4.setObjectName(u"displayPLC4")
        self.displayPLC4.setFont(font3)

        self.gridLayout_19.addWidget(self.displayPLC4, 3, 0, 1, 5)

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


        self.gridLayout_19.addWidget(self.trafficLightFrame4, 2, 4, 1, 1)

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

        self.switchButton4 = QPushButton(self.switchPositionFrame4)
        self.switchButton4.setObjectName(u"switchButton4")
        self.switchButton4.setEnabled(False)
        self.switchButton4.setFont(font2)

        self.gridLayout_20.addWidget(self.switchButton4, 2, 1, 1, 1)


        self.gridLayout_19.addWidget(self.switchPositionFrame4, 1, 1, 2, 1)


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
        self.railwayGateLabel5.setFont(font2)

        self.gridLayout_25.addWidget(self.railwayGateLabel5, 1, 0, 1, 1)

        self.railwayGateValue5 = QLabel(self.railwayCrossingFrame5)
        self.railwayGateValue5.setObjectName(u"railwayGateValue5")
        self.railwayGateValue5.setFont(font1)
        self.railwayGateValue5.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.railwayGateValue5, 1, 1, 1, 1)

        self.railwayLightsLabel5 = QLabel(self.railwayCrossingFrame5)
        self.railwayLightsLabel5.setObjectName(u"railwayLightsLabel5")
        self.railwayLightsLabel5.setFont(font2)

        self.gridLayout_25.addWidget(self.railwayLightsLabel5, 2, 0, 1, 1)

        self.railwayLightsValue5 = QLabel(self.railwayCrossingFrame5)
        self.railwayLightsValue5.setObjectName(u"railwayLightsValue5")
        self.railwayLightsValue5.setFont(font1)
        self.railwayLightsValue5.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.railwayLightsValue5, 2, 1, 1, 1)


        self.gridLayout_23.addWidget(self.railwayCrossingFrame5, 1, 0, 2, 1)

        self.displayPLC5 = QTextBrowser(self.tab5Frame)
        self.displayPLC5.setObjectName(u"displayPLC5")
        self.displayPLC5.setFont(font3)

        self.gridLayout_23.addWidget(self.displayPLC5, 3, 0, 1, 5)

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


        self.gridLayout_23.addWidget(self.trafficLightFrame5, 2, 4, 1, 1)

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

        self.switchFromValue5 = QLabel(self.switchPositionFrame5)
        self.switchFromValue5.setObjectName(u"switchFromValue5")
        self.switchFromValue5.setFont(font1)
        self.switchFromValue5.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.switchFromValue5, 1, 0, 1, 1)

        self.switchArrowLabel5 = QLabel(self.switchPositionFrame5)
        self.switchArrowLabel5.setObjectName(u"switchArrowLabel5")
        self.switchArrowLabel5.setFont(font1)
        self.switchArrowLabel5.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.switchArrowLabel5, 1, 1, 1, 1)

        self.switchToValue5 = QLabel(self.switchPositionFrame5)
        self.switchToValue5.setObjectName(u"switchToValue5")
        self.switchToValue5.setFont(font1)
        self.switchToValue5.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.switchToValue5, 1, 2, 1, 1)

        self.switchButton5 = QPushButton(self.switchPositionFrame5)
        self.switchButton5.setObjectName(u"switchButton5")
        self.switchButton5.setEnabled(False)
        self.switchButton5.setFont(font2)

        self.gridLayout_24.addWidget(self.switchButton5, 2, 1, 1, 1)


        self.gridLayout_23.addWidget(self.switchPositionFrame5, 1, 1, 2, 1)


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
        self.blockLabel6 = QLabel(self.tab6Frame)
        self.blockLabel6.setObjectName(u"blockLabel6")
        self.blockLabel6.setFont(font1)
        self.blockLabel6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.blockLabel6, 0, 3, 1, 1)

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

        self.uploadPLC6 = QPushButton(self.tab6Frame)
        self.uploadPLC6.setObjectName(u"uploadPLC6")
        self.uploadPLC6.setFont(font1)

        self.gridLayout_27.addWidget(self.uploadPLC6, 4, 4, 1, 1)

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

        self.trackLabel6 = QLabel(self.tab6Frame)
        self.trackLabel6.setObjectName(u"trackLabel6")
        self.trackLabel6.setFont(font1)
        self.trackLabel6.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.trackLabel6, 0, 0, 1, 1)

        self.blockSelect6 = QComboBox(self.tab6Frame)
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
        self.railwayGateLabel6.setFont(font2)

        self.gridLayout_29.addWidget(self.railwayGateLabel6, 1, 0, 1, 1)

        self.railwayGateValue6 = QLabel(self.railwayCrossingFrame6)
        self.railwayGateValue6.setObjectName(u"railwayGateValue6")
        self.railwayGateValue6.setFont(font1)
        self.railwayGateValue6.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.railwayGateValue6, 1, 1, 1, 1)

        self.railwayLightsLabel6 = QLabel(self.railwayCrossingFrame6)
        self.railwayLightsLabel6.setObjectName(u"railwayLightsLabel6")
        self.railwayLightsLabel6.setFont(font2)

        self.gridLayout_29.addWidget(self.railwayLightsLabel6, 2, 0, 1, 1)

        self.railwayLightsValue6 = QLabel(self.railwayCrossingFrame6)
        self.railwayLightsValue6.setObjectName(u"railwayLightsValue6")
        self.railwayLightsValue6.setFont(font1)
        self.railwayLightsValue6.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.railwayLightsValue6, 2, 1, 1, 1)


        self.gridLayout_27.addWidget(self.railwayCrossingFrame6, 1, 0, 2, 1)

        self.displayPLC6 = QTextBrowser(self.tab6Frame)
        self.displayPLC6.setObjectName(u"displayPLC6")
        self.displayPLC6.setFont(font3)

        self.gridLayout_27.addWidget(self.displayPLC6, 3, 0, 1, 5)

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


        self.gridLayout_27.addWidget(self.trafficLightFrame6, 2, 4, 1, 1)

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

        self.switchPositionFrame6 = QFrame(self.tab6Frame)
        self.switchPositionFrame6.setObjectName(u"switchPositionFrame6")
        self.switchPositionFrame6.setAutoFillBackground(True)
        self.switchPositionFrame6.setFrameShape(QFrame.Box)
        self.switchPositionFrame6.setFrameShadow(QFrame.Raised)
        self.switchPositionFrame6.setLineWidth(1)
        self.switchPositionFrame6.setMidLineWidth(0)
        self.gridLayout_28 = QGridLayout(self.switchPositionFrame6)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.switchFromValue6 = QLabel(self.switchPositionFrame6)
        self.switchFromValue6.setObjectName(u"switchFromValue6")
        self.switchFromValue6.setFont(font1)
        self.switchFromValue6.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.switchFromValue6, 1, 0, 1, 1)

        self.switchPositionLabel6 = QLabel(self.switchPositionFrame6)
        self.switchPositionLabel6.setObjectName(u"switchPositionLabel6")
        self.switchPositionLabel6.setFont(font1)
        self.switchPositionLabel6.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.switchPositionLabel6, 0, 0, 1, 3)

        self.switchToValue6 = QLabel(self.switchPositionFrame6)
        self.switchToValue6.setObjectName(u"switchToValue6")
        self.switchToValue6.setFont(font1)
        self.switchToValue6.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.switchToValue6, 1, 2, 1, 1)

        self.switchArrowLabel6 = QLabel(self.switchPositionFrame6)
        self.switchArrowLabel6.setObjectName(u"switchArrowLabel6")
        self.switchArrowLabel6.setFont(font1)
        self.switchArrowLabel6.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.switchArrowLabel6, 1, 1, 1, 1)

        self.switchButton6 = QPushButton(self.switchPositionFrame6)
        self.switchButton6.setObjectName(u"switchButton6")
        self.switchButton6.setEnabled(False)
        self.switchButton6.setFont(font2)

        self.gridLayout_28.addWidget(self.switchButton6, 2, 1, 1, 1)


        self.gridLayout_27.addWidget(self.switchPositionFrame6, 1, 1, 2, 1)


        self.gridLayout_30.addWidget(self.tab6Frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab6, "")
        self.tab7 = QWidget()
        self.tab7.setObjectName(u"tab7")
        self.gridLayout_34 = QGridLayout(self.tab7)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.tab7Frame = QFrame(self.tab7)
        self.tab7Frame.setObjectName(u"tab7Frame")
        self.tab7Frame.setFrameShape(QFrame.StyledPanel)
        self.tab7Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.tab7Frame)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.blockLabel7 = QLabel(self.tab7Frame)
        self.blockLabel7.setObjectName(u"blockLabel7")
        self.blockLabel7.setFont(font1)
        self.blockLabel7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_31.addWidget(self.blockLabel7, 0, 3, 1, 1)

        self.occupancyFrame7 = QFrame(self.tab7Frame)
        self.occupancyFrame7.setObjectName(u"occupancyFrame7")
        self.occupancyFrame7.setAutoFillBackground(True)
        self.occupancyFrame7.setFrameShape(QFrame.Box)
        self.occupancyFrame7.setFrameShadow(QFrame.Raised)
        self.occupancyFrame7.setLineWidth(1)
        self.occupancyFrame7.setMidLineWidth(0)
        self.verticalLayout_67 = QVBoxLayout(self.occupancyFrame7)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.occupancyLabel7 = QLabel(self.occupancyFrame7)
        self.occupancyLabel7.setObjectName(u"occupancyLabel7")
        self.occupancyLabel7.setFont(font1)
        self.occupancyLabel7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.occupancyLabel7)

        self.occupancyValue7 = QLabel(self.occupancyFrame7)
        self.occupancyValue7.setObjectName(u"occupancyValue7")
        self.occupancyValue7.setFont(font1)
        self.occupancyValue7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.occupancyValue7)


        self.gridLayout_31.addWidget(self.occupancyFrame7, 2, 2, 1, 1)

        self.authorityFrame7 = QFrame(self.tab7Frame)
        self.authorityFrame7.setObjectName(u"authorityFrame7")
        self.authorityFrame7.setAutoFillBackground(True)
        self.authorityFrame7.setFrameShape(QFrame.Box)
        self.authorityFrame7.setFrameShadow(QFrame.Raised)
        self.authorityFrame7.setLineWidth(1)
        self.authorityFrame7.setMidLineWidth(0)
        self.verticalLayout_68 = QVBoxLayout(self.authorityFrame7)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.authorityLabel7 = QLabel(self.authorityFrame7)
        self.authorityLabel7.setObjectName(u"authorityLabel7")
        self.authorityLabel7.setFont(font1)
        self.authorityLabel7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_68.addWidget(self.authorityLabel7)

        self.authorityValue7 = QLabel(self.authorityFrame7)
        self.authorityValue7.setObjectName(u"authorityValue7")
        self.authorityValue7.setFont(font1)
        self.authorityValue7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_68.addWidget(self.authorityValue7)


        self.gridLayout_31.addWidget(self.authorityFrame7, 1, 2, 1, 1)

        self.uploadPLC7 = QPushButton(self.tab7Frame)
        self.uploadPLC7.setObjectName(u"uploadPLC7")
        self.uploadPLC7.setFont(font1)

        self.gridLayout_31.addWidget(self.uploadPLC7, 4, 4, 1, 1)

        self.suggestedSpeedFrame7 = QFrame(self.tab7Frame)
        self.suggestedSpeedFrame7.setObjectName(u"suggestedSpeedFrame7")
        self.suggestedSpeedFrame7.setAutoFillBackground(True)
        self.suggestedSpeedFrame7.setFrameShape(QFrame.Box)
        self.suggestedSpeedFrame7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.suggestedSpeedFrame7)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.suggestedSpeedLabel7 = QLabel(self.suggestedSpeedFrame7)
        self.suggestedSpeedLabel7.setObjectName(u"suggestedSpeedLabel7")
        self.suggestedSpeedLabel7.setFont(font1)
        self.suggestedSpeedLabel7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_70.addWidget(self.suggestedSpeedLabel7)

        self.suggestedSpeedValue7 = QLabel(self.suggestedSpeedFrame7)
        self.suggestedSpeedValue7.setObjectName(u"suggestedSpeedValue7")
        self.suggestedSpeedValue7.setFont(font1)
        self.suggestedSpeedValue7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_70.addWidget(self.suggestedSpeedValue7)


        self.gridLayout_31.addWidget(self.suggestedSpeedFrame7, 1, 3, 1, 1)

        self.trackLabel7 = QLabel(self.tab7Frame)
        self.trackLabel7.setObjectName(u"trackLabel7")
        self.trackLabel7.setFont(font1)
        self.trackLabel7.setAlignment(Qt.AlignCenter)

        self.gridLayout_31.addWidget(self.trackLabel7, 0, 0, 1, 1)

        self.blockSelect7 = QComboBox(self.tab7Frame)
        self.blockSelect7.setObjectName(u"blockSelect7")
        self.blockSelect7.setEnabled(True)
        self.blockSelect7.setFont(font1)
        self.blockSelect7.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout_31.addWidget(self.blockSelect7, 0, 4, 1, 1)

        self.railwayCrossingFrame7 = QFrame(self.tab7Frame)
        self.railwayCrossingFrame7.setObjectName(u"railwayCrossingFrame7")
        self.railwayCrossingFrame7.setAutoFillBackground(True)
        self.railwayCrossingFrame7.setFrameShape(QFrame.Box)
        self.railwayCrossingFrame7.setFrameShadow(QFrame.Raised)
        self.railwayCrossingFrame7.setLineWidth(1)
        self.railwayCrossingFrame7.setMidLineWidth(0)
        self.gridLayout_33 = QGridLayout(self.railwayCrossingFrame7)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.railwayCrossingLabel7 = QLabel(self.railwayCrossingFrame7)
        self.railwayCrossingLabel7.setObjectName(u"railwayCrossingLabel7")
        self.railwayCrossingLabel7.setFont(font1)
        self.railwayCrossingLabel7.setAlignment(Qt.AlignCenter)

        self.gridLayout_33.addWidget(self.railwayCrossingLabel7, 0, 0, 1, 2)

        self.railwayGateLabel7 = QLabel(self.railwayCrossingFrame7)
        self.railwayGateLabel7.setObjectName(u"railwayGateLabel7")
        self.railwayGateLabel7.setFont(font2)

        self.gridLayout_33.addWidget(self.railwayGateLabel7, 1, 0, 1, 1)

        self.railwayGateValue7 = QLabel(self.railwayCrossingFrame7)
        self.railwayGateValue7.setObjectName(u"railwayGateValue7")
        self.railwayGateValue7.setFont(font1)
        self.railwayGateValue7.setAlignment(Qt.AlignCenter)

        self.gridLayout_33.addWidget(self.railwayGateValue7, 1, 1, 1, 1)

        self.railwayLightsLabel7 = QLabel(self.railwayCrossingFrame7)
        self.railwayLightsLabel7.setObjectName(u"railwayLightsLabel7")
        self.railwayLightsLabel7.setFont(font2)

        self.gridLayout_33.addWidget(self.railwayLightsLabel7, 2, 0, 1, 1)

        self.railwayLightsValue7 = QLabel(self.railwayCrossingFrame7)
        self.railwayLightsValue7.setObjectName(u"railwayLightsValue7")
        self.railwayLightsValue7.setFont(font1)
        self.railwayLightsValue7.setAlignment(Qt.AlignCenter)

        self.gridLayout_33.addWidget(self.railwayLightsValue7, 2, 1, 1, 1)


        self.gridLayout_31.addWidget(self.railwayCrossingFrame7, 1, 0, 2, 1)

        self.displayPLC7 = QTextBrowser(self.tab7Frame)
        self.displayPLC7.setObjectName(u"displayPLC7")
        self.displayPLC7.setFont(font3)

        self.gridLayout_31.addWidget(self.displayPLC7, 3, 0, 1, 5)

        self.trafficLightFrame7 = QFrame(self.tab7Frame)
        self.trafficLightFrame7.setObjectName(u"trafficLightFrame7")
        self.trafficLightFrame7.setAutoFillBackground(True)
        self.trafficLightFrame7.setFrameShape(QFrame.Box)
        self.trafficLightFrame7.setFrameShadow(QFrame.Raised)
        self.trafficLightFrame7.setLineWidth(1)
        self.trafficLightFrame7.setMidLineWidth(0)
        self.verticalLayout_69 = QVBoxLayout(self.trafficLightFrame7)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.trafficLightLabel7 = QLabel(self.trafficLightFrame7)
        self.trafficLightLabel7.setObjectName(u"trafficLightLabel7")
        self.trafficLightLabel7.setFont(font1)
        self.trafficLightLabel7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_69.addWidget(self.trafficLightLabel7)

        self.trafficLightValue7 = QLabel(self.trafficLightFrame7)
        self.trafficLightValue7.setObjectName(u"trafficLightValue7")
        self.trafficLightValue7.setFont(font1)
        self.trafficLightValue7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_69.addWidget(self.trafficLightValue7)


        self.gridLayout_31.addWidget(self.trafficLightFrame7, 2, 4, 1, 1)

        self.commandedSpeedFrame7 = QFrame(self.tab7Frame)
        self.commandedSpeedFrame7.setObjectName(u"commandedSpeedFrame7")
        self.commandedSpeedFrame7.setAutoFillBackground(True)
        self.commandedSpeedFrame7.setFrameShape(QFrame.Box)
        self.commandedSpeedFrame7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.commandedSpeedFrame7)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.commandedSpeedLabel7 = QLabel(self.commandedSpeedFrame7)
        self.commandedSpeedLabel7.setObjectName(u"commandedSpeedLabel7")
        self.commandedSpeedLabel7.setFont(font1)
        self.commandedSpeedLabel7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_65.addWidget(self.commandedSpeedLabel7)

        self.commandedSpeedValue7 = QLabel(self.commandedSpeedFrame7)
        self.commandedSpeedValue7.setObjectName(u"commandedSpeedValue7")
        self.commandedSpeedValue7.setFont(font1)
        self.commandedSpeedValue7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_65.addWidget(self.commandedSpeedValue7)


        self.gridLayout_31.addWidget(self.commandedSpeedFrame7, 2, 3, 1, 1)

        self.statusFrame7 = QFrame(self.tab7Frame)
        self.statusFrame7.setObjectName(u"statusFrame7")
        self.statusFrame7.setAutoFillBackground(True)
        self.statusFrame7.setFrameShape(QFrame.Box)
        self.statusFrame7.setFrameShadow(QFrame.Raised)
        self.statusFrame7.setLineWidth(1)
        self.statusFrame7.setMidLineWidth(0)
        self.verticalLayout_71 = QVBoxLayout(self.statusFrame7)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.statusLabel7 = QLabel(self.statusFrame7)
        self.statusLabel7.setObjectName(u"statusLabel7")
        self.statusLabel7.setFont(font1)
        self.statusLabel7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_71.addWidget(self.statusLabel7)

        self.statusValue7 = QLabel(self.statusFrame7)
        self.statusValue7.setObjectName(u"statusValue7")
        self.statusValue7.setFont(font1)
        self.statusValue7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_71.addWidget(self.statusValue7)


        self.gridLayout_31.addWidget(self.statusFrame7, 1, 4, 1, 1)

        self.switchPositionFrame7 = QFrame(self.tab7Frame)
        self.switchPositionFrame7.setObjectName(u"switchPositionFrame7")
        self.switchPositionFrame7.setAutoFillBackground(True)
        self.switchPositionFrame7.setFrameShape(QFrame.Box)
        self.switchPositionFrame7.setFrameShadow(QFrame.Raised)
        self.switchPositionFrame7.setLineWidth(1)
        self.switchPositionFrame7.setMidLineWidth(0)
        self.gridLayout_32 = QGridLayout(self.switchPositionFrame7)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.switchToValue7 = QLabel(self.switchPositionFrame7)
        self.switchToValue7.setObjectName(u"switchToValue7")
        self.switchToValue7.setFont(font1)
        self.switchToValue7.setAlignment(Qt.AlignCenter)

        self.gridLayout_32.addWidget(self.switchToValue7, 1, 2, 1, 1)

        self.switchArrowLabel7 = QLabel(self.switchPositionFrame7)
        self.switchArrowLabel7.setObjectName(u"switchArrowLabel7")
        self.switchArrowLabel7.setFont(font1)
        self.switchArrowLabel7.setAlignment(Qt.AlignCenter)

        self.gridLayout_32.addWidget(self.switchArrowLabel7, 1, 1, 1, 1)

        self.switchPositionLabel7 = QLabel(self.switchPositionFrame7)
        self.switchPositionLabel7.setObjectName(u"switchPositionLabel7")
        self.switchPositionLabel7.setFont(font1)
        self.switchPositionLabel7.setAlignment(Qt.AlignCenter)

        self.gridLayout_32.addWidget(self.switchPositionLabel7, 0, 0, 1, 3)

        self.switchFromValue7 = QLabel(self.switchPositionFrame7)
        self.switchFromValue7.setObjectName(u"switchFromValue7")
        self.switchFromValue7.setFont(font1)
        self.switchFromValue7.setAlignment(Qt.AlignCenter)

        self.gridLayout_32.addWidget(self.switchFromValue7, 1, 0, 1, 1)

        self.switchButton7 = QPushButton(self.switchPositionFrame7)
        self.switchButton7.setObjectName(u"switchButton7")
        self.switchButton7.setEnabled(False)
        self.switchButton7.setFont(font2)

        self.gridLayout_32.addWidget(self.switchButton7, 2, 1, 1, 1)


        self.gridLayout_31.addWidget(self.switchPositionFrame7, 1, 1, 2, 1)


        self.gridLayout_34.addWidget(self.tab7Frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab7, "")
        self.tab8 = QWidget()
        self.tab8.setObjectName(u"tab8")
        self.gridLayout_38 = QGridLayout(self.tab8)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.tab8Frame = QFrame(self.tab8)
        self.tab8Frame.setObjectName(u"tab8Frame")
        self.tab8Frame.setFrameShape(QFrame.StyledPanel)
        self.tab8Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.tab8Frame)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.blockLabel8 = QLabel(self.tab8Frame)
        self.blockLabel8.setObjectName(u"blockLabel8")
        self.blockLabel8.setFont(font1)
        self.blockLabel8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_35.addWidget(self.blockLabel8, 0, 3, 1, 1)

        self.occupancyFrame8 = QFrame(self.tab8Frame)
        self.occupancyFrame8.setObjectName(u"occupancyFrame8")
        self.occupancyFrame8.setAutoFillBackground(True)
        self.occupancyFrame8.setFrameShape(QFrame.Box)
        self.occupancyFrame8.setFrameShadow(QFrame.Raised)
        self.occupancyFrame8.setLineWidth(1)
        self.occupancyFrame8.setMidLineWidth(0)
        self.verticalLayout_74 = QVBoxLayout(self.occupancyFrame8)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.occupancyLabel8 = QLabel(self.occupancyFrame8)
        self.occupancyLabel8.setObjectName(u"occupancyLabel8")
        self.occupancyLabel8.setFont(font1)
        self.occupancyLabel8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_74.addWidget(self.occupancyLabel8)

        self.occupancyValue8 = QLabel(self.occupancyFrame8)
        self.occupancyValue8.setObjectName(u"occupancyValue8")
        self.occupancyValue8.setFont(font1)
        self.occupancyValue8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_74.addWidget(self.occupancyValue8)


        self.gridLayout_35.addWidget(self.occupancyFrame8, 2, 2, 1, 1)

        self.authorityFrame8 = QFrame(self.tab8Frame)
        self.authorityFrame8.setObjectName(u"authorityFrame8")
        self.authorityFrame8.setAutoFillBackground(True)
        self.authorityFrame8.setFrameShape(QFrame.Box)
        self.authorityFrame8.setFrameShadow(QFrame.Raised)
        self.authorityFrame8.setLineWidth(1)
        self.authorityFrame8.setMidLineWidth(0)
        self.verticalLayout_75 = QVBoxLayout(self.authorityFrame8)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.authorityLabel8 = QLabel(self.authorityFrame8)
        self.authorityLabel8.setObjectName(u"authorityLabel8")
        self.authorityLabel8.setFont(font1)
        self.authorityLabel8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_75.addWidget(self.authorityLabel8)

        self.authorityValue8 = QLabel(self.authorityFrame8)
        self.authorityValue8.setObjectName(u"authorityValue8")
        self.authorityValue8.setFont(font1)
        self.authorityValue8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_75.addWidget(self.authorityValue8)


        self.gridLayout_35.addWidget(self.authorityFrame8, 1, 2, 1, 1)

        self.uploadPLC8 = QPushButton(self.tab8Frame)
        self.uploadPLC8.setObjectName(u"uploadPLC8")
        self.uploadPLC8.setFont(font1)

        self.gridLayout_35.addWidget(self.uploadPLC8, 4, 4, 1, 1)

        self.suggestedSpeedFrame8 = QFrame(self.tab8Frame)
        self.suggestedSpeedFrame8.setObjectName(u"suggestedSpeedFrame8")
        self.suggestedSpeedFrame8.setAutoFillBackground(True)
        self.suggestedSpeedFrame8.setFrameShape(QFrame.Box)
        self.suggestedSpeedFrame8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.suggestedSpeedFrame8)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.suggestedSpeedLabel8 = QLabel(self.suggestedSpeedFrame8)
        self.suggestedSpeedLabel8.setObjectName(u"suggestedSpeedLabel8")
        self.suggestedSpeedLabel8.setFont(font1)
        self.suggestedSpeedLabel8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_77.addWidget(self.suggestedSpeedLabel8)

        self.suggestedSpeedValue8 = QLabel(self.suggestedSpeedFrame8)
        self.suggestedSpeedValue8.setObjectName(u"suggestedSpeedValue8")
        self.suggestedSpeedValue8.setFont(font1)
        self.suggestedSpeedValue8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_77.addWidget(self.suggestedSpeedValue8)


        self.gridLayout_35.addWidget(self.suggestedSpeedFrame8, 1, 3, 1, 1)

        self.trackLabel8 = QLabel(self.tab8Frame)
        self.trackLabel8.setObjectName(u"trackLabel8")
        self.trackLabel8.setFont(font1)
        self.trackLabel8.setAlignment(Qt.AlignCenter)

        self.gridLayout_35.addWidget(self.trackLabel8, 0, 0, 1, 1)

        self.blockSelect8 = QComboBox(self.tab8Frame)
        self.blockSelect8.setObjectName(u"blockSelect8")
        self.blockSelect8.setEnabled(True)
        self.blockSelect8.setFont(font1)
        self.blockSelect8.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout_35.addWidget(self.blockSelect8, 0, 4, 1, 1)

        self.railwayCrossingFrame8 = QFrame(self.tab8Frame)
        self.railwayCrossingFrame8.setObjectName(u"railwayCrossingFrame8")
        self.railwayCrossingFrame8.setAutoFillBackground(True)
        self.railwayCrossingFrame8.setFrameShape(QFrame.Box)
        self.railwayCrossingFrame8.setFrameShadow(QFrame.Raised)
        self.railwayCrossingFrame8.setLineWidth(1)
        self.railwayCrossingFrame8.setMidLineWidth(0)
        self.gridLayout_37 = QGridLayout(self.railwayCrossingFrame8)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.railwayCrossingLabel8 = QLabel(self.railwayCrossingFrame8)
        self.railwayCrossingLabel8.setObjectName(u"railwayCrossingLabel8")
        self.railwayCrossingLabel8.setFont(font1)
        self.railwayCrossingLabel8.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.railwayCrossingLabel8, 0, 0, 1, 2)

        self.railwayGateLabel8 = QLabel(self.railwayCrossingFrame8)
        self.railwayGateLabel8.setObjectName(u"railwayGateLabel8")
        self.railwayGateLabel8.setFont(font2)

        self.gridLayout_37.addWidget(self.railwayGateLabel8, 1, 0, 1, 1)

        self.railwayGateValue8 = QLabel(self.railwayCrossingFrame8)
        self.railwayGateValue8.setObjectName(u"railwayGateValue8")
        self.railwayGateValue8.setFont(font1)
        self.railwayGateValue8.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.railwayGateValue8, 1, 1, 1, 1)

        self.railwayLightsLabel8 = QLabel(self.railwayCrossingFrame8)
        self.railwayLightsLabel8.setObjectName(u"railwayLightsLabel8")
        self.railwayLightsLabel8.setFont(font2)

        self.gridLayout_37.addWidget(self.railwayLightsLabel8, 2, 0, 1, 1)

        self.railwayLightsValue8 = QLabel(self.railwayCrossingFrame8)
        self.railwayLightsValue8.setObjectName(u"railwayLightsValue8")
        self.railwayLightsValue8.setFont(font1)
        self.railwayLightsValue8.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.railwayLightsValue8, 2, 1, 1, 1)


        self.gridLayout_35.addWidget(self.railwayCrossingFrame8, 1, 0, 2, 1)

        self.displayPLC8 = QTextBrowser(self.tab8Frame)
        self.displayPLC8.setObjectName(u"displayPLC8")
        self.displayPLC8.setFont(font3)

        self.gridLayout_35.addWidget(self.displayPLC8, 3, 0, 1, 5)

        self.trafficLightFrame8 = QFrame(self.tab8Frame)
        self.trafficLightFrame8.setObjectName(u"trafficLightFrame8")
        self.trafficLightFrame8.setAutoFillBackground(True)
        self.trafficLightFrame8.setFrameShape(QFrame.Box)
        self.trafficLightFrame8.setFrameShadow(QFrame.Raised)
        self.trafficLightFrame8.setLineWidth(1)
        self.trafficLightFrame8.setMidLineWidth(0)
        self.verticalLayout_76 = QVBoxLayout(self.trafficLightFrame8)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.trafficLightLabel8 = QLabel(self.trafficLightFrame8)
        self.trafficLightLabel8.setObjectName(u"trafficLightLabel8")
        self.trafficLightLabel8.setFont(font1)
        self.trafficLightLabel8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_76.addWidget(self.trafficLightLabel8)

        self.trafficLightValue8 = QLabel(self.trafficLightFrame8)
        self.trafficLightValue8.setObjectName(u"trafficLightValue8")
        self.trafficLightValue8.setFont(font1)
        self.trafficLightValue8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_76.addWidget(self.trafficLightValue8)


        self.gridLayout_35.addWidget(self.trafficLightFrame8, 2, 4, 1, 1)

        self.commandedSpeedFrame8 = QFrame(self.tab8Frame)
        self.commandedSpeedFrame8.setObjectName(u"commandedSpeedFrame8")
        self.commandedSpeedFrame8.setAutoFillBackground(True)
        self.commandedSpeedFrame8.setFrameShape(QFrame.Box)
        self.commandedSpeedFrame8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.commandedSpeedFrame8)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.commandedSpeedLabel8 = QLabel(self.commandedSpeedFrame8)
        self.commandedSpeedLabel8.setObjectName(u"commandedSpeedLabel8")
        self.commandedSpeedLabel8.setFont(font1)
        self.commandedSpeedLabel8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_72.addWidget(self.commandedSpeedLabel8)

        self.commandedSpeedValue8 = QLabel(self.commandedSpeedFrame8)
        self.commandedSpeedValue8.setObjectName(u"commandedSpeedValue8")
        self.commandedSpeedValue8.setFont(font1)
        self.commandedSpeedValue8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_72.addWidget(self.commandedSpeedValue8)


        self.gridLayout_35.addWidget(self.commandedSpeedFrame8, 2, 3, 1, 1)

        self.statusFrame8 = QFrame(self.tab8Frame)
        self.statusFrame8.setObjectName(u"statusFrame8")
        self.statusFrame8.setAutoFillBackground(True)
        self.statusFrame8.setFrameShape(QFrame.Box)
        self.statusFrame8.setFrameShadow(QFrame.Raised)
        self.statusFrame8.setLineWidth(1)
        self.statusFrame8.setMidLineWidth(0)
        self.verticalLayout_78 = QVBoxLayout(self.statusFrame8)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.statusLabel8 = QLabel(self.statusFrame8)
        self.statusLabel8.setObjectName(u"statusLabel8")
        self.statusLabel8.setFont(font1)
        self.statusLabel8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_78.addWidget(self.statusLabel8)

        self.statusValue8 = QLabel(self.statusFrame8)
        self.statusValue8.setObjectName(u"statusValue8")
        self.statusValue8.setFont(font1)
        self.statusValue8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_78.addWidget(self.statusValue8)


        self.gridLayout_35.addWidget(self.statusFrame8, 1, 4, 1, 1)

        self.switchPositionFrame8 = QFrame(self.tab8Frame)
        self.switchPositionFrame8.setObjectName(u"switchPositionFrame8")
        self.switchPositionFrame8.setAutoFillBackground(True)
        self.switchPositionFrame8.setFrameShape(QFrame.Box)
        self.switchPositionFrame8.setFrameShadow(QFrame.Raised)
        self.switchPositionFrame8.setLineWidth(1)
        self.switchPositionFrame8.setMidLineWidth(0)
        self.gridLayout_36 = QGridLayout(self.switchPositionFrame8)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.switchToValue8 = QLabel(self.switchPositionFrame8)
        self.switchToValue8.setObjectName(u"switchToValue8")
        self.switchToValue8.setFont(font1)
        self.switchToValue8.setAlignment(Qt.AlignCenter)

        self.gridLayout_36.addWidget(self.switchToValue8, 1, 2, 1, 1)

        self.switchArrowLabel8 = QLabel(self.switchPositionFrame8)
        self.switchArrowLabel8.setObjectName(u"switchArrowLabel8")
        self.switchArrowLabel8.setFont(font1)
        self.switchArrowLabel8.setAlignment(Qt.AlignCenter)

        self.gridLayout_36.addWidget(self.switchArrowLabel8, 1, 1, 1, 1)

        self.switchPositionLabel8 = QLabel(self.switchPositionFrame8)
        self.switchPositionLabel8.setObjectName(u"switchPositionLabel8")
        self.switchPositionLabel8.setFont(font1)
        self.switchPositionLabel8.setAlignment(Qt.AlignCenter)

        self.gridLayout_36.addWidget(self.switchPositionLabel8, 0, 0, 1, 3)

        self.switchFromValue8 = QLabel(self.switchPositionFrame8)
        self.switchFromValue8.setObjectName(u"switchFromValue8")
        self.switchFromValue8.setFont(font1)
        self.switchFromValue8.setAlignment(Qt.AlignCenter)

        self.gridLayout_36.addWidget(self.switchFromValue8, 1, 0, 1, 1)

        self.switchButton8 = QPushButton(self.switchPositionFrame8)
        self.switchButton8.setObjectName(u"switchButton8")
        self.switchButton8.setEnabled(False)
        self.switchButton8.setFont(font2)

        self.gridLayout_36.addWidget(self.switchButton8, 2, 1, 1, 1)


        self.gridLayout_35.addWidget(self.switchPositionFrame8, 1, 1, 2, 1)


        self.gridLayout_38.addWidget(self.tab8Frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab8, "")
        self.tab9 = QWidget()
        self.tab9.setObjectName(u"tab9")
        self.gridLayout_42 = QGridLayout(self.tab9)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.tab9Frame = QFrame(self.tab9)
        self.tab9Frame.setObjectName(u"tab9Frame")
        self.tab9Frame.setFrameShape(QFrame.StyledPanel)
        self.tab9Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_39 = QGridLayout(self.tab9Frame)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.blockLabel9 = QLabel(self.tab9Frame)
        self.blockLabel9.setObjectName(u"blockLabel9")
        self.blockLabel9.setFont(font1)
        self.blockLabel9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_39.addWidget(self.blockLabel9, 0, 3, 1, 1)

        self.occupancyFrame9 = QFrame(self.tab9Frame)
        self.occupancyFrame9.setObjectName(u"occupancyFrame9")
        self.occupancyFrame9.setAutoFillBackground(True)
        self.occupancyFrame9.setFrameShape(QFrame.Box)
        self.occupancyFrame9.setFrameShadow(QFrame.Raised)
        self.occupancyFrame9.setLineWidth(1)
        self.occupancyFrame9.setMidLineWidth(0)
        self.verticalLayout_81 = QVBoxLayout(self.occupancyFrame9)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.occupancyLabel9 = QLabel(self.occupancyFrame9)
        self.occupancyLabel9.setObjectName(u"occupancyLabel9")
        self.occupancyLabel9.setFont(font1)
        self.occupancyLabel9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_81.addWidget(self.occupancyLabel9)

        self.occupancyValue9 = QLabel(self.occupancyFrame9)
        self.occupancyValue9.setObjectName(u"occupancyValue9")
        self.occupancyValue9.setFont(font1)
        self.occupancyValue9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_81.addWidget(self.occupancyValue9)


        self.gridLayout_39.addWidget(self.occupancyFrame9, 2, 2, 1, 1)

        self.authorityFrame9 = QFrame(self.tab9Frame)
        self.authorityFrame9.setObjectName(u"authorityFrame9")
        self.authorityFrame9.setAutoFillBackground(True)
        self.authorityFrame9.setFrameShape(QFrame.Box)
        self.authorityFrame9.setFrameShadow(QFrame.Raised)
        self.authorityFrame9.setLineWidth(1)
        self.authorityFrame9.setMidLineWidth(0)
        self.verticalLayout_82 = QVBoxLayout(self.authorityFrame9)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.authorityLabel9 = QLabel(self.authorityFrame9)
        self.authorityLabel9.setObjectName(u"authorityLabel9")
        self.authorityLabel9.setFont(font1)
        self.authorityLabel9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_82.addWidget(self.authorityLabel9)

        self.authorityValue9 = QLabel(self.authorityFrame9)
        self.authorityValue9.setObjectName(u"authorityValue9")
        self.authorityValue9.setFont(font1)
        self.authorityValue9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_82.addWidget(self.authorityValue9)


        self.gridLayout_39.addWidget(self.authorityFrame9, 1, 2, 1, 1)

        self.uploadPLC9 = QPushButton(self.tab9Frame)
        self.uploadPLC9.setObjectName(u"uploadPLC9")
        self.uploadPLC9.setFont(font1)

        self.gridLayout_39.addWidget(self.uploadPLC9, 4, 4, 1, 1)

        self.suggestedSpeedFrame9 = QFrame(self.tab9Frame)
        self.suggestedSpeedFrame9.setObjectName(u"suggestedSpeedFrame9")
        self.suggestedSpeedFrame9.setAutoFillBackground(True)
        self.suggestedSpeedFrame9.setFrameShape(QFrame.Box)
        self.suggestedSpeedFrame9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.suggestedSpeedFrame9)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.suggestedSpeedLabel9 = QLabel(self.suggestedSpeedFrame9)
        self.suggestedSpeedLabel9.setObjectName(u"suggestedSpeedLabel9")
        self.suggestedSpeedLabel9.setFont(font1)
        self.suggestedSpeedLabel9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_84.addWidget(self.suggestedSpeedLabel9)

        self.suggestedSpeedValue9 = QLabel(self.suggestedSpeedFrame9)
        self.suggestedSpeedValue9.setObjectName(u"suggestedSpeedValue9")
        self.suggestedSpeedValue9.setFont(font1)
        self.suggestedSpeedValue9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_84.addWidget(self.suggestedSpeedValue9)


        self.gridLayout_39.addWidget(self.suggestedSpeedFrame9, 1, 3, 1, 1)

        self.trackLabel9 = QLabel(self.tab9Frame)
        self.trackLabel9.setObjectName(u"trackLabel9")
        self.trackLabel9.setFont(font1)
        self.trackLabel9.setAlignment(Qt.AlignCenter)

        self.gridLayout_39.addWidget(self.trackLabel9, 0, 0, 1, 1)

        self.blockSelect9 = QComboBox(self.tab9Frame)
        self.blockSelect9.setObjectName(u"blockSelect9")
        self.blockSelect9.setEnabled(True)
        self.blockSelect9.setFont(font1)
        self.blockSelect9.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout_39.addWidget(self.blockSelect9, 0, 4, 1, 1)

        self.railwayCrossingFrame9 = QFrame(self.tab9Frame)
        self.railwayCrossingFrame9.setObjectName(u"railwayCrossingFrame9")
        self.railwayCrossingFrame9.setAutoFillBackground(True)
        self.railwayCrossingFrame9.setFrameShape(QFrame.Box)
        self.railwayCrossingFrame9.setFrameShadow(QFrame.Raised)
        self.railwayCrossingFrame9.setLineWidth(1)
        self.railwayCrossingFrame9.setMidLineWidth(0)
        self.gridLayout_41 = QGridLayout(self.railwayCrossingFrame9)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.railwayCrossingLabel9 = QLabel(self.railwayCrossingFrame9)
        self.railwayCrossingLabel9.setObjectName(u"railwayCrossingLabel9")
        self.railwayCrossingLabel9.setFont(font1)
        self.railwayCrossingLabel9.setAlignment(Qt.AlignCenter)

        self.gridLayout_41.addWidget(self.railwayCrossingLabel9, 0, 0, 1, 2)

        self.railwayGateLabel9 = QLabel(self.railwayCrossingFrame9)
        self.railwayGateLabel9.setObjectName(u"railwayGateLabel9")
        self.railwayGateLabel9.setFont(font2)

        self.gridLayout_41.addWidget(self.railwayGateLabel9, 1, 0, 1, 1)

        self.railwayGateValue9 = QLabel(self.railwayCrossingFrame9)
        self.railwayGateValue9.setObjectName(u"railwayGateValue9")
        self.railwayGateValue9.setFont(font1)
        self.railwayGateValue9.setAlignment(Qt.AlignCenter)

        self.gridLayout_41.addWidget(self.railwayGateValue9, 1, 1, 1, 1)

        self.railwayLightsLabel9 = QLabel(self.railwayCrossingFrame9)
        self.railwayLightsLabel9.setObjectName(u"railwayLightsLabel9")
        self.railwayLightsLabel9.setFont(font2)

        self.gridLayout_41.addWidget(self.railwayLightsLabel9, 2, 0, 1, 1)

        self.railwayLightsValue9 = QLabel(self.railwayCrossingFrame9)
        self.railwayLightsValue9.setObjectName(u"railwayLightsValue9")
        self.railwayLightsValue9.setFont(font1)
        self.railwayLightsValue9.setAlignment(Qt.AlignCenter)

        self.gridLayout_41.addWidget(self.railwayLightsValue9, 2, 1, 1, 1)


        self.gridLayout_39.addWidget(self.railwayCrossingFrame9, 1, 0, 2, 1)

        self.displayPLC9 = QTextBrowser(self.tab9Frame)
        self.displayPLC9.setObjectName(u"displayPLC9")
        self.displayPLC9.setFont(font3)

        self.gridLayout_39.addWidget(self.displayPLC9, 3, 0, 1, 5)

        self.trafficLightFrame9 = QFrame(self.tab9Frame)
        self.trafficLightFrame9.setObjectName(u"trafficLightFrame9")
        self.trafficLightFrame9.setAutoFillBackground(True)
        self.trafficLightFrame9.setFrameShape(QFrame.Box)
        self.trafficLightFrame9.setFrameShadow(QFrame.Raised)
        self.trafficLightFrame9.setLineWidth(1)
        self.trafficLightFrame9.setMidLineWidth(0)
        self.verticalLayout_83 = QVBoxLayout(self.trafficLightFrame9)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.trafficLightLabel9 = QLabel(self.trafficLightFrame9)
        self.trafficLightLabel9.setObjectName(u"trafficLightLabel9")
        self.trafficLightLabel9.setFont(font1)
        self.trafficLightLabel9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_83.addWidget(self.trafficLightLabel9)

        self.trafficLightValue9 = QLabel(self.trafficLightFrame9)
        self.trafficLightValue9.setObjectName(u"trafficLightValue9")
        self.trafficLightValue9.setFont(font1)
        self.trafficLightValue9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_83.addWidget(self.trafficLightValue9)


        self.gridLayout_39.addWidget(self.trafficLightFrame9, 2, 4, 1, 1)

        self.commandedSpeedFrame9 = QFrame(self.tab9Frame)
        self.commandedSpeedFrame9.setObjectName(u"commandedSpeedFrame9")
        self.commandedSpeedFrame9.setAutoFillBackground(True)
        self.commandedSpeedFrame9.setFrameShape(QFrame.Box)
        self.commandedSpeedFrame9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.commandedSpeedFrame9)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.commandedSpeedLabel9 = QLabel(self.commandedSpeedFrame9)
        self.commandedSpeedLabel9.setObjectName(u"commandedSpeedLabel9")
        self.commandedSpeedLabel9.setFont(font1)
        self.commandedSpeedLabel9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_79.addWidget(self.commandedSpeedLabel9)

        self.commandedSpeedValue9 = QLabel(self.commandedSpeedFrame9)
        self.commandedSpeedValue9.setObjectName(u"commandedSpeedValue9")
        self.commandedSpeedValue9.setFont(font1)
        self.commandedSpeedValue9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_79.addWidget(self.commandedSpeedValue9)


        self.gridLayout_39.addWidget(self.commandedSpeedFrame9, 2, 3, 1, 1)

        self.statusFrame9 = QFrame(self.tab9Frame)
        self.statusFrame9.setObjectName(u"statusFrame9")
        self.statusFrame9.setAutoFillBackground(True)
        self.statusFrame9.setFrameShape(QFrame.Box)
        self.statusFrame9.setFrameShadow(QFrame.Raised)
        self.statusFrame9.setLineWidth(1)
        self.statusFrame9.setMidLineWidth(0)
        self.verticalLayout_85 = QVBoxLayout(self.statusFrame9)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.statusLabel9 = QLabel(self.statusFrame9)
        self.statusLabel9.setObjectName(u"statusLabel9")
        self.statusLabel9.setFont(font1)
        self.statusLabel9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_85.addWidget(self.statusLabel9)

        self.statusValue9 = QLabel(self.statusFrame9)
        self.statusValue9.setObjectName(u"statusValue9")
        self.statusValue9.setFont(font1)
        self.statusValue9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_85.addWidget(self.statusValue9)


        self.gridLayout_39.addWidget(self.statusFrame9, 1, 4, 1, 1)

        self.switchPositionFrame9 = QFrame(self.tab9Frame)
        self.switchPositionFrame9.setObjectName(u"switchPositionFrame9")
        self.switchPositionFrame9.setAutoFillBackground(True)
        self.switchPositionFrame9.setFrameShape(QFrame.Box)
        self.switchPositionFrame9.setFrameShadow(QFrame.Raised)
        self.switchPositionFrame9.setLineWidth(1)
        self.switchPositionFrame9.setMidLineWidth(0)
        self.gridLayout_40 = QGridLayout(self.switchPositionFrame9)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.switchPositionLabel9 = QLabel(self.switchPositionFrame9)
        self.switchPositionLabel9.setObjectName(u"switchPositionLabel9")
        self.switchPositionLabel9.setFont(font1)
        self.switchPositionLabel9.setAlignment(Qt.AlignCenter)

        self.gridLayout_40.addWidget(self.switchPositionLabel9, 0, 0, 1, 3)

        self.switchArrowLabel9 = QLabel(self.switchPositionFrame9)
        self.switchArrowLabel9.setObjectName(u"switchArrowLabel9")
        self.switchArrowLabel9.setFont(font1)
        self.switchArrowLabel9.setAlignment(Qt.AlignCenter)

        self.gridLayout_40.addWidget(self.switchArrowLabel9, 1, 1, 1, 1)

        self.switchFromValue9 = QLabel(self.switchPositionFrame9)
        self.switchFromValue9.setObjectName(u"switchFromValue9")
        self.switchFromValue9.setFont(font1)
        self.switchFromValue9.setAlignment(Qt.AlignCenter)

        self.gridLayout_40.addWidget(self.switchFromValue9, 1, 0, 1, 1)

        self.switchToValue9 = QLabel(self.switchPositionFrame9)
        self.switchToValue9.setObjectName(u"switchToValue9")
        self.switchToValue9.setFont(font1)
        self.switchToValue9.setAlignment(Qt.AlignCenter)

        self.gridLayout_40.addWidget(self.switchToValue9, 1, 2, 1, 1)

        self.switchButton9 = QPushButton(self.switchPositionFrame9)
        self.switchButton9.setObjectName(u"switchButton9")
        self.switchButton9.setEnabled(False)
        self.switchButton9.setFont(font2)

        self.gridLayout_40.addWidget(self.switchButton9, 2, 1, 1, 1)


        self.gridLayout_39.addWidget(self.switchPositionFrame9, 1, 1, 2, 1)


        self.gridLayout_42.addWidget(self.tab9Frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab9, "")
        self.tab10 = QWidget()
        self.tab10.setObjectName(u"tab10")
        self.gridLayout_46 = QGridLayout(self.tab10)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.tab10Frame = QFrame(self.tab10)
        self.tab10Frame.setObjectName(u"tab10Frame")
        self.tab10Frame.setFrameShape(QFrame.StyledPanel)
        self.tab10Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_43 = QGridLayout(self.tab10Frame)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.blockLabel10 = QLabel(self.tab10Frame)
        self.blockLabel10.setObjectName(u"blockLabel10")
        self.blockLabel10.setFont(font1)
        self.blockLabel10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_43.addWidget(self.blockLabel10, 0, 3, 1, 1)

        self.occupancyFrame10 = QFrame(self.tab10Frame)
        self.occupancyFrame10.setObjectName(u"occupancyFrame10")
        self.occupancyFrame10.setAutoFillBackground(True)
        self.occupancyFrame10.setFrameShape(QFrame.Box)
        self.occupancyFrame10.setFrameShadow(QFrame.Raised)
        self.occupancyFrame10.setLineWidth(1)
        self.occupancyFrame10.setMidLineWidth(0)
        self.verticalLayout_88 = QVBoxLayout(self.occupancyFrame10)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.occupancyLabel10 = QLabel(self.occupancyFrame10)
        self.occupancyLabel10.setObjectName(u"occupancyLabel10")
        self.occupancyLabel10.setFont(font1)
        self.occupancyLabel10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_88.addWidget(self.occupancyLabel10)

        self.occupancyValue10 = QLabel(self.occupancyFrame10)
        self.occupancyValue10.setObjectName(u"occupancyValue10")
        self.occupancyValue10.setFont(font1)
        self.occupancyValue10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_88.addWidget(self.occupancyValue10)


        self.gridLayout_43.addWidget(self.occupancyFrame10, 2, 2, 1, 1)

        self.authorityFrame10 = QFrame(self.tab10Frame)
        self.authorityFrame10.setObjectName(u"authorityFrame10")
        self.authorityFrame10.setAutoFillBackground(True)
        self.authorityFrame10.setFrameShape(QFrame.Box)
        self.authorityFrame10.setFrameShadow(QFrame.Raised)
        self.authorityFrame10.setLineWidth(1)
        self.authorityFrame10.setMidLineWidth(0)
        self.verticalLayout_89 = QVBoxLayout(self.authorityFrame10)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.authorityLabel10 = QLabel(self.authorityFrame10)
        self.authorityLabel10.setObjectName(u"authorityLabel10")
        self.authorityLabel10.setFont(font1)
        self.authorityLabel10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_89.addWidget(self.authorityLabel10)

        self.authorityValue10 = QLabel(self.authorityFrame10)
        self.authorityValue10.setObjectName(u"authorityValue10")
        self.authorityValue10.setFont(font1)
        self.authorityValue10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_89.addWidget(self.authorityValue10)


        self.gridLayout_43.addWidget(self.authorityFrame10, 1, 2, 1, 1)

        self.uploadPLC10 = QPushButton(self.tab10Frame)
        self.uploadPLC10.setObjectName(u"uploadPLC10")
        self.uploadPLC10.setFont(font1)

        self.gridLayout_43.addWidget(self.uploadPLC10, 4, 4, 1, 1)

        self.suggestedSpeedFrame10 = QFrame(self.tab10Frame)
        self.suggestedSpeedFrame10.setObjectName(u"suggestedSpeedFrame10")
        self.suggestedSpeedFrame10.setAutoFillBackground(True)
        self.suggestedSpeedFrame10.setFrameShape(QFrame.Box)
        self.suggestedSpeedFrame10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.suggestedSpeedFrame10)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.suggestedSpeedLabel10 = QLabel(self.suggestedSpeedFrame10)
        self.suggestedSpeedLabel10.setObjectName(u"suggestedSpeedLabel10")
        self.suggestedSpeedLabel10.setFont(font1)
        self.suggestedSpeedLabel10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_91.addWidget(self.suggestedSpeedLabel10)

        self.suggestedSpeedValue10 = QLabel(self.suggestedSpeedFrame10)
        self.suggestedSpeedValue10.setObjectName(u"suggestedSpeedValue10")
        self.suggestedSpeedValue10.setFont(font1)
        self.suggestedSpeedValue10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_91.addWidget(self.suggestedSpeedValue10)


        self.gridLayout_43.addWidget(self.suggestedSpeedFrame10, 1, 3, 1, 1)

        self.trackLabel10 = QLabel(self.tab10Frame)
        self.trackLabel10.setObjectName(u"trackLabel10")
        self.trackLabel10.setFont(font1)
        self.trackLabel10.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.trackLabel10, 0, 0, 1, 1)

        self.blockSelect10 = QComboBox(self.tab10Frame)
        self.blockSelect10.setObjectName(u"blockSelect10")
        self.blockSelect10.setEnabled(True)
        self.blockSelect10.setFont(font1)
        self.blockSelect10.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout_43.addWidget(self.blockSelect10, 0, 4, 1, 1)

        self.railwayCrossingFrame10 = QFrame(self.tab10Frame)
        self.railwayCrossingFrame10.setObjectName(u"railwayCrossingFrame10")
        self.railwayCrossingFrame10.setAutoFillBackground(True)
        self.railwayCrossingFrame10.setFrameShape(QFrame.Box)
        self.railwayCrossingFrame10.setFrameShadow(QFrame.Raised)
        self.railwayCrossingFrame10.setLineWidth(1)
        self.railwayCrossingFrame10.setMidLineWidth(0)
        self.gridLayout_45 = QGridLayout(self.railwayCrossingFrame10)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.railwayCrossingLabel10 = QLabel(self.railwayCrossingFrame10)
        self.railwayCrossingLabel10.setObjectName(u"railwayCrossingLabel10")
        self.railwayCrossingLabel10.setFont(font1)
        self.railwayCrossingLabel10.setAlignment(Qt.AlignCenter)

        self.gridLayout_45.addWidget(self.railwayCrossingLabel10, 0, 0, 1, 2)

        self.railwayGateLabel10 = QLabel(self.railwayCrossingFrame10)
        self.railwayGateLabel10.setObjectName(u"railwayGateLabel10")
        self.railwayGateLabel10.setFont(font2)

        self.gridLayout_45.addWidget(self.railwayGateLabel10, 1, 0, 1, 1)

        self.railwayGateValue10 = QLabel(self.railwayCrossingFrame10)
        self.railwayGateValue10.setObjectName(u"railwayGateValue10")
        self.railwayGateValue10.setFont(font1)
        self.railwayGateValue10.setAlignment(Qt.AlignCenter)

        self.gridLayout_45.addWidget(self.railwayGateValue10, 1, 1, 1, 1)

        self.railwayLightsLabel10 = QLabel(self.railwayCrossingFrame10)
        self.railwayLightsLabel10.setObjectName(u"railwayLightsLabel10")
        self.railwayLightsLabel10.setFont(font2)

        self.gridLayout_45.addWidget(self.railwayLightsLabel10, 2, 0, 1, 1)

        self.railwayLightsValue10 = QLabel(self.railwayCrossingFrame10)
        self.railwayLightsValue10.setObjectName(u"railwayLightsValue10")
        self.railwayLightsValue10.setFont(font1)
        self.railwayLightsValue10.setAlignment(Qt.AlignCenter)

        self.gridLayout_45.addWidget(self.railwayLightsValue10, 2, 1, 1, 1)


        self.gridLayout_43.addWidget(self.railwayCrossingFrame10, 1, 0, 2, 1)

        self.displayPLC10 = QTextBrowser(self.tab10Frame)
        self.displayPLC10.setObjectName(u"displayPLC10")
        self.displayPLC10.setFont(font3)

        self.gridLayout_43.addWidget(self.displayPLC10, 3, 0, 1, 5)

        self.trafficLightFrame10 = QFrame(self.tab10Frame)
        self.trafficLightFrame10.setObjectName(u"trafficLightFrame10")
        self.trafficLightFrame10.setAutoFillBackground(True)
        self.trafficLightFrame10.setFrameShape(QFrame.Box)
        self.trafficLightFrame10.setFrameShadow(QFrame.Raised)
        self.trafficLightFrame10.setLineWidth(1)
        self.trafficLightFrame10.setMidLineWidth(0)
        self.verticalLayout_90 = QVBoxLayout(self.trafficLightFrame10)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.trafficLightLabel10 = QLabel(self.trafficLightFrame10)
        self.trafficLightLabel10.setObjectName(u"trafficLightLabel10")
        self.trafficLightLabel10.setFont(font1)
        self.trafficLightLabel10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_90.addWidget(self.trafficLightLabel10)

        self.trafficLightValue10 = QLabel(self.trafficLightFrame10)
        self.trafficLightValue10.setObjectName(u"trafficLightValue10")
        self.trafficLightValue10.setFont(font1)
        self.trafficLightValue10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_90.addWidget(self.trafficLightValue10)


        self.gridLayout_43.addWidget(self.trafficLightFrame10, 2, 4, 1, 1)

        self.commandedSpeedFrame10 = QFrame(self.tab10Frame)
        self.commandedSpeedFrame10.setObjectName(u"commandedSpeedFrame10")
        self.commandedSpeedFrame10.setAutoFillBackground(True)
        self.commandedSpeedFrame10.setFrameShape(QFrame.Box)
        self.commandedSpeedFrame10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.commandedSpeedFrame10)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.commandedSpeedLabel10 = QLabel(self.commandedSpeedFrame10)
        self.commandedSpeedLabel10.setObjectName(u"commandedSpeedLabel10")
        self.commandedSpeedLabel10.setFont(font1)
        self.commandedSpeedLabel10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_86.addWidget(self.commandedSpeedLabel10)

        self.commandedSpeedValue10 = QLabel(self.commandedSpeedFrame10)
        self.commandedSpeedValue10.setObjectName(u"commandedSpeedValue10")
        self.commandedSpeedValue10.setFont(font1)
        self.commandedSpeedValue10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_86.addWidget(self.commandedSpeedValue10)


        self.gridLayout_43.addWidget(self.commandedSpeedFrame10, 2, 3, 1, 1)

        self.statusFrame10 = QFrame(self.tab10Frame)
        self.statusFrame10.setObjectName(u"statusFrame10")
        self.statusFrame10.setAutoFillBackground(True)
        self.statusFrame10.setFrameShape(QFrame.Box)
        self.statusFrame10.setFrameShadow(QFrame.Raised)
        self.statusFrame10.setLineWidth(1)
        self.statusFrame10.setMidLineWidth(0)
        self.verticalLayout_92 = QVBoxLayout(self.statusFrame10)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.statusLabel10 = QLabel(self.statusFrame10)
        self.statusLabel10.setObjectName(u"statusLabel10")
        self.statusLabel10.setFont(font1)
        self.statusLabel10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_92.addWidget(self.statusLabel10)

        self.statusValue10 = QLabel(self.statusFrame10)
        self.statusValue10.setObjectName(u"statusValue10")
        self.statusValue10.setFont(font1)
        self.statusValue10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_92.addWidget(self.statusValue10)


        self.gridLayout_43.addWidget(self.statusFrame10, 1, 4, 1, 1)

        self.switchPositionFrame10 = QFrame(self.tab10Frame)
        self.switchPositionFrame10.setObjectName(u"switchPositionFrame10")
        self.switchPositionFrame10.setAutoFillBackground(True)
        self.switchPositionFrame10.setFrameShape(QFrame.Box)
        self.switchPositionFrame10.setFrameShadow(QFrame.Raised)
        self.switchPositionFrame10.setLineWidth(1)
        self.switchPositionFrame10.setMidLineWidth(0)
        self.gridLayout_44 = QGridLayout(self.switchPositionFrame10)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.switchPositionLabel10 = QLabel(self.switchPositionFrame10)
        self.switchPositionLabel10.setObjectName(u"switchPositionLabel10")
        self.switchPositionLabel10.setFont(font1)
        self.switchPositionLabel10.setAlignment(Qt.AlignCenter)

        self.gridLayout_44.addWidget(self.switchPositionLabel10, 0, 0, 1, 3)

        self.switchFromValue10 = QLabel(self.switchPositionFrame10)
        self.switchFromValue10.setObjectName(u"switchFromValue10")
        self.switchFromValue10.setFont(font1)
        self.switchFromValue10.setAlignment(Qt.AlignCenter)

        self.gridLayout_44.addWidget(self.switchFromValue10, 1, 0, 1, 1)

        self.switchArrowLabel10 = QLabel(self.switchPositionFrame10)
        self.switchArrowLabel10.setObjectName(u"switchArrowLabel10")
        self.switchArrowLabel10.setFont(font1)
        self.switchArrowLabel10.setAlignment(Qt.AlignCenter)

        self.gridLayout_44.addWidget(self.switchArrowLabel10, 1, 1, 1, 1)

        self.switchToValue10 = QLabel(self.switchPositionFrame10)
        self.switchToValue10.setObjectName(u"switchToValue10")
        self.switchToValue10.setFont(font1)
        self.switchToValue10.setAlignment(Qt.AlignCenter)

        self.gridLayout_44.addWidget(self.switchToValue10, 1, 2, 1, 1)

        self.switchButton10 = QPushButton(self.switchPositionFrame10)
        self.switchButton10.setObjectName(u"switchButton10")
        self.switchButton10.setEnabled(False)
        self.switchButton10.setFont(font2)

        self.gridLayout_44.addWidget(self.switchButton10, 2, 1, 1, 1)


        self.gridLayout_43.addWidget(self.switchPositionFrame10, 1, 1, 2, 1)


        self.gridLayout_46.addWidget(self.tab10Frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab10, "")
        self.tab11 = QWidget()
        self.tab11.setObjectName(u"tab11")
        self.gridLayout_50 = QGridLayout(self.tab11)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.tab11Frame = QFrame(self.tab11)
        self.tab11Frame.setObjectName(u"tab11Frame")
        self.tab11Frame.setFrameShape(QFrame.StyledPanel)
        self.tab11Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_47 = QGridLayout(self.tab11Frame)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.blockLabel11 = QLabel(self.tab11Frame)
        self.blockLabel11.setObjectName(u"blockLabel11")
        self.blockLabel11.setFont(font1)
        self.blockLabel11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_47.addWidget(self.blockLabel11, 0, 3, 1, 1)

        self.occupancyFrame11 = QFrame(self.tab11Frame)
        self.occupancyFrame11.setObjectName(u"occupancyFrame11")
        self.occupancyFrame11.setAutoFillBackground(True)
        self.occupancyFrame11.setFrameShape(QFrame.Box)
        self.occupancyFrame11.setFrameShadow(QFrame.Raised)
        self.occupancyFrame11.setLineWidth(1)
        self.occupancyFrame11.setMidLineWidth(0)
        self.verticalLayout_95 = QVBoxLayout(self.occupancyFrame11)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.occupancyLabel11 = QLabel(self.occupancyFrame11)
        self.occupancyLabel11.setObjectName(u"occupancyLabel11")
        self.occupancyLabel11.setFont(font1)
        self.occupancyLabel11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_95.addWidget(self.occupancyLabel11)

        self.occupancyValue11 = QLabel(self.occupancyFrame11)
        self.occupancyValue11.setObjectName(u"occupancyValue11")
        self.occupancyValue11.setFont(font1)
        self.occupancyValue11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_95.addWidget(self.occupancyValue11)


        self.gridLayout_47.addWidget(self.occupancyFrame11, 2, 2, 1, 1)

        self.authorityFrame11 = QFrame(self.tab11Frame)
        self.authorityFrame11.setObjectName(u"authorityFrame11")
        self.authorityFrame11.setAutoFillBackground(True)
        self.authorityFrame11.setFrameShape(QFrame.Box)
        self.authorityFrame11.setFrameShadow(QFrame.Raised)
        self.authorityFrame11.setLineWidth(1)
        self.authorityFrame11.setMidLineWidth(0)
        self.verticalLayout_96 = QVBoxLayout(self.authorityFrame11)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.authorityLabel11 = QLabel(self.authorityFrame11)
        self.authorityLabel11.setObjectName(u"authorityLabel11")
        self.authorityLabel11.setFont(font1)
        self.authorityLabel11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_96.addWidget(self.authorityLabel11)

        self.authorityValue11 = QLabel(self.authorityFrame11)
        self.authorityValue11.setObjectName(u"authorityValue11")
        self.authorityValue11.setFont(font1)
        self.authorityValue11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_96.addWidget(self.authorityValue11)


        self.gridLayout_47.addWidget(self.authorityFrame11, 1, 2, 1, 1)

        self.uploadPLC11 = QPushButton(self.tab11Frame)
        self.uploadPLC11.setObjectName(u"uploadPLC11")
        self.uploadPLC11.setFont(font1)

        self.gridLayout_47.addWidget(self.uploadPLC11, 4, 4, 1, 1)

        self.suggestedSpeedFrame11 = QFrame(self.tab11Frame)
        self.suggestedSpeedFrame11.setObjectName(u"suggestedSpeedFrame11")
        self.suggestedSpeedFrame11.setAutoFillBackground(True)
        self.suggestedSpeedFrame11.setFrameShape(QFrame.Box)
        self.suggestedSpeedFrame11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.suggestedSpeedFrame11)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.suggestedSpeedLabel11 = QLabel(self.suggestedSpeedFrame11)
        self.suggestedSpeedLabel11.setObjectName(u"suggestedSpeedLabel11")
        self.suggestedSpeedLabel11.setFont(font1)
        self.suggestedSpeedLabel11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_98.addWidget(self.suggestedSpeedLabel11)

        self.suggestedSpeedValue11 = QLabel(self.suggestedSpeedFrame11)
        self.suggestedSpeedValue11.setObjectName(u"suggestedSpeedValue11")
        self.suggestedSpeedValue11.setFont(font1)
        self.suggestedSpeedValue11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_98.addWidget(self.suggestedSpeedValue11)


        self.gridLayout_47.addWidget(self.suggestedSpeedFrame11, 1, 3, 1, 1)

        self.trackLabel11 = QLabel(self.tab11Frame)
        self.trackLabel11.setObjectName(u"trackLabel11")
        self.trackLabel11.setFont(font1)
        self.trackLabel11.setAlignment(Qt.AlignCenter)

        self.gridLayout_47.addWidget(self.trackLabel11, 0, 0, 1, 1)

        self.blockSelect11 = QComboBox(self.tab11Frame)
        self.blockSelect11.setObjectName(u"blockSelect11")
        self.blockSelect11.setEnabled(True)
        self.blockSelect11.setFont(font1)
        self.blockSelect11.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout_47.addWidget(self.blockSelect11, 0, 4, 1, 1)

        self.railwayCrossingFrame11 = QFrame(self.tab11Frame)
        self.railwayCrossingFrame11.setObjectName(u"railwayCrossingFrame11")
        self.railwayCrossingFrame11.setAutoFillBackground(True)
        self.railwayCrossingFrame11.setFrameShape(QFrame.Box)
        self.railwayCrossingFrame11.setFrameShadow(QFrame.Raised)
        self.railwayCrossingFrame11.setLineWidth(1)
        self.railwayCrossingFrame11.setMidLineWidth(0)
        self.gridLayout_49 = QGridLayout(self.railwayCrossingFrame11)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.railwayCrossingLabel11 = QLabel(self.railwayCrossingFrame11)
        self.railwayCrossingLabel11.setObjectName(u"railwayCrossingLabel11")
        self.railwayCrossingLabel11.setFont(font1)
        self.railwayCrossingLabel11.setAlignment(Qt.AlignCenter)

        self.gridLayout_49.addWidget(self.railwayCrossingLabel11, 0, 0, 1, 2)

        self.railwayGateLabel11 = QLabel(self.railwayCrossingFrame11)
        self.railwayGateLabel11.setObjectName(u"railwayGateLabel11")
        self.railwayGateLabel11.setFont(font2)

        self.gridLayout_49.addWidget(self.railwayGateLabel11, 1, 0, 1, 1)

        self.railwayGateValue11 = QLabel(self.railwayCrossingFrame11)
        self.railwayGateValue11.setObjectName(u"railwayGateValue11")
        self.railwayGateValue11.setFont(font1)
        self.railwayGateValue11.setAlignment(Qt.AlignCenter)

        self.gridLayout_49.addWidget(self.railwayGateValue11, 1, 1, 1, 1)

        self.railwayLightsLabel11 = QLabel(self.railwayCrossingFrame11)
        self.railwayLightsLabel11.setObjectName(u"railwayLightsLabel11")
        self.railwayLightsLabel11.setFont(font2)

        self.gridLayout_49.addWidget(self.railwayLightsLabel11, 2, 0, 1, 1)

        self.railwayLightsValue11 = QLabel(self.railwayCrossingFrame11)
        self.railwayLightsValue11.setObjectName(u"railwayLightsValue11")
        self.railwayLightsValue11.setFont(font1)
        self.railwayLightsValue11.setAlignment(Qt.AlignCenter)

        self.gridLayout_49.addWidget(self.railwayLightsValue11, 2, 1, 1, 1)


        self.gridLayout_47.addWidget(self.railwayCrossingFrame11, 1, 0, 2, 1)

        self.displayPLC11 = QTextBrowser(self.tab11Frame)
        self.displayPLC11.setObjectName(u"displayPLC11")
        self.displayPLC11.setFont(font3)

        self.gridLayout_47.addWidget(self.displayPLC11, 3, 0, 1, 5)

        self.trafficLightFrame11 = QFrame(self.tab11Frame)
        self.trafficLightFrame11.setObjectName(u"trafficLightFrame11")
        self.trafficLightFrame11.setAutoFillBackground(True)
        self.trafficLightFrame11.setFrameShape(QFrame.Box)
        self.trafficLightFrame11.setFrameShadow(QFrame.Raised)
        self.trafficLightFrame11.setLineWidth(1)
        self.trafficLightFrame11.setMidLineWidth(0)
        self.verticalLayout_97 = QVBoxLayout(self.trafficLightFrame11)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.trafficLightLabel11 = QLabel(self.trafficLightFrame11)
        self.trafficLightLabel11.setObjectName(u"trafficLightLabel11")
        self.trafficLightLabel11.setFont(font1)
        self.trafficLightLabel11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_97.addWidget(self.trafficLightLabel11)

        self.trafficLightValue11 = QLabel(self.trafficLightFrame11)
        self.trafficLightValue11.setObjectName(u"trafficLightValue11")
        self.trafficLightValue11.setFont(font1)
        self.trafficLightValue11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_97.addWidget(self.trafficLightValue11)


        self.gridLayout_47.addWidget(self.trafficLightFrame11, 2, 4, 1, 1)

        self.commandedSpeedFrame11 = QFrame(self.tab11Frame)
        self.commandedSpeedFrame11.setObjectName(u"commandedSpeedFrame11")
        self.commandedSpeedFrame11.setAutoFillBackground(True)
        self.commandedSpeedFrame11.setFrameShape(QFrame.Box)
        self.commandedSpeedFrame11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.commandedSpeedFrame11)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.commandedSpeedLabel11 = QLabel(self.commandedSpeedFrame11)
        self.commandedSpeedLabel11.setObjectName(u"commandedSpeedLabel11")
        self.commandedSpeedLabel11.setFont(font1)
        self.commandedSpeedLabel11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_93.addWidget(self.commandedSpeedLabel11)

        self.commandedSpeedValue11 = QLabel(self.commandedSpeedFrame11)
        self.commandedSpeedValue11.setObjectName(u"commandedSpeedValue11")
        self.commandedSpeedValue11.setFont(font1)
        self.commandedSpeedValue11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_93.addWidget(self.commandedSpeedValue11)


        self.gridLayout_47.addWidget(self.commandedSpeedFrame11, 2, 3, 1, 1)

        self.statusFrame11 = QFrame(self.tab11Frame)
        self.statusFrame11.setObjectName(u"statusFrame11")
        self.statusFrame11.setAutoFillBackground(True)
        self.statusFrame11.setFrameShape(QFrame.Box)
        self.statusFrame11.setFrameShadow(QFrame.Raised)
        self.statusFrame11.setLineWidth(1)
        self.statusFrame11.setMidLineWidth(0)
        self.verticalLayout_99 = QVBoxLayout(self.statusFrame11)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.statusLabel11 = QLabel(self.statusFrame11)
        self.statusLabel11.setObjectName(u"statusLabel11")
        self.statusLabel11.setFont(font1)
        self.statusLabel11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_99.addWidget(self.statusLabel11)

        self.statusValue11 = QLabel(self.statusFrame11)
        self.statusValue11.setObjectName(u"statusValue11")
        self.statusValue11.setFont(font1)
        self.statusValue11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_99.addWidget(self.statusValue11)


        self.gridLayout_47.addWidget(self.statusFrame11, 1, 4, 1, 1)

        self.switchPositionFrame11 = QFrame(self.tab11Frame)
        self.switchPositionFrame11.setObjectName(u"switchPositionFrame11")
        self.switchPositionFrame11.setAutoFillBackground(True)
        self.switchPositionFrame11.setFrameShape(QFrame.Box)
        self.switchPositionFrame11.setFrameShadow(QFrame.Raised)
        self.switchPositionFrame11.setLineWidth(1)
        self.switchPositionFrame11.setMidLineWidth(0)
        self.gridLayout_48 = QGridLayout(self.switchPositionFrame11)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.switchPositionLabel11 = QLabel(self.switchPositionFrame11)
        self.switchPositionLabel11.setObjectName(u"switchPositionLabel11")
        self.switchPositionLabel11.setFont(font1)
        self.switchPositionLabel11.setAlignment(Qt.AlignCenter)

        self.gridLayout_48.addWidget(self.switchPositionLabel11, 0, 0, 1, 3)

        self.switchFromValue11 = QLabel(self.switchPositionFrame11)
        self.switchFromValue11.setObjectName(u"switchFromValue11")
        self.switchFromValue11.setFont(font1)
        self.switchFromValue11.setAlignment(Qt.AlignCenter)

        self.gridLayout_48.addWidget(self.switchFromValue11, 1, 0, 1, 1)

        self.switchToValue11 = QLabel(self.switchPositionFrame11)
        self.switchToValue11.setObjectName(u"switchToValue11")
        self.switchToValue11.setFont(font1)
        self.switchToValue11.setAlignment(Qt.AlignCenter)

        self.gridLayout_48.addWidget(self.switchToValue11, 1, 2, 1, 1)

        self.switchArrowLabel11 = QLabel(self.switchPositionFrame11)
        self.switchArrowLabel11.setObjectName(u"switchArrowLabel11")
        self.switchArrowLabel11.setFont(font1)
        self.switchArrowLabel11.setAlignment(Qt.AlignCenter)

        self.gridLayout_48.addWidget(self.switchArrowLabel11, 1, 1, 1, 1)

        self.pushButton = QPushButton(self.switchPositionFrame11)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setFont(font2)

        self.gridLayout_48.addWidget(self.pushButton, 2, 1, 1, 1)


        self.gridLayout_47.addWidget(self.switchPositionFrame11, 1, 1, 2, 1)


        self.gridLayout_50.addWidget(self.tab11Frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab11, "")
        self.tab12 = QWidget()
        self.tab12.setObjectName(u"tab12")
        self.gridLayout_54 = QGridLayout(self.tab12)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.tab12Frame = QFrame(self.tab12)
        self.tab12Frame.setObjectName(u"tab12Frame")
        self.tab12Frame.setFrameShape(QFrame.StyledPanel)
        self.tab12Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_51 = QGridLayout(self.tab12Frame)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.blockLabel12 = QLabel(self.tab12Frame)
        self.blockLabel12.setObjectName(u"blockLabel12")
        self.blockLabel12.setFont(font1)
        self.blockLabel12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_51.addWidget(self.blockLabel12, 0, 3, 1, 1)

        self.occupancyFrame12 = QFrame(self.tab12Frame)
        self.occupancyFrame12.setObjectName(u"occupancyFrame12")
        self.occupancyFrame12.setAutoFillBackground(True)
        self.occupancyFrame12.setFrameShape(QFrame.Box)
        self.occupancyFrame12.setFrameShadow(QFrame.Raised)
        self.occupancyFrame12.setLineWidth(1)
        self.occupancyFrame12.setMidLineWidth(0)
        self.verticalLayout_102 = QVBoxLayout(self.occupancyFrame12)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.occupancyLabel12 = QLabel(self.occupancyFrame12)
        self.occupancyLabel12.setObjectName(u"occupancyLabel12")
        self.occupancyLabel12.setFont(font1)
        self.occupancyLabel12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_102.addWidget(self.occupancyLabel12)

        self.occupancyValue12 = QLabel(self.occupancyFrame12)
        self.occupancyValue12.setObjectName(u"occupancyValue12")
        self.occupancyValue12.setFont(font1)
        self.occupancyValue12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_102.addWidget(self.occupancyValue12)


        self.gridLayout_51.addWidget(self.occupancyFrame12, 2, 2, 1, 1)

        self.authorityFrame12 = QFrame(self.tab12Frame)
        self.authorityFrame12.setObjectName(u"authorityFrame12")
        self.authorityFrame12.setAutoFillBackground(True)
        self.authorityFrame12.setFrameShape(QFrame.Box)
        self.authorityFrame12.setFrameShadow(QFrame.Raised)
        self.authorityFrame12.setLineWidth(1)
        self.authorityFrame12.setMidLineWidth(0)
        self.verticalLayout_103 = QVBoxLayout(self.authorityFrame12)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.authorityLabel12 = QLabel(self.authorityFrame12)
        self.authorityLabel12.setObjectName(u"authorityLabel12")
        self.authorityLabel12.setFont(font1)
        self.authorityLabel12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_103.addWidget(self.authorityLabel12)

        self.authorityValue12 = QLabel(self.authorityFrame12)
        self.authorityValue12.setObjectName(u"authorityValue12")
        self.authorityValue12.setFont(font1)
        self.authorityValue12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_103.addWidget(self.authorityValue12)


        self.gridLayout_51.addWidget(self.authorityFrame12, 1, 2, 1, 1)

        self.uploadPLC12 = QPushButton(self.tab12Frame)
        self.uploadPLC12.setObjectName(u"uploadPLC12")
        self.uploadPLC12.setFont(font1)

        self.gridLayout_51.addWidget(self.uploadPLC12, 4, 4, 1, 1)

        self.suggestedSpeedFrame12 = QFrame(self.tab12Frame)
        self.suggestedSpeedFrame12.setObjectName(u"suggestedSpeedFrame12")
        self.suggestedSpeedFrame12.setAutoFillBackground(True)
        self.suggestedSpeedFrame12.setFrameShape(QFrame.Box)
        self.suggestedSpeedFrame12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.suggestedSpeedFrame12)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.suggestedSpeedLabel12 = QLabel(self.suggestedSpeedFrame12)
        self.suggestedSpeedLabel12.setObjectName(u"suggestedSpeedLabel12")
        self.suggestedSpeedLabel12.setFont(font1)
        self.suggestedSpeedLabel12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_105.addWidget(self.suggestedSpeedLabel12)

        self.suggestedSpeedValue12 = QLabel(self.suggestedSpeedFrame12)
        self.suggestedSpeedValue12.setObjectName(u"suggestedSpeedValue12")
        self.suggestedSpeedValue12.setFont(font1)
        self.suggestedSpeedValue12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_105.addWidget(self.suggestedSpeedValue12)


        self.gridLayout_51.addWidget(self.suggestedSpeedFrame12, 1, 3, 1, 1)

        self.trackLabel12 = QLabel(self.tab12Frame)
        self.trackLabel12.setObjectName(u"trackLabel12")
        self.trackLabel12.setFont(font1)
        self.trackLabel12.setAlignment(Qt.AlignCenter)

        self.gridLayout_51.addWidget(self.trackLabel12, 0, 0, 1, 1)

        self.blockSelect12 = QComboBox(self.tab12Frame)
        self.blockSelect12.setObjectName(u"blockSelect12")
        self.blockSelect12.setEnabled(True)
        self.blockSelect12.setFont(font1)
        self.blockSelect12.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout_51.addWidget(self.blockSelect12, 0, 4, 1, 1)

        self.railwayCrossingFrame12 = QFrame(self.tab12Frame)
        self.railwayCrossingFrame12.setObjectName(u"railwayCrossingFrame12")
        self.railwayCrossingFrame12.setAutoFillBackground(True)
        self.railwayCrossingFrame12.setFrameShape(QFrame.Box)
        self.railwayCrossingFrame12.setFrameShadow(QFrame.Raised)
        self.railwayCrossingFrame12.setLineWidth(1)
        self.railwayCrossingFrame12.setMidLineWidth(0)
        self.gridLayout_53 = QGridLayout(self.railwayCrossingFrame12)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.railwayCrossingLabel12 = QLabel(self.railwayCrossingFrame12)
        self.railwayCrossingLabel12.setObjectName(u"railwayCrossingLabel12")
        self.railwayCrossingLabel12.setFont(font1)
        self.railwayCrossingLabel12.setAlignment(Qt.AlignCenter)

        self.gridLayout_53.addWidget(self.railwayCrossingLabel12, 0, 0, 1, 2)

        self.railwayGateLabel12 = QLabel(self.railwayCrossingFrame12)
        self.railwayGateLabel12.setObjectName(u"railwayGateLabel12")
        self.railwayGateLabel12.setFont(font2)

        self.gridLayout_53.addWidget(self.railwayGateLabel12, 1, 0, 1, 1)

        self.railwayGateValue12 = QLabel(self.railwayCrossingFrame12)
        self.railwayGateValue12.setObjectName(u"railwayGateValue12")
        self.railwayGateValue12.setFont(font1)
        self.railwayGateValue12.setAlignment(Qt.AlignCenter)

        self.gridLayout_53.addWidget(self.railwayGateValue12, 1, 1, 1, 1)

        self.railwayLightsLabel12 = QLabel(self.railwayCrossingFrame12)
        self.railwayLightsLabel12.setObjectName(u"railwayLightsLabel12")
        self.railwayLightsLabel12.setFont(font2)

        self.gridLayout_53.addWidget(self.railwayLightsLabel12, 2, 0, 1, 1)

        self.railwayLightsValue12 = QLabel(self.railwayCrossingFrame12)
        self.railwayLightsValue12.setObjectName(u"railwayLightsValue12")
        self.railwayLightsValue12.setFont(font1)
        self.railwayLightsValue12.setAlignment(Qt.AlignCenter)

        self.gridLayout_53.addWidget(self.railwayLightsValue12, 2, 1, 1, 1)


        self.gridLayout_51.addWidget(self.railwayCrossingFrame12, 1, 0, 2, 1)

        self.displayPLC12 = QTextBrowser(self.tab12Frame)
        self.displayPLC12.setObjectName(u"displayPLC12")
        self.displayPLC12.setFont(font3)

        self.gridLayout_51.addWidget(self.displayPLC12, 3, 0, 1, 5)

        self.trafficLightFrame12 = QFrame(self.tab12Frame)
        self.trafficLightFrame12.setObjectName(u"trafficLightFrame12")
        self.trafficLightFrame12.setAutoFillBackground(True)
        self.trafficLightFrame12.setFrameShape(QFrame.Box)
        self.trafficLightFrame12.setFrameShadow(QFrame.Raised)
        self.trafficLightFrame12.setLineWidth(1)
        self.trafficLightFrame12.setMidLineWidth(0)
        self.verticalLayout_104 = QVBoxLayout(self.trafficLightFrame12)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.trafficLightLabel12 = QLabel(self.trafficLightFrame12)
        self.trafficLightLabel12.setObjectName(u"trafficLightLabel12")
        self.trafficLightLabel12.setFont(font1)
        self.trafficLightLabel12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_104.addWidget(self.trafficLightLabel12)

        self.trafficLightValue12 = QLabel(self.trafficLightFrame12)
        self.trafficLightValue12.setObjectName(u"trafficLightValue12")
        self.trafficLightValue12.setFont(font1)
        self.trafficLightValue12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_104.addWidget(self.trafficLightValue12)


        self.gridLayout_51.addWidget(self.trafficLightFrame12, 2, 4, 1, 1)

        self.commandedSpeedFrame12 = QFrame(self.tab12Frame)
        self.commandedSpeedFrame12.setObjectName(u"commandedSpeedFrame12")
        self.commandedSpeedFrame12.setAutoFillBackground(True)
        self.commandedSpeedFrame12.setFrameShape(QFrame.Box)
        self.commandedSpeedFrame12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.commandedSpeedFrame12)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.commandedSpeedLabel12 = QLabel(self.commandedSpeedFrame12)
        self.commandedSpeedLabel12.setObjectName(u"commandedSpeedLabel12")
        self.commandedSpeedLabel12.setFont(font1)
        self.commandedSpeedLabel12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_100.addWidget(self.commandedSpeedLabel12)

        self.commandedSpeedValue12 = QLabel(self.commandedSpeedFrame12)
        self.commandedSpeedValue12.setObjectName(u"commandedSpeedValue12")
        self.commandedSpeedValue12.setFont(font1)
        self.commandedSpeedValue12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_100.addWidget(self.commandedSpeedValue12)


        self.gridLayout_51.addWidget(self.commandedSpeedFrame12, 2, 3, 1, 1)

        self.statusFrame12 = QFrame(self.tab12Frame)
        self.statusFrame12.setObjectName(u"statusFrame12")
        self.statusFrame12.setAutoFillBackground(True)
        self.statusFrame12.setFrameShape(QFrame.Box)
        self.statusFrame12.setFrameShadow(QFrame.Raised)
        self.statusFrame12.setLineWidth(1)
        self.statusFrame12.setMidLineWidth(0)
        self.verticalLayout_106 = QVBoxLayout(self.statusFrame12)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.statusLabel12 = QLabel(self.statusFrame12)
        self.statusLabel12.setObjectName(u"statusLabel12")
        self.statusLabel12.setFont(font1)
        self.statusLabel12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_106.addWidget(self.statusLabel12)

        self.statusValue12 = QLabel(self.statusFrame12)
        self.statusValue12.setObjectName(u"statusValue12")
        self.statusValue12.setFont(font1)
        self.statusValue12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_106.addWidget(self.statusValue12)


        self.gridLayout_51.addWidget(self.statusFrame12, 1, 4, 1, 1)

        self.switchPositionFrame12 = QFrame(self.tab12Frame)
        self.switchPositionFrame12.setObjectName(u"switchPositionFrame12")
        self.switchPositionFrame12.setAutoFillBackground(True)
        self.switchPositionFrame12.setFrameShape(QFrame.Box)
        self.switchPositionFrame12.setFrameShadow(QFrame.Raised)
        self.switchPositionFrame12.setLineWidth(1)
        self.switchPositionFrame12.setMidLineWidth(0)
        self.gridLayout_52 = QGridLayout(self.switchPositionFrame12)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.switchToValue12 = QLabel(self.switchPositionFrame12)
        self.switchToValue12.setObjectName(u"switchToValue12")
        self.switchToValue12.setFont(font1)
        self.switchToValue12.setAlignment(Qt.AlignCenter)

        self.gridLayout_52.addWidget(self.switchToValue12, 1, 2, 1, 1)

        self.switchPositionLabel12 = QLabel(self.switchPositionFrame12)
        self.switchPositionLabel12.setObjectName(u"switchPositionLabel12")
        self.switchPositionLabel12.setFont(font1)
        self.switchPositionLabel12.setAlignment(Qt.AlignCenter)

        self.gridLayout_52.addWidget(self.switchPositionLabel12, 0, 0, 1, 3)

        self.switchArrowLabel12 = QLabel(self.switchPositionFrame12)
        self.switchArrowLabel12.setObjectName(u"switchArrowLabel12")
        self.switchArrowLabel12.setFont(font1)
        self.switchArrowLabel12.setAlignment(Qt.AlignCenter)

        self.gridLayout_52.addWidget(self.switchArrowLabel12, 1, 1, 1, 1)

        self.switchFromValue12 = QLabel(self.switchPositionFrame12)
        self.switchFromValue12.setObjectName(u"switchFromValue12")
        self.switchFromValue12.setFont(font1)
        self.switchFromValue12.setAlignment(Qt.AlignCenter)

        self.gridLayout_52.addWidget(self.switchFromValue12, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.switchPositionFrame12)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setFont(font2)

        self.gridLayout_52.addWidget(self.pushButton_2, 2, 1, 1, 1)


        self.gridLayout_51.addWidget(self.switchPositionFrame12, 1, 1, 2, 1)


        self.gridLayout_54.addWidget(self.tab12Frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab12, "")
        self.tab13 = QWidget()
        self.tab13.setObjectName(u"tab13")
        self.gridLayout_58 = QGridLayout(self.tab13)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.tab13Frame = QFrame(self.tab13)
        self.tab13Frame.setObjectName(u"tab13Frame")
        self.tab13Frame.setFrameShape(QFrame.StyledPanel)
        self.tab13Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_55 = QGridLayout(self.tab13Frame)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.blockLabel13 = QLabel(self.tab13Frame)
        self.blockLabel13.setObjectName(u"blockLabel13")
        self.blockLabel13.setFont(font1)
        self.blockLabel13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.blockLabel13, 0, 3, 1, 1)

        self.occupancyFrame13 = QFrame(self.tab13Frame)
        self.occupancyFrame13.setObjectName(u"occupancyFrame13")
        self.occupancyFrame13.setAutoFillBackground(True)
        self.occupancyFrame13.setFrameShape(QFrame.Box)
        self.occupancyFrame13.setFrameShadow(QFrame.Raised)
        self.occupancyFrame13.setLineWidth(1)
        self.occupancyFrame13.setMidLineWidth(0)
        self.verticalLayout_109 = QVBoxLayout(self.occupancyFrame13)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.occupancyLabel13 = QLabel(self.occupancyFrame13)
        self.occupancyLabel13.setObjectName(u"occupancyLabel13")
        self.occupancyLabel13.setFont(font1)
        self.occupancyLabel13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_109.addWidget(self.occupancyLabel13)

        self.occupancyValue13 = QLabel(self.occupancyFrame13)
        self.occupancyValue13.setObjectName(u"occupancyValue13")
        self.occupancyValue13.setFont(font1)
        self.occupancyValue13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_109.addWidget(self.occupancyValue13)


        self.gridLayout_55.addWidget(self.occupancyFrame13, 2, 2, 1, 1)

        self.authorityFrame13 = QFrame(self.tab13Frame)
        self.authorityFrame13.setObjectName(u"authorityFrame13")
        self.authorityFrame13.setAutoFillBackground(True)
        self.authorityFrame13.setFrameShape(QFrame.Box)
        self.authorityFrame13.setFrameShadow(QFrame.Raised)
        self.authorityFrame13.setLineWidth(1)
        self.authorityFrame13.setMidLineWidth(0)
        self.verticalLayout_110 = QVBoxLayout(self.authorityFrame13)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.authorityLabel13 = QLabel(self.authorityFrame13)
        self.authorityLabel13.setObjectName(u"authorityLabel13")
        self.authorityLabel13.setFont(font1)
        self.authorityLabel13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_110.addWidget(self.authorityLabel13)

        self.authorityValue13 = QLabel(self.authorityFrame13)
        self.authorityValue13.setObjectName(u"authorityValue13")
        self.authorityValue13.setFont(font1)
        self.authorityValue13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_110.addWidget(self.authorityValue13)


        self.gridLayout_55.addWidget(self.authorityFrame13, 1, 2, 1, 1)

        self.uploadPLC13 = QPushButton(self.tab13Frame)
        self.uploadPLC13.setObjectName(u"uploadPLC13")
        self.uploadPLC13.setFont(font1)

        self.gridLayout_55.addWidget(self.uploadPLC13, 4, 4, 1, 1)

        self.suggestedSpeedFrame13 = QFrame(self.tab13Frame)
        self.suggestedSpeedFrame13.setObjectName(u"suggestedSpeedFrame13")
        self.suggestedSpeedFrame13.setAutoFillBackground(True)
        self.suggestedSpeedFrame13.setFrameShape(QFrame.Box)
        self.suggestedSpeedFrame13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_112 = QVBoxLayout(self.suggestedSpeedFrame13)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.suggestedSpeedLabel13 = QLabel(self.suggestedSpeedFrame13)
        self.suggestedSpeedLabel13.setObjectName(u"suggestedSpeedLabel13")
        self.suggestedSpeedLabel13.setFont(font1)
        self.suggestedSpeedLabel13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_112.addWidget(self.suggestedSpeedLabel13)

        self.suggestedSpeedValue13 = QLabel(self.suggestedSpeedFrame13)
        self.suggestedSpeedValue13.setObjectName(u"suggestedSpeedValue13")
        self.suggestedSpeedValue13.setFont(font1)
        self.suggestedSpeedValue13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_112.addWidget(self.suggestedSpeedValue13)


        self.gridLayout_55.addWidget(self.suggestedSpeedFrame13, 1, 3, 1, 1)

        self.trackLabel13 = QLabel(self.tab13Frame)
        self.trackLabel13.setObjectName(u"trackLabel13")
        self.trackLabel13.setFont(font1)
        self.trackLabel13.setAlignment(Qt.AlignCenter)

        self.gridLayout_55.addWidget(self.trackLabel13, 0, 0, 1, 1)

        self.blockSelect13 = QComboBox(self.tab13Frame)
        self.blockSelect13.setObjectName(u"blockSelect13")
        self.blockSelect13.setEnabled(True)
        self.blockSelect13.setFont(font1)
        self.blockSelect13.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout_55.addWidget(self.blockSelect13, 0, 4, 1, 1)

        self.railwayCrossingFrame13 = QFrame(self.tab13Frame)
        self.railwayCrossingFrame13.setObjectName(u"railwayCrossingFrame13")
        self.railwayCrossingFrame13.setAutoFillBackground(True)
        self.railwayCrossingFrame13.setFrameShape(QFrame.Box)
        self.railwayCrossingFrame13.setFrameShadow(QFrame.Raised)
        self.railwayCrossingFrame13.setLineWidth(1)
        self.railwayCrossingFrame13.setMidLineWidth(0)
        self.gridLayout_57 = QGridLayout(self.railwayCrossingFrame13)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.railwayCrossingLabel13 = QLabel(self.railwayCrossingFrame13)
        self.railwayCrossingLabel13.setObjectName(u"railwayCrossingLabel13")
        self.railwayCrossingLabel13.setFont(font1)
        self.railwayCrossingLabel13.setAlignment(Qt.AlignCenter)

        self.gridLayout_57.addWidget(self.railwayCrossingLabel13, 0, 0, 1, 2)

        self.railwayGateLabel13 = QLabel(self.railwayCrossingFrame13)
        self.railwayGateLabel13.setObjectName(u"railwayGateLabel13")
        self.railwayGateLabel13.setFont(font2)

        self.gridLayout_57.addWidget(self.railwayGateLabel13, 1, 0, 1, 1)

        self.railwayGateValue13 = QLabel(self.railwayCrossingFrame13)
        self.railwayGateValue13.setObjectName(u"railwayGateValue13")
        self.railwayGateValue13.setFont(font1)
        self.railwayGateValue13.setAlignment(Qt.AlignCenter)

        self.gridLayout_57.addWidget(self.railwayGateValue13, 1, 1, 1, 1)

        self.railwayLightsLabel13 = QLabel(self.railwayCrossingFrame13)
        self.railwayLightsLabel13.setObjectName(u"railwayLightsLabel13")
        self.railwayLightsLabel13.setFont(font2)

        self.gridLayout_57.addWidget(self.railwayLightsLabel13, 2, 0, 1, 1)

        self.railwayLightsValue13 = QLabel(self.railwayCrossingFrame13)
        self.railwayLightsValue13.setObjectName(u"railwayLightsValue13")
        self.railwayLightsValue13.setFont(font1)
        self.railwayLightsValue13.setAlignment(Qt.AlignCenter)

        self.gridLayout_57.addWidget(self.railwayLightsValue13, 2, 1, 1, 1)


        self.gridLayout_55.addWidget(self.railwayCrossingFrame13, 1, 0, 2, 1)

        self.displayPLC13 = QTextBrowser(self.tab13Frame)
        self.displayPLC13.setObjectName(u"displayPLC13")
        self.displayPLC13.setFont(font3)

        self.gridLayout_55.addWidget(self.displayPLC13, 3, 0, 1, 5)

        self.trafficLightFrame13 = QFrame(self.tab13Frame)
        self.trafficLightFrame13.setObjectName(u"trafficLightFrame13")
        self.trafficLightFrame13.setAutoFillBackground(True)
        self.trafficLightFrame13.setFrameShape(QFrame.Box)
        self.trafficLightFrame13.setFrameShadow(QFrame.Raised)
        self.trafficLightFrame13.setLineWidth(1)
        self.trafficLightFrame13.setMidLineWidth(0)
        self.verticalLayout_111 = QVBoxLayout(self.trafficLightFrame13)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.trafficLightLabel13 = QLabel(self.trafficLightFrame13)
        self.trafficLightLabel13.setObjectName(u"trafficLightLabel13")
        self.trafficLightLabel13.setFont(font1)
        self.trafficLightLabel13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_111.addWidget(self.trafficLightLabel13)

        self.trafficLightValue13 = QLabel(self.trafficLightFrame13)
        self.trafficLightValue13.setObjectName(u"trafficLightValue13")
        self.trafficLightValue13.setFont(font1)
        self.trafficLightValue13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_111.addWidget(self.trafficLightValue13)


        self.gridLayout_55.addWidget(self.trafficLightFrame13, 2, 4, 1, 1)

        self.commandedSpeedFrame13 = QFrame(self.tab13Frame)
        self.commandedSpeedFrame13.setObjectName(u"commandedSpeedFrame13")
        self.commandedSpeedFrame13.setAutoFillBackground(True)
        self.commandedSpeedFrame13.setFrameShape(QFrame.Box)
        self.commandedSpeedFrame13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.commandedSpeedFrame13)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.commandedSpeedLabel13 = QLabel(self.commandedSpeedFrame13)
        self.commandedSpeedLabel13.setObjectName(u"commandedSpeedLabel13")
        self.commandedSpeedLabel13.setFont(font1)
        self.commandedSpeedLabel13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_107.addWidget(self.commandedSpeedLabel13)

        self.commandedSpeedValue13 = QLabel(self.commandedSpeedFrame13)
        self.commandedSpeedValue13.setObjectName(u"commandedSpeedValue13")
        self.commandedSpeedValue13.setFont(font1)
        self.commandedSpeedValue13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_107.addWidget(self.commandedSpeedValue13)


        self.gridLayout_55.addWidget(self.commandedSpeedFrame13, 2, 3, 1, 1)

        self.statusFrame13 = QFrame(self.tab13Frame)
        self.statusFrame13.setObjectName(u"statusFrame13")
        self.statusFrame13.setAutoFillBackground(True)
        self.statusFrame13.setFrameShape(QFrame.Box)
        self.statusFrame13.setFrameShadow(QFrame.Raised)
        self.statusFrame13.setLineWidth(1)
        self.statusFrame13.setMidLineWidth(0)
        self.verticalLayout_113 = QVBoxLayout(self.statusFrame13)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.statusLabel13 = QLabel(self.statusFrame13)
        self.statusLabel13.setObjectName(u"statusLabel13")
        self.statusLabel13.setFont(font1)
        self.statusLabel13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_113.addWidget(self.statusLabel13)

        self.statusValue13 = QLabel(self.statusFrame13)
        self.statusValue13.setObjectName(u"statusValue13")
        self.statusValue13.setFont(font1)
        self.statusValue13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_113.addWidget(self.statusValue13)


        self.gridLayout_55.addWidget(self.statusFrame13, 1, 4, 1, 1)

        self.switchPositionFrame13 = QFrame(self.tab13Frame)
        self.switchPositionFrame13.setObjectName(u"switchPositionFrame13")
        self.switchPositionFrame13.setAutoFillBackground(True)
        self.switchPositionFrame13.setFrameShape(QFrame.Box)
        self.switchPositionFrame13.setFrameShadow(QFrame.Raised)
        self.switchPositionFrame13.setLineWidth(1)
        self.switchPositionFrame13.setMidLineWidth(0)
        self.gridLayout_56 = QGridLayout(self.switchPositionFrame13)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.switchPositionLabel13 = QLabel(self.switchPositionFrame13)
        self.switchPositionLabel13.setObjectName(u"switchPositionLabel13")
        self.switchPositionLabel13.setFont(font1)
        self.switchPositionLabel13.setAlignment(Qt.AlignCenter)

        self.gridLayout_56.addWidget(self.switchPositionLabel13, 0, 0, 1, 3)

        self.switchArrowLabel13 = QLabel(self.switchPositionFrame13)
        self.switchArrowLabel13.setObjectName(u"switchArrowLabel13")
        self.switchArrowLabel13.setFont(font1)
        self.switchArrowLabel13.setAlignment(Qt.AlignCenter)

        self.gridLayout_56.addWidget(self.switchArrowLabel13, 1, 1, 1, 1)

        self.switchFromValue13 = QLabel(self.switchPositionFrame13)
        self.switchFromValue13.setObjectName(u"switchFromValue13")
        self.switchFromValue13.setFont(font1)
        self.switchFromValue13.setAlignment(Qt.AlignCenter)

        self.gridLayout_56.addWidget(self.switchFromValue13, 1, 0, 1, 1)

        self.switchToValue13 = QLabel(self.switchPositionFrame13)
        self.switchToValue13.setObjectName(u"switchToValue13")
        self.switchToValue13.setFont(font1)
        self.switchToValue13.setAlignment(Qt.AlignCenter)

        self.gridLayout_56.addWidget(self.switchToValue13, 1, 2, 1, 1)

        self.switchButton13 = QPushButton(self.switchPositionFrame13)
        self.switchButton13.setObjectName(u"switchButton13")
        self.switchButton13.setEnabled(False)
        self.switchButton13.setFont(font2)

        self.gridLayout_56.addWidget(self.switchButton13, 2, 1, 1, 1)


        self.gridLayout_55.addWidget(self.switchPositionFrame13, 1, 1, 2, 1)


        self.gridLayout_58.addWidget(self.tab13Frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab13, "")
        self.tab14 = QWidget()
        self.tab14.setObjectName(u"tab14")
        self.gridLayout_62 = QGridLayout(self.tab14)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.tab14Frame = QFrame(self.tab14)
        self.tab14Frame.setObjectName(u"tab14Frame")
        self.tab14Frame.setFrameShape(QFrame.StyledPanel)
        self.tab14Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_59 = QGridLayout(self.tab14Frame)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.blockLabel14 = QLabel(self.tab14Frame)
        self.blockLabel14.setObjectName(u"blockLabel14")
        self.blockLabel14.setFont(font1)
        self.blockLabel14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_59.addWidget(self.blockLabel14, 0, 3, 1, 1)

        self.occupancyFrame14 = QFrame(self.tab14Frame)
        self.occupancyFrame14.setObjectName(u"occupancyFrame14")
        self.occupancyFrame14.setAutoFillBackground(True)
        self.occupancyFrame14.setFrameShape(QFrame.Box)
        self.occupancyFrame14.setFrameShadow(QFrame.Raised)
        self.occupancyFrame14.setLineWidth(1)
        self.occupancyFrame14.setMidLineWidth(0)
        self.verticalLayout_116 = QVBoxLayout(self.occupancyFrame14)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.occupancyLabel14 = QLabel(self.occupancyFrame14)
        self.occupancyLabel14.setObjectName(u"occupancyLabel14")
        self.occupancyLabel14.setFont(font1)
        self.occupancyLabel14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_116.addWidget(self.occupancyLabel14)

        self.occupancyValue14 = QLabel(self.occupancyFrame14)
        self.occupancyValue14.setObjectName(u"occupancyValue14")
        self.occupancyValue14.setFont(font1)
        self.occupancyValue14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_116.addWidget(self.occupancyValue14)


        self.gridLayout_59.addWidget(self.occupancyFrame14, 2, 2, 1, 1)

        self.authorityFrame14 = QFrame(self.tab14Frame)
        self.authorityFrame14.setObjectName(u"authorityFrame14")
        self.authorityFrame14.setAutoFillBackground(True)
        self.authorityFrame14.setFrameShape(QFrame.Box)
        self.authorityFrame14.setFrameShadow(QFrame.Raised)
        self.authorityFrame14.setLineWidth(1)
        self.authorityFrame14.setMidLineWidth(0)
        self.verticalLayout_117 = QVBoxLayout(self.authorityFrame14)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.authorityLabel14 = QLabel(self.authorityFrame14)
        self.authorityLabel14.setObjectName(u"authorityLabel14")
        self.authorityLabel14.setFont(font1)
        self.authorityLabel14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_117.addWidget(self.authorityLabel14)

        self.authorityValue14 = QLabel(self.authorityFrame14)
        self.authorityValue14.setObjectName(u"authorityValue14")
        self.authorityValue14.setFont(font1)
        self.authorityValue14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_117.addWidget(self.authorityValue14)


        self.gridLayout_59.addWidget(self.authorityFrame14, 1, 2, 1, 1)

        self.uploadPLC14 = QPushButton(self.tab14Frame)
        self.uploadPLC14.setObjectName(u"uploadPLC14")
        self.uploadPLC14.setFont(font1)

        self.gridLayout_59.addWidget(self.uploadPLC14, 4, 4, 1, 1)

        self.suggestedSpeedFrame14 = QFrame(self.tab14Frame)
        self.suggestedSpeedFrame14.setObjectName(u"suggestedSpeedFrame14")
        self.suggestedSpeedFrame14.setAutoFillBackground(True)
        self.suggestedSpeedFrame14.setFrameShape(QFrame.Box)
        self.suggestedSpeedFrame14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_119 = QVBoxLayout(self.suggestedSpeedFrame14)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.suggestedSpeedLabel14 = QLabel(self.suggestedSpeedFrame14)
        self.suggestedSpeedLabel14.setObjectName(u"suggestedSpeedLabel14")
        self.suggestedSpeedLabel14.setFont(font1)
        self.suggestedSpeedLabel14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_119.addWidget(self.suggestedSpeedLabel14)

        self.suggestedSpeedValue14 = QLabel(self.suggestedSpeedFrame14)
        self.suggestedSpeedValue14.setObjectName(u"suggestedSpeedValue14")
        self.suggestedSpeedValue14.setFont(font1)
        self.suggestedSpeedValue14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_119.addWidget(self.suggestedSpeedValue14)


        self.gridLayout_59.addWidget(self.suggestedSpeedFrame14, 1, 3, 1, 1)

        self.trackLabel14 = QLabel(self.tab14Frame)
        self.trackLabel14.setObjectName(u"trackLabel14")
        self.trackLabel14.setFont(font1)
        self.trackLabel14.setAlignment(Qt.AlignCenter)

        self.gridLayout_59.addWidget(self.trackLabel14, 0, 0, 1, 1)

        self.blockSelect14 = QComboBox(self.tab14Frame)
        self.blockSelect14.setObjectName(u"blockSelect14")
        self.blockSelect14.setEnabled(True)
        self.blockSelect14.setFont(font1)
        self.blockSelect14.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout_59.addWidget(self.blockSelect14, 0, 4, 1, 1)

        self.railwayCrossingFrame14 = QFrame(self.tab14Frame)
        self.railwayCrossingFrame14.setObjectName(u"railwayCrossingFrame14")
        self.railwayCrossingFrame14.setAutoFillBackground(True)
        self.railwayCrossingFrame14.setFrameShape(QFrame.Box)
        self.railwayCrossingFrame14.setFrameShadow(QFrame.Raised)
        self.railwayCrossingFrame14.setLineWidth(1)
        self.railwayCrossingFrame14.setMidLineWidth(0)
        self.gridLayout_61 = QGridLayout(self.railwayCrossingFrame14)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.railwayCrossingLabel14 = QLabel(self.railwayCrossingFrame14)
        self.railwayCrossingLabel14.setObjectName(u"railwayCrossingLabel14")
        self.railwayCrossingLabel14.setFont(font1)
        self.railwayCrossingLabel14.setAlignment(Qt.AlignCenter)

        self.gridLayout_61.addWidget(self.railwayCrossingLabel14, 0, 0, 1, 2)

        self.railwayGateLabel14 = QLabel(self.railwayCrossingFrame14)
        self.railwayGateLabel14.setObjectName(u"railwayGateLabel14")
        self.railwayGateLabel14.setFont(font2)

        self.gridLayout_61.addWidget(self.railwayGateLabel14, 1, 0, 1, 1)

        self.railwayGateValue14 = QLabel(self.railwayCrossingFrame14)
        self.railwayGateValue14.setObjectName(u"railwayGateValue14")
        self.railwayGateValue14.setFont(font1)
        self.railwayGateValue14.setAlignment(Qt.AlignCenter)

        self.gridLayout_61.addWidget(self.railwayGateValue14, 1, 1, 1, 1)

        self.railwayLightsLabel14 = QLabel(self.railwayCrossingFrame14)
        self.railwayLightsLabel14.setObjectName(u"railwayLightsLabel14")
        self.railwayLightsLabel14.setFont(font2)

        self.gridLayout_61.addWidget(self.railwayLightsLabel14, 2, 0, 1, 1)

        self.railwayLightsValue14 = QLabel(self.railwayCrossingFrame14)
        self.railwayLightsValue14.setObjectName(u"railwayLightsValue14")
        self.railwayLightsValue14.setFont(font1)
        self.railwayLightsValue14.setAlignment(Qt.AlignCenter)

        self.gridLayout_61.addWidget(self.railwayLightsValue14, 2, 1, 1, 1)


        self.gridLayout_59.addWidget(self.railwayCrossingFrame14, 1, 0, 2, 1)

        self.displayPLC14 = QTextBrowser(self.tab14Frame)
        self.displayPLC14.setObjectName(u"displayPLC14")
        self.displayPLC14.setFont(font3)

        self.gridLayout_59.addWidget(self.displayPLC14, 3, 0, 1, 5)

        self.trafficLightFrame14 = QFrame(self.tab14Frame)
        self.trafficLightFrame14.setObjectName(u"trafficLightFrame14")
        self.trafficLightFrame14.setAutoFillBackground(True)
        self.trafficLightFrame14.setFrameShape(QFrame.Box)
        self.trafficLightFrame14.setFrameShadow(QFrame.Raised)
        self.trafficLightFrame14.setLineWidth(1)
        self.trafficLightFrame14.setMidLineWidth(0)
        self.verticalLayout_118 = QVBoxLayout(self.trafficLightFrame14)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.trafficLightLabel14 = QLabel(self.trafficLightFrame14)
        self.trafficLightLabel14.setObjectName(u"trafficLightLabel14")
        self.trafficLightLabel14.setFont(font1)
        self.trafficLightLabel14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_118.addWidget(self.trafficLightLabel14)

        self.trafficLightValue14 = QLabel(self.trafficLightFrame14)
        self.trafficLightValue14.setObjectName(u"trafficLightValue14")
        self.trafficLightValue14.setFont(font1)
        self.trafficLightValue14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_118.addWidget(self.trafficLightValue14)


        self.gridLayout_59.addWidget(self.trafficLightFrame14, 2, 4, 1, 1)

        self.commandedSpeedFrame14 = QFrame(self.tab14Frame)
        self.commandedSpeedFrame14.setObjectName(u"commandedSpeedFrame14")
        self.commandedSpeedFrame14.setAutoFillBackground(True)
        self.commandedSpeedFrame14.setFrameShape(QFrame.Box)
        self.commandedSpeedFrame14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.commandedSpeedFrame14)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.commandedSpeedLabel14 = QLabel(self.commandedSpeedFrame14)
        self.commandedSpeedLabel14.setObjectName(u"commandedSpeedLabel14")
        self.commandedSpeedLabel14.setFont(font1)
        self.commandedSpeedLabel14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_114.addWidget(self.commandedSpeedLabel14)

        self.commandedSpeedValue14 = QLabel(self.commandedSpeedFrame14)
        self.commandedSpeedValue14.setObjectName(u"commandedSpeedValue14")
        self.commandedSpeedValue14.setFont(font1)
        self.commandedSpeedValue14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_114.addWidget(self.commandedSpeedValue14)


        self.gridLayout_59.addWidget(self.commandedSpeedFrame14, 2, 3, 1, 1)

        self.statusFrame14 = QFrame(self.tab14Frame)
        self.statusFrame14.setObjectName(u"statusFrame14")
        self.statusFrame14.setAutoFillBackground(True)
        self.statusFrame14.setFrameShape(QFrame.Box)
        self.statusFrame14.setFrameShadow(QFrame.Raised)
        self.statusFrame14.setLineWidth(1)
        self.statusFrame14.setMidLineWidth(0)
        self.verticalLayout_120 = QVBoxLayout(self.statusFrame14)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.statusLabel14 = QLabel(self.statusFrame14)
        self.statusLabel14.setObjectName(u"statusLabel14")
        self.statusLabel14.setFont(font1)
        self.statusLabel14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_120.addWidget(self.statusLabel14)

        self.statusValue14 = QLabel(self.statusFrame14)
        self.statusValue14.setObjectName(u"statusValue14")
        self.statusValue14.setFont(font1)
        self.statusValue14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_120.addWidget(self.statusValue14)


        self.gridLayout_59.addWidget(self.statusFrame14, 1, 4, 1, 1)

        self.switchPositionFrame14 = QFrame(self.tab14Frame)
        self.switchPositionFrame14.setObjectName(u"switchPositionFrame14")
        self.switchPositionFrame14.setAutoFillBackground(True)
        self.switchPositionFrame14.setFrameShape(QFrame.Box)
        self.switchPositionFrame14.setFrameShadow(QFrame.Raised)
        self.switchPositionFrame14.setLineWidth(1)
        self.switchPositionFrame14.setMidLineWidth(0)
        self.gridLayout_60 = QGridLayout(self.switchPositionFrame14)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.switchToValue14 = QLabel(self.switchPositionFrame14)
        self.switchToValue14.setObjectName(u"switchToValue14")
        self.switchToValue14.setFont(font1)
        self.switchToValue14.setAlignment(Qt.AlignCenter)

        self.gridLayout_60.addWidget(self.switchToValue14, 1, 2, 1, 1)

        self.switchFromValue14 = QLabel(self.switchPositionFrame14)
        self.switchFromValue14.setObjectName(u"switchFromValue14")
        self.switchFromValue14.setFont(font1)
        self.switchFromValue14.setAlignment(Qt.AlignCenter)

        self.gridLayout_60.addWidget(self.switchFromValue14, 1, 0, 1, 1)

        self.switchArrowLabel14 = QLabel(self.switchPositionFrame14)
        self.switchArrowLabel14.setObjectName(u"switchArrowLabel14")
        self.switchArrowLabel14.setFont(font1)
        self.switchArrowLabel14.setAlignment(Qt.AlignCenter)

        self.gridLayout_60.addWidget(self.switchArrowLabel14, 1, 1, 1, 1)

        self.switchPositionLabel14 = QLabel(self.switchPositionFrame14)
        self.switchPositionLabel14.setObjectName(u"switchPositionLabel14")
        self.switchPositionLabel14.setFont(font1)
        self.switchPositionLabel14.setAlignment(Qt.AlignCenter)

        self.gridLayout_60.addWidget(self.switchPositionLabel14, 0, 0, 1, 3)

        self.switchButton14 = QPushButton(self.switchPositionFrame14)
        self.switchButton14.setObjectName(u"switchButton14")
        self.switchButton14.setEnabled(False)
        self.switchButton14.setFont(font2)

        self.gridLayout_60.addWidget(self.switchButton14, 2, 1, 1, 1)


        self.gridLayout_59.addWidget(self.switchPositionFrame14, 1, 1, 2, 1)


        self.gridLayout_62.addWidget(self.tab14Frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab14, "")
        self.tab15 = QWidget()
        self.tab15.setObjectName(u"tab15")
        self.gridLayout_2 = QGridLayout(self.tab15)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tab15Frame = QFrame(self.tab15)
        self.tab15Frame.setObjectName(u"tab15Frame")
        self.tab15Frame.setFrameShape(QFrame.StyledPanel)
        self.tab15Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_63 = QGridLayout(self.tab15Frame)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.blockLabel15 = QLabel(self.tab15Frame)
        self.blockLabel15.setObjectName(u"blockLabel15")
        self.blockLabel15.setFont(font1)
        self.blockLabel15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_63.addWidget(self.blockLabel15, 0, 3, 1, 1)

        self.occupancyFrame15 = QFrame(self.tab15Frame)
        self.occupancyFrame15.setObjectName(u"occupancyFrame15")
        self.occupancyFrame15.setAutoFillBackground(True)
        self.occupancyFrame15.setFrameShape(QFrame.Box)
        self.occupancyFrame15.setFrameShadow(QFrame.Raised)
        self.occupancyFrame15.setLineWidth(1)
        self.occupancyFrame15.setMidLineWidth(0)
        self.verticalLayout_123 = QVBoxLayout(self.occupancyFrame15)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.occupancyLabel15 = QLabel(self.occupancyFrame15)
        self.occupancyLabel15.setObjectName(u"occupancyLabel15")
        self.occupancyLabel15.setFont(font1)
        self.occupancyLabel15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_123.addWidget(self.occupancyLabel15)

        self.occupancyValue15 = QLabel(self.occupancyFrame15)
        self.occupancyValue15.setObjectName(u"occupancyValue15")
        self.occupancyValue15.setFont(font1)
        self.occupancyValue15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_123.addWidget(self.occupancyValue15)


        self.gridLayout_63.addWidget(self.occupancyFrame15, 2, 2, 1, 1)

        self.authorityFrame15 = QFrame(self.tab15Frame)
        self.authorityFrame15.setObjectName(u"authorityFrame15")
        self.authorityFrame15.setAutoFillBackground(True)
        self.authorityFrame15.setFrameShape(QFrame.Box)
        self.authorityFrame15.setFrameShadow(QFrame.Raised)
        self.authorityFrame15.setLineWidth(1)
        self.authorityFrame15.setMidLineWidth(0)
        self.verticalLayout_124 = QVBoxLayout(self.authorityFrame15)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.authorityLabel15 = QLabel(self.authorityFrame15)
        self.authorityLabel15.setObjectName(u"authorityLabel15")
        self.authorityLabel15.setFont(font1)
        self.authorityLabel15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_124.addWidget(self.authorityLabel15)

        self.authorityValue15 = QLabel(self.authorityFrame15)
        self.authorityValue15.setObjectName(u"authorityValue15")
        self.authorityValue15.setFont(font1)
        self.authorityValue15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_124.addWidget(self.authorityValue15)


        self.gridLayout_63.addWidget(self.authorityFrame15, 1, 2, 1, 1)

        self.uploadPLC14_2 = QPushButton(self.tab15Frame)
        self.uploadPLC14_2.setObjectName(u"uploadPLC14_2")
        self.uploadPLC14_2.setFont(font1)

        self.gridLayout_63.addWidget(self.uploadPLC14_2, 4, 4, 1, 1)

        self.suggestedSpeedFrame15 = QFrame(self.tab15Frame)
        self.suggestedSpeedFrame15.setObjectName(u"suggestedSpeedFrame15")
        self.suggestedSpeedFrame15.setAutoFillBackground(True)
        self.suggestedSpeedFrame15.setFrameShape(QFrame.Box)
        self.suggestedSpeedFrame15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_126 = QVBoxLayout(self.suggestedSpeedFrame15)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.suggestedSpeedLabel15 = QLabel(self.suggestedSpeedFrame15)
        self.suggestedSpeedLabel15.setObjectName(u"suggestedSpeedLabel15")
        self.suggestedSpeedLabel15.setFont(font1)
        self.suggestedSpeedLabel15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_126.addWidget(self.suggestedSpeedLabel15)

        self.suggestedSpeedValue15 = QLabel(self.suggestedSpeedFrame15)
        self.suggestedSpeedValue15.setObjectName(u"suggestedSpeedValue15")
        self.suggestedSpeedValue15.setFont(font1)
        self.suggestedSpeedValue15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_126.addWidget(self.suggestedSpeedValue15)


        self.gridLayout_63.addWidget(self.suggestedSpeedFrame15, 1, 3, 1, 1)

        self.trackLabel15 = QLabel(self.tab15Frame)
        self.trackLabel15.setObjectName(u"trackLabel15")
        self.trackLabel15.setFont(font1)
        self.trackLabel15.setAlignment(Qt.AlignCenter)

        self.gridLayout_63.addWidget(self.trackLabel15, 0, 0, 1, 1)

        self.blockSelect15 = QComboBox(self.tab15Frame)
        self.blockSelect15.setObjectName(u"blockSelect15")
        self.blockSelect15.setEnabled(True)
        self.blockSelect15.setFont(font1)
        self.blockSelect15.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout_63.addWidget(self.blockSelect15, 0, 4, 1, 1)

        self.railwayCrossingFrame15 = QFrame(self.tab15Frame)
        self.railwayCrossingFrame15.setObjectName(u"railwayCrossingFrame15")
        self.railwayCrossingFrame15.setAutoFillBackground(True)
        self.railwayCrossingFrame15.setFrameShape(QFrame.Box)
        self.railwayCrossingFrame15.setFrameShadow(QFrame.Raised)
        self.railwayCrossingFrame15.setLineWidth(1)
        self.railwayCrossingFrame15.setMidLineWidth(0)
        self.gridLayout_65 = QGridLayout(self.railwayCrossingFrame15)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.railwayCrossingLabel15 = QLabel(self.railwayCrossingFrame15)
        self.railwayCrossingLabel15.setObjectName(u"railwayCrossingLabel15")
        self.railwayCrossingLabel15.setFont(font1)
        self.railwayCrossingLabel15.setAlignment(Qt.AlignCenter)

        self.gridLayout_65.addWidget(self.railwayCrossingLabel15, 0, 0, 1, 2)

        self.railwayGateLabel15 = QLabel(self.railwayCrossingFrame15)
        self.railwayGateLabel15.setObjectName(u"railwayGateLabel15")
        self.railwayGateLabel15.setFont(font2)

        self.gridLayout_65.addWidget(self.railwayGateLabel15, 1, 0, 1, 1)

        self.railwayGateValue15 = QLabel(self.railwayCrossingFrame15)
        self.railwayGateValue15.setObjectName(u"railwayGateValue15")
        self.railwayGateValue15.setFont(font1)
        self.railwayGateValue15.setAlignment(Qt.AlignCenter)

        self.gridLayout_65.addWidget(self.railwayGateValue15, 1, 1, 1, 1)

        self.railwayLightsLabel15 = QLabel(self.railwayCrossingFrame15)
        self.railwayLightsLabel15.setObjectName(u"railwayLightsLabel15")
        self.railwayLightsLabel15.setFont(font2)

        self.gridLayout_65.addWidget(self.railwayLightsLabel15, 2, 0, 1, 1)

        self.railwayLightsValue15 = QLabel(self.railwayCrossingFrame15)
        self.railwayLightsValue15.setObjectName(u"railwayLightsValue15")
        self.railwayLightsValue15.setFont(font1)
        self.railwayLightsValue15.setAlignment(Qt.AlignCenter)

        self.gridLayout_65.addWidget(self.railwayLightsValue15, 2, 1, 1, 1)


        self.gridLayout_63.addWidget(self.railwayCrossingFrame15, 1, 0, 2, 1)

        self.displayPLC15 = QTextBrowser(self.tab15Frame)
        self.displayPLC15.setObjectName(u"displayPLC15")
        self.displayPLC15.setFont(font3)

        self.gridLayout_63.addWidget(self.displayPLC15, 3, 0, 1, 5)

        self.trafficLightFrame15 = QFrame(self.tab15Frame)
        self.trafficLightFrame15.setObjectName(u"trafficLightFrame15")
        self.trafficLightFrame15.setAutoFillBackground(True)
        self.trafficLightFrame15.setFrameShape(QFrame.Box)
        self.trafficLightFrame15.setFrameShadow(QFrame.Raised)
        self.trafficLightFrame15.setLineWidth(1)
        self.trafficLightFrame15.setMidLineWidth(0)
        self.verticalLayout_125 = QVBoxLayout(self.trafficLightFrame15)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.trafficLightLabel15 = QLabel(self.trafficLightFrame15)
        self.trafficLightLabel15.setObjectName(u"trafficLightLabel15")
        self.trafficLightLabel15.setFont(font1)
        self.trafficLightLabel15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_125.addWidget(self.trafficLightLabel15)

        self.trafficLightValue15 = QLabel(self.trafficLightFrame15)
        self.trafficLightValue15.setObjectName(u"trafficLightValue15")
        self.trafficLightValue15.setFont(font1)
        self.trafficLightValue15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_125.addWidget(self.trafficLightValue15)


        self.gridLayout_63.addWidget(self.trafficLightFrame15, 2, 4, 1, 1)

        self.commandedSpeedFrame15 = QFrame(self.tab15Frame)
        self.commandedSpeedFrame15.setObjectName(u"commandedSpeedFrame15")
        self.commandedSpeedFrame15.setAutoFillBackground(True)
        self.commandedSpeedFrame15.setFrameShape(QFrame.Box)
        self.commandedSpeedFrame15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_121 = QVBoxLayout(self.commandedSpeedFrame15)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.commandedSpeedLabel15 = QLabel(self.commandedSpeedFrame15)
        self.commandedSpeedLabel15.setObjectName(u"commandedSpeedLabel15")
        self.commandedSpeedLabel15.setFont(font1)
        self.commandedSpeedLabel15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_121.addWidget(self.commandedSpeedLabel15)

        self.commandedSpeedValue15 = QLabel(self.commandedSpeedFrame15)
        self.commandedSpeedValue15.setObjectName(u"commandedSpeedValue15")
        self.commandedSpeedValue15.setFont(font1)
        self.commandedSpeedValue15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_121.addWidget(self.commandedSpeedValue15)


        self.gridLayout_63.addWidget(self.commandedSpeedFrame15, 2, 3, 1, 1)

        self.statusFrame15 = QFrame(self.tab15Frame)
        self.statusFrame15.setObjectName(u"statusFrame15")
        self.statusFrame15.setAutoFillBackground(True)
        self.statusFrame15.setFrameShape(QFrame.Box)
        self.statusFrame15.setFrameShadow(QFrame.Raised)
        self.statusFrame15.setLineWidth(1)
        self.statusFrame15.setMidLineWidth(0)
        self.verticalLayout_127 = QVBoxLayout(self.statusFrame15)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.statusLabel15 = QLabel(self.statusFrame15)
        self.statusLabel15.setObjectName(u"statusLabel15")
        self.statusLabel15.setFont(font1)
        self.statusLabel15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_127.addWidget(self.statusLabel15)

        self.statusValue15 = QLabel(self.statusFrame15)
        self.statusValue15.setObjectName(u"statusValue15")
        self.statusValue15.setFont(font1)
        self.statusValue15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_127.addWidget(self.statusValue15)


        self.gridLayout_63.addWidget(self.statusFrame15, 1, 4, 1, 1)

        self.switchPositionFrame15 = QFrame(self.tab15Frame)
        self.switchPositionFrame15.setObjectName(u"switchPositionFrame15")
        self.switchPositionFrame15.setAutoFillBackground(True)
        self.switchPositionFrame15.setFrameShape(QFrame.Box)
        self.switchPositionFrame15.setFrameShadow(QFrame.Raised)
        self.switchPositionFrame15.setLineWidth(1)
        self.switchPositionFrame15.setMidLineWidth(0)
        self.gridLayout_64 = QGridLayout(self.switchPositionFrame15)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.switchFromValue15 = QLabel(self.switchPositionFrame15)
        self.switchFromValue15.setObjectName(u"switchFromValue15")
        self.switchFromValue15.setFont(font1)
        self.switchFromValue15.setAlignment(Qt.AlignCenter)

        self.gridLayout_64.addWidget(self.switchFromValue15, 1, 0, 1, 1)

        self.switchPositionLabel15 = QLabel(self.switchPositionFrame15)
        self.switchPositionLabel15.setObjectName(u"switchPositionLabel15")
        self.switchPositionLabel15.setFont(font1)
        self.switchPositionLabel15.setAlignment(Qt.AlignCenter)

        self.gridLayout_64.addWidget(self.switchPositionLabel15, 0, 0, 1, 3)

        self.switchArrowLabel15 = QLabel(self.switchPositionFrame15)
        self.switchArrowLabel15.setObjectName(u"switchArrowLabel15")
        self.switchArrowLabel15.setFont(font1)
        self.switchArrowLabel15.setAlignment(Qt.AlignCenter)

        self.gridLayout_64.addWidget(self.switchArrowLabel15, 1, 1, 1, 1)

        self.switchToValue15 = QLabel(self.switchPositionFrame15)
        self.switchToValue15.setObjectName(u"switchToValue15")
        self.switchToValue15.setFont(font1)
        self.switchToValue15.setAlignment(Qt.AlignCenter)

        self.gridLayout_64.addWidget(self.switchToValue15, 1, 2, 1, 1)

        self.switchButton15 = QPushButton(self.switchPositionFrame15)
        self.switchButton15.setObjectName(u"switchButton15")
        self.switchButton15.setEnabled(False)
        self.switchButton15.setFont(font2)

        self.gridLayout_64.addWidget(self.switchButton15, 2, 1, 1, 1)


        self.gridLayout_63.addWidget(self.switchPositionFrame15, 1, 1, 2, 1)


        self.gridLayout_2.addWidget(self.tab15Frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab15, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wayside Controller", None))
        self.trackLabel1.setText(QCoreApplication.translate("MainWindow", u"Track Line: Green", None))
        self.uploadPLC1.setText(QCoreApplication.translate("MainWindow", u"Upload PLC", None))
        self.railwayCrossingLabel1.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel1.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel1.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.authorityLabel1.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.authorityValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.suggestedSpeedLabel1.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.suggestedSpeedValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.blockLabel1.setText(QCoreApplication.translate("MainWindow", u"Block:", None))
        self.blockSelect1.setItemText(0, "")

        self.blockSelect1.setCurrentText("")
        self.trafficLightLabel1.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.occupancyLabel1.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.occupancyValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel1.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel1.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchFromValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchToValue1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchPositionLabel1.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchArrowLabel1.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.switchButton1.setText(QCoreApplication.translate("MainWindow", u"Move", None))
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
        self.blockSelect2.setCurrentText("")
        self.railwayCrossingLabel2.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel2.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel2.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trafficLightLabel2.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel2.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel2.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchPositionLabel2.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchArrowLabel2.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.switchToValue2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchFromValue2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchButton2.setText(QCoreApplication.translate("MainWindow", u"Move", None))
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
        self.blockSelect3.setCurrentText("")
        self.railwayCrossingLabel3.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel3.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel3.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trafficLightLabel3.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel3.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel3.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchFromValue3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchArrowLabel3.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.switchToValue3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchPositionLabel3.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchButton3.setText(QCoreApplication.translate("MainWindow", u"Move", None))
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
        self.blockSelect4.setCurrentText("")
        self.railwayCrossingLabel4.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel4.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel4.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trafficLightLabel4.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel4.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel4.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchFromValue4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchArrowLabel4.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.switchToValue4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchPositionLabel4.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchButton4.setText(QCoreApplication.translate("MainWindow", u"Move", None))
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
        self.blockSelect5.setCurrentText("")
        self.railwayCrossingLabel5.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel5.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel5.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trafficLightLabel5.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel5.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel5.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchPositionLabel5.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchFromValue5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchArrowLabel5.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.switchToValue5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchButton5.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), QCoreApplication.translate("MainWindow", u"Wayside 5", None))
        self.blockLabel6.setText(QCoreApplication.translate("MainWindow", u"Block:", None))
        self.occupancyLabel6.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.occupancyValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.authorityLabel6.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.authorityValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.uploadPLC6.setText(QCoreApplication.translate("MainWindow", u"Upload PLC", None))
        self.suggestedSpeedLabel6.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.suggestedSpeedValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trackLabel6.setText(QCoreApplication.translate("MainWindow", u"Track Line: Red", None))
        self.blockSelect6.setCurrentText("")
        self.railwayCrossingLabel6.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel6.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel6.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trafficLightLabel6.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel6.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel6.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchFromValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchPositionLabel6.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchToValue6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchArrowLabel6.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.switchButton6.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab6), QCoreApplication.translate("MainWindow", u"Wayside 6", None))
        self.blockLabel7.setText(QCoreApplication.translate("MainWindow", u"Block:", None))
        self.occupancyLabel7.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.occupancyValue7.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.authorityLabel7.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.authorityValue7.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.uploadPLC7.setText(QCoreApplication.translate("MainWindow", u"Upload PLC", None))
        self.suggestedSpeedLabel7.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.suggestedSpeedValue7.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trackLabel7.setText(QCoreApplication.translate("MainWindow", u"Track Line: Red", None))
        self.blockSelect7.setCurrentText("")
        self.railwayCrossingLabel7.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel7.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue7.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel7.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue7.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trafficLightLabel7.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue7.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel7.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue7.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel7.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue7.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchToValue7.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchArrowLabel7.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.switchPositionLabel7.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchFromValue7.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchButton7.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab7), QCoreApplication.translate("MainWindow", u"Wayside 7", None))
        self.blockLabel8.setText(QCoreApplication.translate("MainWindow", u"Block:", None))
        self.occupancyLabel8.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.occupancyValue8.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.authorityLabel8.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.authorityValue8.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.uploadPLC8.setText(QCoreApplication.translate("MainWindow", u"Upload PLC", None))
        self.suggestedSpeedLabel8.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.suggestedSpeedValue8.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trackLabel8.setText(QCoreApplication.translate("MainWindow", u"Track Line: Red", None))
        self.blockSelect8.setCurrentText("")
        self.railwayCrossingLabel8.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel8.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue8.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel8.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue8.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trafficLightLabel8.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue8.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel8.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue8.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel8.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue8.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchToValue8.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchArrowLabel8.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.switchPositionLabel8.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchFromValue8.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchButton8.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab8), QCoreApplication.translate("MainWindow", u"Wayside 8", None))
        self.blockLabel9.setText(QCoreApplication.translate("MainWindow", u"Block:", None))
        self.occupancyLabel9.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.occupancyValue9.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.authorityLabel9.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.authorityValue9.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.uploadPLC9.setText(QCoreApplication.translate("MainWindow", u"Upload PLC", None))
        self.suggestedSpeedLabel9.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.suggestedSpeedValue9.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trackLabel9.setText(QCoreApplication.translate("MainWindow", u"Track Line: Red", None))
        self.blockSelect9.setCurrentText("")
        self.railwayCrossingLabel9.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel9.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue9.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel9.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue9.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trafficLightLabel9.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue9.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel9.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue9.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel9.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue9.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchPositionLabel9.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchArrowLabel9.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.switchFromValue9.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchToValue9.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchButton9.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab9), QCoreApplication.translate("MainWindow", u"Wayside 9", None))
        self.blockLabel10.setText(QCoreApplication.translate("MainWindow", u"Block:", None))
        self.occupancyLabel10.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.occupancyValue10.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.authorityLabel10.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.authorityValue10.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.uploadPLC10.setText(QCoreApplication.translate("MainWindow", u"Upload PLC", None))
        self.suggestedSpeedLabel10.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.suggestedSpeedValue10.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trackLabel10.setText(QCoreApplication.translate("MainWindow", u"Track Line: Red", None))
        self.blockSelect10.setCurrentText("")
        self.railwayCrossingLabel10.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel10.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue10.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel10.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue10.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trafficLightLabel10.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue10.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel10.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue10.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel10.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue10.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchPositionLabel10.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchFromValue10.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchArrowLabel10.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.switchToValue10.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchButton10.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab10), QCoreApplication.translate("MainWindow", u"Wayside 10", None))
        self.blockLabel11.setText(QCoreApplication.translate("MainWindow", u"Block:", None))
        self.occupancyLabel11.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.occupancyValue11.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.authorityLabel11.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.authorityValue11.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.uploadPLC11.setText(QCoreApplication.translate("MainWindow", u"Upload PLC", None))
        self.suggestedSpeedLabel11.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.suggestedSpeedValue11.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trackLabel11.setText(QCoreApplication.translate("MainWindow", u"Track Line: Red", None))
        self.blockSelect11.setCurrentText("")
        self.railwayCrossingLabel11.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel11.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue11.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel11.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue11.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trafficLightLabel11.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue11.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel11.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue11.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel11.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue11.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchPositionLabel11.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchFromValue11.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchToValue11.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchArrowLabel11.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab11), QCoreApplication.translate("MainWindow", u"Wayside 11", None))
        self.blockLabel12.setText(QCoreApplication.translate("MainWindow", u"Block:", None))
        self.occupancyLabel12.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.occupancyValue12.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.authorityLabel12.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.authorityValue12.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.uploadPLC12.setText(QCoreApplication.translate("MainWindow", u"Upload PLC", None))
        self.suggestedSpeedLabel12.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.suggestedSpeedValue12.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trackLabel12.setText(QCoreApplication.translate("MainWindow", u"Track Line: Red", None))
        self.blockSelect12.setCurrentText("")
        self.railwayCrossingLabel12.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel12.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue12.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel12.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue12.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trafficLightLabel12.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue12.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel12.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue12.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel12.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue12.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchToValue12.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchPositionLabel12.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchArrowLabel12.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.switchFromValue12.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab12), QCoreApplication.translate("MainWindow", u"Wayside 12", None))
        self.blockLabel13.setText(QCoreApplication.translate("MainWindow", u"Block:", None))
        self.occupancyLabel13.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.occupancyValue13.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.authorityLabel13.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.authorityValue13.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.uploadPLC13.setText(QCoreApplication.translate("MainWindow", u"Upload PLC", None))
        self.suggestedSpeedLabel13.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.suggestedSpeedValue13.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trackLabel13.setText(QCoreApplication.translate("MainWindow", u"Track Line: Red", None))
        self.blockSelect13.setCurrentText("")
        self.railwayCrossingLabel13.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel13.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue13.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel13.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue13.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trafficLightLabel13.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue13.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel13.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue13.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel13.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue13.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchPositionLabel13.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchArrowLabel13.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.switchFromValue13.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchToValue13.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchButton13.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab13), QCoreApplication.translate("MainWindow", u"Wayside 13", None))
        self.blockLabel14.setText(QCoreApplication.translate("MainWindow", u"Block:", None))
        self.occupancyLabel14.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.occupancyValue14.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.authorityLabel14.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.authorityValue14.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.uploadPLC14.setText(QCoreApplication.translate("MainWindow", u"Upload PLC", None))
        self.suggestedSpeedLabel14.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.suggestedSpeedValue14.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trackLabel14.setText(QCoreApplication.translate("MainWindow", u"Track Line: Red", None))
        self.blockSelect14.setCurrentText("")
        self.railwayCrossingLabel14.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel14.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue14.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel14.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue14.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trafficLightLabel14.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue14.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel14.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue14.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel14.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue14.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchToValue14.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchFromValue14.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchArrowLabel14.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.switchPositionLabel14.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchButton14.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab14), QCoreApplication.translate("MainWindow", u"Wayside 14", None))
        self.blockLabel15.setText(QCoreApplication.translate("MainWindow", u"Block:", None))
        self.occupancyLabel15.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.occupancyValue15.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.authorityLabel15.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.authorityValue15.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.uploadPLC14_2.setText(QCoreApplication.translate("MainWindow", u"Upload PLC", None))
        self.suggestedSpeedLabel15.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.suggestedSpeedValue15.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trackLabel15.setText(QCoreApplication.translate("MainWindow", u"Track Line: Red", None))
        self.blockSelect15.setCurrentText("")
        self.railwayCrossingLabel15.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.railwayGateLabel15.setText(QCoreApplication.translate("MainWindow", u"Gate:", None))
        self.railwayGateValue15.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.railwayLightsLabel15.setText(QCoreApplication.translate("MainWindow", u"Lights:", None))
        self.railwayLightsValue15.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trafficLightLabel15.setText(QCoreApplication.translate("MainWindow", u"Traffic Light Color", None))
        self.trafficLightValue15.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.commandedSpeedLabel15.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None))
        self.commandedSpeedValue15.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel15.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue15.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchFromValue15.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchPositionLabel15.setText(QCoreApplication.translate("MainWindow", u"Switch Position", None))
        self.switchArrowLabel15.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.switchToValue15.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.switchButton15.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab15), QCoreApplication.translate("MainWindow", u"Wayside 15", None))
    # retranslateUi

