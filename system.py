import systemui as system
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys

from CTCOffice.testUiMain import MainTestWindow
from CTCOffice.main import MainWindow
from signals import s

# TODO: Import main window class from file that used to run your module independently
# Note: You will probably need to update your import to be the path from the root directory instead of the relative path

class SystemWindow(QMainWindow, system.Ui_MainWindow):
    def __init__(self, parent=None):
      super(SystemWindow, self).__init__(parent)
      self.setupUi(self)

      self.main_windowCTC = MainWindow()
      self.test_windowCTC = MainTestWindow()
      self.pushButton_ctc.clicked.connect(self.open_CTC)
      self.pushButton_ctc_test.clicked.connect(self.open_CTC_test)

      self.pushButton_start.clicked.connect(self.pause_timer)


      self.timer = QTimer()
      self.timer.setInterval(100)
      self.timer.timeout.connect(self.timer_timeout)

# TODO: unconnect lines for module and add functions as indicated to open window
      # self.pushButton_trackcontrol.clicked.connect(self.open_TrackController)
      # self.pushButton_trackcontrol_test.clicked.connect(self.open_TrackController_test)

      # self.pushButton_trackmodel.clicked.connect(self.open_TrackModel)
      # self.pushButton_trackmodel_test.clicked.connect(self.open_TrackModel_test)
      
      # self.pushButton_trainmodel.clicked.connect(self.open_TrainModel)
      # self.pushButton_trainmodel_test.clicked.connect(self.open_TrainModel_test)

      # self.pushButton_traincontrol.clicked.connect(self.open_TrainController)
      # self.pushButton_traincontrol_test.clicked.connect(self.open_TrainController_test)

    def open_CTC(self):
      
      self.main_windowCTC.show()

    def open_CTC_test(self):
      
      self.test_windowCTC.show()

    def timer_timeout(self):
      print("Timer")
      s.timer_tick.emit()
    
    def pause_timer(self):
      if self.pushButton_start.isChecked():
        self.timer.start()
      else:
        self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemWindow()
    window.show()

    sys.exit(app.exec())