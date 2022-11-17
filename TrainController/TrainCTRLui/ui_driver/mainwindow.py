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

class TrainController(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TrainController()
        self.ui.setupUi(self)


        #Initialization of internal variables
        self.Kp = 35
        self.Ki = 1

        self.maxPow = 120000 #120kW, per the Datasheet
        self.powOutput = 0
        self.temp = 70
        self.auth = True
        self.cmdSpd = 1
        self.curSpd = 0
        self.speedLim = 43
        self.driverCmd = 0
        self.dispatch = False
        
        self.engineFault = False
        self.trackSigFault = False
        self.brakeFault = False
        self.faultMode = False

        #initialize various button states and make them toggleable
        self.ui.manModeBtn.setCheckable(True)
        self.ui.manModeBtn.toggle()
        self.ui.manModeBtn.setChecked(True)

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
        self.ui.speedSlider.setMaximum(self.speedLim)

        #Button Connections
        self.ui.manModeBtn.clicked.connect(self.setManMode)
        self.ui.tempDial.sliderReleased.connect(self.tempAdjust)
        self.ui.speedSlider.sliderReleased.connect(self.setSpdSlider)
        self.ui.eBrakeBtn.clicked.connect(self.powerCalc)
        self.ui.sBrakeBtn.clicked.connect(self.powerCalc)
        
        #Light toggles
        self.ui.elightBtn.clicked.connect(self.eLights)
        self.ui.ilightBtn.clicked.connect(self.iLights)

        #Door toggles
        self.ui.rdoorBtn.clicked.connect(self.rDoors)
        self.ui.ldoorBtn.clicked.connect(self.lDoors)

        #Signals
        s.send_TrainCtrl_speed.connect(self.curSpdAdjust)
        s.send_TrackModel_next_block_info.connect(self.cmdSpdAdjust)
        s.send_TrackModel_block_info.connect(self.cmdSpdAdjust)

    
    #Manual Mode toggling function
    def setManMode(self):
        if not self.ui.manModeBtn.isChecked(): #Case for True
            self.ui.elightBtn.setDisabled(True)
            self.ui.ilightBtn.setDisabled(True)
            self.ui.rdoorBtn.setDisabled(True)
            self.ui.ldoorBtn.setDisabled(True)
            self.ui.sBrakeBtn.setDisabled(True)
            self.ui.speedSlider.setDisabled(True)
        else: #Case for False
            self.ui.elightBtn.setDisabled(False)
            self.ui.ilightBtn.setDisabled(False)
            self.ui.rdoorBtn.setDisabled(False)
            self.ui.ldoorBtn.setDisabled(False)
            self.ui.sBrakeBtn.setDisabled(False)
            self.ui.speedSlider.setDisabled(False)

    #Function to check if train is dispatched, and if not feed starting values
    # def isDispatched(self, id, info):
    #     if not self.dispatch:
    #         self.cmdSpd = int(info['commanded_speed']*0.621371)
    #         self.auth = info['authority']
    #         cmdStr = 'Commanded Speed: ' + str(self.cmdSpd) + ' MPH'
    #         self.ui.cmdSpd.setText(cmdStr)
    #         self.ui.speedSlider.setMaximum(self.cmdSpd)
    #         self.dispatch = True
    #         self.powerCalc()
    #     else:
    #         print('Already Dispatched')

    #Functions to send door signals
    def rDoors(self):
        s.send_TrainModel_rDoor.emit(self.ui.rdoorBtn.isChecked())
    def lDoors(self):
        s.send_TrainModel_lDoor.emit(self.ui.ldoorBtn.isChecked())

    #Functions to send light signals
    def eLights(self):
        s.send_TrainModel_eLight.emit(self.ui.elightBtn.isChecked())
    def iLights(self):
        s.send_TrainModel_iLight.emit(self.ui.ilightBtn.isChecked())

    #Function to adjust temp
    def tempAdjust(self):
        self.temp = self.ui.tempDial.value()
        tempStr = 'Current Temp: ' + str(self.temp) + 'F'
        self.ui.curTempLabel.setText(tempStr)
        s.send_TrainModel_temp.emit(self.temp)

    #Function to adjust commanded speed, is called externally
    def cmdSpdAdjust(self, id, info):
        self.cmdSpd = int(info['commanded_speed']*0.621371)
        self.auth = info['authority']
        self.dispatch = True
        cmdStr = 'Commanded Speed: ' + str(self.cmdSpd) + ' MPH'
        self.ui.cmdSpd.setText(cmdStr)
        if self.speedLim > self.cmdSpd:
            self.ui.speedSlider.setMaximum(self.cmdSpd)
        else:
            self.ui.speedSlider.setMaximum(self.speedLim)
        self.powerCalc()
    
    #Function to adjust current speed, is called externally
    def curSpdAdjust(self, spd):
        self.curSpd = spd
        curStr = 'Current Speed: ' + str((self.curSpd)*2.23694) + ' MPH'
        self.ui.curSpd.setText(curStr)
        self.powerCalc()

    #Function to adjust speed limit, is called externally
    def speedLimUpdate(self, lim):
        self.speedLim = lim
        if self.speedLim > self.cmdSpd:
            self.ui.speedSlider.setMaximum(self.cmdSpd)
        else:
            self.ui.speedSlider.setMaximum(self.speedLim)
        # self.powerCalc()

    #Function to adjust driver set speed based on slider in ui. Called internally when slider is adjusted
    def setSpdSlider(self):
        if not self.auth:
            dialog = trainDialog('Not authorized to travel on block, setting power to 0 and engaging sbrake')
            self.powOutput = 0
            self.ui.speedSlider.setDisabled(True)
            self.ui.speedSlider.setValue(0)
            self.ui.driverSpd.setText('0MPH')
            dialog.exec()
        else:
            if self.speedLim > self.cmdSpd:
                self.ui.speedSlider.setMaximum(self.cmdSpd)
            else:
                self.ui.speedSlider.setMaximum(self.speedLim)    
            self.driverCmd = self.ui.speedSlider.value()
            self.ui.driverSpd.setText(str(self.driverCmd)+'MPH')
            # self.powerCalc()

    #Major Power calculation and Velocity adjustment method
    def powerCalc(self):
        # print("powerCalc")
        if self.auth:
            if self.faultMode: #First checking for faults
                if self.trackSigFault:
                    self.ui.trackSigStatus.setText('Track Signal Status: NOT DETECTED')
                if self.engineFault:
                    self.ui.engFailStatus.setText('Engine Status: FAILING')
                if self.brakeFault:
                    self.ui.brakeFailStatus.setText('Brake Status: FAILING')
                self.faultDialog = trainDialog('Failure detected, setting power to 0 and engaging ebrake')
                self.powOutput = 0
                self.ui.eBrakeBtn.setChecked(True)
                #Send brake states to Train Model and display popup to user indicating fault
                s.send_TrainModel_eBrake.emit(self.ui.eBrakeBtn.isChecked())
                s.send_TrainModel_sBrake.emit(self.ui.sBrakeBtn.isChecked())
                self.faultDialog.show()

            else: #No Faults Found
                if self.ui.manModeBtn.isChecked(): #Base calculation on driver set speed if in manual mode
                    error_k = self.driverCmd/2.23694 - self.curSpd
                else: #Automatic mode case
                    error_k = self.cmdSpd*0.277778 - self.curSpd


                pow = self.Kp * error_k + self.Ki * self.curSpd

                #Automatic mode handling
                if not self.ui.manModeBtn.isChecked():
                    #If power becomes negative, set to 0 and engage SBrake
                    if pow < 0:
                        pow = 0
                        self.ui.sBrakeBtn.setChecked(True)
                        s.send_TrainModel_sBrake.emit(self.ui.sBrakeBtn.isChecked())
                    else:
                        if self.ui.sBrakeBtn.isChecked():
                            self.ui.sBrakeBtn.setChecked(False)
                    
                # print(self.cmdSpd, self.speedLim)
                # print("power", pow)
                # print("error", error_k)
                # print("speed", self.curSpd)

                #Check to make sure max power is not exceeded
                if pow > self.maxPow:
                    pow = self.maxPow
                    self.maxPowError = trainDialog('Max power exceeded, capping power output')
                    self.maxPowError.show()

                #Set power to 0 if brakes active
                if self.ui.eBrakeBtn.isChecked() or self.ui.sBrakeBtn.isChecked():
                    pow = 0
                    if self.ui.eBrakeBtn.isChecked():
                        self.ui.sBrakeBtn.setChecked(False)
                        #Send Brake State signals to train model
                        s.send_TrainModel_eBrake.emit(self.ui.eBrakeBtn.isChecked())
                        s.send_TrainModel_sBrake.emit(self.ui.sBrakeBtn.isChecked())
                    elif self.ui.sBrakeBtn.isChecked():
                        self.ui.eBrakeBtn.setChecked(False)
                        #Send Brake State signals to train model
                        s.send_TrainModel_eBrake.emit(self.ui.eBrakeBtn.isChecked())
                        s.send_TrainModel_sBrake.emit(self.ui.sBrakeBtn.isChecked())
                    else:
                        print('No Brakes Enabled, calculating power...')
                        
                
                self.powOutput = pow
                s.send_TrainModel_powerOutput.emit(self.powOutput)
        else:
            self.ui.sBrakeBtn.setChecked(True)
            s.send_TrainModel_sBrake.emit(self.ui.sBrakeBtn.isChecked())        
    
    #TODO:

        #Handle Service Brake operation in automatic mode.
    
        #Get beacon data, open proper doors and activate intercom (show dialog too)

        #Get passenger Ebrake activation, update power

        #Get info when underground, turn on ext lights
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TrainController()
    widget.show()
    sys.exit(app.exec())
