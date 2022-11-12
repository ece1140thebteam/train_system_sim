import systemui as system
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys

from CTCOffice.testUiMain import MainTestWindow as MainTestWindowCTC
from CTCOffice.main import MainWindow as MainWindowCTC

from track_model.track_model_qc.widget import TrackModel as TrackModelGUI
# TODO: Import main window class from file that used to run your module independently
# Note: You will probably need to update your import to be the path from the root directory instead of the relative path

class SystemWindow(QMainWindow, system.Ui_MainWindow):
    def __init__(self, parent=None):
      super(SystemWindow, self).__init__(parent)
      self.setupUi(self)

      self.pushButton_ctc.clicked.connect(self.open_CTC)
      self.pushButton_ctc_test.clicked.connect(self.open_CTC_test)

# TODO: unconnect lines for module and add functions as indicated to open window
      # self.pushButton_trackcontrol.clicked.connect(self.open_TrackController)
      # self.pushButton_trackcontrol_test.clicked.connect(self.open_TrackController_test)

      self.pushButton_trackmodel.clicked.connect(self.open_TrackModel)
      # self.pushButton_trackmodel_test.clicked.connect(self.open_TrackModel_test)
      
      # self.pushButton_trainmodel.clicked.connect(self.open_TrainModel)
      # self.pushButton_trainmodel_test.clicked.connect(self.open_TrainModel_test)

      # self.pushButton_traincontrol.clicked.connect(self.open_TrainController)
      # self.pushButton_traincontrol_test.clicked.connect(self.open_TrainController_test)

    def open_CTC(self):
      self.main_window = MainWindowCTC()
      self.main_window.show()

    def open_CTC_test(self):
      self.test_window = MainTestWindowCTC()
      self.test_window.show()

    def open_TrackModel(self):
      self.trackmodel_main_window = TrackModelGUI()
      self.trackmodel_main_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemWindow()
    window.show()

    sys.exit(app.exec())