# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer 
import math
import random

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
#     pyuic6 -o form.py -x form.ui
from .ui_form import Ui_TrainModel
from .ui_form_test import Ui_testTrainModel
from signals import s

class TestTrainModel(QMainWindow):
    def __init__(self, Train, parent=None):
        super().__init__(parent)
        self.ui = Ui_testTrainModel()
        self.ui.setupUi(self)

        self.train = Train

        self.ui.ebrakecmd.setCheckable(True)
        self.ui.ebrakecmd.toggle()
        self.ui.ebrakecmd.setChecked(False)

        self.ui.sbrakecmd.setCheckable(True)
        self.ui.sbrakecmd.toggle()
        self.ui.sbrakecmd.setChecked(False)

        self.ui.rdoorcmd.setCheckable(True)
        self.ui.rdoorcmd.toggle()
        self.ui.rdoorcmd.setChecked(False)

        self.ui.ldoorcmd.setCheckable(True)
        self.ui.ldoorcmd.toggle()
        self.ui.ldoorcmd.setChecked(False)

        self.ui.lightcmd.setCheckable(True)
        self.ui.lightcmd.toggle()
        self.ui.lightcmd.setChecked(False)
        self.ui.ebrakecmd.clicked.connect(self.e_brake)
        self.ui.sbrakecmd.clicked.connect(self.s_brake)
        self.ui.ldoorcmd.clicked.connect(self.left_door)
        self.ui.rdoorcmd.clicked.connect(self.right_door)
        self.ui.lightcmd.clicked.connect(self.light_set)
        self.ui.tempbox.valueChanged.connect(self.temp_set)
        self.ui.powerbox.valueChanged.connect(self.power_set)
        self.ui.gradebox.valueChanged.connect(self.grade_set)
        self.ui.speedcmdbox.valueChanged.connect(self.speed_cmd_set)
        self.ui.speedlmtbox.valueChanged.connect(self.speed_lmt_set)


    def e_brake(self):
        if self.ui.eBrake.isChecked() or self.ui.ebrakecmd.isChecked(): 
            self.train.ebrakecmd = True
        else:
            self.train.ebrakecmd = False
        self.train.e_brake()

    def right_door(self):
        if self.ui.rdoorcmd.isChecked():
            self.train.rdoorcmd = True
        else:
            self.train.rdoorcmd = False
        self.train.right_door()

    def left_door(self):
        if self.ui.ldoorcmd.isChecked():
            self.train.ldoorcmd = True
        else:
            self.train.ldoorcmd = False
        self.train.left_door()

    def light_set(self):
        if self.ui.lightcmd.isChecked():
            self.train.lightcmd = True
        else:
            self.train.lightcmd = False
        self.train.light_set()

    def s_brake(self):
        if not(self.brakefail):
            if not(self.ebrake):
                if self.ui.sbrakecmd.isChecked(): 
                    self.train.sbrakecmd = True
                else:
                    self.train.sbrakecmd = False
        self.train.s_brake()

    def temp_set(self):
        self.train.tempcmd = self.ui.tempbox.value()
        self.train.temp_set(self.train.tempcmd)

    def power_set(self):
        self.train.powercmd = self.ui.powerbox.value()*1000
        self.train.power_set()

    def grade_set(self):
        self.train.grade = self.ui.gradebox.value()
        self.train.grade_set()

    def speed_cmd_set(self):
        self.train.speedcmd = self.ui.speedcmdbox.value()*0.44704
        self.train.speed_cmd_set()
    
    def speed_lmt_set(self):
        self.train.speedlmt = self.ui.speedlmtbox.value()*0.44704
        self.ui.speedcmdbox.setRange(0,self.ui.speedlmtbox.value())
        self.train.speed_lmt_set()

