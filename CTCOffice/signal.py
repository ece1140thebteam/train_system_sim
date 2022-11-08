from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class signals(QObject):
  throughput_signal = pyqtSignal()

s = signals()