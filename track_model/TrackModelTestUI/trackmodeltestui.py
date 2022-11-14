# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

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
        self.lineDropDown.currentTextChanged.connect(self.populate_block_dropdown)
        self.updateTypeDropdown.currentTextChanged.connect(self.update_type_inputs)
        self.update_type_inputs()
        self.populate_line_dropdown()
        self.updateButton.clicked.connect(self.send_update)

    def update_type_inputs(self):
        print('updating dropdown')
        update_type = self.updateTypeDropdown.currentText()

        if update_type == "Occupancy":
            self.updateValueLabel.setText("Occupied?")
            self.set_update_dropdown_yes_no()
        elif update_type == 'Failure':
            self.updateValueLabel.setText("Failure Type")
            self.set_update_dropdown_failures()
        elif update_type == 'Authority':
            self.updateValueLabel.setText("Authority Value")
            self.set_update_dropdown_authority()

    def set_update_dropdown_authority(self):
        self.inputValueDropdown.clear()
        self.inputValueDropdown.addItem('1')
        self.inputValueDropdown.addItem('0')

    def set_update_dropdown_yes_no(self):
        self.inputValueDropdown.clear()
        self.inputValueDropdown.addItem('Yes')
        self.inputValueDropdown.addItem('No')

    def set_update_dropdown_failures(self):
        self.inputValueDropdown.clear()
        self.inputValueDropdown.addItem('Power failure')
        self.inputValueDropdown.addItem('Track Circuit failure')
        self.inputValueDropdown.addItem('Broken Rail')
        self.inputValueDropdown.addItem('None')

    def send_update(self):
        print(self.updateTypeDropdown.currentText())

        if self.updateTypeDropdown.currentText() == "Occupancy":
            self.send_occupancy_update()
        elif self.updateTypeDropdown.currentText() == "Failure":
            self.send_failure_update()
        elif self.updateTypeDropdown.currentText() == "Authority":
            self.send_authority_update()

    def send_failure_update(self):
        print('updating failure')
        line = self.lineDropDown.currentText()
        block = self.blockDropDown.currentText()
        failureType = self.inputValueDropdown.currentText()

        s.send_TrackModel_failure_status.emit(line, int(block), failureType)

    def send_authority_update(self):
        print('authority upddate')
        line = self.lineDropDown.currentText()
        block = self.blockDropDown.currentText()
        authority = int(self.inputValueDropdown.currentText())

        s.send_TrackModel_block_authority.emit(line, int(block), authority)

    def send_commanded_speed_update(self):
        pass

    def send_occupancy_update(self):
        line = self.lineDropDown.currentText()
        block = self.blockDropDown.currentText()
        occupancy = self.inputValueDropdown.currentText()=='Yes'

        s.send_TrackModel_track_occupancy.emit(line, int(block), occupancy)

    def populate_block_dropdown(self, text):
        self.blockDropDown.clear()
        for section in self.track[text]:
            for block in self.track[text][section]:
                self.blockDropDown.addItem(str(block))

    def populate_line_dropdown(self):
        self.lineDropDown.clear()
        for line in self.track:
            self.lineDropDown.addItem(line)

    def load_ui(self):
        path = Path(__file__).resolve().parent / "form.ui"
        uic.loadUi(path, self)

    def update_track_info(self, track):
        self.track = dict()
        for line in track:
            self.track[line] = dict()
            for section in track[line]:
                self.track[line][section] = list()
                for block in track[line][section]:
                    self.track[line][section].append(int(block))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TrackModelTestUI()
    widget.show()
    sys.exit(app.exec())
