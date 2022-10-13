from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt 6 Signal and Slot")
        self.setWindowIcon(QIcon("../Images/TrainIcon.png"))
        self.setGeometry(500, 200, 500, 400)
        self.create_widgets()

    def create_widgets(self):
        self.btn = QPushButton("Click Me", self)
        #btn.move(100,100)
        self.btn.setGeometry(100,100,100,100)
        self.btn.setStyleSheet('background-color:red')
        self.btn.setIcon(QIcon("../Images/TrainIcon.png"))
        self.btn.clicked.connect(self.clicked_btn)

        #self.label.move(100, 200)
        self.label = QLabel("My Label", self)
        self.label.setGeometry(100,200,200,100)
        self.label.setStyleSheet("color:green")
        self.label.setFont(QFont("Times New Roman", 15))

    def clicked_btn(self):
        self.label.setText("Text is changed")
        self.label.setStyleSheet('background-color:red')
        self.btn.setDisabled(True)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
