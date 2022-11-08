# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyuic6 test_form.ui -o ui_testform.py, or
#     pyside2-uic test_form.ui -o ui_testform.py
from ui_testform import Ui_TrainCTRLTestUI

class TrainCTRLTestUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TrainCTRLTestUI()
        self.ui.setupUi(self)

        self.maxPow = 120000 #120kW, per the Datasheet
        self.powOutput = 0
        self.temp = 70
        self.auth = True
        self.cmdSpd = 0
        self.curSpd = 0
        self.speedLim = 40

        #initialize various button states and make them toggleable
        self.ui.manModeBtn.setCheckable(True)
        self.ui.manModeBtn.toggle()
        self.ui.manModeBtn.setChecked(True)

        self.ui.activateEFault.setCheckable(True)
        self.ui.activateEFault.toggle()
        self.ui.activateEFault.setChecked(False)

        self.ui.activateBFault.setCheckable(True)
        self.ui.activateBFault.toggle()
        self.ui.activateBFault.setChecked(False)

        self.ui.activateSFault.setCheckable(True)
        self.ui.activateSFault.toggle()
        self.ui.activateSFault.setChecked(False)

        #Initializing values for display
        self.ui.cmdPowOutput.setText('Commanded Power Output: 0.0kW')
        
        self.ui.cmdSpdDial.setValue(0)
        self.ui.cmdLabel.setText('Commanded Speed: 0MPH')

        self.ui.curSpdDial.setValue(0)
        self.ui.curInputLabel.setText('Current Speed: 0MPH')

        self.ui.spdLimDial.setValue(0)
        self.ui.spdLimLabel.setText('Speed Limit: 0MPH')
        

        #Button Connections
        self.ui.cmdSpdDial.valueChanged.connect(self.cmdSpdAdjust)
        self.ui.curSpdDial.valueChanged.connect(self.curInput)
        self.ui.spdLimDial.valueChanged.connect(self.spdLimInput)
        self.ui.activateEFault.clicked.connect(self.EFaultHandler)
        self.ui.activateBFault.clicked.connect(self.BFaultHandler)
        self.ui.activateSFault.clicked.connect(self.SFaultHandler)
        self.ui.authBox.clicked.connect(self.authUpdate)
        self.ui.faultReset.clicked.connect(self.faultReset)

    #Fault Handler Function
    #Called when a fault mode is triggered through the test ui, sets fault mode to true
    #and disables the rest of the buttons
    def EFaultHandler(self):
        self.faultMode = True
        self.ui.activateBFault.setDisabled(True)
        self.ui.activateSFault.setDisabled(True)
    
    def authUpdate():
        print('Authority removed from train')

    def BFaultHandler(self):
        self.faultMode = True
        self.ui.activateEFault.setDisabled(True)
        self.ui.activateSFault.setDisabled(True)

    def SFaultHandler(self):
        self.faultMode = True
        self.ui.activateEFault.setDisabled(True)
        self.ui.activateBFault.setDisabled(True)

    def faultReset(self):
        self.faultMode = False
        self.ui.activateBFault.setEnabled(True)
        self.ui.activateEFault.setEnabled(True)
        self.ui.activateSFault.setEnabled(True)

    def cmdSpdAdjust(self):
        self.cmdSpd = self.ui.cmdSpdDial.value()
        tempStr = 'Commanded Speed: ' + str(self.cmdSpd) + 'MPH'
        self.ui.cmdLabel.setText(tempStr)
        #self.powerCalc()

    def curInput(self):
        self.curSpd = self.ui.curSpdDial.value()
        tempStr = 'Current Speed: ' + str(self.curSpd) + 'MPH'
        self.ui.curInputLabel.setText(tempStr)
        #self.powerCalc()

    def spdLimInput(self):
        self.speedLim = self.ui.spdLimDial.value()
        tempStr = 'Speed Limit: ' + str(self.speedLim) + 'MPH'
        self.ui.spdLimLabel.setText(tempStr)
        #self.powerCalc()


    #Major Power calculation and Velocity adjustment method

    #def powerCalc(self):
     #   if self.faultMode:
      #      print('Failure detected, setting power to 0 and engaging ebrake')
       #     self.powOutput = 0
        #    self.ui.eBrakeBtn.setChecked(True)
        #else:
        #    if self.ui.manModeBtn.isChecked():
        #        error_k = self.driverCmd - self.curSpd
        #    else:
        ##        if self.cmdSpd > self.speedLim:
         #           error_k = self.speedLim - self.curSpd
         #       else:
         #           error_k = self.cmdSpd - self.curSpd

            #pow = self.Kp * error_k + self.Ki * self.curSpd

            #if pow > self.maxPow:
            #    pow = self.maxPow
            #    print('Max power exceeded, capping power output')

            #if self.ui.eBrakeBtn.isChecked() or self.ui.sBrakeBtn.isChecked():
             #   pow = 0
              #  if self.ui.eBrakeBtn.isChecked():
               #     print('EBrake Engaged, power output set to 0')
                #    self.ui.sBrakeBtn.setChecked(False)
                #elif self.ui.sBrakeBtn.isChecked():
                 #   print('SBrake Engaged, power output set to 0')
                  #  self.ui.eBrakeBtn.setChecked(False)
                #else:
                 #   print('Brake Case got triggered but no brakes are on!')

            #if pow < 0:
             #   pow = 0
              #  self.ui.sBrakeBtn.setChecked(True)
            #else:
             #   self.powOutput = pow

            #Print statement to see the outputs that go to backend
            #self.ui.cmdPowOutput.setText(
             #   'Commanded Power Output: ' + str(self.powOutput) + 'kW')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TrainCTRLTestUI()
    widget.show()
    sys.exit(app.exec())
