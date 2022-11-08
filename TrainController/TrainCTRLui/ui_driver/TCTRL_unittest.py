#Unit testing for Train Controller
import unittest
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from mainwindow import TrainController

class TrainCTRLUnitTester(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        app = QApplication(sys.argv)
        self.testTrain = TrainController()
    
    #Testing that current speed is updated both internally and visually when it receives a new speed
    #from track signal
    def test_CurSpd(self):
        self.assertEqual(self.testTrain.curSpd, 0)
        self.assertEqual(self.testTrain.ui.curSpd.text(), 'Current Speed: 0 MPH')
        self.testTrain.getCur(70)
        self.assertEqual(self.testTrain.curSpd,70)
        self.assertEqual(self.testTrain.ui.curSpd.text(), 'Current Speed: 70 MPH')
    
    #Testing that manual mode is able to be enabled/disabled
    def test_ManualMode(self):
        self.testTrain.ui.manModeBtn.setChecked(False)
        self.testTrain.setManMode()
        self.assertFalse(self.testTrain.ui.manModeBtn.isChecked())
        self.assertFalse(self.testTrain.ui.elightBtn.isEnabled())
        self.assertFalse(self.testTrain.ui.ilightBtn.isEnabled())
        self.assertFalse(self.testTrain.ui.rdoorBtn.isEnabled())
        self.assertFalse(self.testTrain.ui.ldoorBtn.isEnabled())
        self.assertFalse(self.testTrain.ui.sBrakeBtn.isEnabled())
        self.assertFalse(self.testTrain.ui.speedSlider.isEnabled())

        self.testTrain.ui.manModeBtn.setChecked(True)
        self.testTrain.setManMode()
        self.assertTrue(self.testTrain.ui.manModeBtn.isChecked())
        self.assertTrue(self.testTrain.ui.elightBtn.isEnabled())
        self.assertTrue(self.testTrain.ui.ilightBtn.isEnabled())
        self.assertTrue(self.testTrain.ui.rdoorBtn.isEnabled())
        self.assertTrue(self.testTrain.ui.ldoorBtn.isEnabled())
        self.assertTrue(self.testTrain.ui.sBrakeBtn.isEnabled())
        self.assertTrue(self.testTrain.ui.speedSlider.isEnabled())
    
    #Testing that an engine fault detection sets output power to 0 and engages the emergency brake
    def test_EngineFault(self):
        self.testTrain.faultMode = True
        self.testTrain.engineFault = True
        self.testTrain.powerCalc()

        self.assertEqual(self.testTrain.powOutput, 0)
        self.assertEqual(self.testTrain.ui.eBrakeBtn.isChecked(), True)

if __name__ == '__main__':
    unittest.main()