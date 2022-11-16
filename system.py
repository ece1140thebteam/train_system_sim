import sys
import datetime

import systemui as system
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from CTCOffice.testUiMain import MainTestWindow as MainTestWindowCTC
from CTCOffice.main import MainWindow as MainWindowCTC
from TrainController.TrainCTRLui.ui_driver.mainwindow import TrainController
from TrainController.TrainCTRLui.ui_driver.trainctrltestui import TrainCTRLTestUI
from TrainController.TrainCTRLui.ui_driver.engineerui import engineerUI
from track_model.track_model_qc.widget import TrackModel as TrackModelGUI
from track_model.TrackModelTestUI.trackmodeltestui import TrackModelTestUI as TrackModelTestUI
 
from signals import s
from Wayside_Controller.main import MainWindow as TrackControllerWindow
from Train_Model.TrainModel import TrainModel, TestTrainModel


class SystemWindow(QMainWindow, system.Ui_MainWindow):
    def __init__(self, parent=None):
      super(SystemWindow, self).__init__(parent)
      self.setupUi(self)
      self.second = 0

      self.label_time.setText(str(round(self.second, 1)))
      
      self.trackController = TrackControllerWindow()
      self.trainmodel = TrainModel()
      self.trainmodel_test = TestTrainModel(self.trainmodel)
      self.pushButton_ctc.clicked.connect(self.open_CTC)
      self.pushButton_ctc_test.clicked.connect(self.open_CTC_test)
      self.pushButton_trainmodel.clicked.connect(self.open_trainmodel)
      self.pushButton_trainmodel_test.clicked.connect(self.open_trainmodel_test)

      #Create list of trains for indexing
      self.Trains = []


      self.pushButton_traincontrol.clicked.connect(self.open_traincontrol)
      self.pushButton_traincontrol_test.clicked.connect(self.open_traincontrol_test)
      self.main_windowCTC = MainWindowCTC()
      self.test_windowCTC = MainTestWindowCTC()
      self.pushButton_ctc.clicked.connect(self.open_CTC)
      self.pushButton_ctc_test.clicked.connect(self.open_CTC_test)

      self.pushButton_start.clicked.connect(self.pause_timer)


      self.timer = QTimer()
      self.timer.setInterval(100)
      self.timer.timeout.connect(self.timer_timeout)

      # self.update_speed()
      # self.horizontalSlider.valueChanged.connect(self.update_speed)

# TODO: unconnect lines for module and add functions as indicated to open window
      self.pushButton_trackcontrol.clicked.connect(self.open_TrackController)
      # self.pushButton_trackcontrol_test.clicked.connect(self.open_TrackController_test)

      self.trackmodel = TrackModelGUI()
      self.trackModelTestUI = TrackModelTestUI()
      self.pushButton_trackmodel.clicked.connect(self.open_TrackModel)
      self.pushButton_trackmodel_test.clicked.connect(self.open_TrackModelTestUI)
      
      # self.pushButton_trainmodel.clicked.connect(self.open_TrainModel)
      # self.pushButton_trainmodel_test.clicked.connect(self.open_TrainModel_test)

      # self.pushButton_traincontrol.clicked.connect(self.open_TrainController)
      # self.pushButton_traincontrol_test.clicked.connect(self.open_TrainController_test)

      s.send_CTC_create_train.connect(self.open_traincontrol)

    def open_CTC(self):
      
      self.main_windowCTC.show()

    def open_CTC_test(self):
      
      self.test_windowCTC.show()

    def open_TrackController(self):
      self.trackController.show()

    def timer_timeout(self):
      self.second += 0.1 * self.horizontalSlider.value()
      self.label_time.setText(str(datetime.timedelta(seconds=round(self.second))))
      s.timer_tick.emit(self.horizontalSlider.value())
    
    def pause_timer(self):
      if self.pushButton_start.isChecked():
        self.timer.start()
      else:
        self.timer.stop()

    def open_trainmodel(self):
      self.trainmodel.show()

    def open_trainmodel_test(self):
      self.trainmodel_test.show()
    def open_traincontrol(self):
      self.Trains.append(TrainController())
      self.Train = self.Trains[0]
      self.engWindow = engineerUI(self.Train)
      self.Train.show()
      self.engWindow.show()

    def open_traincontrol_test(self):
      self.test_window = TrainCTRLTestUI(self.Trains[0])
      self.test_window.show()

  
    def open_TrackModel(self):
      self.trackmodel.show()

    def open_TrackModelTestUI(self):
      self.trackModelTestUI.show()

    # def update_speed(self):
    #   self.label_speed.setText(str(self.horizontalSlider.value()))
    #   self.timer.setInterval(100/self.horizontalSlider.value())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemWindow()
    window.show()

    sys.exit(app.exec())