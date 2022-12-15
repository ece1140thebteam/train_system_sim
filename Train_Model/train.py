from signals import s
import random
import math
from PyQt6.QtCore import *

class Train():
    
    def __init__(self, id, signals, line):
        
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
        self.id = id
        self.sig = signals
        self.override_lights = False
        self.line = line

        s.timer_tick.connect(self.timer)

        self.sig.send_TrainModel_eLight.connect(self.elight_set)
        self.sig.send_TrainModel_iLight.connect(self.ilight_set)
        self.sig.send_TrainModel_powerOutput.connect(self.power_set)
        self.sig.send_TrainModel_lDoor.connect(self.left_door)
        self.sig.send_TrainModel_rDoor.connect(self.right_door)
        self.sig.send_TrainModel_eBrake.connect(self.e_brake)
        self.sig.send_TrainModel_temp.connect(self.temp_set)
        self.sig.send_TrainModel_sBrake.connect(self.s_brake)

    def timer(self, mul):
        self.tickrate = 0.1*mul
        self.calc_speed()
        if self.auth == 0:
            self.current_track()
            self.station()
        if self.auth == 1 and self.atStation:
            self.atStation = False
            if self.beacon is None:
                return
            self.rdoorcmd = False
            self.ldoorcmd = False
            self.right_door(False)
            self.left_door(False)

    def e_brake(self, cmd):
        self.ebrakecmd = cmd
        self.sig.send_TrainCtrl_eBrake.emit(self.ebrakecmd)

    def elight_set(self, on):
        if on:
            self.elight = True
        else:
            self.elight = False

    def ilight_set(self, on):
        if on:
            self.ilight = True
        else:
            self.ilight = False

    def power_set(self, power):
        self.powercmd = power

    def temp_set(self, cmd):
        self.temp = cmd

    def s_brake(self, cmd):
        if not(self.brakefail):
            if not(self.ebrakecmd):
                self.sbrakecmd = cmd

    def current_track(self):
        if self.block is None:
            s.send_TrackModel_get_block_info.emit(self.line, -1, self.id)
        else:
            s.send_TrackModel_get_block_info.emit(self.line, self.block['block_num'], self.id)

    def next_track(self):
        if self.block is None:
            s.send_TrackModel_get_next_block_info.emit(self.line, -1, -1, self.id)
        elif self.prev_block is None:
            s.send_TrackModel_get_next_block_info.emit(self.line, self.block['block_num'], 0, self.id)
        else:
            s.send_TrackModel_get_next_block_info.emit(self.line, self.block['block_num'], self.prev_block['block_num'], self.id)

    def update_blocks(self, block):
        if (self.block != None) and (self.block['block_num'] != block['block_num']):
            self.prev_block = self.block
        self.block = block
        if self.block['yard']:
            s.send_TrackModel_track_occupancy.emit(self.line, self.prev_block['block_num'], False)
        s.send_TrackModel_track_occupancy.emit(self.line, self.block['block_num'], True)
        self.grade = self.block['grade']
        self.speedcmd = self.block['commanded_speed']*0.277777
        self.auth = self.block['authority']
        if (self.auth == 0):
            sbrakecmd = True
        else:
            sbrakecmd = False
        self.s_brake(sbrakecmd)
        self.beacon = self.block['beacon']
        if (self.block['underground']):
            self.elightcmd = True
            self.ilightcmd = True
            self.sig.send_TrainCtrl_lights.emit(True)
            self.override_lights = True
        else:
            if (self.override_lights):
                self.elightcmd = False
                self.ilightcmd = False
                self.override_lights = False
                self.sig.send_TrainCtrl_lights.emit(False)
        self.speedlmt = self.block['speed_limit']/3.6

    def station(self):
        if self.beacon is not None and not(self.atStation):
            self.atStation = True
        if self.speed == 0 and self.atStation and not(self.stationStop):
            self.passenger += self.prev_block['passengers_waiting']
            deboarding = random.randint(int(self.passenger/10), int(self.passenger/5))
            self.passenger -= deboarding
            s.send_TrackModel_passengers_onboarded.emit(self.line, self.block['block_num'], deboarding)
            self.stationStop = True
            if self.beacon['station_side'] == 'right':
                self.rdoorcmd = True
                self.right_door(self.rdoorcmd)
            else:
                self.ldoorcmd = True
                self.left_door(self.ldoorcmd)

    def right_door(self, open):
        if (open and self.speed == 0):
            self.rdoor = True
        else:
            self.rdoor = False
    
    def left_door(self, open):
        if (open and self.speed == 0):
            self.ldoor = True
        else:
            self.ldoor = False

    def engine_failure(self, check):
        if check:
            self.enginefail = True
            self.sig.send_TrainCtrl_failure.emit(True, "Engine")
        else:
            self.enginefail = False
            self.sig.send_TrainCtrl_failure.emit(False, "None")
    
    def brake_failure(self, check):
        if check:
            self.brakefail = True
            self.sig.send_TrainCtrl_failure.emit(True, "Brake")
        else:
            self.brakefail = False
            self.sig.send_TrainCtrl_failure.emit(False, "None")

    def signal_failure(self, check):
        if check:
            self.signalfail = True
            self.sig.send_TrainCtrl_failure.emit(True, "Signal")
        else:
            self.signalfail = False
            self.sig.send_TrainCtrl_failure.emit(False, "None")

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
        self.calc_accel()
        #self.ui.accel.setText("Acceleration: " + ("%.2f" % (self.accel*3.2808399)) + " ft/s^2")
        #calculating the new speed
        self.speed = self.prev_speed + sample_time/2 * (self.accel + self.prev_accel)
        #not allowing for negative velcoity values
        if (self.speed < 0):
            self.speed = 0
        #show speed
        self.sig.send_TrainCtrl_speed.emit(self.speed)
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
            s.send_TrackModel_track_occupancy.emit(self.line, self.prev_block['block_num'], False)