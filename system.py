import sys

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

import systemui as system
from CTCOffice.testUiMain import MainTestWindow
from CTCOffice.main import MainWindow
from Train_Model.TrainModel import TrainModel, TestTrainModel


class SystemWindow(QMainWindow, system.Ui_MainWindow):
    def __init__(self, parent=None):
      super(SystemWindow, self).__init__(parent)
      self.setupUi(self)
      
      self.trainmodel = TrainModel()
      self.trainmodel_test = TestTrainModel(self.trainmodel)
      self.pushButton_ctc.clicked.connect(self.open_CTC)
      self.pushButton_ctc_test.clicked.connect(self.open_CTC_test)
      self.pushButton_trainmodel.clicked.connect(self.open_trainmodel)
      self.pushButton_trainmodel_test.clicked.connect(self.open_trainmodel_test)

    def open_CTC(self):
      self.main_window = MainWindow()
      self.main_window.show()

    def open_CTC_test(self):
      self.test_window = MainTestWindow()
      self.test_window.show()

    def open_trainmodel(self):
      self.trainmodel.show()

    def open_trainmodel_test(self):
      self.trainmodel_test.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemWindow()
    window.show()

    sys.exit(app.exec())