import TrackBlock

class TrackSection():
    def __init__(self, section_number: int):
        self.section_number = section_number
        self.blocks = dict()

    def add_block(self, block):
        if block.block_id in self.blocks:
            print("adding already present block")
        
        self.blocks[block.id] = block