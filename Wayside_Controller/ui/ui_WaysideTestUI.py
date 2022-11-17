# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WaysideTestUI.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(538, 258)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(80)
        self.formLayout.setVerticalSpacing(30)
        self.SetInputLabel = QLabel(self.frame)
        self.SetInputLabel.setObjectName(u"SetInputLabel")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(15)
        self.SetInputLabel.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.SetInputLabel)

        self.SetInputComboBox = QComboBox(self.frame)
        self.SetInputComboBox.setObjectName(u"SetInputComboBox")
        self.SetInputComboBox.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.SetInputComboBox)

        self.LineLabel = QLabel(self.frame)
        self.LineLabel.setObjectName(u"LineLabel")
        self.LineLabel.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.LineLabel)

        self.LineComboBox = QComboBox(self.frame)
        self.LineComboBox.setObjectName(u"LineComboBox")
        self.LineComboBox.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.LineComboBox)

        self.BlockLabel = QLabel(self.frame)
        self.BlockLabel.setObjectName(u"BlockLabel")
        self.BlockLabel.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.BlockLabel)

        self.BlockComboBox = QComboBox(self.frame)
        self.BlockComboBox.setObjectName(u"BlockComboBox")
        self.BlockComboBox.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.BlockComboBox)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 2, 1)

        self.horizontalSpacer = QSpacerItem(49, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFormAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.formLayout_2.setHorizontalSpacing(80)
        self.formLayout_2.setVerticalSpacing(30)
        self.ValueLabel = QLabel(self.frame)
        self.ValueLabel.setObjectName(u"ValueLabel")
        self.ValueLabel.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.ValueLabel)

        self.ValueInputLabel = QLabel(self.frame)
        self.ValueInputLabel.setObjectName(u"ValueInputLabel")
        self.ValueInputLabel.setFont(font)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.ValueInputLabel)

        self.ValueInputSpinBox = QSpinBox(self.frame)
        self.ValueInputSpinBox.setObjectName(u"ValueInputSpinBox")
        self.ValueInputSpinBox.setFont(font)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.ValueInputSpinBox)

        self.ValueComboBox = QComboBox(self.frame)
        self.ValueComboBox.setObjectName(u"ValueComboBox")
        self.ValueComboBox.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.ValueComboBox)


        self.gridLayout.addLayout(self.formLayout_2, 0, 2, 1, 1)

        self.UpdatePushButton = QPushButton(self.frame)
        self.UpdatePushButton.setObjectName(u"UpdatePushButton")
        self.UpdatePushButton.setFont(font)

        self.gridLayout.addWidget(self.UpdatePushButton, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.SetInputLabel.setText(QCoreApplication.translate("MainWindow", u"Set Input", None))
        self.SetInputComboBox.setCurrentText("")
        self.LineLabel.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.BlockLabel.setText(QCoreApplication.translate("MainWindow", u"Block", None))
        self.ValueLabel.setText("")
        self.ValueInputLabel.setText("")
        self.UpdatePushButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
    # retranslateUi

