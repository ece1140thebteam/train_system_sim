from signals import s
from Train_Model.TrainModel import TrainModel

class trainDirectory():
    def __init__(self, train):
        self.trains = []
        self.trains.append(train)
        s.send_TrackModel_block_info.connect(self.update_block)
        s.send_TrackModel_next_block_info.connect(self.update_block)

    def update_block(self, id, block):
        self.trains[id].update_blocks(block)