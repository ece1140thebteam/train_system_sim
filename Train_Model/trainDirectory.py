from signals import s
from Train_Model.TrainModel import TrainModel
from Train_Model.train import Train
from PyQt6.QtCore import *

class trainSignals(QObject):
    #######################################################
    # Train Model to Train Controller
    send_TrainCtrl_ebrake = pyqtSignal(bool) #ebrake
    send_TrainCtrl_failure = pyqtSignal(bool, str) #failure on/off then failure type
    send_TrainCtrl_speed = pyqtSignal(float) #train currrent speed

    #######################################################
    # Train Controller to Train Model
    # Send power calculation from Train Controller to Train Model
    send_TrainModel_powerOutput = pyqtSignal(float) #power value

    # Send service/emergency brake command from Train Controller to Train Model
    send_TrainModel_sBrake = pyqtSignal(bool) #brake state
    send_TrainModel_eBrake = pyqtSignal(bool) #brake state

    # Send external/internal light command from Train Controller to Train Model
    send_TrainModel_eLight = pyqtSignal(bool) #light state
    send_TrainModel_iLight = pyqtSignal(bool) #light state

    #Send left/right door command from Train Controller to Train Model
    send_TrainModel_lDoor = pyqtSignal(bool) #door state
    send_TrainModel_rDoor = pyqtSignal(bool) #door state

    #Send cabin temperature command from Train Controller to Train Model
    send_TrainModel_temp = pyqtSignal(int) #temp command

class trainDirectory():
    def __init__(self):
        self.idCounter = 0
        self.trains = []
        #self.trainctrl = []
        self.add_train()
        s.send_TrackModel_block_info.connect(self.update_block)
        s.send_TrackModel_next_block_info.connect(self.update_block)

    def update_block(self, id, block):
        self.trains[id].update_blocks(block)

    def add_train(self):
        #create the signals for between model and controller then pass through each constructor
        signals = trainSignals()
        train = Train(self.idCounter, signals)
        #trainctrl = Train_CTRL_BE(self.idCounter, signals)
        self.trains.append(train)
        #self.trainctrl.append(trainctrl)
        self.idCounter += 1