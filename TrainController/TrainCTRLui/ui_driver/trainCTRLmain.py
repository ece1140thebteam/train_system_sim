# This Python file uses the following encoding: utf-8
import sys

from PyQt6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QApplication, QMainWindow
from mainwindow import TrainController
from trainctrltestui import TrainCTRLTestUI
from engineerui import engineerUI

def main():
    
    #Define both CTRL and Test UIs
    app = QApplication(sys.argv)
    train1 = TrainController()
    test1 = TrainCTRLTestUI(train1)
    engUI = engineerUI(train1)
    
    train1.show()
    test1.show()
    engUI.show()

    sys.exit(app.exec())

main()