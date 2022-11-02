
import TrackLine


class Track():
    def __init__(self):
        self.track_lines = dict()
        self.heater_on = False

    def add_switch(self, line, start, connections):
        self.track_lines[line].add_switch(start, connections)

    def turn_heater_off(self):
        self.heater_on = False

        for line in self.track_lines:
            for block in self.track_lines[line].blocks:
                self.track_lines[line].blocks[block].track_heater = 'Off'

    def turn_heater_on(self):
        self.heater_on = True

        for line in self.track_lines:
            for block in self.track_lines[line].blocks:
                self.track_lines[line].blocks[block].track_heater = 'On'

    def add_block(self, block):
        if block.line in self.track_lines:
            self.track_lines[block.line].add_block(block)
        else:
            self.track_lines[block.line] = TrackLine.TrackLine(block.line)
            self.track_lines[block.line].add_block(block)

    def print(self):
        for line in self.track_lines:
            print('-------------------')
            print(line)
            self.track_lines[line].print()
            print('-------------------')
            print()