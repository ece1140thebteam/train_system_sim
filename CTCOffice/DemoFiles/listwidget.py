from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 CheckBox")
        self.setWindowIcon(QIcon("../Images/TrainIcon.png"))
        self.setGeometry(500, 200, 500, 400)

        vbox = QVBoxLayout()

        self.list_widget = QListWidget()
        self.list_widget.insertItem(0, "PyQt6")
        self.list_widget.insertItem(1, "wxPython")
        self.list_widget.insertItem(2, "Kivy")
        self.list_widget.insertItem(3, "TKinter")
        self.list_widget.insertItem(4, "PySide2")
        self.list_widget.setStyleSheet('background-color:yellow')
        self.list_widget.clicked.connect(self.item_selected)

        self.label = QLabel("Hello")
        self.label.setFont(QFont("Times New Roman", 14))

        vbox.addWidget(self.list_widget)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def item_selected(self):
        item = self.list_widget.currentItem()
        self.label.setText("You have selected: " + str(item.text()))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())