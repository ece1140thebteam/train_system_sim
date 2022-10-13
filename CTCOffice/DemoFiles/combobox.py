from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 CheckBox")
        self.setWindowIcon(QIcon("../Images/TrainIcon.png"))
        self.setGeometry(500, 200, 500, 400)

        vbox = QVBoxLayout()

        self.combo = QComboBox()
        self.combo.addItem("PyQt6")
        self.combo.addItem("PyQt7")
        self.combo.addItem("PyQt8")
        self.combo.addItem("PyQt9")
        self.combo.addItem("PyQt10")

        self.combo.currentTextChanged.connect(self.combo_item)

        self.label = QLabel("Hello")

        vbox.addWidget(self.combo)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def combo_item(self):
        value = self.combo.currentText()
        self.label.setText("You have selected: " + value)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())