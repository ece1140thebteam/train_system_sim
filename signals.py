from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class signals(QObject):
  # How to use signals
  #
  # Add import to file `from signals import s`
  #
  # See "CTCOffice/main.py" line 98 to see how to connect signal output
  # See "CTCOffice/testUiMain.py" line 180 to see how to emit signal 
  send_throughput_signal = pyqtSignal(str, int)

s = signals()