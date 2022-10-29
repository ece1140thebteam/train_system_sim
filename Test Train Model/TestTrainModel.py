# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer 
import math

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_TestTrainModel

class TestTrainModel(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TestTrainModel()
        self.ui.setupUi(self)

        #data
        self.friction = 0.01
        self.length = 107
        self.height = 11.2
        self.width = 8.69
        self.passenger = 100
        self.crew = 2
        self.mass = 48.55 #metric ton
        self.speed = 0 #m/s
        self.accel = 0 #m/s^2
        self.prev_accel = 0
        self.prev_speed = 0
        self.lights = False
        self.rdoor = False
        self.ldoor = False
        self.temp = 70 # F
        self.speedcmd = 19 #m/s
        self.speedlmt = 20 #m/s
        self.ebrake = False
        self.sbrake = False
        self.tempcmd = 70
        self.grade = 0
        self.enginefail = False
        self.brakefail = False
        self.signalfail = False
        self.powercmd = 0 # Watts

        #timer set up for speed calculation
        self.update_timer = QTimer()
        self.update_timer.setInterval(250) # milliseconds i believe
        self.update_timer.setSingleShot(False)
        self.update_timer.timeout.connect(self.calc_speed)
        self.update_timer.start()

        #text
        self.ui.length.setText("Length: " + str(self.length))
        self.ui.height.setText("Height: " + str(self.height))
        self.ui.width.setText("Width: " + str(self.width))
        self.ui.crew.setText("Crew Count: " + str(self.crew))
        self.ui.passenger.setText("Passengers: " + str(self.passenger))
        self.ui.speed.setText("Speed: " + str(int(self.speed*2.23694)) + " mph")
        self.ui.accel.setText("Acceleration: " + ("%.2f" % (self.accel*3.2808399)) + " ft/s^2")
        self.ui.light.setText("Lights: Off")
        self.ui.rdoors.setText("Right Doors: Closed")
        self.ui.ldoors.setText("Left Doors: Closed")
        self.ui.temp.setText("Temperature: " + str(self.temp))
        self.ui.mass.setText("Mass: " + ("%.2f" % (self.mass*1.10231)) + " tons")
        self.ui.brakefailure.setText("Brake Failure: " + str(self.brakefail))
        self.ui.enginefailure.setText("Engine Failure: " + str(self.enginefail))
        self.ui.signalfailure.setText("Signal Failure: " + str(self.signalfail))

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

        #functions
        self.ui.eBrake.clicked.connect(self.e_brake)
        self.ui.brakefail.clicked.connect(self.brake_failure)
        self.ui.enginefail.clicked.connect(self.engine_failure)
        self.ui.signalfail.clicked.connect(self.signal_failure)
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
        if not(self.brakefail):
            if self.ui.eBrake.isChecked() or self.ui.ebrakecmd.isChecked(): 
                self.ebrake = True
            else:
                self.ebrake = False

    def engine_failure(self):
        if self.ui.enginefail.isChecked():
            self.enginefail = True
            self.ui.powerbox.setValue(0)
        else:
            self.enginefail = False
        self.ui.enginefailure.setText("Engine Failure: " + str(self.enginefail))
    
    def brake_failure(self):
        if self.ui.brakefail.isChecked():
            self.brakefail = True
            self.ebrake = False
        else:
            self.brakefail = False
        self.ui.brakefailure.setText("Brake Failure: " + str(self.brakefail))

    def signal_failure(self):
        if self.ui.signalfail.isChecked():
            self.signalfail = True
        else:
            self.signalfail = False
        self.ui.signalfailure.setText("Signal Failure: " + str(self.signalfail))

    def right_door(self):
        if self.ui.rdoorcmd.isChecked():
            self.rdoor = True
            self.ui.rdoors.setText("Right Doors: Open")
        else:
            self.rdoor = False
            self.ui.rdoors.setText("Right Doors: Closed")

    def left_door(self):
        if self.ui.ldoorcmd.isChecked():
            self.ldoor = True
            self.ui.ldoors.setText("Left Doors: Open")
        else:
            self.ldoor = False
            self.ui.ldoors.setText("Left Doors: Closed")

    def light_set(self):
        if self.ui.lightcmd.isChecked():
            self.lights = True
            self.ui.light.setText("Lights: On")
        else:
            self.lights = False
            self.ui.light.setText("Lights: Off")

    def s_brake(self):
        if not(self.brakefail):
            if not(self.ebrake):
                if self.ui.sbrakecmd.isChecked(): 
                    self.sbrake = True
                else:
                    self.sbrake = False

    def temp_set(self):
        self.temp = self.ui.tempbox.value()
        self.ui.temp.setText("Temperature: " + str(self.temp))

    def power_set(self):
        self.powercmd = self.ui.powerbox.value()*1000

    def grade_set(self):
        self.grade = self.ui.gradebox.value()

    def speed_cmd_set(self):
        self.speedcmd = self.ui.speedcmdbox.value()*0.44704
    
    def speed_lmt_set(self):
        self.speedlmt = self.ui.speedlmtbox.value()*0.44704
        self.ui.speedcmdbox.setRange(0,self.ui.speedlmtbox.value())

    def calc_accel(self):
        power = self.powercmd

        # handling if there is an engine failure caused by Murphy
        if (self.enginefail):
            power = 0

        # calculating the slope of the current block
        angle = math.radians(self.grade)

        mass = self.mass*1000 #convert metric tons to kg

        # calculating the force of the engine
        normal_force = mass * math.cos(angle) * 9.81
        friction_force = self.friction * normal_force
        gravity_force = mass * math.sin(angle) * 9.81
        try:
            force = power / self.speed
            force = force - friction_force - gravity_force
            if (force > 20450):
                force = 20450
        except ZeroDivisionError:
            # edge case where the train is at zero speed and starting to move. Setting the force to max force
            force = 20450
            if (power == 0):
                force = 0

        # handling if there is a brake failure caused by Murphy
        if (self.brakefail):
            self.ebrake = False
            self.sbrake = False

        # calculating the acceleration
        self.prev_accel = self.accel
        self.accel = force / mass
        # checking the acceleration limit
        if (self.accel > 1):
            self.accel = 1
        # emergency brake is selected
        if (self.ebrake):
            self.accel = -2.73
            return
        # service brake is selected
        elif (self.sbrake):
            self.accel = -1.2
            return

    def calc_speed(self):
        sample_time = 0.25
        # setting the prev speed
        self.prev_speed = self.speed
        # calculating the new acceleration
        self.ui.accel.setText("Acceleration: " + ("%.2f" % (self.accel*3.2808399)) + " ft/s^2")
        self.calc_accel()
        #self.ui.accel.setText("Acceleration: " + ("%.2f" % (self.accel*3.2808399)) + " ft/s^2")
        # calculating the new speed
        self.speed = self.prev_speed + sample_time/2 * (self.accel + self.prev_accel)
        # not allowing for negative velcoity values
        if (self.speed < 0):
            self.speed = 0
        #show speed
        self.ui.speed.setText("Speed: " + str(int(self.speed*2.23694)) + " mph")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TestTrainModel()
    widget.show()
    sys.exit(app.exec())
