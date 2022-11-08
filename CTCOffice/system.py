from PyQt6 import QtGui

import ui.system as system
import ui.ctcOfficeLayout as ctcOfficeLayout
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys
import sqlite3
import time

from testUiMain import MainTestWindow
from main import MainWindow


mydb = sqlite3.connect("ctcOffice.db")
cursor = mydb.cursor()


class SystemWindow(QMainWindow, system.Ui_MainWindow):
    def __init__(self, parent=None):
      super(SystemWindow, self).__init__(parent)
      self.setupUi(self)

      self.pushButton.clicked.connect(self.open_CTC)
      self.pushButton_2.clicked.connect(self.open_test)



    def open_CTC(self):
      self.main_window = MainWindow()
      self.main_window.show()

    def open_test(self):
      self.test_window = MainTestWindow()
      self.test_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemWindow()
    window.show()

    sys.exit(app.exec())