class TrainModel(QMainWindow):
    def __init__(self, trainD, parent=None):
        super().__init__(parent)
        self.ui = Ui_TrainModel()
        self.ui.setupUi(self)
        
        #data
        self.train = None
        self.directory = trainD
        self.totalRemoved = 0

        #buttons
        self.ui.eBrake.setCheckable(True)
        self.ui.eBrake.toggle()
        self.ui.eBrake.setChecked(False)

        self.ui.enginefail.setCheckable(True)
        self.ui.enginefail.toggle()
        self.ui.enginefail.setChecked(False)

        self.ui.brakefail.setCheckable(True)
        self.ui.brakefail.toggle()
        self.ui.brakefail.setChecked(False)

        self.ui.signalfail.setCheckable(True)
        self.ui.signalfail.toggle()
        self.ui.signalfail.setChecked(False)

        #functions
        self.ui.eBrake.clicked.connect(self.e_brake)
        self.ui.brakefail.clicked.connect(self.brake_failure)
        self.ui.enginefail.clicked.connect(self.engine_failure)
        self.ui.signalfail.clicked.connect(self.signal_failure)
        self.ui.trainSelect.currentTextChanged.connect(self.update_train)
        s.send_Update_Combo.connect(self.update_combo)
        s.send_delete_train.connect(self.delete)

        s.timer_tick.connect(self.timer)

    def timer(self, mul):
        tickrate = mul*0.1
        if (self.train != None):
            self.update_UI()
        else:
            self.first_train()

    def update_train(self):
        id = int(self.ui.trainSelect.currentText()[6:]) - 1
        self.train = self.directory.trains[id]

    def delete(self, id):
        self.ui.trainSelect.removeItem(id-self.totalRemoved)
        self.totalRemoved += 1

    def update_combo(self, id):
        self.ui.trainSelect.addItem("Train " + str(id))

    def update_UI(self):
        self.ui.length.setText("Length: " + str(self.train.length))
        self.ui.height.setText("Height: " + str(self.train.height))
        self.ui.width.setText("Width: " + str(self.train.width))
        self.ui.crew.setText("Crew Count: " + str(self.train.crew))
        self.ui.passenger.setText("Passengers: " + str(self.train.passenger))
        self.ui.speed.setText("Speed: " + str(int(self.train.speed*2.23694)) + " mph")
        self.ui.accel.setText("Acceleration: " + ("%.2f" % (self.train.accel*3.2808399)) + " ft/s^2")
        self.ui.temp.setText("Temperature: " + str(self.train.temp))
        self.ui.mass.setText("Mass: " + ("%.2f" % (self.train.mass*1.10231)) + " tons")
        self.ui.powercmd.setText("Power Command: " + ("%.2f" % (self.train.powercmd)) + " W")
        self.ui.tempcmd.setText("Temperature Cmd: " + str(self.train.tempcmd) + " F")
        self.ui.speedcmd.setText("Speed Command: " + str(int(self.train.speedcmd*2.23694)) + " mph")
        self.ui.speedlmt.setText("Speed Limit: " + str(int(self.train.speedlmt*2.23694)) + " mph")
        self.ui.grade.setText("Grade: " + str(self.train.grade) + " deg")
        self.beacon_set()
        self.e_brake_update()
        self.right_door()
        self.left_door()
        self.elight_set()
        self.ilight_set()
        self.s_brake()
            

    def first_train(self):
        try:
            self.train = self.directory.trains[0]
        except:
            return

    def beacon_set(self):
        try:
            if (self.train.beacon['station_name'] is None):
                self.ui.beacon.setText("Beacon: None")
                self.ui.station.setText("Station: None")
            else:
                self.ui.beacon.setText("Beacon: " + self.train.beacon['station_side'])
                self.ui.station.setText("Station: " + self.train.beacon['station_name'])
        except:
            pass
        self.ui.auth.setText("Authority: " + str(self.train.auth))

    def e_brake(self):
        self.train.e_brake(self.ui.eBrake.isChecked())

    def e_brake_update(self):
        if self.train.ebrakecmd: 
            self.ui.eBrake.setChecked(True)
            self.ui.ebrakecmd.setText("E Brake Command: On")
        else:
            self.ui.eBrake.setChecked(False)
            self.ui.ebrakecmd.setText("E Brake Command: Off")

    def engine_failure(self):
        self.train.engine_failure(self.ui.enginefail.isChecked())
        self.ui.enginefailure.setText("Engine Failure: " + str(self.train.enginefail))
    
    def brake_failure(self):
        self.train.brake_failure(self.ui.brakefail.isChecked())
        self.ui.brakefailure.setText("Brake Failure: " + str(self.train.brakefail))

    def signal_failure(self):
        self.train.signal_failure(self.ui.signalfail.isChecked())
        self.ui.signalfailure.setText("Signal Failure: " + str(self.train.signalfail))

    def right_door(self):
        if (self.train.rdoor):
            self.ui.rdoors.setText("Right Doors: Open")
            self.ui.rdoorcmd.setText("Right Door Cmd: On")
        else:
            self.ui.rdoors.setText("Right Doors: Closed")
            self.ui.rdoorcmd.setText("Right Door Cmd: Off")

    def left_door(self):
        if (self.train.ldoor):
            self.ui.ldoors.setText("Left Doors: Open")
            self.ui.ldoorcmd.setText("Left Door Cmd: On")
        else:
            self.ui.ldoors.setText("Left Doors: Closed")
            self.ui.ldoorcmd.setText("Left Door Cmd: Off")

    def elight_set(self):
        if self.train.elight:
            self.ui.elight.setText("Exterior Lights: On")
            self.ui.elightcmd.setText("E-Light Command: On")
        else:
            self.ui.elight.setText("Exterior Lights: Off")
            self.ui.elightcmd.setText("E-Light Command: Off")

    def ilight_set(self):
        if self.train.ilight:
            self.ui.ilight.setText("Interior Lights: On")
            self.ui.ilightcmd.setText("I-Light Command: On")
        else:
            self.ui.ilight.setText("Interior Lights: Off")
            self.ui.ilightcmd.setText("I-Light Command: Off")

    def s_brake(self):
        if self.train.sbrakecmd: 
            self.ui.sbrakecmd.setText("S Brake Command: On")
        else:
            self.ui.sbrakecmd.setText("S Brake Command: Off")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TrainModel()
    widget.show()
    widget2 = TestTrainModel(widget)
    widget2.show()
    sys.exit(app.exec())
