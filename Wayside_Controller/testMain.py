# Cassandra Oliva
# Main python file for Wayside Controller Test UI

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# signals used to communicate between modules
from signals import s
from Wayside_Controller.ui import WaysideTestUI as WaysideTestUI    # import UI

class MainTestWindow(QMainWindow, WaysideTestUI.Ui_MainWindow):
   def __init__(self, parent=None):
      super(MainTestWindow, self).__init__(parent)
      self.setupUi(self)


if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainTestWindow()
   window.show()
   sys.exit(app.exec())