# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyuic6 form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_TrainController
from tctrl_dialog import trainDialog

class TrainController(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TrainController()
        self.ui.setupUi(self)

        

        self.Kp = 1
        self.Ki = 0.5

        self.maxPow = 120000 #120kW, per the Datasheet
        self.powOutput = 0
        self.temp = 70
        self.auth = False
        self.cmdSpd = 0
        self.curSpd = 0
        self.speedLim = 0
        self.driverCmd = 0
        
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
        self.ui.tempDial.valueChanged.connect(self.tempAdjust)
        self.ui.speedSlider.valueChanged.connect(self.setSpdSlider)
        self.ui.eBrakeBtn.clicked.connect(self.powerCalc)
        self.ui.sBrakeBtn.clicked.connect(self.powerCalc)

    
    #Mutator Functions
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

    def tempAdjust(self):
        self.temp = self.ui.tempDial.value()
        tempStr = 'Current Temp: ' + str(self.temp) + 'F'
        self.ui.curTempLabel.setText(tempStr)

    def cmdSpdAdjust(self):
        cmdStr = 'Commanded Speed: ' + str(self.cmdSpd) + ' MPH'
        self.ui.cmdSpd.setText(cmdStr)
        if self.speedLim > self.cmdSpd:
            self.ui.speedSlider.setMaximum(self.cmdSpd)
        else:
            self.ui.speedSlider.setMaximum(self.speedLim)
        self.powerCalc()
    
    def curSpdAdjust(self):
        curStr = 'Current Speed: ' + str(self.curSpd) + ' MPH'
        self.ui.curSpd.setText(curStr)
        self.powerCalc()

    def speedLimUpdate(self, lim):
        self.speedLim = lim
        if self.speedLim > self.cmdSpd:
            self.ui.speedSlider.setMaximum(self.cmdSpd)
        else:
            self.ui.speedSlider.setMaximum(self.speedLim)
        self.powerCalc()

    def setSpdSlider(self):
        if not self.auth:
            dialog = trainDialog('Not authorized to travel on block, setting power to 0 and engaging ebrake')
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
            self.curSpd = self.driverCmd
            self.powerCalc()

    #Major Power calculation and Velocity adjustment method
    def powerCalc(self):
        if self.faultMode:
            if self.trackSigFault:
                self.ui.trackSigStatus.setText('Track Signal Status: NOT DETECTED')
            if self.engineFault:
                self.ui.engFailStatus.setText('Engine Status: FAILING')
            if self.brakeFault:
                self.ui.brakeFailStatus.setText('Brake Status: FAILING')
            print('Failure detected, setting power to 0 and engaging ebrake')
            self.powOutput = 0
            self.ui.eBrakeBtn.setChecked(True)
        else:
            if self.ui.manModeBtn.isChecked():
                error_k = self.driverCmd - self.curSpd
            else:
                if self.cmdSpd > self.speedLim:
                    error_k = self.speedLim - self.curSpd
                else:
                    error_k = self.cmdSpd - self.curSpd

            pow = self.Kp * error_k + self.Ki * self.curSpd

            if pow > self.maxPow:
                pow = self.maxPow
                print('Max power exceeded, capping power output')

            if self.ui.eBrakeBtn.isChecked() or self.ui.sBrakeBtn.isChecked():
                pow = 0
                if self.ui.eBrakeBtn.isChecked():
                    brakeDialog = trainDialog('EBrake Engaged, power output set to 0')
                    self.ui.sBrakeBtn.setChecked(False)
                elif self.ui.sBrakeBtn.isChecked():
                    brakeDialog = trainDialog('SBrake Engaged, power output set to 0')
                    self.ui.eBrakeBtn.setChecked(False)
                else:
                    print('No Brakes Enabled, calculating power...')
                brakeDialog.exec()
            if pow < 0:
                pow = 0
                self.ui.sBrakeBtn.setChecked(True)
            else:
                self.powOutput = pow
    
    #Function used to interface with other modules/DB to get track signal
    def getCur(self, cur):
            self.curSpd = cur
            self.curSpdAdjust()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TrainController()
    widget.show()
    sys.exit(app.exec())
