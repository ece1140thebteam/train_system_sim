# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyuic6 form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from TrainController.TrainCTRLui.ui_driver.ui_form import Ui_TrainController
from TrainController.TrainCTRLui.ui_driver.tctrl_dialog import trainDialog
from signals import s
from TrainController.TrainCTRLui.ui_driver.trainbackend import Train_CTRL_BE

class TrainController(QMainWindow):
    def __init__(self, directory, parent=None):
        super().__init__(parent)
        self.ui = Ui_TrainController()
        self.ui.setupUi(self)

        #INITIALIZE CURRENT TRAIN FOR DEVELOPMENT PURPOSES ONLY
        self.curTrain = None
        self.directory = directory

        self.authPopupHappened = False

        #initialize various button states and make them toggleable
        self.ui.manModeBtn.setCheckable(True)
        self.ui.manModeBtn.toggle()
        self.ui.manModeBtn.setChecked(False)

        self.ui.elightBtn.setCheckable(True)
        self.ui.elightBtn.toggle()
        self.ui.elightBtn.setChecked(False)

        self.ui.ilightBtn.setCheckable(True)
        self.ui.ilightBtn.toggle()
        self.ui.ilightBtn.setChecked(False)

        self.ui.ldoorBtn.setCheckable(True)
        self.ui.ldoorBtn.toggle()
        self.ui.ldoorBtn.setChecked(False)

        self.ui.rdoorBtn.setCheckable(True)
        self.ui.rdoorBtn.toggle()
        self.ui.rdoorBtn.setChecked(False)

        self.ui.sBrakeBtn.setCheckable(True)
        self.ui.sBrakeBtn.toggle()
        self.ui.sBrakeBtn.setChecked(False)

        self.ui.eBrakeBtn.setCheckable(True)
        self.ui.eBrakeBtn.toggle()
        self.ui.eBrakeBtn.setChecked(False)
        
        self.ui.intercomBtn.setCheckable(True)
        self.ui.intercomBtn.toggle()
        self.ui.intercomBtn.setChecked(False)

        #Initializing values for display
        self.ui.driverSpd.setText('0MPH')
        self.ui.curSpd.setText('Current Speed: 0 MPH')
        self.ui.cmdSpd.setText('Commanded Speed: 30 MPH')
        self.ui.curTempLabel.setText('Current Temp: 70F')
        self.ui.tempDial.setValue(70)
        self.ui.brakeFailStatus.setText('Brake Status: Working')
        self.ui.engFailStatus.setText('Engine Status: Working')
        self.ui.trackSigStatus.setText('Track Signal Status: Detected')
        self.ui.speedSlider.setMaximum(70)

        #Button Connections
        self.ui.manModeBtn.clicked.connect(self.setManMode)
        self.ui.tempDial.sliderReleased.connect(self.tempAdjust)
        self.ui.speedSlider.sliderReleased.connect(self.setSpdSlider)
        self.ui.eBrakeBtn.clicked.connect(self.eBrakeToggle)
        self.ui.sBrakeBtn.clicked.connect(self.sBrakeToggle)
        
        #Light toggles
        self.ui.elightBtn.clicked.connect(self.eLights)
        self.ui.ilightBtn.clicked.connect(self.iLights)

        #Door toggles
        self.ui.rdoorBtn.clicked.connect(self.rDoors)
        self.ui.ldoorBtn.clicked.connect(self.lDoors)

        #Train Select operation
        self.ui.trainSelect.currentTextChanged.connect(self.update_train)

        #Timer signal to govern UI Updates
        s.timer_tick.connect(self.timer)
        s.send_Update_Combo.connect(self.update_combo)

    #function for timer tick handling
    def timer(self, mul):
        if (self.curTrain != None):
            self.UpdateUI()
        else:
            self.first()

    #Function to instantiate first train into list
    def first(self):
        try:
            self.curTrain = self.directory.trainctrl[0]
        except:
            return

    #Sbrake activation function
    def sBrakeToggle(self):
        self.curTrain.sBrake = self.ui.sBrakeBtn.isChecked()
        self.curTrain.sBrakeSig()

    #Ebrake activation function
    def eBrakeToggle(self):
        self.curTrain.eBrake = self.ui.eBrakeBtn.isChecked()
        self.curTrain.eBrakeSig()
    
    #Manual Mode toggling function
    def setManMode(self):
        if not self.ui.manModeBtn.isChecked(): #Case for True
            self.ui.elightBtn.setDisabled(True)
            self.ui.ilightBtn.setDisabled(True)
            self.ui.rdoorBtn.setDisabled(True)
            self.ui.ldoorBtn.setDisabled(True)
            self.ui.sBrakeBtn.setDisabled(True)
            self.ui.speedSlider.setDisabled(True)
            self.ui.trainSelect.setDisabled(False)
            self.curTrain.manMode = False
        else: #Case for False
            self.ui.elightBtn.setDisabled(False)
            self.ui.ilightBtn.setDisabled(False)
            self.ui.rdoorBtn.setDisabled(False)
            self.ui.ldoorBtn.setDisabled(False)
            self.ui.sBrakeBtn.setDisabled(False)
            self.ui.speedSlider.setDisabled(False)
            self.ui.trainSelect.setDisabled(True)
            self.curTrain.manMode = True


    #Functions to send door signals
    def rDoors(self):
        if self.curTrain.curSpd == 0:
            self.curTrain.rdoors = self.ui.rdoorBtn.isChecked()
            self.curTrain.rDoors()
    def lDoors(self):
        if self.curTrain.curSpd == 0:
            self.curTrain.ldoors = self.ui.ldoorBtn.isChecked()
            self.curTrain.lDoors()

    #Functions to send light signals
    def eLights(self):
        self.curTrain.elights = self.ui.elightBtn.isChecked()
        self.curTrain.eLights()
    def iLights(self):
        self.curTrain.ilights = self.ui.ilightBtn.isChecked()
        self.curTrain.iLights()

    #Function to adjust temp
    def tempAdjust(self):
        self.curTrain.temp = self.ui.tempDial.value()
        tempStr = 'Current Temp: ' + str(self.curTrain.temp) + 'F'
        self.ui.curTempLabel.setText(tempStr)
        self.curTrain.tempAdjust()
        

    #Function to adjust driver set speed based on slider in ui. Called internally when slider is adjusted
    def setSpdSlider(self):
        self.curTrain.driverCmd = self.ui.speedSlider.value()
        self.ui.driverSpd.setText(str(int(self.curTrain.driverCmd*0.621371))+'MPH')
        
    def beaconHandler(self):
        if (self.curTrain.beacon is not None) and (self.curTrain.atStation == True):
            self.intercomstr = ('Arrived at '+ str(self.curTrain.station) + ' Station \nDoors opening on ' + str(self.curTrain.side) + ' side')
            self.curTrain.intercom = True
            self.ui.intercomBtn.setChecked(True)
            self.ui.label.setText(self.intercomstr)
        else:
            self.intercomstr = ('Intercom Not Active')
            self.ui.intercomBtn.setChecked(False)
            self.ui.label.setText(self.intercomstr)

    #Function to periodically update ui based on backend train data
    def UpdateUI(self):
        
        #update current speed
        curStr = 'Current Speed: ' + str(int((self.curTrain.curSpd*2.236935599991052))) + ' MPH'
        self.ui.curSpd.setText(curStr)

        #update commanded speed
        cmdStr = 'Commanded Speed: ' + str(int(self.curTrain.cmdSpd*0.621371)) + ' MPH'
        self.ui.cmdSpd.setText(cmdStr)

        #update power output
        powStr = 'Power Output: ' + str(int(self.curTrain.powOutput)) + ' kW'
        self.ui.powOut.setText(powStr)
        
        #Read current brake states of train and update UI accordingly
        self.ui.eBrakeBtn.setChecked(self.curTrain.eBrake)
        self.ui.sBrakeBtn.setChecked(self.curTrain.sBrake)
        
        #Read current light states and update accordingly
        self.ui.ilightBtn.setChecked(self.curTrain.ilights)
        self.ui.elightBtn.setChecked(self.curTrain.elights)

        #Update door status
        self.ui.rdoorBtn.setChecked(self.curTrain.rdoors)
        self.ui.ldoorBtn.setChecked(self.curTrain.ldoors)

        #Update temp
        self.ui.curTempLabel.setText("Current Temp: " + str(self.curTrain.temp))

        #check for faults, give appropriate messages
        if self.curTrain.faultMode:
            if self.curTrain.trackSigFault:
                self.ui.trackSigStatus.setText('Track Signal Status: NOT DETECTED')
            if self.curTrain.engineFault:
                self.ui.engFailStatus.setText('Engine Status: FAILING')
            if self.curTrain.brakeFault:
                self.ui.brakeFailStatus.setText('Brake Status: FAILING')
            self.faultDialog = trainDialog('Failure detected, setting power to 0 and engaging ebrake')
        else:
            self.ui.brakeFailStatus.setText('Brake Status: Working')
            self.ui.engFailStatus.setText('Engine Status: Working')
            self.ui.trackSigStatus.setText('Track Signal Status: Detected')

            #check authority of current working train
            #if no authority but stopped at a station: give beacon message
            if not self.curTrain.auth:
                if self.curTrain.curSpd <= 0:
                    self.beaconHandler()
            #otherwise, train is moving when it shouldn't be, give auth error message
                else:
                    if self.curTrain.curSpd > 0:
                        dialog = trainDialog('Not authorized to travel on block, setting power to 0 and engaging sbrake')
                        self.authPopupHappened = True 
                        self.ui.speedSlider.setDisabled(True)
                        self.ui.speedSlider.setValue(0)
                        self.ui.driverSpd.setText('0MPH')
                        dialog.exec()
            else:
                self.authPopupHappened = False
                
        #If authority is good and no faults, continue with update
            if(self.curTrain.manMode == True):
                if not(self.ui.speedSlider.isEnabled()):
                    self.ui.speedSlider.setDisabled(False)
                self.ui.speedSlider.setMaximum(self.curTrain.cmdSpd)

    def update_train(self):
        id = int(self.ui.trainSelect.currentText()[6:]) - 1
        self.curTrain = self.directory.trainctrl[id]


    def update_combo(self, id):
        self.ui.trainSelect.addItem("Train " + str(id))
        self.UpdateUI()


#TODO:
#Popup when at station displaying door side and station name via beacon data
#Automatic light functionality
#Test ui?
#Test Fault Functionality between modules
#Somewhat functioning test ui? Use signals from train signals file?
#Passenger EBrake
#DO NOT OPEN TRAIN CONTROL UI IF YOU HAVEN'T DISPATCHED A TRAIN

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TrainController()
    widget.show()
    sys.exit(app.exec())
