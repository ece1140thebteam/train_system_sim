import systemui as system
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys

from CTCOffice.testUiMain import MainTestWindow
from CTCOffice.main import MainWindow
from TrainController.TrainCTRLui.ui_driver.mainwindow import TrainController
from TrainController.TrainCTRLui.ui_driver.trainctrltestui import TrainCTRLTestUI
from TrainController.TrainCTRLui.ui_driver.engineerui import engineerUI


class SystemWindow(QMainWindow, system.Ui_MainWindow):
    def __init__(self, parent=None):
      super(SystemWindow, self).__init__(parent)
      self.setupUi(self)

      #Create list of trains for indexing
      self.Trains = []

      self.pushButton_ctc.clicked.connect(self.open_CTC)
      self.pushButton_ctc_test.clicked.connect(self.open_CTC_test)

      self.pushButton_traincontrol.clicked.connect(self.open_traincontrol)
      self.pushButton_traincontrol_test.clicked.connect(self.open_traincontrol_test)



    def open_CTC(self):
      self.main_window = MainWindow()
      self.main_window.show()

    def open_CTC_test(self):
      self.test_window = MainTestWindow()
      self.test_window.show()

    def open_traincontrol(self):
      self.Trains.append(TrainController())
      self.Train = self.Trains[0]
      self.engWindow = engineerUI(self.Train)
      self.Train.show()
      self.engWindow.show()

    def open_traincontrol_test(self):
      self.test_window = TrainCTRLTestUI(self.Trains[0])
      self.test_window.show()

  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemWindow()
    window.show()

    sys.exit(app.exec())