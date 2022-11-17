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
      self.controllers = dict()
      # GUI connections
      self.uploadPLC1.clicked.connect(self.getFile1)
      self.uploadPLC2.clicked.connect(self.getFile2)
      self.uploadPLC3.clicked.connect(self.getFile3)
      self.blockSelect1.currentTextChanged.connect(self.displayController1Block)
      self.blockSelect2.currentTextChanged.connect(self.displayController2Block)
      self.blockSelect3.currentTextChanged.connect(self.displayController3Block)
      
      # signals from Track Model
      s.send_TrackModel_track_occupancy.connect(self.update_occupancy)
      s.send_TrackModel_tc_track_failure.connect(self.update_status)

      # signals from CTC
      s.send_CTC_authority.connect(self.update_authority) # [{'line':line, 'block':block, 'authority':0}]
      s.send_CTC_suggested_speed.connect(self.update_suggested_speed) # [{'line':line, 'block':block, 'speed':0}]
      s.send_CTC_maintenance_mode_signal.connect(self.update_maintenance_mode) # [{'line':line, 'block':block, 'mode':0}]
      s.send_CTC_switch_position_signal.connect(self.update_switch_position) # [{'line':line, 'block':block, 'switch':0}]
      #s.timer_tick.connect(self.handle_time_increment)

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



   # update block occupancy coming from track model
   def update_occupancy(self, line, block, occupancy):
      track_info[line][block]['occupancy'] = occupancy
      #s.send_TrackController_track_occupancy.emit({'line':line, 'block':block, 'occupancy':occupancy}) # ?????????????????????????????????
      self.run_controllerx(track_info[line][block]['controller'])
   


   # update block status (failures) coming from track model
   def update_status(self, line, block, failure):
      track_info[line][block]['failure'] = int(failure != 'None')
      if failure == 'None': failure = '' # ???????????????????????????????????????????????????????
      #s.send_CTC_test_failure.emit(line, block, failure) # !!!!!!!!!!!!!
      self.run_controllerx(track_info[line][block]['controller'])



   # update block authority coming from ctc
   def update_authority(self, updates_list):
      controllers_to_update = []
      for update in updates_list:
         line = update['line']
         block = update['block']
         authority = update['authority']

         controller = track_info[line][block]['controller']
         if controller not in controllers_to_update: 
            controllers_to_update.append(controller)

         track_info[line][block]['authority'] = authority

      for controller in controllers_to_update:
         self.run_controllerx(controller)



   # update block suggested speed coming from ctc
   def update_suggested_speed(self, updates_list):
      controllers_to_update = []
      for update in updates_list:
         line = update['line']
         block = update['block']
         speed = update['speed']

         controller = track_info[line][block]['controller']
         if controller not in controllers_to_update: 
            controllers_to_update.append(controller)

         track_info[line][block]['suggested_speed'] = speed

      for controller in controllers_to_update:
         self.run_controllerx(controller)



   # update block maintenance coming from ctc
   def update_maintenance_mode(self, updates_list):
      controllers_to_update = []
      for update in updates_list:
         line = update['line']
         block = update['block']
         maintenance = update['mode']

         track_info[line][block]['maintenance'] = maintenance
         
         controller = track_info[line][block]['controller']
         if controller not in controllers_to_update: 
            controllers_to_update.append(controller)

         #s.send_TrackModel_maintenance_status.emit(line, block, maintenance==1)
         
      for controller in controllers_to_update:
         self.run_controllerx(controller)



   # update manual switch positions coming from ctc
   def update_switch_position(self, updates_list):
      controllers_to_update = []
      for update in updates_list:
         line = update['line']
         block = update['block']
         sw = update['switch']
         track_info[line][block]['switch'] = sw

         controller = track_info[line][block]['controller']
         if controller not in controllers_to_update: 
            controllers_to_update.append(controller)

         #s.send_TrackController_switch_pos.emit(line, block, sw)

      for controller in controllers_to_update:
         self.run_controllerx(controller)



   def run_controllerx(self, controller_num):
      print(self.controllers)
      print(controller_num)
      if controller_num in self.controllers:
         print(self.controllers[controller_num])
         print(f'running wayside controller {controller_num}')

         for statement in self.controllers[controller_num]:
            exec(statement)
      else:
         print('no plc uploaded for that controllers')
      #TODO IMPLEMENT THE DIFFERENT CONTROLLERS

      if controller_num == 1:
         if track_info['Green'][0]['occupancy'] == 1:
            track_info['Green'][63]['switch'] == 1

   



   def getFile1(self):
      filename = QFileDialog.getOpenFileName(self, "Select PLC Script", "", "Text Files (*.txt)")

      self.controllers[1] = []
      if filename[0] != '':
         with open(filename[0], 'r') as file:
            self.controllers[1] = file.readlines()
            plc = ''
            for line in self.controllers[1]: plc+=line
            self.displayPLC1.setText(plc)
      print(self.controllers[1])


   def getFile2(self):
      filename = QFileDialog.getOpenFileName(self, "Select PLC Script", "", "Text Files (*.txt)")

      self.controllers[2] = []
      if filename[0] != '':
         with open(filename[0], 'r') as file:
            self.controllers[2] = file.readlines()
            plc = ''
            for line in self.controllers[2]: plc+=line
            self.displayPLC2.setText(file.read())
      print(self.controllers[2])


   def getFile3(self):

      filename = QFileDialog.getOpenFileName(self, "Select PLC Script", "", "Text Files (*.txt)")

      self.controllers[3] = []
      if filename[0] != '':
         with open(filename[0], 'r') as file:
            self.controllers[3] = file.readlines()
            plc = ''
            for line in self.controllers[3]: plc+=line
            self.displayPLC3.setText(file.read())
      print(self.controllers[3])







if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec())



