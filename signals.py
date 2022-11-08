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

  #######################################################
  # CTC Test 
  # Send track occupancy from Track Controller to CTC
  send_CTC_test_track_occupancy = pyqtSignal(str, int, int) # Line, block, occupancy (0=open, 1=occupied)

  # Send crossing status from Track Controller to CTC
  send_CTC_test_crossing = pyqtSignal(str, int, int) # Line, block, status (0=deactivated, 1=activated)

  # Send track failure from Track Controller to CTC
  send_CTC_test_failure = pyqtSignal(str, int, str) # Line, block, failure type

  # Send throughput from Track Model to CTC
  send_CTC_test_throughput_signal = pyqtSignal(str, int)

  #######################################################
  # CTC to Wayside 
  # Send switch position from CTC to Track Controller
  send_CTC_switch_position_signal = pyqtSignal(str, list) # Line, position (0=normal, 1=reverse)

  # Send maintenance mode from CTC to Track Controller
  send_CTC_maintenance_mode_signal = pyqtSignal(str, list) # Line, mode (0=disabled, 1=enables)

  # Send suggested speed from CTC to Track Controller
  send_CTC_suggested_speed = pyqtSignal(str, list) # Line, speed

  # Send block authority from CTC to Track Controller
  send_CTC_authority = pyqtSignal(str, list) # Line, authority (0=no, 1=yes)

  #######################################################
  # Wayside to CTC 
  # Send track occupancy from Track Controller to CTC
  send_TrackController_track_occupancy = pyqtSignal(str, list) # Line, occupancy (0=open, 1=occupied)

  # Send crossing status from Track Controller to CTC
  send_TrackController_crossing = pyqtSignal(str, list) # Line, status (0=deactivated, 1=activated)

  # Send track failure from Track Controller to CTC
  send_TrackController_failure = pyqtSignal(str, list) # Line, failure type

  #######################################################
  # Track Model to CTC
  # Send throughput from Track Model to CTC
  send_TrackModel_throughput_signal = pyqtSignal(str, int)


# Create a single instance of this class to be used in all modules. 
# By using a single instance this will ensure the same singals are being used globally
s = signals()