import random
from PySide6.QtWidgets import QWidget, QHBoxLayout, QSlider, QMessageBox, QColorDialog, QMenuBar, QLabel, QTextEdit
from PySide6.QtCharts import QChart, QLineSeries, QChartView, QSplineSeries, QValueAxis, QDateTimeAxis
from PySide6.QtCore import Qt, QDateTime, Signal
from PySide6.QtGui import QColor, QMouseEvent

class AktienW(QWidget):

    def __init__(self, parent):
        super(AktienW, self).__init__(parent)

        #Achsen
        self.time_axis = QDateTimeAxis()
        self.time_axis.setTitleText("Zeitachse")
        self.time_axis.setFormat("dd.MM hh:mm:ss")
        self.time_axis.setTickCount(11)
        self.time_axis.setRange(QDateTime.currentDateTime(), QDateTime.currentDateTime().addDays(50))

        self.aktien_axis = QValueAxis()
        self.aktien_axis.setTitleText("Aktienwert in €")
        self.aktien_axis.setRange(0, 100)

        self.chart = QChart()
        self.chart.addAxis(self.time_axis, Qt.AlignBottom)
        self.chart.addAxis(self.aktien_axis, Qt.AlignLeft)

        self.chart_view = QChartView()
        self.chart_view.setChart(self.chart)


        self.my_layout = QHBoxLayout()
        self.my_layout.addWidget(self.chart_view)
        self.setLayout(self.my_layout)

        self.series = QSplineSeries()
        self.chart.addSeries(self.series)
        self.series.setName("Aktienverlauf")
        self.series.attachAxis(self.aktien_axis)
        self.series.attachAxis(self.time_axis)
        self.series.clicked.connect(self.wert_einlesen)

        self.days = 0

    #def set_aktien_range(self, aktie_min, aktie_max):
    #    self.aktien_axis.setRange(aktie_min, aktie_max)

    def wert_einlesen(self, current_value):
        print(round(current_value.y(), 2))

    def set_color(self, color):
        self.series.setColor(color)

    def add_aktie(self, aktie):
        self.series.append(QDateTime.currentDateTime().addDays(self.days).toMSecsSinceEpoch(), aktie)
        self.days = self.days + 1