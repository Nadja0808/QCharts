import random
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit, QSlider, QColorDialog, \
    QMenuBar
from PySide6.QtCore import QTimer, Signal, QRandomGenerator, Qt
#from WidgetChart import WidgetChart
from AktienW import AktienW


class CentralW(QWidget):
    set_aktie = Signal(int)
    #wert_auslesen = Signal(float)

    def __init__(self, parent):
        super(CentralW, self).__init__(parent)

        self.interval = 1000

        self.chart_view = AktienW(parent)
        self.set_aktie.connect(self.chart_view.add_aktie)

        self.menuBar = QMenuBar()
        self.fileMenu = self.menuBar.addMenu("Farbpalette")
        self.fileMenu.addAction("Farbauswahl", self.get_color)

        self.button_start = QPushButton("Start")
        self.button_start.clicked.connect(self.timer_start)

        self.button_stop = QPushButton("Stop")
        self.button_stop.clicked.connect(self.timer_stop)

        self.h_box_layout = QHBoxLayout()
        self.h_box_layout.addWidget(self.button_start)
        self.h_box_layout.addWidget(self.button_stop)
        self.h_box_layout.addWidget(self.menuBar)

        self.v_box_layout = QVBoxLayout()
        self.v_box_layout.addWidget(self.chart_view)
        self.v_box_layout.addLayout(self.h_box_layout)
        self.setLayout(self.v_box_layout)

        #self.aktie = [0, 25, 40, 75, 100, 0, 25, 40, 75, 100, 0, 25, 40, 75, 100]

        self.aktie = []
        for i in range(100):
            aktie = random.randint(-10, 100)
            self.aktie.append(aktie)

        self.i = 0

        #Timer
        self.timer = QTimer()
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.timer_timeout)

    def get_color(self):
        color = QColorDialog.getColor()
        self.chart_view.set_color(color)

    def timer_interval(self, value):
        self.interval = value
        self.timer.setInterval(value)

    def timer_start(self):
        self.timer.start(self.interval)
        print("ok")

    def timer_stop(self):
        self.timer.stop()

    def timer_timeout(self):
        self.set_aktie.emit(self.aktie[self.i])
        self.i = self.i + 1

