# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'engineer_form.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_engineerUI(object):
    def setupUi(self, engineerUI):
        if not engineerUI.objectName():
            engineerUI.setObjectName(u"engineerUI")
        engineerUI.resize(235, 181)
        self.username = QLabel(engineerUI)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(30, 10, 61, 16))
        self.password = QLabel(engineerUI)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(30, 50, 61, 20))
        self.userInput = QLineEdit(engineerUI)
        self.userInput.setObjectName(u"userInput")
        self.userInput.setGeometry(QRect(100, 10, 113, 22))
        self.passInput = QLineEdit(engineerUI)
        self.passInput.setObjectName(u"passInput")
        self.passInput.setGeometry(QRect(100, 50, 113, 22))
        self.default_2 = QPushButton(engineerUI)
        self.default_2.setObjectName(u"default_2")
        self.default_2.setGeometry(QRect(40, 120, 111, 24))
        self.ok = QPushButton(engineerUI)
        self.ok.setObjectName(u"ok")
        self.ok.setGeometry(QRect(150, 80, 61, 24))

        self.retranslateUi(engineerUI)

        QMetaObject.connectSlotsByName(engineerUI)
    # setupUi

    def retranslateUi(self, engineerUI):
        engineerUI.setWindowTitle(QCoreApplication.translate("engineerUI", u"Engineer UI", None))
        self.username.setText(QCoreApplication.translate("engineerUI", u"Username: ", None))
        self.password.setText(QCoreApplication.translate("engineerUI", u"Password:", None))
        self.default_2.setText(QCoreApplication.translate("engineerUI", u"Use Default Values", None))
        self.ok.setText(QCoreApplication.translate("engineerUI", u"Ok", None))
    # retranslateUi

