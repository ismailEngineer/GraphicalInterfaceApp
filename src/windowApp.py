from PyQt5.QtWidgets import (
QApplication,
QWidget,
QPushButton,
QVBoxLayout,
QHBoxLayout,
)
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
import sys


class WindowApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "WindowApp"
        #self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('windowIcon.png'))

    def run_window(self):
        layout = QHBoxLayout()
        layout.addWidget(QPushButton('Left'))
        layout.addWidget(QPushButton('Center'))
        layout.addWidget(QPushButton('Right'))
        self.setLayout(layout)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = WindowApp()
    w.run_window()
    sys.exit(app.exec_())
