from PySide6.QtWidgets import QMainWindow
from CentralWidget import CentralWidget
from CentralW import CentralW
from AktienW import AktienW


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Aktienkurs")

        self.setCentralWidget(CentralW(self))