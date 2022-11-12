# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ctcOfficeTestLayout.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_CTCOffice_Testing(object):
    def setupUi(self, CTCOffice_Testing):
        if not CTCOffice_Testing.objectName():
            CTCOffice_Testing.setObjectName(u"CTCOffice_Testing")
        CTCOffice_Testing.resize(449, 300)
        self.horizontalLayout_18 = QHBoxLayout(CTCOffice_Testing)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(CTCOffice_Testing)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(CTCOffice_Testing)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.comboBox_occupancy_Line = QComboBox(CTCOffice_Testing)
        self.comboBox_occupancy_Line.addItem("")
        self.comboBox_occupancy_Line.addItem("")
        self.comboBox_occupancy_Line.addItem("")
        self.comboBox_occupancy_Line.setObjectName(u"comboBox_occupancy_Line")

        self.horizontalLayout.addWidget(self.comboBox_occupancy_Line)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(CTCOffice_Testing)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.comboBox_occupancy_blockNumber = QComboBox(CTCOffice_Testing)
        self.comboBox_occupancy_blockNumber.setObjectName(u"comboBox_occupancy_blockNumber")

        self.horizontalLayout_3.addWidget(self.comboBox_occupancy_blockNumber)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(CTCOffice_Testing)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.comboBox_occupancy_status = QComboBox(CTCOffice_Testing)
        self.comboBox_occupancy_status.addItem("")
        self.comboBox_occupancy_status.addItem("")
        self.comboBox_occupancy_status.setObjectName(u"comboBox_occupancy_status")

        self.horizontalLayout_4.addWidget(self.comboBox_occupancy_status)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.pushButton_trackOccupancy = QPushButton(CTCOffice_Testing)
        self.pushButton_trackOccupancy.setObjectName(u"pushButton_trackOccupancy")

        self.verticalLayout.addWidget(self.pushButton_trackOccupancy)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(CTCOffice_Testing)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_2.addWidget(self.label_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_10 = QLabel(CTCOffice_Testing)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_5.addWidget(self.label_10)

        self.comboBox_crossing_line = QComboBox(CTCOffice_Testing)
        self.comboBox_crossing_line.addItem("")
        self.comboBox_crossing_line.addItem("")
        self.comboBox_crossing_line.addItem("")
        self.comboBox_crossing_line.setObjectName(u"comboBox_crossing_line")

        self.horizontalLayout_5.addWidget(self.comboBox_crossing_line)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_11 = QLabel(CTCOffice_Testing)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_7.addWidget(self.label_11)

        self.comboBox_crossing_blockNumber = QComboBox(CTCOffice_Testing)
        self.comboBox_crossing_blockNumber.setObjectName(u"comboBox_crossing_blockNumber")

        self.horizontalLayout_7.addWidget(self.comboBox_crossing_blockNumber)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(CTCOffice_Testing)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.comboBox_crossing_status = QComboBox(CTCOffice_Testing)
        self.comboBox_crossing_status.addItem("")
        self.comboBox_crossing_status.addItem("")
        self.comboBox_crossing_status.setObjectName(u"comboBox_crossing_status")

        self.horizontalLayout_8.addWidget(self.comboBox_crossing_status)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.pushButton_crossing = QPushButton(CTCOffice_Testing)
        self.pushButton_crossing.setObjectName(u"pushButton_crossing")

        self.verticalLayout_2.addWidget(self.pushButton_crossing)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)


        self.horizontalLayout_18.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_13 = QLabel(CTCOffice_Testing)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.verticalLayout_3.addWidget(self.label_13)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_14 = QLabel(CTCOffice_Testing)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_9.addWidget(self.label_14)

        self.comboBox_trackFailure_line = QComboBox(CTCOffice_Testing)
        self.comboBox_trackFailure_line.addItem("")
        self.comboBox_trackFailure_line.addItem("")
        self.comboBox_trackFailure_line.addItem("")
        self.comboBox_trackFailure_line.setObjectName(u"comboBox_trackFailure_line")

        self.horizontalLayout_9.addWidget(self.comboBox_trackFailure_line)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_15 = QLabel(CTCOffice_Testing)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_11.addWidget(self.label_15)

        self.comboBox_trackFailure_blockNumber = QComboBox(CTCOffice_Testing)
        self.comboBox_trackFailure_blockNumber.setObjectName(u"comboBox_trackFailure_blockNumber")

        self.horizontalLayout_11.addWidget(self.comboBox_trackFailure_blockNumber)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_16 = QLabel(CTCOffice_Testing)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_12.addWidget(self.label_16)

        self.comboBox_trackFailure_status = QComboBox(CTCOffice_Testing)
        self.comboBox_trackFailure_status.addItem("")
        self.comboBox_trackFailure_status.addItem("")
        self.comboBox_trackFailure_status.addItem("")
        self.comboBox_trackFailure_status.addItem("")
        self.comboBox_trackFailure_status.setObjectName(u"comboBox_trackFailure_status")

        self.horizontalLayout_12.addWidget(self.comboBox_trackFailure_status)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.pushButton_trackFailure = QPushButton(CTCOffice_Testing)
        self.pushButton_trackFailure.setObjectName(u"pushButton_trackFailure")

        self.verticalLayout_3.addWidget(self.pushButton_trackFailure)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_21 = QLabel(CTCOffice_Testing)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.verticalLayout_5.addWidget(self.label_21)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_22 = QLabel(CTCOffice_Testing)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_17.addWidget(self.label_22)

        self.comboBox_setThroughput_line = QComboBox(CTCOffice_Testing)
        self.comboBox_setThroughput_line.addItem("")
        self.comboBox_setThroughput_line.addItem("")
        self.comboBox_setThroughput_line.addItem("")
        self.comboBox_setThroughput_line.setObjectName(u"comboBox_setThroughput_line")

        self.horizontalLayout_17.addWidget(self.comboBox_setThroughput_line)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_24 = QLabel(CTCOffice_Testing)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_19.addWidget(self.label_24)

        self.spinBox_setThroughput_throughput = QSpinBox(CTCOffice_Testing)
        self.spinBox_setThroughput_throughput.setObjectName(u"spinBox_setThroughput_throughput")

        self.horizontalLayout_19.addWidget(self.spinBox_setThroughput_throughput)


        self.verticalLayout_5.addLayout(self.horizontalLayout_19)

        self.pushButton_throughput = QPushButton(CTCOffice_Testing)
        self.pushButton_throughput.setObjectName(u"pushButton_throughput")

        self.verticalLayout_5.addWidget(self.pushButton_throughput)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)


        self.horizontalLayout_18.addLayout(self.verticalLayout_7)


        self.retranslateUi(CTCOffice_Testing)

        QMetaObject.connectSlotsByName(CTCOffice_Testing)
    # setupUi

    def retranslateUi(self, CTCOffice_Testing):
        CTCOffice_Testing.setWindowTitle(QCoreApplication.translate("CTCOffice_Testing", u"CTC Office Test UI", None))
        self.label_5.setText(QCoreApplication.translate("CTCOffice_Testing", u"Set Track Occupancy", None))
        self.label_6.setText(QCoreApplication.translate("CTCOffice_Testing", u"Line", None))
        self.comboBox_occupancy_Line.setItemText(0, QCoreApplication.translate("CTCOffice_Testing", u"Blue", None))
        self.comboBox_occupancy_Line.setItemText(1, QCoreApplication.translate("CTCOffice_Testing", u"Red", None))
        self.comboBox_occupancy_Line.setItemText(2, QCoreApplication.translate("CTCOffice_Testing", u"Green", None))

        self.label_8.setText(QCoreApplication.translate("CTCOffice_Testing", u"Block Number", None))
        self.label_9.setText(QCoreApplication.translate("CTCOffice_Testing", u"Track Status", None))
        self.comboBox_occupancy_status.setItemText(0, QCoreApplication.translate("CTCOffice_Testing", u"Train", None))
        self.comboBox_occupancy_status.setItemText(1, QCoreApplication.translate("CTCOffice_Testing", u"No Train", None))

        self.pushButton_trackOccupancy.setText(QCoreApplication.translate("CTCOffice_Testing", u"Set Status", None))
        self.label_7.setText(QCoreApplication.translate("CTCOffice_Testing", u"Set Crossing", None))
        self.label_10.setText(QCoreApplication.translate("CTCOffice_Testing", u"Line", None))
        self.comboBox_crossing_line.setItemText(0, QCoreApplication.translate("CTCOffice_Testing", u"Blue", None))
        self.comboBox_crossing_line.setItemText(1, QCoreApplication.translate("CTCOffice_Testing", u"Red", None))
        self.comboBox_crossing_line.setItemText(2, QCoreApplication.translate("CTCOffice_Testing", u"Green", None))

        self.label_11.setText(QCoreApplication.translate("CTCOffice_Testing", u"Block Number", None))
        self.label_12.setText(QCoreApplication.translate("CTCOffice_Testing", u"Crossing Status", None))
        self.comboBox_crossing_status.setItemText(0, QCoreApplication.translate("CTCOffice_Testing", u"Inactive", None))
        self.comboBox_crossing_status.setItemText(1, QCoreApplication.translate("CTCOffice_Testing", u"Active", None))

        self.pushButton_crossing.setText(QCoreApplication.translate("CTCOffice_Testing", u"Set Status", None))
        self.label_13.setText(QCoreApplication.translate("CTCOffice_Testing", u"Set Track Failure", None))
        self.label_14.setText(QCoreApplication.translate("CTCOffice_Testing", u"Line", None))
        self.comboBox_trackFailure_line.setItemText(0, QCoreApplication.translate("CTCOffice_Testing", u"Blue", None))
        self.comboBox_trackFailure_line.setItemText(1, QCoreApplication.translate("CTCOffice_Testing", u"Red", None))
        self.comboBox_trackFailure_line.setItemText(2, QCoreApplication.translate("CTCOffice_Testing", u"Green", None))

        self.label_15.setText(QCoreApplication.translate("CTCOffice_Testing", u"Block Number", None))
        self.label_16.setText(QCoreApplication.translate("CTCOffice_Testing", u"Track Status", None))
        self.comboBox_trackFailure_status.setItemText(0, QCoreApplication.translate("CTCOffice_Testing", u"No Failure", None))
        self.comboBox_trackFailure_status.setItemText(1, QCoreApplication.translate("CTCOffice_Testing", u"Broken Rail", None))
        self.comboBox_trackFailure_status.setItemText(2, QCoreApplication.translate("CTCOffice_Testing", u"Track Circuit Fail", None))
        self.comboBox_trackFailure_status.setItemText(3, QCoreApplication.translate("CTCOffice_Testing", u"Power Failure", None))

        self.pushButton_trackFailure.setText(QCoreApplication.translate("CTCOffice_Testing", u"Set Status", None))
        self.label_21.setText(QCoreApplication.translate("CTCOffice_Testing", u"Set Throughput", None))
        self.label_22.setText(QCoreApplication.translate("CTCOffice_Testing", u"Line", None))
        self.comboBox_setThroughput_line.setItemText(0, QCoreApplication.translate("CTCOffice_Testing", u"Blue", None))
        self.comboBox_setThroughput_line.setItemText(1, QCoreApplication.translate("CTCOffice_Testing", u"Red", None))
        self.comboBox_setThroughput_line.setItemText(2, QCoreApplication.translate("CTCOffice_Testing", u"Green", None))

        self.label_24.setText(QCoreApplication.translate("CTCOffice_Testing", u"Throughput", None))
        self.pushButton_throughput.setText(QCoreApplication.translate("CTCOffice_Testing", u"Set Throughput", None))
    # retranslateUi

