

from configparser import SectionProxy
from http.client import SWITCHING_PROTOCOLS
from pdb import line_prefix
import random
class Switch():
    def __init__(self, line, section, block, pos1, pos2):
        self.section    = section
        self.line       = line
        self.block_num  = block
        self.curr_pos   = pos1
        self.pos1       = pos1
        self.pos2       = pos2
    
    def update_switch_position(self, pos):
        if pos == self.pos1 or pos == self.pos2:
            self.curr_pos = pos

class TrackBlock():
    def __init__(self, 
            line:               str,
            section:            str,
            block_number:       str,
            block_len:          str,
            block_grade:        str,
            speed_limit:        str,
            underground:        str,
            station:            str,
            switch:             str,
            elevation:          str,
            has_rail_crossing:  str,
            cum_elevation:      str,
            can_travel_to:      str,
        ):

        self.line           = line
        self.section        = section
        self.block_number   = int(block_number)
        self.block_len      = float(block_len)
        self.block_grade    = float(block_grade)
        self.speed_limit    = float(speed_limit)
        self.underground    = underground
        self.station        = station
        self.switch         = switch
        self.elevation      = float(elevation)
        self.cum_elevation  = float(cum_elevation)
        self.has_rail_crossing = has_rail_crossing
        self.can_travel_to  = can_travel_to
        self.crossing_open  = None if not has_rail_crossing else False
        self.circuit_open   = True
        self.signal         = "Red"
        self.light          = "Off"
        self.switch_pos     = switch if switch is None else switch.curr_pos
        self.track_heater   = 'Off'
        self.failure_mode   = 'No Failures'
        self.beacon1        = None
        self.beacon2        = None
        self.authority      = 1 # TODO REMOVE
        self.maintenance_mode = False
        self.commanded_speed = self.speed_limit #TODO REMOVE

        self.passengers_waiting = random.randint(6, 16)
        self.passengers_deboarded = 0

        if self.station:
            # TODO Add side of track
            self.beacon1 = {
                'station': self.station

            }
            self.beacon2 = {
                'station': self.station

            }

    def passengers_onboarded(self, deboarded):
        onboarded = self.passengers_waiting
        self.passengers_waiting = random.randint(6, 16)

        self.passengers_deboarded = deboarded

        return onboarded

    def update_failure(self,type):
        self.failure_mode = type

    def update_switch_pos(self, pos):
        if pos in self.switch:
            self.switch_pos = pos
            return True
        else:
            return False

    def print(self):
        print(f'line: {self.line}')
        print(f'section: {self.section}')
        print(f'block_number: {self.block_number}')
        print(f'block_len: {self.block_len}')
        print(f'block_grade: {self.block_grade}')
        print(f'speed_limit: {self.speed_limit}')
        print(f'underground: {self.underground}')
        print(f'station: {self.station}')
        print(f'switch: {self.switch}')
        print(f'elevation: {self.elevation}')
        print(f'cum_elevation: {self.cum_elevation}')
        print(f'has_rail_crossing: {self.has_rail_crossing}')
        print(f'crossing_open: {self.crossing_open}')
        print(f'can_travel_to: {str(self.can_travel_to)}')
        print(f'light: {str(self.light)}')


