from PySide6.QtWidgets import QMainWindow
from CentralWidget import CentralWidget
from Central import Central
from CentralW import CentralW
from Aktie import Aktie


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Aktienkurs")

        self.setCentralWidget(Central(self))