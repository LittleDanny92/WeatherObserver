from PyQt5 import (
    QtWidgets,
    QtCore,
    QtGui
    )

from center import center

from weather import Weather
from weatherdatacollector import WeatherDataCollector

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("WeatherObserver")
        self.setFixedSize(450,600)
        center(self.frameGeometry())

        self.init_gui()

    def init_gui(self):

        main = QtWidgets.QWidget()
        main_layout = QtWidgets.QVBoxLayout()
        main.setLayout(main_layout)

        location_layout = QtWidgets.QHBoxLayout()
        actual_weather_layout = QtWidgets.QHBoxLayout()
        actual_temp_layout = QtWidgets.QHBoxLayout()
        feels_like_layout = QtWidgets.QHBoxLayout()

        forecast_layout = QtWidgets.QHBoxLayout()
        day_one_layout = QtWidgets.QVBoxLayout()
        day_two_layout = QtWidgets.QVBoxLayout()
        day_three_layout = QtWidgets.QVBoxLayout()
        day_four_layout = QtWidgets.QVBoxLayout()



        main_layout.addStretch()
        
        main_layout.addLayout(location_layout)
        main_layout.addLayout(actual_weather_layout)
        main_layout.addLayout(actual_temp_layout)
        main_layout.addLayout(feels_like_layout)

        main_layout.addLayout(forecast_layout)
        
        main_layout.addStretch()

        self.location_label = QtWidgets.QLabel("Brno", self)
        self.location_label.setFont(QtGui.QFont("Arial", 20))
        self.location_label.setFixedSize(400,75)
        self.location_label.setAlignment(QtCore.Qt.AlignCenter)
        location_layout.addWidget(self.location_label)

        self.actual_weather_icon_label = QtWidgets.QLabel("", self)
        self.actual_weather_icon_label.setFixedSize(400,75)
        self.actual_weather_icon_label.setAlignment(QtCore.Qt.AlignCenter)
        actual_weather_layout.addWidget(self.actual_weather_icon_label)

        self.actual_temp_label = QtWidgets.QLabel("-.- °C", self)
        self.actual_temp_label.setFont(QtGui.QFont("Arial", 16))
        self.actual_temp_label.setFixedSize(400,75)
        self.actual_temp_label.setAlignment(QtCore.Qt.AlignCenter)
        actual_temp_layout.addWidget(self.actual_temp_label)

        self.feels_like_label = QtWidgets.QLabel("Feels like:  -.- °C", self)
        self.feels_like_label.setFont(QtGui.QFont("Arial", 12))
        self.feels_like_label.setFixedSize(400,75)
        self.feels_like_label.setAlignment(QtCore.Qt.AlignHCenter)
        feels_like_layout.addWidget(self.feels_like_label)
        

        self.day_one_label = QtWidgets.QLabel("Day1", self)
        self.day_one_label.setFont(QtGui.QFont("Arial", 16))
        self.day_one_label.setAlignment(QtCore.Qt.AlignCenter)
        day_one_layout.addWidget(self.day_one_label)
        self.day_one_icon_label = QtWidgets.QLabel("icon", self)
        day_one_layout.addWidget(self.day_one_icon_label)

        forecast_layout.addLayout(day_one_layout)

        self.day_two_label = QtWidgets.QLabel("Day2", self)
        self.day_two_label.setFont(QtGui.QFont("Arial", 16))
        self.day_two_label.setAlignment(QtCore.Qt.AlignCenter)
        day_two_layout.addWidget(self.day_two_label)
        self.day_two_icon_label = QtWidgets.QLabel("icon", self)
        day_two_layout.addWidget(self.day_two_icon_label)

        forecast_layout.addLayout(day_two_layout)

        self.day_three_label = QtWidgets.QLabel("Day3", self)
        self.day_three_label.setFont(QtGui.QFont("Arial", 16))
        self.day_three_label.setAlignment(QtCore.Qt.AlignCenter)
        day_three_layout.addWidget(self.day_three_label)
        self.day_three_icon_label = QtWidgets.QLabel("icon", self)
        day_three_layout.addWidget(self.day_three_icon_label)

        forecast_layout.addLayout(day_three_layout)

        self.day_four_label = QtWidgets.QLabel("Day4", self)
        self.day_four_label.setFont(QtGui.QFont("Arial", 16))
        self.day_four_label.setAlignment(QtCore.Qt.AlignCenter)
        day_four_layout.addWidget(self.day_four_label)
        self.day_four_icon_label = QtWidgets.QLabel("icon", self)
        day_four_layout.addWidget(self.day_four_icon_label)

        forecast_layout.addLayout(day_four_layout)

        self.setCentralWidget(main)

        # Create actions and menu bar
        newAction = QtWidgets.QAction('&Create New Forecast', self)        
        newAction.setShortcut('Ctrl+n')
        newAction.setStatusTip('Create Forecast')
        newAction.triggered.connect(self.show_forecast)

        exitAction = QtWidgets.QAction('&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exit_program)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(exitAction)

    def show_forecast(self):
        pass

    def exit_program(self):
        pass