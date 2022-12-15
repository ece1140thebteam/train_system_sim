from Train_Model.train import Train
from TrainController.TrainCTRLui.ui_driver.trainbackend import Train_CTRL_BE
from PyQt6.QtCore import *
from signals import s
from TrainController.TrainCTRLui.ui_driver.engineerui import engineerUI

class trainSignals(QObject):
    #######################################################
    # Train Model to Train Controller
    #send_TrainCtrl_ebrake = pyqtSignal(bool) #ebrake # BIG WEDNESDAY ISSUE (small)
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
        self.trainctrl = []
        s.send_TrackModel_block_info.connect(self.update_block)
        s.send_TrackModel_next_block_info.connect(self.update_block)
        s.send_CTC_create_train.connect(self.add_train)

    def update_block(self, id, block):
        if 'yard' in block:
            if block['yard']:
                print('Train {id} has reached the yard.')
                self.trains[id].update_blocks(block)
                self.trainctrl[id].cmdSpdAdjust(block)
                self.trains[id] = None
                self.trainctrl[id] = None
        elif id < self.idCounter:
            if self.trains[id] is not None:
                self.trains[id].update_blocks(block)
                self.trainctrl[id].cmdSpdAdjust(block)

    def add_train(self, line):
        #create the signals for between model and controller then pass through each constructor
        signals = trainSignals()
        self.trainctrl.append(Train_CTRL_BE(signals))
        self.trains.append(Train(self.idCounter, signals, line))
        self.idCounter += 1
        self.trains[self.idCounter-1].next_track()
        s.send_Update_Combo.emit(self.idCounter)

        #create engineer Kp/Ki window at the time of train controller's instantiation
        self.engWindow = engineerUI(self.trainctrl[self.idCounter-1])
        self.engWindow.show()