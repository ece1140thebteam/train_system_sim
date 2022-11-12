# This Python file uses the following encoding: utf-8
import sys

from PyQt6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyuic6 test_form.ui -o ui_testform.py, or
#     pyside2-uic test_form.ui -o ui_testform.py
from TrainController.TrainCTRLui.ui_driver.ui_testform import Ui_TrainCTRLTestUI
from TrainController.TrainCTRLui.ui_driver.mainwindow import TrainController

class TrainCTRLTestUI(QWidget):
    def __init__(self, TrainController, parent=None):
        super().__init__(parent)
        self.ui = Ui_TrainCTRLTestUI()
        self.ui.setupUi(self)

        self.Train = TrainController
        self.maxPow = 120000 #120kW, per the Datasheet
        self.powOutput = 0
        self.temp = 70
        self.auth = False
        self.cmdSpd = 0
        self.curSpd = 0
        self.speedLim = 40
        self.faultMode = False

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
        self.ui.authBox.setChecked(False)
        

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
    
    def authUpdate(self):
        if self.Train.auth == True:
            self.Train.auth = False
        else:
            self.Train.auth = True

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
        self.Train.cmdSpd = self.cmdSpd
        tempStr = 'Commanded Speed: ' + str(self.cmdSpd) + 'MPH'
        self.ui.cmdLabel.setText(tempStr)
        self.Train.cmdSpdAdjust()
        self.powUpdate

    def curInput(self):
        self.curSpd = self.ui.curSpdDial.value()
        self.Train.curSpd = self.curSpd
        tempStr = 'Current Speed: ' + str(self.curSpd) + 'MPH'
        self.ui.curInputLabel.setText(tempStr)
        self.Train.curSpdAdjust()
        self.powUpdate()

    def spdLimInput(self):
        self.speedLim = self.ui.spdLimDial.value()
        self.Train.speedLim = self.speedLim
        tempStr = 'Speed Limit: ' + str(self.speedLim) + 'MPH'
        self.ui.spdLimLabel.setText(tempStr)
        self.Train.powerCalc()
        self.powUpdate()
    
    def powUpdate(self):
        #Print statement to see the outputs that go to backend
        self.ui.cmdPowOutput.setText( 'Commanded Power Output: ' + str(self.Train.powOutput) + 'kW')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TrainCTRLTestUI()
    widget.show()
    sys.exit(app.exec())
