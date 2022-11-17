# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import random

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QFile
from PyQt6 import uic, QtGui
from signals import s

class TrackModelTestUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()
        s.send_TrackModel_map_info.connect(self.update_track_info)
        s.get_TrackModel_map_info.emit()
        s.send_TrackModel_updated.connect(s.get_TrackModel_map_info.emit)
        self.lineDropDown.currentTextChanged.connect(self.populate_block_dropdown)
        self.blockDropDown.currentTextChanged.connect(self.block_num_changed)

        self.updateTypeDropdown.currentTextChanged.connect(self.update_type_inputs)
        self.update_type_inputs()
        self.populate_line_dropdown()
        self.updateButton.clicked.connect(self.send_update)

        s.timer_tick.connect(self.handle_time_increment)
        
        s.send_TrackModel_next_block_info.connect(self.receive_block_info)
        s.send_TrackModel_block_info.connect(self.receive_block_info)
        self.dispatchTrainButton.clicked.connect(self.test_train_run)
        self.reset_run_train()

    def reset_run_train(self):
        self.run_train = False
        self.current_block_info = None
        self.current_block = 0
        self.previous_block = 0
        self.traveled_in_block = 0
        self.is_dwelling = False
        self.dwelling_t  = 0

    def test_train_run(self):
        self.current_line = self.lineDropDown.currentText()

        if self.dispatchTrainButton.isChecked():
            # print('start runnning')
            self.run_train = True
        else:
            # print('stop runnning')
            self.run_train = False
    def connect_timer(self):
        s.timer_tick.connect(self.handle_time_increment)

    def disconnect_timer(self):
        s.timer_tick.disconnect()

    def receive_block_info(self, train_num, block_info):
        # do these per block with multiple trains

        # if its a new block
        if block_info['block_num'] != self.current_block:
            if block_info['block_num'] == -1:
                print(f'TRAIN DERAILED AT BLOCK {self.current_block}')
                s.send_TrackModel_track_occupancy.emit(self.current_line, self.current_block, False)
                self.train_derailed()
                return
            if 'yard' in block_info:
                print('ARRIVED AT YARD')
                s.send_TrackModel_track_occupancy.emit(self.current_line, self.current_block, False)
                self.train_derailed()
                return
            self.current_block_info = block_info
            self.traveled_in_block = 0
            self.previous_block = self.current_block
            self.current_block = self.current_block_info['block_num']

        self.current_block_info = block_info
        self.stopped_at_station = False


    def train_derailed(self):
        self.dispatchTrainButton.setChecked(False)
        self.run_train = False
        self.reset_run_train()

    def handle_time_increment(self):
        if self.run_train:
            # if self.is_dwelling:
            #     self.dwelling_t += .1
            #     if self.dwelling_t < 30:
            #         return
            #     else:
            #         self.dwelling_t = 0
            #         self.is_dwelling = False

            # print('timer')
            line = self.current_line
            dt = .1 #100 ms, TODO udpate
            # dispatch from yard
            if self.current_block_info == None:
                #line, current_block, previous block, train num
                # print('dispatching train to '+line)
                s.send_TrackModel_get_next_block_info.emit(line, 0, -1, 0)
                return
            
            if self.traveled_in_block == 0:
                s.send_TrackModel_track_occupancy.emit(line, self.current_block_info['block_num'], True) 
                
                if self.previous_block>0: 
                    s.send_TrackModel_track_occupancy.emit(line, self.previous_block, False) 
            
            if self.current_block_info['commanded_speed'] == 0 or self.current_block_info['authority']==0:
                s.send_TrackModel_get_block_info.emit(line, self.current_block, 0) 

            distance = self.current_block_info['commanded_speed']*dt*self.current_block_info['authority']

            self.traveled_in_block += distance


            if self.current_block_info['beacon']['station_name'] is not None:
                if self.traveled_in_block > self.current_block_info['length']/2 and not self.stopped_at_station:
                    #stop onboard passengers
                    passengers_deboarded = random.randint(1, 20)
                    s.send_TrackModel_passengers_onboarded.emit(line, self.current_block, passengers_deboarded)
                    self.stopped_at_station = True
                    print('train is dwelling')
                    self.is_dwelling = True

            if self.traveled_in_block > self.current_block_info['length']:
                s.send_TrackModel_get_next_block_info.emit(line, self.current_block, self.previous_block, 0)

    def block_num_changed(self, text):
        if self.updateTypeDropdown.currentText() == "Switch Position":
            self.set_update_value_switch_pos(text)
            pass

    def update_type_inputs(self):
        update_type = self.updateTypeDropdown.currentText()
        self.populate_block_dropdown(self.lineDropDown.currentText())

        if update_type == "Occupancy":
            self.updateValueLabel.setText("Occupied?")
            self.set_update_dropdown_yes_no()
        elif update_type == 'Failure':
            self.updateValueLabel.setText("Failure Type")
            self.set_update_dropdown_failures()
        elif update_type == 'Authority':
            self.updateValueLabel.setText("Authority Value")
            self.set_update_dropdown_authority()
        elif update_type == 'Commanded Speed':
            self.updateValueSpinboxLabel.setText("Speed (km/h)")
            self.set_update_input_speed()
        elif update_type == "Maintenance":
            self.updateValueLabel.setText("Maintenance?")
            self.set_update_dropdown_yes_no()
        elif update_type == "Signal":
            self.updateValueLabel.setText("Color")
            self.set_update_value_signal_colors()
        elif update_type == "Switch Position":
            self.updateValueLabel.setText("Position")

    def set_update_value_switch_pos(self, text):
        if text == '': return
        line = self.lineDropDown.currentText()
        block = int(text)
        self.enable_input_value_dropdown()
        sw = self.track[line]['switches'][block]
        self.inputValueDropdown.clear()
        self.inputValueDropdown.addItem(str(sw[0]))
        self.inputValueDropdown.addItem(str(sw[1]))

    def enable_input_value_dropdown(self):
        self.inputValueDropdown.setEnabled(True)
        self.inputValueSpinBox.setEnabled(False)
        self.updateValueSpinboxLabel.setText("")

    def enable_input_value_spinbox(self):
        self.inputValueDropdown.setEnabled(False)
        self.inputValueSpinBox.setEnabled(True)
        self.updateValueLabel.setText("")

    def set_update_input_speed(self):
        self.enable_input_value_spinbox()

    def set_update_value_signal_colors(self):
        self.enable_input_value_dropdown()
        self.inputValueDropdown.clear()
        self.inputValueDropdown.addItem('Red')
        self.inputValueDropdown.addItem('Green')

    def set_update_dropdown_authority(self):
        self.enable_input_value_dropdown()
        self.inputValueDropdown.clear()
        self.inputValueDropdown.addItem('1')
        self.inputValueDropdown.addItem('0')

    def set_update_dropdown_yes_no(self):
        self.enable_input_value_dropdown()
        self.inputValueDropdown.clear()
        self.inputValueDropdown.addItem('Yes')
        self.inputValueDropdown.addItem('No')

    def set_update_dropdown_failures(self):
        self.enable_input_value_dropdown()
        self.inputValueDropdown.clear()
        self.inputValueDropdown.addItem('Power failure')
        self.inputValueDropdown.addItem('Track Circuit failure')
        self.inputValueDropdown.addItem('Broken Rail')
        self.inputValueDropdown.addItem('None')

    def send_update(self):
        # print(self.updateTypeDropdown.currentText())
        if self.updateTypeDropdown.currentText()    == "Occupancy":
            self.send_occupancy_update()
        elif self.updateTypeDropdown.currentText()  == "Failure":
            self.send_failure_update()
        elif self.updateTypeDropdown.currentText()  == "Authority":
            self.send_authority_update()
        elif self.updateTypeDropdown.currentText()  == "Commanded Speed":
            self.send_commanded_speed_update()
        elif self.updateTypeDropdown.currentText()  == "Maintenance":
            self.send_maintenance_update()
        elif self.updateTypeDropdown.currentText()  == "Signal":
            self.send_signal_update()
        elif self.updateTypeDropdown.currentText()  == "Switch Position":
            self.send_switch_position_update()

    def send_switch_position_update(self):
        line = self.lineDropDown.currentText()
        block = self.blockDropDown.currentText()
        position = self.inputValueDropdown.currentText()

        s.send_TrackModel_switch_position.emit(line, int(block), int(position))

    def send_signal_update(self):
        line = self.lineDropDown.currentText()
        block = self.blockDropDown.currentText()
        color = self.inputValueDropdown.currentText()

        s.send_TrackModel_signal_status.emit(line, int(block), color)

    def send_maintenance_update(self):
        line = self.lineDropDown.currentText()
        block = self.blockDropDown.currentText()
        maintenance = self.inputValueDropdown.currentText()=='Yes'

        s.send_TrackModel_maintenance_status.emit(line, int(block), maintenance)

    def send_commanded_speed_update(self):
        # print('sending speed')

        line = self.lineDropDown.currentText()
        block = self.blockDropDown.currentText()
        speed = self.inputValueSpinBox.value()

        s.send_TrackModel_commanded_speed.emit(line, int(block), speed)

    def send_failure_update(self):
        # print('updating failure')
        line = self.lineDropDown.currentText()
        block = self.blockDropDown.currentText()
        failureType = self.inputValueDropdown.currentText()

        s.send_TrackModel_failure_status.emit(line, int(block), failureType)

    def send_authority_update(self):
        # print('authority upddate')
        line = self.lineDropDown.currentText()
        block = self.blockDropDown.currentText()
        authority = int(self.inputValueDropdown.currentText())

        s.send_TrackModel_block_authority.emit(line, int(block), authority)

    def send_occupancy_update(self):
        line = self.lineDropDown.currentText()
        block = self.blockDropDown.currentText()
        occupancy = self.inputValueDropdown.currentText()=='Yes'

        s.send_TrackModel_track_occupancy.emit(line, int(block), occupancy)

    def populate_block_dropdown(self, text):
        if text == '': return
        self.blockDropDown.clear()
        if self.updateTypeDropdown.currentText() == "Switch Position":
            for b in self.track[text]['switches']:
                self.blockDropDown.addItem(str(b))

        else:
            for section in self.track[text]['sections']:
                for block in self.track[text]['sections'][section]:
                    self.blockDropDown.addItem(str(block))

#    def populate_block_dropdown(self, text):
#        self.blockDropDown.clear()
#        for section in self.track[text]['sections']:
#            for block in self.track[text]['sections'][section]:
#                self.blockDropDown.addItem(str(block))

    def populate_line_dropdown(self):
        self.lineDropDown.clear()
        for line in self.track:
            self.lineDropDown.addItem(line)

    def load_ui(self):
        path = Path(__file__).resolve().parent / "form.ui"
        uic.loadUi(path, self)

    def update_track_info(self, track):
        print('updating list')
        self.track = track
        self.populate_line_dropdown()
#        print(track)
#        for line in track:
#            self.track[line] = dict()
#            for section in track[line]['sections']:
#                self.track[line][section] = list()
#                for block in track[line]['sections'][section]:
#                    self.track[line][section].append(int(block))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TrackModelTestUI()
    widget.show()
    sys.exit(app.exec())
