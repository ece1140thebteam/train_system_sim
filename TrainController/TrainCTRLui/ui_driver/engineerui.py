# This Python file uses the following encoding: utf-8
import sys

from PyQt6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from TrainController.TrainCTRLui.ui_driver.eng_form import Ui_engineerUI
from TrainController.TrainCTRLui.ui_driver.tctrl_dialog import trainDialog
from TrainController.TrainCTRLui.ui_driver.mainwindow import TrainController

class engineerUI(QWidget):
    def __init__(self, TrainController, parent=None):
        super().__init__(parent)
        self.ui = Ui_engineerUI()
        self.ui.setupUi(self)
        self.Train = TrainController

        self.kval = False
        self.username = 'Engineer1'
        self.password = 'Trains1'
        self.kp = 0
        self.ki = 0

        self.ui.ok.clicked.connect(self.checkinput)
        self.ui.default_2.clicked.connect(self.close)
        
        
    def checkinput(self):
        if(self.kval == False):
            user = self.ui.userInput.text()
            passw = self.ui.passInput.text()
            if(user == self.username and passw == self.password):
                self.readk()
            else:
                self.popup = trainDialog('Invalid Username/Password! Using default kp/ki values')
                self.popup.exec()
                self.close()
        else:
            self.Train.Kp = self.ui.userInput.text()
            self.Train.Ki = self.ui.passInput.text()
            self.pop = trainDialog('Kp/Ki Values Stored!')
            self.pop.show()
            self.close()

    def readk(self):
        self.ui.username.setText('KP VALUE:')
        self.ui.password.setText('KI VALUE:')
        self.ui.passInput.clear()
        self.ui.userInput.clear()
        self.kval = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = engineerUI()
    widget.show()
    sys.exit(app.exec())
