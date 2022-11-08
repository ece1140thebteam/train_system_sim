import systemui as system
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys

from CTCOffice.testUiMain import MainTestWindow
from CTCOffice.main import MainWindow

class SystemWindow(QMainWindow, system.Ui_MainWindow):
    def __init__(self, parent=None):
      super(SystemWindow, self).__init__(parent)
      self.setupUi(self)

      self.pushButton_ctc.clicked.connect(self.open_CTC)
      self.pushButton_ctc_test.clicked.connect(self.open_CTC_test)



    def open_CTC(self):
      self.main_window = MainWindow()
      self.main_window.show()

    def open_CTC_test(self):
      self.test_window = MainTestWindow()
      self.test_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemWindow()
    window.show()

    sys.exit(app.exec())