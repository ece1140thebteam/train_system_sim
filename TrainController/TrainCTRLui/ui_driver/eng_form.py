# Form implementation generated from reading ui file 'engineer_form.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_engineerUI(object):
    def setupUi(self, engineerUI):
        engineerUI.setObjectName("engineerUI")
        engineerUI.resize(235, 181)
        self.username = QtWidgets.QLabel(engineerUI)
        self.username.setGeometry(QtCore.QRect(30, 10, 61, 16))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLabel(engineerUI)
        self.password.setGeometry(QtCore.QRect(30, 50, 61, 20))
        self.password.setObjectName("password")
        self.userInput = QtWidgets.QLineEdit(engineerUI)
        self.userInput.setGeometry(QtCore.QRect(100, 10, 113, 22))
        self.userInput.setObjectName("userInput")
        self.passInput = QtWidgets.QLineEdit(engineerUI)
        self.passInput.setGeometry(QtCore.QRect(100, 50, 113, 22))
        self.passInput.setObjectName("passInput")
        self.default_2 = QtWidgets.QPushButton(engineerUI)
        self.default_2.setGeometry(QtCore.QRect(40, 120, 111, 24))
        self.default_2.setObjectName("default_2")
        self.ok = QtWidgets.QPushButton(engineerUI)
        self.ok.setGeometry(QtCore.QRect(150, 80, 61, 24))
        self.ok.setObjectName("ok")

        self.retranslateUi(engineerUI)
        QtCore.QMetaObject.connectSlotsByName(engineerUI)

    def retranslateUi(self, engineerUI):
        _translate = QtCore.QCoreApplication.translate
        engineerUI.setWindowTitle(_translate("engineerUI", "Engineer UI"))
        self.username.setText(_translate("engineerUI", "Username: "))
        self.password.setText(_translate("engineerUI", "Password:"))
        self.default_2.setText(_translate("engineerUI", "Use Default Values"))
        self.ok.setText(_translate("engineerUI", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    engineerUI = QtWidgets.QWidget()
    ui = Ui_engineerUI()
    ui.setupUi(engineerUI)
    engineerUI.show()
    sys.exit(app.exec())
