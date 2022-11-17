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

class MainWindow(QMainWindow, WaysideMainUI.Ui_MainWindow):
   def __init__(self, parent=None):
      super(MainWindow, self).__init__(parent)
      self.setupUi(self)

      # Upload PLC button connections
      self.uploadPLC1.clicked.connect(self.getFile1)
      s.timer_tick.connect(self.handle_time_increment)
      s.send_CTC_switch_position_signal.connect(self.update_switch_position)

   def update_switch_position(self, line:str, positions:list):
      pass
   
   def handle_time_increment(self):
      # print('hi')
      pass

   def getFile1(self):

      filename = QFileDialog.getOpenFileName(self, "Select PLC Script", "", "Text Files (*.txt)")

      if filename[0] != '':
         with open(filename[0], 'r') as file:
            self.displayPLC1.setText(file.read())




if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec())



