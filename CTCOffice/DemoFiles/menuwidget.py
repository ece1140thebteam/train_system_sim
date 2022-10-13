from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMenu, QMainWindow
from PyQt6.QtGui import QIcon, QFont, QAction
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 CheckBox")
        self.setWindowIcon(QIcon("../Images/TrainIcon.png"))
        self.setGeometry(500, 200, 500, 400)

        self.create_menu()

    def create_menu(self):
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("File")

        new_action = QAction(QIcon("../Images/TrainIcon.png"), "New", self)
        new_action.setShortcut("Ctrl+N")
        file_menu.addAction(new_action)

        save_action = QAction(QIcon("../Images/TrainIcon.png"), "Save", self)
        new_action.setShortcut("Ctrl+S")
        file_menu.addAction(save_action)

        copy_action = QAction(QIcon("../Images/TrainIcon.png"), "Copy", self)
        new_action.setShortcut("Ctrl+C")
        file_menu.addAction(copy_action)

        file_menu.addSeparator()

        exit_action = QAction(QIcon("../Images/TrainIcon.png"), "Exit", self)
        exit_action.triggered.connect(self.close_window)
        file_menu.addAction(exit_action)

    def close_window(self):
        self.close()

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())