class BlockInfo():
    def __init__(self):
        self.block_number = 0
        self.line = ''
        self.section = ''
        self.maintenance_mode = 0
        self.infrastructure = ''
        self.failure = ''
        self.switch_position = None
        self.occupancy = 0
        self.crossing = None
        self.authority = 0
        self.signal_state = 'None'
        self.suggested_speed = 0

    def set_data(self, 
        block_number, 
        line, 
        section,  
        infrastructure):
        self.block_number = block_number
        self.line = line
        self.section = section
        self.infrastructure = infrastructure

    def set_switch(self, switch_position):
        self.switch_position = switch_position
    
    def set_suggested_speed(self, speed):
        self.suggested_speed = speed
    
    def set_authority(self, authority):
        self.authority = authority

    def set_failure(self, failure):
        self.failure = failure

    def set_crossing(self, crossing):
        self.crossing = crossing

    def set_maintenance_mode(self, mode):
        self.maintenance_mode = mode
    
    def set_occupancy(self, state):
        self.occupancy = state
    
    def set_signal_state(self, state):
        self.signal_state = state
