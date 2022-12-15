from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class signals(QObject):
  # ! Info on signals
  # How to use signals
  #
  # Add import to file `from signals import s`
  #
  # See "CTCOffice/main.py" line 98 to see how to connect signal output
  # See "CTCOffice/testUiMain.py" line 180 to see how to emit signal 

  #######################################################
  # CTC Test 
  # Send track occupancy from Track Controller to CTC
  send_CTC_test_track_occupancy = pyqtSignal(list) # Line, block, occupancy (0=open, 1=occupied)

  # Send crossing status from Track Controller to CTC
  send_CTC_test_crossing = pyqtSignal(str, int, int) # Line, block, status (0=deactivated, 1=activated)

  # Send track failure from Track Controller to CTC
  send_CTC_test_failure = pyqtSignal(str, int, str) # Line, block, failure type

  # Send throughput from Track Model to CTC
  send_CTC_test_throughput_signal = pyqtSignal(str, int)

  #######################################################
  # CTC to Wayside 
  # Send switch position from CTC to Track Controller
  send_CTC_switch_position_signal = pyqtSignal(list) # [{'line':line, 'block':block, 'switch':0}]

  # Send maintenance mode from CTC to Track Controller
  send_CTC_maintenance_mode_signal = pyqtSignal(list) # [{'line':line, 'block':block, 'mode':0}]

  # Send suggested speed from CTC to Track Controller
  send_CTC_suggested_speed = pyqtSignal(list) # [{'line':line, 'block':block, 'speed':0}]

  # Send block authority from CTC to Track Controller
  send_CTC_authority = pyqtSignal(list) # [{'line':line, 'block':block, 'authority':0}]

  #######################################################
  # Wayside to CTC 
  # Send track occupancy from Track Controller to CTC
  # SHOULD NOT BE USED CURRENTLY......CTC SHOULD GET THIS STRAIGHT FROM TRACK MODEL
  send_TrackController_track_occupancy = pyqtSignal(list) # Line, occupancy (0=open, 1=occupied)

  # send switch position from Track controller
  send_TrackController_switch_pos = pyqtSignal(str, int, int)

  # Send railway crossing status from Track Controller
  send_TrackController_crossing = pyqtSignal(str, int, int) # Line, block, (0=deactivated, 1=activated)

  # Send traffic light colors from Track Controller
  send_TrackController_traffic_light = pyqtSignal(list) # [{'line':line, 'block':block, 'traffic_light':0 for RED, 1 for GREEN}]

  # #######################################################
  # # Wayside to Track Model
  # # send switch position from Track controller to track model
  # send_TrackController_switch_pos = pyqtSignal(str, int, int)

  #######################################################
  # CTC to Train Control
  send_CTC_create_train = pyqtSignal(str)

  #######################################################
  # Track Model to CTC
  # Send throughput from Track Model to CTC
  send_TrackModel_throughput_signal = pyqtSignal(str, int) #line, throughput
  send_TrackModel_map_info          = pyqtSignal(dict) 
  get_TrackModel_map_info           = pyqtSignal()

  # track model to track controller
  send_TrackModel_tc_track_failure = pyqtSignal(str, int, str)  #line, block, failure str
  #######################################################
  # Track Model test
  # Send throughput from Track Model test to Track Model
  send_TrackModel_track_occupancy         = pyqtSignal(str, int, bool)  #line, block, occupancy (true for occupied)
  send_TrackModel_commanded_speed         = pyqtSignal(str, int, int)   #line, block, speed
  send_TrackModel_signal_status           = pyqtSignal(str, int, str)   #line, block, signal color
  send_TrackModel_railway_crossing_status = pyqtSignal(str, int, bool)  #line, block, rail crossing status (true for open)
  send_TrackModel_switch_position         = pyqtSignal(str, int, int)   #line, block, target for switch position
  send_TrackModel_failure_status          = pyqtSignal(str, int, str)  #line, block, maintenance bool (true for under maintenance)
  send_TrackModel_maintenance_status      = pyqtSignal(str, int, bool)  #line, block, maintenance bool (true for under maintenance)
  send_TrackModel_block_authority         = pyqtSignal(str, int, int)  #line, block, authority (int)
  send_TrackModel_updated                 = pyqtSignal()  #line, block, authority (int)
  send_TrackModel_get_next_block_info     = pyqtSignal(str, int, int, int) #line, current_block, previous block, train num
  send_TrackModel_get_block_info          = pyqtSignal(str, int, int) #line, block, train num
  
  # Train send to track model when passengers board train
  send_TrackModel_passengers_onboarded    = pyqtSignal(str, int, int) #line, block, passengers deboarded

  # Update combo boxes for train UIs
  send_Update_Combo = pyqtSignal(int) #train id

  #######################################################
  # Track Model to Train Model
  # Send throughput from Track Model test to Track Model
  send_TrackModel_next_block_info = pyqtSignal(int, dict) #trainID, block info
  send_TrackModel_block_info = pyqtSignal(int, dict) #trainID, block info

  #######################################################
  #Train to train model and train controller when train is deleted
  send_delete_train = pyqtSignal(int) #train id
  
  timer_tick = pyqtSignal(int) # Timer multiplier


# Create a single instance of this class to be used in all modules. 
# By using a single instance this will ensure the same singals are being used globally
s = signals()