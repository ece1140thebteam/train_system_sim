import CTCOffice.ui.ctcOfficeTestLayout as ctcOfficeTestLayout
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import sys
import sqlite3

from signals import s


mydb = sqlite3.connect("CTCOffice/ctcOffice.db")

cursor = mydb.cursor()


class MainTestWindow(QWidget, ctcOfficeTestLayout.Ui_CTCOffice_Testing):
    def __init__(self, parent=None):
        super(MainTestWindow, self).__init__(parent)
        self.setupUi(self)


        # Initialize Static Data
        self.redBlocks = []
        self.greenBlocks = []
        self.redCrossings = []
        self.greenCrossings = []
        self.blueBlocks = []
        self.blueCrossings = []
        self.get_blocks()
        self.get_crossings()

        # Initialize Components
        self.update_crossing()
        self.update_occupancy()
        self.update_track_failure()

        # ComboBox Connections
        self.comboBox_crossing_line.currentTextChanged.connect(self.update_crossing)
        self.comboBox_trackFailure_line.currentTextChanged.connect(self.update_track_failure)
        self.comboBox_occupancy_Line.currentTextChanged.connect(self.update_occupancy)

        # Button Connections
        self.pushButton_throughput.clicked.connect(self.set_throughput)
        self.pushButton_trackFailure.clicked.connect(self.set_failure)
        self.pushButton_trackOccupancy.clicked.connect(self.set_occupancy)
        self.pushButton_crossing.clicked.connect(self.set_crossings)

    def get_blocks(self):
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT Block_Number FROM track_blocks WHERE line = 'Red'")
        blocks = my_cursor.fetchall()
        for block in blocks:
            self.redBlocks.append(str(block[0]))

        my_cursor.execute("SELECT Block_Number FROM track_blocks WHERE line = 'Green'")
        blocks = my_cursor.fetchall()
        for block in blocks:
            self.greenBlocks.append(str(block[0]))

        my_cursor.execute("SELECT Block_Number FROM track_blocks WHERE line = 'Blue'")
        blocks = my_cursor.fetchall()
        for block in blocks:
            self.blueBlocks.append(str(block[0]))

    def update_occupancy(self):
        block_box = self.comboBox_occupancy_blockNumber
        block_box.clear()
        if self.comboBox_occupancy_Line.currentText() == "Red":
            block_box.addItems(self.redBlocks)
        elif self.comboBox_occupancy_Line.currentText() == "Green":
            block_box.addItems(self.greenBlocks)
        elif self.comboBox_occupancy_Line.currentText() == "Blue":
            block_box.addItems(self.blueBlocks)

    def update_crossing(self):
        block_box = self.comboBox_crossing_blockNumber
        block_box.clear()
        if self.comboBox_crossing_line.currentText() == "Red":
            block_box.addItems(self.redCrossings)
        elif self.comboBox_crossing_line.currentText() == "Green":
            block_box.addItems(self.greenCrossings)
        elif self.comboBox_crossing_line.currentText() == "Blue":
            block_box.addItems(self.blueCrossings)

    def update_track_failure(self):
        block_box = self.comboBox_trackFailure_blockNumber
        block_box.clear()
        if self.comboBox_trackFailure_line.currentText() == "Red":
            block_box.addItems(self.redBlocks)
        elif self.comboBox_trackFailure_line.currentText() == "Green":
            block_box.addItems(self.greenBlocks)
        elif self.comboBox_trackFailure_line.currentText() == "Blue":
            block_box.addItems(self.blueBlocks)

    def set_throughput(self):
        # query = "UPDATE throughput SET throughput = (%s) WHERE Line = (%s)"
        query = "UPDATE throughput SET throughput = ? WHERE Line = ?"
        throughput = self.spinBox_setThroughput_throughput.value()
        if self.comboBox_setThroughput_line.currentText() == "Red":
            line = 'Red'
        elif self.comboBox_setThroughput_line.currentText() == "Green":
            line = 'Green'
        else:
            line = 'Blue'

        # cursor.execute(query, values)
        # mydb.commit()

        s.send_throughput_signal.emit(line, throughput)

    def set_failure(self):
        # query = "UPDATE track_blocks SET Failure_State = (%s) WHERE Line = (%s) and Block_Number = (%s)"
        query = "UPDATE track_blocks SET Failure_State = ? WHERE Line = ? and Block_Number = ?"
        line = self.comboBox_trackFailure_line.currentText()
        blockNumber = self.comboBox_trackFailure_blockNumber.currentText()
        state = self.comboBox_trackFailure_status.currentText()
        if state == "Power Failure":
            values = (state, line, blockNumber)
        elif state == "Broken Rail":
            values = (state, line, blockNumber)
        elif state == "Track Circuit Fail":
            values = (state, line, blockNumber)
        else:
            values = ('', line, blockNumber)

        cursor.execute(query, values)
        mydb.commit()

    def set_occupancy(self):
        # query = "UPDATE track_blocks SET Occupancy = (%s) WHERE Line = (%s) and Block_Number = (%s)"
        query = "UPDATE track_blocks SET Occupancy = ? WHERE Line = ? and Block_Number = ?"
        line = self.comboBox_occupancy_Line.currentText()
        blockNumber = self.comboBox_occupancy_blockNumber.currentText()
        state = self.comboBox_occupancy_status.currentText()
        if state == "Train":
            values = (1, line, blockNumber)
        else:
            values = (0, line, blockNumber)

        cursor.execute(query, values)
        mydb.commit()

    def get_crossings(self):
        cursor.execute(
            "SELECT Block_Number FROM track_blocks WHERE line = 'Red' AND Infrastructure = 'RAILWAY CROSSING'")
        blocks = cursor.fetchall()
        for block in blocks:
            self.redCrossings.append(str(block[0]))

        cursor.execute(
            "SELECT Block_Number FROM track_blocks WHERE line = 'Green' AND Infrastructure = 'RAILWAY CROSSING'")
        blocks = cursor.fetchall()
        for block in blocks:
            self.greenCrossings.append(str(block[0]))

        cursor.execute(
            "SELECT Block_Number FROM track_blocks WHERE line = 'Blue' AND Infrastructure = 'RAILWAY CROSSING'")
        blocks = cursor.fetchall()
        for block in blocks:
            self.blueCrossings.append(str(block[0]))

    def set_crossings(self):
        # query = "UPDATE track_blocks SET Crossing = (%s) WHERE Line = (%s) and Block_Number = (%s)"
        query = "UPDATE track_blocks SET Crossing = ? WHERE Line = ? and Block_Number = ?"
        line = self.comboBox_crossing_line.currentText()
        blockNumber = self.comboBox_crossing_blockNumber.currentText()
        state = self.comboBox_crossing_status.currentText()
        if state == "Active":
            values = (1, line, blockNumber)
        else:
            values = (0, line, blockNumber)

        cursor.execute(query, values)
        mydb.commit()

        # self.parentWidget().setThroughput("Red", 100)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainTestWindow()
    window.show()

    sys.exit(app.exec())
