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

      # TODO: initialize all waysides by running all PLC scripts

      # GUI connections
      self.uploadPLC1.clicked.connect(self.getFile1)
      self.uploadPLC2.clicked.connect(self.getFile2)
      self.uploadPLC3.clicked.connect(self.getFile3)
      #self.uploadPLC4.clicked.connect(self.getFile4)
      #self.uploadPLC5.clicked.connect(self.getFile5)
      #self.uploadPLC6.clicked.connect(self.getFile6)

      self.blockSelect1.currentTextChanged.connect(self.displayController1Blocks)
      self.blockSelect2.currentTextChanged.connect(self.displayController2Blocks)
      self.blockSelect3.currentTextChanged.connect(self.displayController3Blocks)
      self.blockSelect4.currentTextChanged.connect(self.displayController4Blocks)
      self.blockSelect5.currentTextChanged.connect(self.displayController5Blocks)
      self.blockSelect6.currentTextChanged.connect(self.displayController6Blocks)
      
      
      # signals from CTC
      s.send_CTC_authority.connect(self.update_authority) # [{'line':line, 'block':block, 'authority':0}]
      s.send_CTC_suggested_speed.connect(self.update_suggested_speed) # [{'line':line, 'block':block, 'speed':0}]
      s.send_CTC_maintenance_mode_signal.connect(self.update_maintenance_mode) # [{'line':line, 'block':block, 'mode':0}]
      s.send_CTC_switch_position_signal.connect(self.update_switch_position) # [{'line':line, 'block':block, 'switch':0}]
      #s.timer_tick.connect(self.handle_time_increment)
      
      # signals from Track Model
      s.send_TrackModel_track_occupancy.connect(self.update_occupancy) #line, block, occupancy (true for occupied)
      s.send_TrackModel_tc_track_failure.connect(self.update_status) #line, block, failure str


      # Allocate blocks with corresponding controller
      for line in track_info:
         if line == 'Green':
            for block in track_info[line]:
               if block == 0 or (block >= 36 and block <= 73):
                     track_info[line][block]['controller'] = 1
                     self.blockSelect1.addItem(str(block))
               elif block >= 74 and block <= 143:
                  track_info[line][block]['controller'] = 2
                  self.blockSelect2.addItem(str(block))
               elif (block >= 1 and block <= 35) or (block >= 144 and block <= 150):
                  track_info[line][block]['controller'] = 3
                  self.blockSelect3.addItem(str(block))
         elif line == 'Red':
            for block in track_info[line]:
               if (block >= 0 and block <= 30) or block == 76:
                     track_info[line][block]['controller'] = 4
                     self.blockSelect4.addItem(str(block))
               elif (block >= 31 and block <= 40) or (block >= 71 and block <= 75):
                  track_info[line][block]['controller'] = 5
                  self.blockSelect5.addItem(str(block))
               elif (block >= 41 and block <= 70):
                  track_info[line][block]['controller'] = 6
                  self.blockSelect6.addItem(str(block))


   # CONTROLLER 1 GUI
   def displayController1Blocks(self, blockText):
      
      block = int(blockText)
      
      # displays Switch Positions
      if track_info['Green'][block]['switch_pos'] == 0: # default position
         if block == 57:
            self.switchFromValue1.setText('57')
            self.switchToValue1.setText('Yard')
         elif block == 63:
            self.switchFromValue1.setText('63')
            self.switchToValue1.setText('Yard')
      elif track_info['Green'][block]['switch_pos'] == 1: # nondefault position
         if block == 57:
            self.switchFromValue1.setText('57')
            self.switchToValue1.setText('58')
         elif block == 63:
            self.switchFromValue1.setText('63')
            self.switchToValue1.setText('62')
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



   # CONTROLLER 2 GUI
   def displayController2Blocks(self, blockText):
      
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



   # CONTROLLER 3 GUI
   def displayController3Blocks(self, blockText):
     
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
            self.switchToValue3.setText('1')
         elif block == 28:
            self.switchFromValue3.setText('28')
            self.switchToValue3.setText('29')
      elif track_info['Green'][block]['switch_pos'] == 1: # nondefault position
         if block == 13:
            self.switchFromValue3.setText('13')
            self.switchToValue3.setText('12')
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
         self.trafficLightValue3.setText('Green')
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



   # CONTROLLER 4 GUI
   def displayController4Blocks(self, blockText):
      
      block = int(blockText)
      
      # displays Switch Positions
      if track_info['Red'][block]['switch_pos'] == 0: # default position
         if block == 9:
            self.switchFromValue4.setText('9')
            self.switchToValue4.setText('Yard')
         elif block == 16:
            self.switchFromValue4.setText('16')
            self.switchToValue4.setText('1')
         elif block == 27:
            self.switchFromValue4.setText('27')
            self.switchToValue4.setText('28')
      elif track_info['Red'][block]['switch_pos'] == 1: # nondefault position
         if block == 9:
            self.switchFromValue4.setText('9')
            self.switchToValue4.setText('10')
         elif block == 16:
            self.switchFromValue4.setText('16')
            self.switchToValue4.setText('15')
         elif block == 27:
            self.switchFromValue4.setText('27')
            self.switchToValue4.setText('76')
      else:
         self.switchFromValue4.setText(track_info['Red'][block]['switch_pos'])
         self.switchToValue4.setText(track_info['Red'][block]['switch_pos'])


      # displays Traffic Light Colors
      if track_info['Red'][block]['traffic_light'] == 0:
         self.trafficLightValue4.setText('Red')
      elif track_info['Red'][block]['traffic_light'] == 1:
         self.trafficLightValue4.setText('Green')
      else:
         self.trafficLightValue4.setText(track_info['Red'][block]['traffic_light'])


      # displays Track Status
      if track_info['Red'][block]['failure'] == 0:
         self.statusValue4.setText('Normal')
      elif track_info['Red'][block]['failure'] == 1:
         self.statusValue4.setText('Failure')


      # displays Track Maintenance
      if track_info['Red'][block]['maintenance'] == 0:
         self.maintenanceValue4.setText('Off')
      else:
         self.maintenanceValue4.setText('On')
      

      # displays Authority, Occupancy, Suggested Speed, Commanded Speed, and Railway Crossings
      self.authorityValue4.setText(str(track_info['Red'][block]['authority']))
      self.occupancyValue4.setText(str(track_info['Red'][block]['occupancy']))
      self.suggestedSpeedValue4.setText(str(track_info['Red'][block]['suggested_speed']))
      self.commandedSpeedValue4.setText(str(track_info['Red'][block]['commanded_speed']))
      self.railwayGateValue4.setText(track_info['Red'][block]['track_crossing'])
      self.railwayLightsValue4.setText(track_info['Red'][block]['track_crossing'])



   # CONTROLLER 5 GUI
   def displayController5Blocks(self, blockText):
      
      block = int(blockText)
      
      # displays Switch Positions
      if track_info['Red'][block]['switch_pos'] == 0: # default position
         if block == 33:
            self.switchFromValue5.setText('33')
            self.switchToValue5.setText('32')
         elif block == 38:
            self.switchFromValue5.setText('38')
            self.switchToValue5.setText('39')
      elif track_info['Red'][block]['switch_pos'] == 1: # nondefault position
         if block == 33:
            self.switchFromValue5.setText('33')
            self.switchToValue5.setText('72')
         elif block == 38:
            self.switchFromValue5.setText('38')
            self.switchToValue5.setText('71')
      else:
         self.switchFromValue5.setText(track_info['Red'][block]['switch_pos'])
         self.switchToValue5.setText(track_info['Red'][block]['switch_pos'])


      # displays Traffic Light Colors
      if track_info['Red'][block]['traffic_light'] == 0:
         self.trafficLightValue5.setText('Red')
      elif track_info['Red'][block]['traffic_light'] == 1:
         self.trafficLightValue5.setText('Green')
      else:
         self.trafficLightValue5.setText(track_info['Red'][block]['traffic_light'])


      # displays Track Status
      if track_info['Red'][block]['failure'] == 0:
         self.statusValue5.setText('Normal')
      elif track_info['Red'][block]['failure'] == 1:
         self.statusValue5.setText('Failure')


      # displays Track Maintenance
      if track_info['Red'][block]['maintenance'] == 0:
         self.maintenanceValue5.setText('Off')
      else:
         self.maintenanceValue5.setText('On')

      
      # displays Authority, Occupancy, Suggested Speed, Commanded Speed, and Railway Crossings
      self.authorityValue5.setText(str(track_info['Red'][block]['authority']))
      self.occupancyValue5.setText(str(track_info['Red'][block]['occupancy']))
      self.suggestedSpeedValue5.setText(str(track_info['Red'][block]['suggested_speed']))
      self.commandedSpeedValue5.setText(str(track_info['Red'][block]['commanded_speed']))
      self.railwayGateValue5.setText(track_info['Red'][block]['track_crossing'])
      self.railwayLightsValue5.setText(track_info['Red'][block]['track_crossing'])



   # CONTROLLER 6 GUI
   def displayController6Blocks(self, blockText):
     
      block = int(blockText)

      # displays Railway Crossings
      if track_info['Red'][block]['track_crossing'] == 0: # railway crossing inactive
         self.railwayGateValue6.setText('Up')
         self.railwayLightsValue6.setText('Off')
      elif track_info['Red'][block]['track_crossing'] == 1: # railway crossing active
         self.railwayGateValue6.setText('Down')
         self.railwayLightsValue6.setText('On')
      else: # railway crossing does not exist for this block
         self.railwayGateValue6.setText(track_info['Red'][block]['track_crossing'])
         self.railwayLightsValue6.setText(track_info['Red'][block]['track_crossing'])

      
      # displays Switch Positions
      if track_info['Red'][block]['switch_pos'] == 0: # default position
         if block == 44:
            self.switchFromValue6.setText('44')
            self.switchToValue6.setText('43')
         elif block == 52:
            self.switchFromValue6.setText('52')
            self.switchToValue6.setText('53')
      elif track_info['Red'][block]['switch_pos'] == 1: # nondefault position
         if block == 44:
            self.switchFromValue6.setText('44')
            self.switchToValue6.setText('67')
         elif block == 52:
            self.switchFromValue6.setText('52')
            self.switchToValue6.setText('66')
      else:
         self.switchFromValue6.setText(track_info['Red'][block]['switch_pos'])
         self.switchToValue6.setText(track_info['Red'][block]['switch_pos'])


      # displays Traffic Light Colors
      if track_info['Red'][block]['traffic_light'] == 0:
         self.trafficLightValue6.setText('Red')
      elif track_info['Red'][block]['traffic_light'] == 1:
         self.trafficLightValue6.setText('Green')
      else:
         self.trafficLightValue6.setText(track_info['Red'][block]['traffic_light'])


      # displays Track Status
      if track_info['Red'][block]['failure'] == 0:
         self.statusValue6.setText('Normal')
      elif track_info['Red'][block]['failure'] == 1:
         self.statusValue6.setText('Failure')


      # displays Track Maintenance
      if track_info['Red'][block]['maintenance'] == 0:
         self.maintenanceValue6.setText('Off')
      else:
         self.maintenanceValue6.setText('On')

      
      # displays Authority, Occupancy, Suggested Speed, and Commanded Speed
      self.authorityValue6.setText(str(track_info['Red'][block]['authority']))
      self.occupancyValue6.setText(str(track_info['Red'][block]['occupancy']))
      self.suggestedSpeedValue6.setText(str(track_info['Red'][block]['suggested_speed']))
      self.commandedSpeedValue6.setText(str(track_info['Red'][block]['commanded_speed']))



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
         track_info[line][block]['commanded_speed'] = speed  # set suggested_speed as commanded_speed by default, but this will change if needed in run_controllerx

      for controller in controllers_to_update:
         self.run_controllerx(controller)



   # update block maintenance coming from ctc
   def update_maintenance_mode(self, updates_list):
      controllers_to_update = []
      for update in updates_list:
         line = update['line']
         block = update['block']
         maintenance = update['mode']
         
         controller = track_info[line][block]['controller']
         if controller not in controllers_to_update: 
            controllers_to_update.append(controller)

         track_info[line][block]['maintenance'] = maintenance
         
      for controller in controllers_to_update:
         self.run_controllerx(controller)



   # update manual switch positions coming from ctc
   def update_switch_position(self, updates_list):
      for update in updates_list:
         line = update['line']
         block = update['block']
         switch = update['switch']

         controller = track_info[line][block]['controller']
         maintenance = track_info[line][block]['maintenance']
         
         # if block is in maintenance mode, allow CTC to set switch position by overriding PLC logic
         if (maintenance == 1): # SAFETY CRITICAL: can NOT manually set switch position if maintenance mode is off!
            track_info[line][block]['switch_pos'] = switch
            s.send_TrackController_switch_pos.emit(line, block, switch)



   # update block occupancy coming from track model
   def update_occupancy(self, line, block, occupancy):
      track_info[line][block]['occupancy'] = occupancy
      self.run_controllerx(track_info[line][block]['controller'])
   


   # update block status (failures) coming from track model
   def update_status(self, line, block, failure):
      track_info[line][block]['failure'] = int(failure != 'None')
      self.run_controllerx(track_info[line][block]['controller'])


   # run PLC script for specified controller
   def run_controllerx(self, controller_num):
         
      # TODO: ACTUALLY EXECUTE PLC .TXT FILE
      #for statement in self.controllers[controller_num]:
      #   exec(statement)

      for line in track_info:
         for block in track_info[line]:
            if track_info[line][block]['controller'] == controller_num: # only emit signals for blocks in corresponding controller
               
               if track_info[line][block]['switch_pos']!='-':
                  s.send_TrackController_switch_pos.emit(line, block, track_info[line][block]['switch_pos'])

               #s.send_TrackModel_block_authority.emit(line, block, authority)
               #s.send_TrackModel_commanded_speed.emit(line, block, int(speed))
      

   



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
            self.displayPLC2.setText(plc)
      print(self.controllers[2])


   def getFile3(self):

      filename = QFileDialog.getOpenFileName(self, "Select PLC Script", "", "Text Files (*.txt)")

      self.controllers[3] = []
      if filename[0] != '':
         with open(filename[0], 'r') as file:
            self.controllers[3] = file.readlines()
            plc = ''
            for line in self.controllers[3]: plc+=line
            self.displayPLC3.setText(plc)
      print(self.controllers[3])







if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec())



