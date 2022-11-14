import random

class TrackLine():
    def __init__(self, line_name: str):
        self.line_name = line_name
        self.sections = dict()
        self.graph = [] #negative connections represent switches

        self.blocks   = dict()
        self.switches = dict()
        self.stations = dict()  #{station: passengers}

    def add_switch(self, start, connections):
        self.switches[start] = connections

    def get_block(self, block_num):
        return self.blocks[block_num]

    def set_maintenance_mode(self, section, mode):
        for block in self.sections[section]:
            block.maintenance_mode = mode
    
    def set_failure_type(self, block, failure):
        self.blocks[block].failure_mode = failure

    def add_block(self, block):
        if block.station is not None:
            self.stations[block.station] = random.randint(10,30)
        # print(block.block_number)
        # section lookup table
        if block.section in self.sections:
            self.sections[block.section].append(block.block_number)
        else:
            self.sections[block.section] = [block.block_number]
        
        # add to graph that creates connections 
        if block.block_number >= len(self.graph):
            self.graph.extend([None]*(block.block_number-len(self.graph)+1))
            # print(self.graph)
        
        self.graph[block.block_number] = block.can_travel_to
        self.blocks[block.block_number] = block
        
        # if block.section in self.sections:
        #     self.sections[block.section].add_block(block)

        
    def print(self):
        print('SWITCHES')
        for switch in self.switches:
            print(self.switches[switch])
            print(f'{switch} -> ({self.switches[switch][0]}|{self.switches[switch][1]})')
        
        print('\nSECTIONS:')
        for section in self.sections:
            print(section)
            print(self.sections[section])
            print()
        
        print('\nConnectivity Graph')
        for i in range(0, 4):
            for k in range(0, len(self.graph)):
                if i == 0:
                    print(f'{k}\t', end='')
                else:
                    if self.graph[k] is not None and i-1 < len(self.graph[k]):
                        print(f'{self.graph[k][i-1]}\t', end='')
                    else:
                        print(f'-\t', end='')
            if i == 0: print()
            print()

        
    def get_route(self, from_block: int, to_block: int):
        pass
    

