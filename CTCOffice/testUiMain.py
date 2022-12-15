import CTCOffice.ui.ctcOfficeTestLayout as ctcOfficeTestLayout
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import sys

from signals import s



class MainTestWindow(QWidget, ctcOfficeTestLayout.Ui_CTCOffice_Testing):
    def __init__(self, parent=None):
        super(MainTestWindow, self).__init__(parent)
        self.setupUi(self)

        self.redBlocks = []
        self.greenBlocks = []
        # Initialize Static Data
        for i in range(1,76):
            self.redBlocks.append(str(i))
        for i in range(1,151):
            self.greenBlocks.append(str(i))
        self.redCrossings = ['47']
        self.greenCrossings = ['19']
        self.blueBlocks = []
        self.blueCrossings = []
        # self.get_blocks()
        # self.get_crossings()

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

    # def get_blocks(self):
    #     my_cursor.execute("SELECT Block_Number FROM track_blocks WHERE line = 'Red'")
    #     blocks = my_cursor.fetchall()
    #     for block in blocks:
    #         self.redBlocks.append(str(block[0]))

    #     my_cursor.execute("SELECT Block_Number FROM track_blocks WHERE line = 'Green'")
    #     blocks = my_cursor.fetchall()
    #     for block in blocks:
    #         self.greenBlocks.append(str(block[0]))

    #     my_cursor.execute("SELECT Block_Number FROM track_blocks WHERE line = 'Blue'")
    #     blocks = my_cursor.fetchall()
    #     for block in blocks:
    #         self.blueBlocks.append(str(block[0]))

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
        throughput = self.spinBox_setThroughput_throughput.value()
        if self.comboBox_setThroughput_line.currentText() == "Red":
            line = 'Red'
        elif self.comboBox_setThroughput_line.currentText() == "Green":
            line = 'Green'
        else:
            line = 'Blue'

        s.send_CTC_test_throughput_signal.emit(line, throughput)

    def set_failure(self):
        line = self.comboBox_trackFailure_line.currentText()
        blockNumber = self.comboBox_trackFailure_blockNumber.currentText()
        state = self.comboBox_trackFailure_status.currentText()

        if state == "No Failure":
            state = ''

        s.send_CTC_test_failure.emit(line, int(blockNumber), state)



    def set_occupancy(self):
        line = self.comboBox_occupancy_Line.currentText()
        blockNumber = self.comboBox_occupancy_blockNumber.currentText()
        state = self.comboBox_occupancy_status.currentText()
        if state == "Train":
            status = 1
        else:
            status = 0

        # s.send_CTC_test_track_occupancy.emit(line, int(blockNumber), status)
        s.send_CTC_test_track_occupancy.emit([{'line':line, 'block':int(blockNumber), 'occupancy':status}])

    # def get_crossings(self):
    #     cursor.execute(
    #         "SELECT Block_Number FROM track_blocks WHERE line = 'Red' AND Infrastructure = 'RAILWAY CROSSING'")
    #     blocks = cursor.fetchall()
    #     for block in blocks:
    #         self.redCrossings.append(str(block[0]))

    #     cursor.execute(
    #         "SELECT Block_Number FROM track_blocks WHERE line = 'Green' AND Infrastructure = 'RAILWAY CROSSING'")
    #     blocks = cursor.fetchall()
    #     for block in blocks:
    #         self.greenCrossings.append(str(block[0]))

    #     cursor.execute(
    #         "SELECT Block_Number FROM track_blocks WHERE line = 'Blue' AND Infrastructure = 'RAILWAY CROSSING'")
    #     blocks = cursor.fetchall()
    #     for block in blocks:
    #         self.blueCrossings.append(str(block[0]))

    def set_crossings(self):
        line = self.comboBox_crossing_line.currentText()
        blockNumber = self.comboBox_crossing_blockNumber.currentText()
        state = self.comboBox_crossing_status.currentText()
        if state == "Active":
            status = 1
        else:
            status = 0

        s.send_CTC_test_crossing.emit(line, int(blockNumber), status)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainTestWindow()
    window.show()

    sys.exit(app.exec())
