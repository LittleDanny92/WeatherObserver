from PyQt5 import (
    QtWidgets,
    QtCore,
    QtGui
    )

from datetime import datetime

from center import center

from locationwindow import LocationWindow
from weather import Weather
from weatherdatacollector import WeatherDataCollector



class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("WeatherObserver")
        self.setFixedSize(620,750)
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

        day_one_icon_layout = QtWidgets.QHBoxLayout()
        day_two_icon_layout = QtWidgets.QHBoxLayout()
        day_three_icon_layout = QtWidgets.QHBoxLayout()
        day_four_icon_layout = QtWidgets.QHBoxLayout()

        info_layout = QtWidgets.QHBoxLayout()

        main_layout.addStretch()
        
        main_layout.addLayout(location_layout)
        main_layout.addLayout(actual_weather_layout)
        main_layout.addLayout(actual_temp_layout)
        main_layout.addLayout(feels_like_layout)

        main_layout.addLayout(forecast_layout)

        main_layout.addStretch()

        main_layout.addLayout(info_layout)

        self.location_label = QtWidgets.QLabel("", self)
        self.location_label.setFont(QtGui.QFont("Arial", 20))
        self.location_label.setFixedSize(400,75)
        self.location_label.setAlignment(QtCore.Qt.AlignCenter)
        location_layout.addWidget(self.location_label)

        self.actual_weather_icon_label = QtWidgets.QLabel(self)
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
        

        self.day_one_label = QtWidgets.QLabel("", self)
        self.day_one_label.setFixedSize(150,50)
        self.day_one_label.setFont(QtGui.QFont("Arial", 14))
        self.day_one_label.setAlignment(QtCore.Qt.AlignCenter)
        day_one_layout.addWidget(self.day_one_label)

        self.day_one_icon_max_label = QtWidgets.QLabel("", self)
        self.day_one_icon_max_label.setFixedSize(50,50)
        self.day_one_icon_max_label.setAlignment(QtCore.Qt.AlignCenter)
        self.day_one_icon_min_label = QtWidgets.QLabel("", self)
        self.day_one_icon_min_label.setFixedSize(50,50)
        self.day_one_icon_min_label.setAlignment(QtCore.Qt.AlignCenter)
        day_one_icon_layout.addWidget(self.day_one_icon_max_label)
        day_one_icon_layout.addWidget(self.day_one_icon_min_label)
        day_one_layout.addLayout(day_one_icon_layout)

        self.day_one_temp_label = QtWidgets.QLabel("-.- °C/-.- °C", self)
        self.day_one_temp_label.setFixedSize(150,50)
        self.day_one_temp_label.setFont(QtGui.QFont("Arial", 11))
        self.day_one_temp_label.setAlignment(QtCore.Qt.AlignCenter)
        day_one_layout.addWidget(self.day_one_temp_label)
        
        forecast_layout.addLayout(day_one_layout)

        self.day_two_label = QtWidgets.QLabel("", self)
        self.day_two_label.setFixedSize(150,50)
        self.day_two_label.setFont(QtGui.QFont("Arial", 14))
        self.day_two_label.setAlignment(QtCore.Qt.AlignCenter)
        day_two_layout.addWidget(self.day_two_label)

        self.day_two_icon_max_label = QtWidgets.QLabel("", self)
        self.day_two_icon_max_label.setFixedSize(50,50)
        self.day_two_icon_max_label.setAlignment(QtCore.Qt.AlignCenter)
        self.day_two_icon_min_label = QtWidgets.QLabel("", self)
        self.day_two_icon_min_label.setFixedSize(50,50)
        self.day_two_icon_min_label.setAlignment(QtCore.Qt.AlignCenter)
        day_two_icon_layout.addWidget(self.day_two_icon_max_label)
        day_two_icon_layout.addWidget(self.day_two_icon_min_label)
        day_two_layout.addLayout(day_two_icon_layout)

        self.day_two_temp_label = QtWidgets.QLabel("-.- °C/-.- °C", self)
        self.day_two_temp_label.setFixedSize(150,50)
        self.day_two_temp_label.setFont(QtGui.QFont("Arial", 11))
        self.day_two_temp_label.setAlignment(QtCore.Qt.AlignCenter)
        day_two_layout.addWidget(self.day_two_temp_label)

        forecast_layout.addLayout(day_two_layout)

        self.day_three_label = QtWidgets.QLabel("", self)
        self.day_three_label.setFixedSize(150,50)
        self.day_three_label.setFont(QtGui.QFont("Arial", 14))
        self.day_three_label.setAlignment(QtCore.Qt.AlignCenter)
        day_three_layout.addWidget(self.day_three_label)

        self.day_three_icon_max_label = QtWidgets.QLabel("", self)
        self.day_three_icon_max_label.setFixedSize(50,50)
        self.day_three_icon_max_label.setAlignment(QtCore.Qt.AlignCenter)
        self.day_three_icon_min_label = QtWidgets.QLabel("", self)
        self.day_three_icon_min_label.setFixedSize(50,50)
        self.day_three_icon_min_label.setAlignment(QtCore.Qt.AlignCenter)
        day_three_icon_layout.addWidget(self.day_three_icon_max_label)
        day_three_icon_layout.addWidget(self.day_three_icon_min_label)
        day_three_layout.addLayout(day_three_icon_layout)

        self.day_three_temp_label = QtWidgets.QLabel("-.- °C/-.- °C", self)
        self.day_three_temp_label.setFixedSize(150,50)
        self.day_three_temp_label.setFont(QtGui.QFont("Arial", 11))
        self.day_three_temp_label.setAlignment(QtCore.Qt.AlignCenter)
        day_three_layout.addWidget(self.day_three_temp_label)

        forecast_layout.addLayout(day_three_layout)

        self.day_four_label = QtWidgets.QLabel("", self)
        self.day_four_label.setFixedSize(150,50)
        self.day_four_label.setFont(QtGui.QFont("Arial", 14))
        self.day_four_label.setAlignment(QtCore.Qt.AlignCenter)
        day_four_layout.addWidget(self.day_four_label)

        self.day_four_icon_max_label = QtWidgets.QLabel("", self)
        self.day_four_icon_max_label.setFixedSize(50,50)
        self.day_four_icon_max_label.setAlignment(QtCore.Qt.AlignCenter)
        self.day_four_icon_min_label = QtWidgets.QLabel("", self)
        self.day_four_icon_min_label.setFixedSize(50,50)
        self.day_four_icon_min_label.setAlignment(QtCore.Qt.AlignCenter)
        day_four_icon_layout.addWidget(self.day_four_icon_max_label)
        day_four_icon_layout.addWidget(self.day_four_icon_min_label)
        day_four_layout.addLayout(day_four_icon_layout)

        self.day_four_temp_label = QtWidgets.QLabel("-.- °C/-.- °C", self)
        self.day_four_temp_label.setFixedSize(150,50)
        self.day_four_temp_label.setFont(QtGui.QFont("Arial", 11))
        self.day_four_temp_label.setAlignment(QtCore.Qt.AlignCenter)
        day_four_layout.addWidget(self.day_four_temp_label)

        forecast_layout.addLayout(day_four_layout)

        self.setCentralWidget(main)

        # Create actions and menu bar
        self.new_action = QtWidgets.QAction('&Create New Forecast', self)        
        self.new_action.setShortcut('Ctrl+n')
        self.new_action.setStatusTip('Create Forecast')
        self.new_action.triggered.connect(self.create_new_forecast)

        self.exit_action = QtWidgets.QAction('&Exit', self)        
        self.exit_action.setShortcut('Ctrl+q')
        self.exit_action.setStatusTip('Exit application')
        self.exit_action.triggered.connect(QtWidgets.qApp.quit)

        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu('&File')
        self.file_menu.addAction(self.new_action)
        self.file_menu.addAction(self.exit_action)

        self.creator_name_label = QtWidgets.QLabel("Made by D.H. 2023", self)
        self.creator_name_label.setFont(QtGui.QFont("Arial", 9))
        self.creator_name_label.setFixedSize(160,25)
        self.creator_name_label.setAlignment(QtCore.Qt.AlignLeft)
        info_layout.addWidget(self.creator_name_label)

        self.data_source_label = QtWidgets.QLabel("Weather data source: openweathermap.org", self)
        self.data_source_label.setFont(QtGui.QFont("Arial", 10))
        self.data_source_label.setFixedSize(350,25)
        self.data_source_label.setAlignment(QtCore.Qt.AlignRight)
        info_layout.addWidget(self.data_source_label)
                
        self.error_msg_box = QtWidgets.QMessageBox()
        self.error_msg_box.setWindowTitle("Error")
        self.error_msg_box.setIcon(QtWidgets.QMessageBox.Warning)

        self.info_msg_box = QtWidgets.QMessageBox()
        self.info_msg_box.setWindowTitle("Information")
        self.info_msg_box.setIcon(QtWidgets.QMessageBox.Information)

        self.get_location_window = LocationWindow()

    def create_new_forecast(self):

        location_accepted = self.get_location_window.exec()
        if location_accepted == QtWidgets.QDialog.Accepted:
            try:
                self.get_weather(self.get_location_window.get_location())
                self.show_forecast()
            #except Exception as err:
             #   print(f"HTTP error occurred: {err}")
            except:
                self.info_msg_box.setText("Something horrible happened! Maybe You didnt write the location?")
                self.info_msg_box.exec()
            

    def show_forecast(self):

        self.location_label.setText(self.weather_data_collector.city)
        self.actual_weather_icon_label.setPixmap(
            QtGui.QPixmap(f"images/{self.weather.weather_condition}.png").scaled(80, 80, QtCore.Qt.KeepAspectRatio)
            )
        self.actual_temp_label.setText(f"{round(self.weather.actual_temp)} °C")
        self.feels_like_label.setText(f"Feels like:  {round(self.weather.feel_temp,1)} °C")

        self.day_one_label.setText(f"{self.get_week_day(self.weather.forecast[0][0])}")
        self.day_one_icon_max_label.setPixmap(
            QtGui.QPixmap(f"images/{self.weather.forecast[0][2]}.png").scaled(40, 40, QtCore.Qt.KeepAspectRatio)
            )
        self.day_one_icon_min_label.setPixmap(
            QtGui.QPixmap(f"images/{self.weather.forecast[0][4]}.png").scaled(40, 40, QtCore.Qt.KeepAspectRatio)
            )
        self.day_one_temp_label.setText(
            f"{round(self.weather.forecast[0][1],1)} °C/{round(self.weather.forecast[0][3],1)} °C"
            )

        self.day_two_label.setText(f"{self.get_week_day(self.weather.forecast[1][0])}")
        self.day_two_icon_max_label.setPixmap(
            QtGui.QPixmap(f"images/{self.weather.forecast[1][2]}.png").scaled(40, 40, QtCore.Qt.KeepAspectRatio)
            )
        self.day_two_icon_min_label.setPixmap(
            QtGui.QPixmap(f"images/{self.weather.forecast[1][4]}.png").scaled(40, 40, QtCore.Qt.KeepAspectRatio)
            )
        self.day_two_temp_label.setText(
            f"{round(self.weather.forecast[1][1],1)} °C/{round(self.weather.forecast[1][3],1)} °C"
            )

        self.day_three_label.setText(f"{self.get_week_day(self.weather.forecast[2][0])}")
        self.day_three_icon_max_label.setPixmap(
            QtGui.QPixmap(f"images/{self.weather.forecast[2][2]}.png").scaled(40, 40, QtCore.Qt.KeepAspectRatio)
            )
        self.day_three_icon_min_label.setPixmap(
            QtGui.QPixmap(f"images/{self.weather.forecast[2][4]}.png").scaled(40, 40, QtCore.Qt.KeepAspectRatio)
            )
        self.day_three_temp_label.setText(
            f"{round(self.weather.forecast[2][1],1)} °C/{round(self.weather.forecast[2][3],1)} °C"
            )

        self.day_four_label.setText(f"{self.get_week_day(self.weather.forecast[3][0])}")
        self.day_four_icon_max_label.setPixmap(
            QtGui.QPixmap(f"images/{self.weather.forecast[3][2]}.png").scaled(40, 40, QtCore.Qt.KeepAspectRatio)
            )
        self.day_four_icon_min_label.setPixmap(
            QtGui.QPixmap(f"images/{self.weather.forecast[3][4]}.png").scaled(40, 40, QtCore.Qt.KeepAspectRatio)
            )
        self.day_four_temp_label.setText(
            f"{round(self.weather.forecast[3][1],1)} °C/{round(self.weather.forecast[3][3],1)} °C"
            )

    def get_weather(self,city):
        self.weather_data_collector = WeatherDataCollector(city)

        self.get_actual_weather(self.weather_data_collector)
        self.get_forecast(self.weather_data_collector)

        self.weather = Weather(
            self.weather_data_collector.actual_weather_data[0],
            self.weather_data_collector.actual_weather_data[1],
            self.weather_data_collector.actual_weather_data[2],
            self.weather_data_collector.forecast_data
            )

    def get_actual_weather(self,collector):
        collector.collect_actual_weather_data()

    def get_forecast(self,collector):
        collector.collect_forecast_data()

    def get_week_day(self, date):
        today = datetime.strptime(date, "%Y-%m-%d") 
        return today.strftime("%a")