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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1067, 510)
        self.verticalLayoutWidget = QWidget(Widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(310, 0, 151, 501))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.blockLineTitle = QLabel(self.verticalLayoutWidget)
        self.blockLineTitle.setObjectName(u"blockLineTitle")
        self.blockLineTitle.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setBold(True)
        self.blockLineTitle.setFont(font)

        self.verticalLayout.addWidget(self.blockLineTitle)

        self.blockLineInfo = QLabel(self.verticalLayoutWidget)
        self.blockLineInfo.setObjectName(u"blockLineInfo")
        self.blockLineInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.blockLineInfo)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.blockLineSection = QLabel(self.verticalLayoutWidget)
        self.blockLineSection.setObjectName(u"blockLineSection")
        self.blockLineSection.setMaximumSize(QSize(16777215, 20))
        self.blockLineSection.setFont(font)

        self.verticalLayout.addWidget(self.blockLineSection)

        self.blockSectionInfo = QLabel(self.verticalLayoutWidget)
        self.blockSectionInfo.setObjectName(u"blockSectionInfo")
        self.blockSectionInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.blockSectionInfo)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.blockNumTitle = QLabel(self.verticalLayoutWidget)
        self.blockNumTitle.setObjectName(u"blockNumTitle")
        self.blockNumTitle.setMaximumSize(QSize(16777215, 20))
        self.blockNumTitle.setFont(font)

        self.verticalLayout.addWidget(self.blockNumTitle)

        self.blockNumberInfo = QLabel(self.verticalLayoutWidget)
        self.blockNumberInfo.setObjectName(u"blockNumberInfo")
        self.blockNumberInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.blockNumberInfo)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.blockGradeTitle = QLabel(self.verticalLayoutWidget)
        self.blockGradeTitle.setObjectName(u"blockGradeTitle")
        self.blockGradeTitle.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle.setFont(font)

        self.verticalLayout.addWidget(self.blockGradeTitle)

        self.blockGradeInfo = QLabel(self.verticalLayoutWidget)
        self.blockGradeInfo.setObjectName(u"blockGradeInfo")
        self.blockGradeInfo.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout.addWidget(self.blockGradeInfo)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.blockGradeTitle_2 = QLabel(self.verticalLayoutWidget)
        self.blockGradeTitle_2.setObjectName(u"blockGradeTitle_2")
        self.blockGradeTitle_2.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle_2.setFont(font)

        self.verticalLayout.addWidget(self.blockGradeTitle_2)

        self.blockSpeedLimitInfo = QLabel(self.verticalLayoutWidget)
        self.blockSpeedLimitInfo.setObjectName(u"blockSpeedLimitInfo")
        self.blockSpeedLimitInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.blockSpeedLimitInfo)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.blockGradeTitle_3 = QLabel(self.verticalLayoutWidget)
        self.blockGradeTitle_3.setObjectName(u"blockGradeTitle_3")
        self.blockGradeTitle_3.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle_3.setFont(font)

        self.verticalLayout.addWidget(self.blockGradeTitle_3)

        self.blockLengthInfo = QLabel(self.verticalLayoutWidget)
        self.blockLengthInfo.setObjectName(u"blockLengthInfo")
        self.blockLengthInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.blockLengthInfo)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.blockGradeTitle_4 = QLabel(self.verticalLayoutWidget)
        self.blockGradeTitle_4.setObjectName(u"blockGradeTitle_4")
        self.blockGradeTitle_4.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle_4.setFont(font)
        self.blockGradeTitle_4.setLineWidth(1)
        self.blockGradeTitle_4.setMidLineWidth(0)
        self.blockGradeTitle_4.setMargin(0)

        self.verticalLayout.addWidget(self.blockGradeTitle_4)

        self.blockStationInfo = QLabel(self.verticalLayoutWidget)
        self.blockStationInfo.setObjectName(u"blockStationInfo")
        self.blockStationInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.blockStationInfo)

        self.blockGradeTitle_26 = QLabel(self.verticalLayoutWidget)
        self.blockGradeTitle_26.setObjectName(u"blockGradeTitle_26")
        self.blockGradeTitle_26.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle_26.setFont(font)

        self.verticalLayout.addWidget(self.blockGradeTitle_26)

        self.blockTrackHeaterInfo = QLabel(self.verticalLayoutWidget)
        self.blockTrackHeaterInfo.setObjectName(u"blockTrackHeaterInfo")
        self.blockTrackHeaterInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.blockTrackHeaterInfo)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayoutWidget_2 = QWidget(Widget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 40, 311, 461))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.blockListTreeWidget = QTreeWidget(self.verticalLayoutWidget_2)
        self.blockListTreeWidget.setObjectName(u"blockListTreeWidget")
        self.blockListTreeWidget.setEnabled(True)
        self.blockListTreeWidget.setWordWrap(False)
        self.blockListTreeWidget.header().setCascadingSectionResizes(False)
        self.blockListTreeWidget.header().setMinimumSectionSize(50)
        self.blockListTreeWidget.header().setDefaultSectionSize(100)

        self.horizontalLayout_5.addWidget(self.blockListTreeWidget)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayoutWidget = QWidget(Widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 61, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 0, 6, 0)
        self.temperatureSpinBox = QSpinBox(self.horizontalLayoutWidget)
        self.temperatureSpinBox.setObjectName(u"temperatureSpinBox")
        self.temperatureSpinBox.setValue(32)

        self.horizontalLayout_2.addWidget(self.temperatureSpinBox)

        self.horizontalLayoutWidget_2 = QWidget(Widget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(190, 0, 121, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.uploadTrackButton = QPushButton(self.horizontalLayoutWidget_2)
        self.uploadTrackButton.setObjectName(u"uploadTrackButton")

        self.horizontalLayout_3.addWidget(self.uploadTrackButton)

        self.horizontalLayoutWidget_3 = QWidget(Widget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(60, 0, 131, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.verticalLayoutWidget_3 = QWidget(Widget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(460, 0, 160, 501))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.blockGradeTitle_17 = QLabel(self.verticalLayoutWidget_3)
        self.blockGradeTitle_17.setObjectName(u"blockGradeTitle_17")
        self.blockGradeTitle_17.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle_17.setFont(font)
        self.blockGradeTitle_17.setLineWidth(1)
        self.blockGradeTitle_17.setMidLineWidth(0)
        self.blockGradeTitle_17.setMargin(0)

        self.verticalLayout_4.addWidget(self.blockGradeTitle_17)

        self.blockSwitchInfo = QLabel(self.verticalLayoutWidget_3)
        self.blockSwitchInfo.setObjectName(u"blockSwitchInfo")
        self.blockSwitchInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.blockSwitchInfo)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_14)

        self.blockGradeTitle_6 = QLabel(self.verticalLayoutWidget_3)
        self.blockGradeTitle_6.setObjectName(u"blockGradeTitle_6")
        self.blockGradeTitle_6.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle_6.setFont(font)

        self.verticalLayout_4.addWidget(self.blockGradeTitle_6)

        self.blockElevationInfo = QLabel(self.verticalLayoutWidget_3)
        self.blockElevationInfo.setObjectName(u"blockElevationInfo")
        self.blockElevationInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.blockElevationInfo)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_13)

        self.blockGradeTitle_5 = QLabel(self.verticalLayoutWidget_3)
        self.blockGradeTitle_5.setObjectName(u"blockGradeTitle_5")
        self.blockGradeTitle_5.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle_5.setFont(font)

        self.verticalLayout_4.addWidget(self.blockGradeTitle_5)

        self.blockCumulativeElevationInfo = QLabel(self.verticalLayoutWidget_3)
        self.blockCumulativeElevationInfo.setObjectName(u"blockCumulativeElevationInfo")
        self.blockCumulativeElevationInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.blockCumulativeElevationInfo)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_12)

        self.blockGradeTitle_18 = QLabel(self.verticalLayoutWidget_3)
        self.blockGradeTitle_18.setObjectName(u"blockGradeTitle_18")
        self.blockGradeTitle_18.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle_18.setFont(font)

        self.verticalLayout_4.addWidget(self.blockGradeTitle_18)

        self.blockRailCrossingInfo = QLabel(self.verticalLayoutWidget_3)
        self.blockRailCrossingInfo.setObjectName(u"blockRailCrossingInfo")
        self.blockRailCrossingInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.blockRailCrossingInfo)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_11)

        self.blockGradeTitle_20 = QLabel(self.verticalLayoutWidget_3)
        self.blockGradeTitle_20.setObjectName(u"blockGradeTitle_20")
        self.blockGradeTitle_20.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle_20.setFont(font)

        self.verticalLayout_4.addWidget(self.blockGradeTitle_20)

        self.blockUndergroundInfo = QLabel(self.verticalLayoutWidget_3)
        self.blockUndergroundInfo.setObjectName(u"blockUndergroundInfo")
        self.blockUndergroundInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.blockUndergroundInfo)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_10)

        self.blockGradeTitle_22 = QLabel(self.verticalLayoutWidget_3)
        self.blockGradeTitle_22.setObjectName(u"blockGradeTitle_22")
        self.blockGradeTitle_22.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle_22.setFont(font)

        self.verticalLayout_4.addWidget(self.blockGradeTitle_22)

        self.blockAuthorityInfo = QLabel(self.verticalLayoutWidget_3)
        self.blockAuthorityInfo.setObjectName(u"blockAuthorityInfo")
        self.blockAuthorityInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.blockAuthorityInfo)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_9)

        self.blockGradeTitle_24 = QLabel(self.verticalLayoutWidget_3)
        self.blockGradeTitle_24.setObjectName(u"blockGradeTitle_24")
        self.blockGradeTitle_24.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle_24.setFont(font)

        self.verticalLayout_4.addWidget(self.blockGradeTitle_24)

        self.blockMaintenanceModeInfo = QLabel(self.verticalLayoutWidget_3)
        self.blockMaintenanceModeInfo.setObjectName(u"blockMaintenanceModeInfo")
        self.blockMaintenanceModeInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.blockMaintenanceModeInfo)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.verticalLayoutWidget_4 = QWidget(Widget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(620, 0, 160, 501))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.blockGradeTitle_33 = QLabel(self.verticalLayoutWidget_4)
        self.blockGradeTitle_33.setObjectName(u"blockGradeTitle_33")
        self.blockGradeTitle_33.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle_33.setFont(font)
        self.blockGradeTitle_33.setLineWidth(1)
        self.blockGradeTitle_33.setMidLineWidth(0)
        self.blockGradeTitle_33.setMargin(0)

        self.verticalLayout_5.addWidget(self.blockGradeTitle_33)

        self.blockDirectionsOfTravel = QLabel(self.verticalLayoutWidget_4)
        self.blockDirectionsOfTravel.setObjectName(u"blockDirectionsOfTravel")
        self.blockDirectionsOfTravel.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.blockDirectionsOfTravel)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_19)

        self.blockGradeTitle_30 = QLabel(self.verticalLayoutWidget_4)
        self.blockGradeTitle_30.setObjectName(u"blockGradeTitle_30")
        self.blockGradeTitle_30.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle_30.setFont(font)
        self.blockGradeTitle_30.setLineWidth(1)
        self.blockGradeTitle_30.setMidLineWidth(0)
        self.blockGradeTitle_30.setMargin(0)

        self.verticalLayout_5.addWidget(self.blockGradeTitle_30)

        self.blockBeaconInfo = QLabel(self.verticalLayoutWidget_4)
        self.blockBeaconInfo.setObjectName(u"blockBeaconInfo")
        self.blockBeaconInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.blockBeaconInfo)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_15)

        self.blockGradeTitle_31 = QLabel(self.verticalLayoutWidget_4)
        self.blockGradeTitle_31.setObjectName(u"blockGradeTitle_31")
        self.blockGradeTitle_31.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle_31.setFont(font)
        self.blockGradeTitle_31.setLineWidth(1)
        self.blockGradeTitle_31.setMidLineWidth(0)
        self.blockGradeTitle_31.setMargin(0)

        self.verticalLayout_5.addWidget(self.blockGradeTitle_31)

        self.blockCommandedSpeedInfo = QLabel(self.verticalLayoutWidget_4)
        self.blockCommandedSpeedInfo.setObjectName(u"blockCommandedSpeedInfo")
        self.blockCommandedSpeedInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.blockCommandedSpeedInfo)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_20)

        self.blockGradeTitle_32 = QLabel(self.verticalLayoutWidget_4)
        self.blockGradeTitle_32.setObjectName(u"blockGradeTitle_32")
        self.blockGradeTitle_32.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle_32.setFont(font)

        self.verticalLayout_5.addWidget(self.blockGradeTitle_32)

        self.blockFailureModeInfo = QLabel(self.verticalLayoutWidget_4)
        self.blockFailureModeInfo.setObjectName(u"blockFailureModeInfo")
        self.blockFailureModeInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.blockFailureModeInfo)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_16)

        self.blockGradeTitle_34 = QLabel(self.verticalLayoutWidget_4)
        self.blockGradeTitle_34.setObjectName(u"blockGradeTitle_34")
        self.blockGradeTitle_34.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle_34.setFont(font)

        self.verticalLayout_5.addWidget(self.blockGradeTitle_34)

        self.blockSwitchPositionInfo = QLabel(self.verticalLayoutWidget_4)
        self.blockSwitchPositionInfo.setObjectName(u"blockSwitchPositionInfo")
        self.blockSwitchPositionInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.blockSwitchPositionInfo)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_17)

        self.blockGradeTitle_36 = QLabel(self.verticalLayoutWidget_4)
        self.blockGradeTitle_36.setObjectName(u"blockGradeTitle_36")
        self.blockGradeTitle_36.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle_36.setFont(font)

        self.verticalLayout_5.addWidget(self.blockGradeTitle_36)

        self.blockSignalInfo = QLabel(self.verticalLayoutWidget_4)
        self.blockSignalInfo.setObjectName(u"blockSignalInfo")
        self.blockSignalInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.blockSignalInfo)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_18)

        self.blockGradeTitle_38 = QLabel(self.verticalLayoutWidget_4)
        self.blockGradeTitle_38.setObjectName(u"blockGradeTitle_38")
        self.blockGradeTitle_38.setMaximumSize(QSize(16777215, 20))
        self.blockGradeTitle_38.setFont(font)

        self.verticalLayout_5.addWidget(self.blockGradeTitle_38)

        self.blockTrackCircuitInfo = QLabel(self.verticalLayoutWidget_4)
        self.blockTrackCircuitInfo.setObjectName(u"blockTrackCircuitInfo")
        self.blockTrackCircuitInfo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.blockTrackCircuitInfo)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_21)

        self.verticalLayoutWidget_5 = QWidget(Widget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(780, 0, 281, 311))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stationTree = QTreeWidget(self.verticalLayoutWidget_5)
        __qtreewidgetitem = QTreeWidgetItem(self.stationTree)
        __qtreewidgetitem.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsEnabled);
        self.stationTree.setObjectName(u"stationTree")

        self.verticalLayout_3.addWidget(self.stationTree)

        self.verticalLayoutWidget_6 = QWidget(Widget)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(780, 310, 281, 191))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.switchPosTree = QTreeWidget(self.verticalLayoutWidget_6)
        self.switchPosTree.headerItem().setText(3, "")
        __qtreewidgetitem1 = QTreeWidgetItem(self.switchPosTree)
        __qtreewidgetitem1.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsEnabled);
        self.switchPosTree.setObjectName(u"switchPosTree")

        self.verticalLayout_6.addWidget(self.switchPosTree)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.blockLineTitle.setText(QCoreApplication.translate("Widget", u"Line", None))
        self.blockLineInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockLineSection.setText(QCoreApplication.translate("Widget", u"Section", None))
        self.blockSectionInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockNumTitle.setText(QCoreApplication.translate("Widget", u"Block Number", None))
        self.blockNumberInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockGradeTitle.setText(QCoreApplication.translate("Widget", u"Block Grade", None))
        self.blockGradeInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockGradeTitle_2.setText(QCoreApplication.translate("Widget", u"Speed Limit", None))
        self.blockSpeedLimitInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockGradeTitle_3.setText(QCoreApplication.translate("Widget", u"Block Length", None))
        self.blockLengthInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockGradeTitle_4.setText(QCoreApplication.translate("Widget", u"Station", None))
        self.blockStationInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockGradeTitle_26.setText(QCoreApplication.translate("Widget", u"Track Heater", None))
        self.blockTrackHeaterInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        ___qtreewidgetitem = self.blockListTreeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Widget", u"Occupancy", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Widget", u"Signal", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Widget", u"Track", None));
        self.uploadTrackButton.setText(QCoreApplication.translate("Widget", u"Upload Track", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Temperature \u00b0F", None))
        self.blockGradeTitle_17.setText(QCoreApplication.translate("Widget", u"Switch", None))
        self.blockSwitchInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockGradeTitle_6.setText(QCoreApplication.translate("Widget", u"Elevation", None))
        self.blockElevationInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockGradeTitle_5.setText(QCoreApplication.translate("Widget", u"Cumulative Elevation", None))
        self.blockCumulativeElevationInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockGradeTitle_18.setText(QCoreApplication.translate("Widget", u"Rail Crossing", None))
        self.blockRailCrossingInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockGradeTitle_20.setText(QCoreApplication.translate("Widget", u"Underground", None))
        self.blockUndergroundInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockGradeTitle_22.setText(QCoreApplication.translate("Widget", u"Authority", None))
        self.blockAuthorityInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockGradeTitle_24.setText(QCoreApplication.translate("Widget", u"Maintenance Mode", None))
        self.blockMaintenanceModeInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockGradeTitle_33.setText(QCoreApplication.translate("Widget", u"Directions of Travel", None))
        self.blockDirectionsOfTravel.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockGradeTitle_30.setText(QCoreApplication.translate("Widget", u"Beacon", None))
        self.blockBeaconInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockGradeTitle_31.setText(QCoreApplication.translate("Widget", u"Commanded Speed", None))
        self.blockCommandedSpeedInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockGradeTitle_32.setText(QCoreApplication.translate("Widget", u"Failure Mode", None))
        self.blockFailureModeInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockGradeTitle_34.setText(QCoreApplication.translate("Widget", u"Switch Position", None))
        self.blockSwitchPositionInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockGradeTitle_36.setText(QCoreApplication.translate("Widget", u"Signal", None))
        self.blockSignalInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        self.blockGradeTitle_38.setText(QCoreApplication.translate("Widget", u"Track Circuit", None))
        self.blockTrackCircuitInfo.setText(QCoreApplication.translate("Widget", u"-", None))
        ___qtreewidgetitem1 = self.stationTree.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("Widget", u"Deboarded", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Widget", u"Waiting", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Widget", u"Station", None));

        __sortingEnabled = self.stationTree.isSortingEnabled()
        self.stationTree.setSortingEnabled(False)
        self.stationTree.setSortingEnabled(__sortingEnabled)

        ___qtreewidgetitem2 = self.switchPosTree.headerItem()
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("Widget", u"Block 2", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("Widget", u"Block 1", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Widget", u"Switch", None));

        __sortingEnabled1 = self.switchPosTree.isSortingEnabled()
        self.switchPosTree.setSortingEnabled(False)
        self.switchPosTree.setSortingEnabled(__sortingEnabled1)

    # retranslateUi

