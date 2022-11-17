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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_TrackModelTestUI(object):
    def setupUi(self, TrackModelTestUI):
        if not TrackModelTestUI.objectName():
            TrackModelTestUI.setObjectName(u"TrackModelTestUI")
        TrackModelTestUI.resize(423, 306)
        self.verticalLayoutWidget = QWidget(TrackModelTestUI)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 40, 141, 61))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.updateTypeDropdown = QComboBox(self.verticalLayoutWidget)
        self.updateTypeDropdown.addItem("")
        self.updateTypeDropdown.addItem("")
        self.updateTypeDropdown.addItem("")
        self.updateTypeDropdown.addItem("")
        self.updateTypeDropdown.addItem("")
        self.updateTypeDropdown.addItem("")
        self.updateTypeDropdown.addItem("")
        self.updateTypeDropdown.setObjectName(u"updateTypeDropdown")

        self.verticalLayout.addWidget(self.updateTypeDropdown)

        self.verticalLayoutWidget_4 = QWidget(TrackModelTestUI)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(140, 40, 141, 61))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_4.addWidget(self.label_4)

        self.lineDropDown = QComboBox(self.verticalLayoutWidget_4)
        self.lineDropDown.setObjectName(u"lineDropDown")

        self.verticalLayout_4.addWidget(self.lineDropDown)

        self.verticalLayoutWidget_5 = QWidget(TrackModelTestUI)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(280, 40, 141, 61))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_5.addWidget(self.label_5)

        self.blockDropDown = QComboBox(self.verticalLayoutWidget_5)
        self.blockDropDown.setObjectName(u"blockDropDown")

        self.verticalLayout_5.addWidget(self.blockDropDown)

        self.updateButton = QPushButton(TrackModelTestUI)
        self.updateButton.setObjectName(u"updateButton")
        self.updateButton.setGeometry(QRect(300, 130, 100, 32))
        self.verticalLayoutWidget_6 = QWidget(TrackModelTestUI)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(0, 100, 141, 61))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.updateValueLabel = QLabel(self.verticalLayoutWidget_6)
        self.updateValueLabel.setObjectName(u"updateValueLabel")
        self.updateValueLabel.setFont(font)

        self.verticalLayout_6.addWidget(self.updateValueLabel)

        self.inputValueDropdown = QComboBox(self.verticalLayoutWidget_6)
        self.inputValueDropdown.setObjectName(u"inputValueDropdown")
        self.inputValueDropdown.setEnabled(True)

        self.verticalLayout_6.addWidget(self.inputValueDropdown)

        self.verticalLayoutWidget_7 = QWidget(TrackModelTestUI)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(140, 100, 141, 61))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.updateValueSpinboxLabel = QLabel(self.verticalLayoutWidget_7)
        self.updateValueSpinboxLabel.setObjectName(u"updateValueSpinboxLabel")
        self.updateValueSpinboxLabel.setFont(font)

        self.verticalLayout_7.addWidget(self.updateValueSpinboxLabel)

        self.inputValueSpinBox = QSpinBox(self.verticalLayoutWidget_7)
        self.inputValueSpinBox.setObjectName(u"inputValueSpinBox")
        self.inputValueSpinBox.setWrapping(False)

        self.verticalLayout_7.addWidget(self.inputValueSpinBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.dispatchTrainButton = QPushButton(TrackModelTestUI)
        self.dispatchTrainButton.setObjectName(u"dispatchTrainButton")
        self.dispatchTrainButton.setGeometry(QRect(80, 230, 271, 32))
        self.dispatchTrainButton.setCheckable(True)

        self.retranslateUi(TrackModelTestUI)

        QMetaObject.connectSlotsByName(TrackModelTestUI)
    # setupUi

    def retranslateUi(self, TrackModelTestUI):
        TrackModelTestUI.setWindowTitle(QCoreApplication.translate("TrackModelTestUI", u"TrackModelTestUI", None))
        self.label.setText(QCoreApplication.translate("TrackModelTestUI", u"Update", None))
        self.updateTypeDropdown.setItemText(0, QCoreApplication.translate("TrackModelTestUI", u"Occupancy", None))
        self.updateTypeDropdown.setItemText(1, QCoreApplication.translate("TrackModelTestUI", u"Switch Position", None))
        self.updateTypeDropdown.setItemText(2, QCoreApplication.translate("TrackModelTestUI", u"Maintenance", None))
        self.updateTypeDropdown.setItemText(3, QCoreApplication.translate("TrackModelTestUI", u"Authority", None))
        self.updateTypeDropdown.setItemText(4, QCoreApplication.translate("TrackModelTestUI", u"Failure", None))
        self.updateTypeDropdown.setItemText(5, QCoreApplication.translate("TrackModelTestUI", u"Commanded Speed", None))
        self.updateTypeDropdown.setItemText(6, QCoreApplication.translate("TrackModelTestUI", u"Signal", None))

        self.label_4.setText(QCoreApplication.translate("TrackModelTestUI", u"Line", None))
        self.label_5.setText(QCoreApplication.translate("TrackModelTestUI", u"Block", None))
        self.updateButton.setText(QCoreApplication.translate("TrackModelTestUI", u"Send Update", None))
        self.updateValueLabel.setText("")
        self.updateValueSpinboxLabel.setText("")
        self.dispatchTrainButton.setText(QCoreApplication.translate("TrackModelTestUI", u"Dispatch Train from Yard to Selected Line", None))
    # retranslateUi

