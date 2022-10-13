from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CTC Office")
        self.setWindowIcon(QIcon("../Images/TrainIcon.png"))
        self.setStyleSheet('background-color:black')
        stylesheet = (
            'background-color:black'
        )
        self.setStyleSheet(stylesheet)


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
