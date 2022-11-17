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



