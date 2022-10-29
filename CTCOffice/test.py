import unittest
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


from main import MainWindow

import sys


class TestCtc(unittest.TestCase):
    def test_throughput(self):
        app = QApplication(sys.argv)
        window = MainWindow()

        window.update_throughput("Red", 100)
        self.assertEqual(window.throughputs[0].get_throughput(), 100)

        window.update_throughput("Green", 200)
        self.assertEqual(window.throughputs[1].get_throughput(), 200)

    def test_failure(self):
        app = QApplication(sys.argv)
        window = MainWindow()

        window.update_failure("Red", 1, "Power Failure")

        self.assertEqual(window.lines[0].get(1).failure, "Power Failure")

    def test_crossing(self):
        app = QApplication(sys.argv)
        window = MainWindow()

        window.update_crossing("Red", 1, 0)
        self.assertEqual(window.lines[0].get(1).crossing, 0)

        window.update_crossing("Red", 1, 1)
        self.assertEqual(window.lines[0].get(1).crossing, 1)

if __name__ == '__main__':
    unittest.main()
