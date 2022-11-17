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

      # Upload PLC button connections
      self.uploadPLC1.clicked.connect(self.getFile1)
      s.send_TrackModel_track_occupancy.connect(self.update_block_occupancy)

      s.send_CTC_switch_position_signal.connect(self.ctc_set_switch_position) # [{'line':line, 'block':block, 'switch':0}]

      # Send maintenance mode from CTC to Track Controller
      s.send_CTC_maintenance_mode_signal.connect(self.ctc_set_maintenance_mode) # [{'line':line, 'block':block, 'mode':0}]

      # Send suggested speed from CTC to Track Controller
      s.send_CTC_suggested_speed.connect(self.ctc_set_suggested_speed) # [{'line':line, 'block':block, 'speed':0}]

      # Send block authority from CTC to Track Controller
      s.send_CTC_authority.connect(self.ctc_set_authority) # [{'line':line, 'block':block, 'authority':0}]

      # Allocate blocks with corresponding controller
      for line in track_info:
         if line == 'Red':
            pass
         elif line == 'Green':
            for block in track_info[line]:
               if block == 0 or (block >= 36 and block <= 73):
                     track_info['Green'][block]['controller'] = 1
               elif block >= 74 and block <= 143:
                  track_info['Green'][block]['controller'] = 2
               elif (block >= 1 and block <= 35) or (block >= 144 and block <= 150):
                  track_info['Green'][block]['controller'] = 3

               #print(track_info[line][block]['controller'])
      
             

      #blockinfo = track_info['Green'][block]
      #authority = blockinfo['authority']
      #track_info['Green'][block]['']

            
      #s.timer_tick.connect(self.handle_time_increment)
      #s.send_CTC_switch_position_signal.connect(self.update_switch_position)
   def ctc_set_switch_position(self, updates_list):
      controllers_to_update = []
      for update in updates_list:
         line = update['line']
         block = update['block']
         sw = update['switch']
         track_info[line][block]['switch'] = sw

         controller = track_info[line][block]['controller']
         if controller not in controllers_to_update: 
            controllers_to_update.append(controller)

         s.send_TrackController_switch_pos.emit(line, block, sw)

      for controller in controllers_to_update:
         self.run_controllerx(controller)


   def ctc_set_maintenance_mode(self, updates_list):
      controllers_to_update = []
      for update in updates_list:
         line = update['line']
         block = update['block']
         m = update['mode']

         track_info[line][block]['maintenance'] = m
         
         controller = track_info[line][block]['controller']
         if controller not in controllers_to_update: 
            controllers_to_update.append(controller)
         print(m)
         s.send_TrackModel_maintenance_status.emit(line, block, m==1)
         
      for controller in controllers_to_update:
         self.run_controllerx(controller)

   def ctc_set_suggested_speed(self, updates_list):
      controllers_to_update = []
      for update in updates_list:
         line = update['line']
         block = update['block']
         s = update['speed']

         controller = track_info[line][block]['controller']
         if controller not in controllers_to_update: 
            controllers_to_update.append(controller)

         track_info[line][block]['suggested_speed'] = s

      for controller in controllers_to_update:
         self.run_controllerx(controller)

   def ctc_set_authority(self, updates_list):
      controllers_to_update = []
      print(updates_list)
      for update in updates_list:
         line = update['line']
         block = update['block']
         auth = update['authority']

         controller = track_info[line][block]['controller']
         if controller not in controllers_to_update: 
            controllers_to_update.append(controller)

         track_info[line][block]['authority'] = auth

      for controller in controllers_to_update:
         self.run_controllerx(controller)

   def run_controllerx(self, controller_num):
      print(f'running wayside controller {controller_num}')
      #TODO IMPLEMENT THE DIFFERENT CONTROLLERS

   def update_block_occupancy(self, line, block, occupancy):
      track_info[line][block]['occupancy'] = occupancy

      self.run_controllerx(track_info[line][block]['controller'])
      print('track controller occupancy updated')
   
   def update_authority(self, line, block, authority):
      track_info[line][block]['authority'] = authority

      self.run_controllerx(track_info[line][block]['controller'])
      print('track controller authority updated')

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



