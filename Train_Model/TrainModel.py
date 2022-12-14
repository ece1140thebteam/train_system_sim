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
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TrainModel()
        self.ui.setupUi(self)
        
        #data
        self.friction = 0.01
        self.length = 32.2 #m
        self.height = 3.42 #m
        self.width = 2.65 #m
        self.passenger = 100
        self.crew = 2
        self.mass = 48.55 #metric ton
        self.speed = 0 #m/s
        self.accel = 0 #m/s^2
        self.prev_accel = 0
        self.prev_speed = 0
        self.ilight = False
        self.elight = False
        self.rdoor = False
        self.ldoor = False
        self.temp = 70 # F
        self.ldoorcmd = False
        self.rdoorcmd = False
        self.speedcmd = 19 #m/s
        self.speedlmt = 20 #m/s 
        self.elightcmd = False
        self.ilightcmd = False
        self.tempcmd = 70
        self.grade = 0
        self.enginefail = False
        self.brakefail = False
        self.signalfail = False
        self.powercmd = 50000 # Watts
        self.ebrakecmd = False
        self.sbrakecmd = False
        self.distance = 0
        self.tickrate = 0
        self.distance_traveled = 0
        self.block = None
        self.prev_block = None
        self.auth = 1
        self.beacon = None
        self.atStation = False
        self.stationStop = False

        #text
        self.ui.length.setText("Length: " + str(self.length))
        self.ui.height.setText("Height: " + str(self.height))
        self.ui.width.setText("Width: " + str(self.width))
        self.ui.crew.setText("Crew Count: " + str(self.crew))
        self.ui.passenger.setText("Passengers: " + str(self.passenger))
        self.ui.speed.setText("Speed: " + str(int(self.speed*2.23694)) + " mph")
        self.ui.accel.setText("Acceleration: " + ("%.2f" % (self.accel*3.2808399)) + " ft/s^2")
        self.ui.elight.setText("Exterior Lights: Off")
        self.ui.ilight.setText("Interior Lights: Off")
        self.ui.rdoors.setText("Right Doors: Closed")
        self.ui.ldoors.setText("Left Doors: Closed")
        self.ui.temp.setText("Temperature: " + str(self.temp))
        self.ui.mass.setText("Mass: " + ("%.2f" % (self.mass*1.10231)) + " tons")
        self.ui.rdoorcmd.setText("Right Door Cmd: Off")
        self.ui.ldoorcmd.setText("Left Door Cmd: Off")
        self.ui.elightcmd.setText("E-Light Command: Off")
        self.ui.ilightcmd.setText("I-Light Command: Off")
        self.ui.ebrakecmd.setText("E Brake Command: Off")
        self.ui.sbrakecmd.setText("S Brake Command: Off")
        self.ui.powercmd.setText("Power Command: " + ("%.2f" % (self.powercmd)) + " W")
        self.ui.tempcmd.setText("Temperature Cmd: " + str(self.tempcmd) + " F")
        self.ui.speedcmd.setText("Speed Command: " + str(int(self.speedcmd*2.23694)) + " mph")
        self.ui.speedlmt.setText("Speed Limit: " + str(int(self.speedlmt*2.23694)) + " mph")
        self.ui.grade.setText("Grade: " + str(self.grade) + " deg")
        self.ui.brakefailure.setText("Brake Failure: " + str(self.brakefail))
        self.ui.enginefailure.setText("Engine Failure: " + str(self.enginefail))
        self.ui.signalfailure.setText("Signal Failure: " + str(self.signalfail))
        self.ui.beacon.setText("Beacon: None")
        self.ui.auth.setText("Authority: " + str(self.auth))
        self.ui.station.setText("Station: None")

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

        #signals
        s.send_TrainModel_eLight.connect(self.elight_set)
        s.send_TrainModel_iLight.connect(self.ilight_set)
        s.send_TrainModel_powerOutput.connect(self.power_set)
        s.send_TrainModel_lDoor.connect(self.left_door)
        s.send_TrainModel_rDoor.connect(self.right_door)
        s.send_TrackModel_next_block_info.connect(self.update_blocks)
        s.send_TrainModel_eBrake.connect(self.e_brake)
        s.send_TrainModel_temp.connect(self.temp_set)
        s.send_TrackModel_block_info.connect(self.update_blocks)
        s.send_TrainModel_sBrake.connect(self.s_brake)
        s.timer_tick.connect(self.timer)
        self.next_track()

    def timer(self, mul):
        self.tickrate = 0.1*mul
        self.calc_speed()
        if self.auth == 0:
            self.current_track()
            self.station()
        if self.auth == 1 and self.atStation:
            self.atStation = False
            if self.beacon['station_side'] is 'right':
                self.rdoorcmd = False
                self.right_door(self.rdoorcmd)
            else:
                self.ldoorcmd = False
                self.left_door(self.ldoorcmd)

    def current_track(self):
        if self.block is None:
            s.send_TrackModel_get_block_info.emit("Green", 0, 0)
        else:
            s.send_TrackModel_get_block_info.emit("Green", self.block['block_num'], 0)
    
    def next_track(self):
        if self.block is None:
            s.send_TrackModel_get_next_block_info.emit("Green", 0, -1, 0)
        elif self.prev_block is None:
            s.send_TrackModel_get_next_block_info.emit("Green", self.block['block_num'], 0, 0)
        else:
            s.send_TrackModel_get_next_block_info.emit("Green", self.block['block_num'], self.prev_block['block_num'], 0)

    def update_blocks(self, train, block):
        if (self.block != None) and (self.block['block_num'] != block['block_num']):
            self.prev_block = self.block
        self.block = block
        s.send_TrackModel_track_occupancy.emit("Green", self.block['block_num'], True)
        self.grade = self.block['grade']
        self.grade_set()
        self.speedcmd = self.block['commanded_speed']
        self.auth = self.block['authority']
        if (self.auth == 0):
            sbrakecmd = True
        else:
            sbrakecmd = False
        self.s_brake(sbrakecmd)
        self.beacon = self.block['beacon']
        self.beacon_set()
        if (self.block['underground']):
            self.elightcmd = True
            self.ilightcmd = True
        else:
            self.elightcmd = False
            self.ilightcmd = False
        self.elight_set(self.elightcmd)
        self.ilight_set(self.ilightcmd)
        self.speedlmt = self.block['speed_limit']/3.6
        self.speed_lmt_set()

    def station(self):
        if self.beacon['station_name'] != None and not(self.atStation):
            self.atStation = True
        if self.speed == 0 and self.atStation and not(self.stationStop):
            self.passenger += self.prev_block['passengers_waiting']
            deboarding = random.randint(int(self.passenger/10), int(self.passenger/5))
            self.passenger -= deboarding
            self.ui.passenger.setText("Passengers: " + str(self.passenger))
            s.send_TrackModel_passengers_onboarded.emit("Green", self.block['block_num'], deboarding)
            self.stationStop = True
            if self.beacon['station_side'] is 'right':
                self.rdoorcmd = True
                self.right_door(self.rdoorcmd)
            else:
                self.ldoorcmd = True
                self.left_door(self.ldoorcmd)

    def beacon_set(self):
        station = self.beacon['station_name']
        if (station is None):
            self.ui.beacon.setText("Beacon: None")
            self.ui.station.setText("Station: None")
        else:
            self.ui.beacon.setText("Beacon: " + self.beacon['station_side'])
            self.ui.station.setText("Station: " + station)
        self.ui.auth.setText("Authority: " + str(self.auth))


    def e_brake(self, cmd = False):
        if self.ui.eBrake.isChecked() or cmd: 
            self.ebrakecmd = True
            self.ui.ebrakecmd.setText("E Brake Command: On")
        else:
            self.ebrakecmd = False
            self.ui.ebrakecmd.setText("E Brake Command: Off")

    def engine_failure(self):
        if self.ui.enginefail.isChecked():
            self.enginefail = True
            s.send_TrainCtrl_failure.emit(self.enginefail, "Engine")
        else:
            self.enginefail = False
            s.send_TrainCtrl_failure.emit(False, "None")
        self.ui.enginefailure.setText("Engine Failure: " + str(self.enginefail))
    
    def brake_failure(self):
        if self.ui.brakefail.isChecked():
            self.brakefail = True
            s.send_TrainCtrl_failure.emit(self.brakefail, "Brake")
        else:
            self.brakefail = False
            s.send_TrainCtrl_failure.emit(False, "None")
        self.ui.brakefailure.setText("Brake Failure: " + str(self.brakefail))

    def signal_failure(self):
        if self.ui.signalfail.isChecked():
            self.signalfail = True
            s.send_TrainCtrl_failure.emit(self.signalfail, "Signal")
        else:
            self.signalfail = False
            s.send_TrainCtrl_failure.emit(False, "None")
        self.ui.signalfailure.setText("Signal Failure: " + str(self.signalfail))

    def calc_accel(self):
        power = self.powercmd

        # handling if there is an engine failure caused by Murphy
        if (self.enginefail):
            power = 0

        # calculating the slope of the current block
        angle = math.radians(self.grade)

        mass = self.mass*1000 #convert metric tons to kg

        power *= 1000

        # calculating the force of the engine
        normal_force = mass * math.cos(angle) * 9.81
        friction_force = self.friction * normal_force
        gravity_force = mass * math.sin(angle) * 9.81
        try:
            force = power / self.speed
            force = force -  gravity_force - friction_force
            if (force > 25000):
                force = 25000
        except ZeroDivisionError:
            # edge case where the train is at zero speed and starting to move. Setting the force to max force
            force = 25000
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
        if (self.accel > 0.5):
            self.accel = 0.5
        # emergency brake is selected
        if (self.ebrakecmd):
            self.accel = -2.73
            return
        # service brake is selected
        elif (self.sbrakecmd):
            self.accel = -1.2
            return

    def calc_speed(self):
        sample_time = self.tickrate
        # setting the prev speed
        self.prev_speed = self.speed
        # calculating the new acceleration
        self.ui.accel.setText("Acceleration: " + ("%.2f" % (self.accel*3.2808399)) + " ft/s^2")
        self.calc_accel()
        #self.ui.accel.setText("Acceleration: " + ("%.2f" % (self.accel*3.2808399)) + " ft/s^2")
        #calculating the new speed
        self.speed = self.prev_speed + sample_time/2 * (self.accel + self.prev_accel)
        #not allowing for negative velcoity values
        if (self.speed < 0):
            self.speed = 0
        #show speed
        s.send_TrainCtrl_speed.emit(self.speed)

        self.ui.speed.setText("Speed: " + str(int(self.speed*2.23694)) + " mph")
        self.calculate_distance()

    def calculate_distance(self):
        sample_time = self.tickrate
        # calculating the distance traveled in the last time sample
        distance = self.prev_speed * sample_time + 0.5 * self.accel * sample_time**2
        if distance < 0:
            distance = 0
        self.distance = distance
        # calculating the total distance traveled by the train
        self.distance_traveled += distance
        if self.block is None:
            return
        if (self.distance_traveled > self.block['length']):
            self.distance_traveled -= self.block['length']
            self.next_track()
        if (self.distance_traveled > self.length) and (self.prev_block != None):
            s.send_TrackModel_track_occupancy.emit("Green", self.prev_block['block_num'], False)

    #test ui updates:

    def right_door(self, open):
        if (open and self.speed == 0):
            self.rdoor = True
            self.ui.rdoors.setText("Right Doors: Open")
            self.ui.rdoorcmd.setText("Right Door Cmd: On")
        else:
            self.rdoor = False
            self.ui.rdoors.setText("Right Doors: Closed")
            self.ui.rdoorcmd.setText("Right Door Cmd: Off")

    def left_door(self, open):
        if (open and self.speed == 0):
            self.ldoor = True
            self.ui.ldoors.setText("Left Doors: Open")
            self.ui.ldoorcmd.setText("Left Door Cmd: On")
        else:
            self.ldoor = False
            self.ui.ldoors.setText("Left Doors: Closed")
            self.ui.ldoorcmd.setText("Left Door Cmd: Off")

    def elight_set(self, on):
        if on:
            self.elight = True
            self.ui.elight.setText("Exterior Lights: On")
            self.ui.elightcmd.setText("E-Light Command: On")
        else:
            self.elight = False
            self.ui.elight.setText("Exterior Lights: Off")
            self.ui.elightcmd.setText("E-Light Command: Off")

    def ilight_set(self, on):
        if on:
            self.ilight = True
            self.ui.ilight.setText("Interior Lights: On")
            self.ui.ilightcmd.setText("I-Light Command: On")
        else:
            self.ilight = False
            self.ui.ilight.setText("Interior Lights: Off")
            self.ui.ilightcmd.setText("I-Light Command: Off")

    def s_brake(self, cmd):
        if not(self.brakefail):
            if not(self.ebrakecmd):
                self.sbrakecmd = cmd
                if self.sbrakecmd: 
                    self.ui.sbrakecmd.setText("S Brake Command: On")
                else:
                    self.ui.sbrakecmd.setText("S Brake Command: Off")

    def temp_set(self, cmd):
        self.temp = cmd
        self.ui.tempcmd.setText("Temperature Cmd: " + str(self.tempcmd) + " F")
        self.ui.temp.setText("Temperature: " + str(self.temp) + " F")

    def power_set(self, power):
        self.powercmd = power
        self.ui.powercmd.setText("Power Command: " + ("%.2f" % (self.powercmd)) + " W")

    def grade_set(self):
        self.ui.grade.setText("Grade: " + str(self.grade) + " deg")

    def speed_cmd_set(self):
        self.ui.speedcmd.setText("Speed Command: " + str(int(self.speedcmd*2.23694)) + " mph")
        
    def speed_lmt_set(self):
        self.ui.speedlmt.setText("Speed Limit: " + str(int(self.speedlmt*2.23694)) + " mph")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TrainModel()
    widget.show()
    widget2 = TestTrainModel(widget)
    widget2.show()
    sys.exit(app.exec())
