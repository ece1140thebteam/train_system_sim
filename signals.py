from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class signals(QObject):
  send_throughput_signal = pyqtSignal(str, int)

s = signals()