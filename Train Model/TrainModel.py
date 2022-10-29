# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer 
import math

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
#     pyuic6 -o form.py -x form.ui
from ui_form import Ui_TrainModel

class TrainModel(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TrainModel()
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
        self.temp = 75 # F
        self.ldoorcmd = False
        self.rdoorcmd = False
        self.speedcmd = 19 #m/s
        self.speedlmt = 20 #m/s
        self.lightcmd = False
        self.tempcmd = 75
        self.grade = 0
        self.enginefail = False
        self.brakefail = False
        self.signalfail = False
        self.powercmd = 50000 # Watts
        self.ebrakecmd = False
        self.sbrakecmd = False

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
        self.ui.rdoorcmd.setText("Right Door Cmd: Off")
        self.ui.ldoorcmd.setText("Left Door Cmd: Off")
        self.ui.lightcmd.setText("Light Command: Off")
        self.ui.ebrakecmd.setText("E Brake Command: Off")
        self.ui.sbrakecmd.setText("S Brake Command: Off")
        self.ui.powercmd.setText("Power Command: " + str(self.powercmd) + " W")
        self.ui.tempcmd.setText("Temperature Cmd: " + str(self.tempcmd) + " F")
        self.ui.speedcmd.setText("Speed Command: " + str(int(self.speedcmd*2.23694)) + " mph")
        self.ui.speedlmt.setText("Speed Limit: " + str(int(self.speedlmt*2.23694)) + " mph")
        self.ui.grade.setText("Grade: " + str(self.grade) + " deg")
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

        #functions
        self.ui.eBrake.clicked.connect(self.e_brake)
        self.ui.brakefail.clicked.connect(self.brake_failure)
        self.ui.enginefail.clicked.connect(self.engine_failure)
        self.ui.signalfail.clicked.connect(self.signal_failure)


    def e_brake(self):
        if self.ui.eBrake.isChecked(): 
            self.ebrakecmd = True
            self.ui.ebrakecmd.setText("E Brake Command: On")
        else:
            self.ebrakecmd = False
            self.ui.ebrakecmd.setText("E Brake Command: Off")

    def engine_failure(self):
        if self.ui.enginefail.isChecked():
            self.enginefail = True
        else:
            self.enginefail = False
        self.ui.enginefailure.setText("Engine Failure: " + str(self.enginefail))
    
    def brake_failure(self):
        if self.ui.brakefail.isChecked():
            self.brakefail = True
        else:
            self.brakefail = False
        self.ui.brakefailure.setText("Brake Failure: " + str(self.brakefail))

    def signal_failure(self):
        if self.ui.signalfail.isChecked():
            self.signalfail = True
        else:
            self.signalfail = False
        self.ui.signalfailure.setText("Signal Failure: " + str(self.signalfail))

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
            self.ebrakecmd = False
            self.sbrakecmd = False

        # calculating the acceleration
        self.prev_accel = self.accel
        self.accel = force / mass
        # checking the acceleration limit
        if (self.accel > 1):
            self.accel = 1
        # emergency brake is selected
        if (self.ebrakecmd):
            self.accel = -2.73
            return
        # service brake is selected
        elif (self.sbrakecmd):
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
    widget = TrainModel()
    widget.show()
    sys.exit(app.exec())
