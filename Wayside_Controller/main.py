# Cassandra Oliva
# Main python file for Wayside Controllers

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# signals used to communicate between modules
from signals import s

from Wayside_Controller.ui import WaysideMainUI as WaysideMainUI    # import UI
from Wayside_Controller.blockInfo import track_info as track_info

class MainWindow(QMainWindow, WaysideMainUI.Ui_MainWindow):
   def __init__(self, parent=None):
      super(MainWindow, self).__init__(parent)
      self.setupUi(self)

      # GUI connections
      self.uploadPLC1.clicked.connect(self.getFile1)
      self.blockSelect1.currentTextChanged.connect(self.displayController1Block)
      self.blockSelect2.currentTextChanged.connect(self.displayController2Block)
      self.blockSelect3.currentTextChanged.connect(self.displayController3Block)

      # Allocate blocks with corresponding controller
      for line in track_info:
         if line == 'Red':
            pass
         elif line == 'Green':
            for block in track_info[line]:
               if block == 0 or (block >= 36 and block <= 73):
                     track_info['Green'][block]['controller'] = 1
                     self.blockSelect1.addItem(str(block))
               elif block >= 74 and block <= 143:
                  track_info['Green'][block]['controller'] = 2
                  self.blockSelect2.addItem(str(block))
               elif (block >= 1 and block <= 35) or (block >= 144 and block <= 150):
                  track_info['Green'][block]['controller'] = 3
                  self.blockSelect3.addItem(str(block))

            
      #s.timer_tick.connect(self.handle_time_increment)
      #s.send_CTC_switch_position_signal.connect(self.update_switch_position)

   # controller 1 GUI
   def displayController1Block(self, blockText):
      
      block = int(blockText)
      
      # displays Switch Positions
      if track_info['Green'][block]['switch_pos'] == 0: # default position
         if block == 57:
            self.switchFromValue1.setText('57')
            self.switchToValue1.setText('58')
         elif block == 63:
            self.switchFromValue1.setText('63')
            self.switchToValue1.setText('62')
      elif track_info['Green'][block]['switch_pos'] == 1: # nondefault position
         if block == 57:
            self.switchFromValue1.setText('57')
            self.switchToValue1.setText('Yard')
         elif block == 63:
            self.switchFromValue1.setText('63')
            self.switchToValue1.setText('Yard')
      else:
         self.switchFromValue1.setText(track_info['Green'][block]['switch_pos'])
         self.switchToValue1.setText(track_info['Green'][block]['switch_pos'])


      # displays Traffic Light Colors
      if track_info['Green'][block]['traffic_light'] == 0:
         self.trafficLightValue1.setText('Red')
      elif track_info['Green'][block]['traffic_light'] == 1:
         self.trafficLightValue1.setText('Green')
      else:
         self.trafficLightValue1.setText(track_info['Green'][block]['traffic_light'])


      # displays Track Status
      if track_info['Green'][block]['failure'] == 0:
         self.statusValue1.setText('Normal')
      elif track_info['Green'][block]['failure'] == 1:
         self.statusValue1.setText('Failure')


      # displays Track Maintenance
      if track_info['Green'][block]['maintenance'] == 0:
         self.maintenanceValue1.setText('Off')
      else:
         self.maintenanceValue1.setText('On')

      
      # displays Authority, Occupancy, Suggested Speed, Commanded Speed, and Railway Crossings
      self.authorityValue1.setText(str(track_info['Green'][block]['authority']))
      self.occupancyValue1.setText(str(track_info['Green'][block]['occupancy']))
      self.suggestedSpeedValue1.setText(str(track_info['Green'][block]['suggested_speed']))
      self.commandedSpeedValue1.setText(str(track_info['Green'][block]['commanded_speed']))
      self.railwayGateValue1.setText(track_info['Green'][block]['track_crossing'])
      self.railwayLightsValue1.setText(track_info['Green'][block]['track_crossing'])



   # controller 2 GUI
   def displayController2Block(self, blockText):
      
      block = int(blockText)
      
      # displays Switch Positions
      if track_info['Green'][block]['switch_pos'] == 0: # default position
         if block == 77:
            self.switchFromValue2.setText('77')
            self.switchToValue2.setText('76')
         elif block == 85:
            self.switchFromValue2.setText('85')
            self.switchToValue2.setText('86')
      elif track_info['Green'][block]['switch_pos'] == 1: # nondefault position
         if block == 77:
            self.switchFromValue2.setText('77')
            self.switchToValue2.setText('101')
         elif block == 85:
            self.switchFromValue2.setText('85')
            self.switchToValue2.setText('100')
      else:
         self.switchFromValue2.setText(track_info['Green'][block]['switch_pos'])
         self.switchToValue2.setText(track_info['Green'][block]['switch_pos'])


      # displays Traffic Light Colors
      if track_info['Green'][block]['traffic_light'] == 0:
         self.trafficLightValue2.setText('Red')
      elif track_info['Green'][block]['traffic_light'] == 1:
         self.trafficLightValue2.setText('Green')
      else:
         self.trafficLightValue2.setText(track_info['Green'][block]['traffic_light'])


      # displays Track Status
      if track_info['Green'][block]['failure'] == 0:
         self.statusValue2.setText('Normal')
      elif track_info['Green'][block]['failure'] == 1:
         self.statusValue2.setText('Failure')


      # displays Track Maintenance
      if track_info['Green'][block]['maintenance'] == 0:
         self.maintenanceValue2.setText('Off')
      else:
         self.maintenanceValue2.setText('On')

      
      # displays Authority, Occupancy, Suggested Speed, Commanded Speed, and Railway Crossings
      self.authorityValue2.setText(str(track_info['Green'][block]['authority']))
      self.occupancyValue2.setText(str(track_info['Green'][block]['occupancy']))
      self.suggestedSpeedValue2.setText(str(track_info['Green'][block]['suggested_speed']))
      self.commandedSpeedValue2.setText(str(track_info['Green'][block]['commanded_speed']))
      self.railwayGateValue2.setText(track_info['Green'][block]['track_crossing'])
      self.railwayLightsValue2.setText(track_info['Green'][block]['track_crossing'])



   # controller 3 GUI
   def displayController3Block(self, blockText):
     
      block = int(blockText)

      # displays Railway Crossings
      if track_info['Green'][block]['track_crossing'] == 0: # railway crossing inactive
         self.railwayGateValue3.setText('Up')
         self.railwayLightsValue3.setText('Off')
      elif track_info['Green'][block]['track_crossing'] == 1: # railway crossing active
         self.railwayGateValue3.setText('Down')
         self.railwayLightsValue3.setText('On')
      else: # railway crossing does not exist for this block
         self.railwayGateValue3.setText(track_info['Green'][block]['track_crossing'])
         self.railwayLightsValue3.setText(track_info['Green'][block]['track_crossing'])

      
      # displays Switch Positions
      if track_info['Green'][block]['switch_pos'] == 0: # default position
         if block == 13:
            self.switchFromValue3.setText('13')
            self.switchToValue3.setText('12')
         elif block == 28:
            self.switchFromValue3.setText('28')
            self.switchToValue3.setText('29')
      elif track_info['Green'][block]['switch_pos'] == 1: # nondefault position
         if block == 13:
            self.switchFromValue3.setText('13')
            self.switchToValue3.setText('1')
         elif block == 28:
            self.switchFromValue3.setText('28')
            self.switchToValue3.setText('150')
      else:
         self.switchFromValue3.setText(track_info['Green'][block]['switch_pos'])
         self.switchToValue3.setText(track_info['Green'][block]['switch_pos'])


      # displays Traffic Light Colors
      if track_info['Green'][block]['traffic_light'] == 0:
         self.trafficLightValue3.setText('Red')
      elif track_info['Green'][block]['traffic_light'] == 1:
         self.trafficLightValue3setText('Green')
      else:
         self.trafficLightValue3.setText(track_info['Green'][block]['traffic_light'])


      # displays Track Status
      if track_info['Green'][block]['failure'] == 0:
         self.statusValue3.setText('Normal')
      elif track_info['Green'][block]['failure'] == 1:
         self.statusValue3.setText('Failure')


      # displays Track Maintenance
      if track_info['Green'][block]['maintenance'] == 0:
         self.maintenanceValue3.setText('Off')
      else:
         self.maintenanceValue3.setText('On')

      
      # displays Authority, Occupancy, Suggested Speed, and Commanded Speed
      self.authorityValue3.setText(str(track_info['Green'][block]['authority']))
      self.occupancyValue3.setText(str(track_info['Green'][block]['occupancy']))
      self.suggestedSpeedValue3.setText(str(track_info['Green'][block]['suggested_speed']))
      self.commandedSpeedValue3.setText(str(track_info['Green'][block]['commanded_speed']))



   def update_switch_position(self, list):
      pass

   def handle_time_increment(self):
      # print('hi')
      pass

   def getFile1(self):

      filename = QFileDialog.getOpenFileName(self, "Select PLC Script", "", "Text Files (*.txt)")

      if filename[0] != '':
         with open(filename[0], 'r') as file:
            self.displayPLC1.setText(file.read())


def run_plc1():
   pass
    #switch_pos = track["Red"][0]['authority'] && track["Red"][0]['authority'] && 

def run_controller_x(controller_num):
    if controller_num == 1:
        run_plc1()

def update_occupancy(line, block, occ):
    track_info[line][block]['occupancy'] = occ

    run_controller_x(track_info[line][block]['controller'])





if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec())



