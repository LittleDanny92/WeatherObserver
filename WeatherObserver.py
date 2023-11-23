import requests
from pprint import pprint
import datetime

class Weather:
    def __init__(self, actual_temp, feel_temp, weather_condition, forecast):
        self._actual_temp = actual_temp
        self._feel_temp = feel_temp
        self._weather_condition = weather_condition
        self._forecast = forecast

    @property
    def actual_temp(self): return self._actual_temp

    @property
    def feel_temp(self): return self._feel_temp

    @property
    def weather_condition(self): return self._weather_condition

    @property
    def forecast(self): return self._forecast

    def __str__(self):
        return f"Actual temperature: {self.actual_temp}, feels like: {self.feel_temp} and it is {self.weather_condition}"


class WeatherDataCollector:

    __api_key = "4d382de40de2b645998c8ab0095e917c"
    __units = "metric"
    
    __actual_weather_data = None
    __forecast_data = None

    def __init__(self, city):
        self._city = city

        self._actual_weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={self._city}&units={self.units}&appid={self.api_key}"
        self._forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={self._city}&units={self.units}&appid={self.api_key}"
        
    @property
    def city(self): return self._city

    @property
    def api_key(self): return self.__api_key

    @property
    def units(self): return self.__units


    def collect_actual_weather_data(self):
        weather_data = requests.get(self._actual_weather_url)

        if weather_data.status_code == 200:
            self.__actual_weather_data = weather_data

        elif weather_data.status_code == 401:
            print("Unauthorized entrence")

        elif weather_data.status_code == 404:
            print("The page was not found :-/")

    def collect_forecast_data(self):
        forecast_data = requests.get(self._forecast_url)

        """
        forecast_temp = []
        
        if forecast_data.status_code == 200:
            for i in forecast_data.json()["list"]:
                #forecast_temp.append(datetime.datetime.fromtimestamp(i["dt"]), "|", i["main"]["temp"], "|", i["weather"]) 
                forecast_temp.append(datetime.datetime.fromtimestamp(i["dt"]))
            return forecast_temp

        elif forecast_data.status_code == 401:
            print("Unauthorized entrence")

        elif forecast_data.status_code == 404:
            print("The page was not found :-/")    
        """

if __name__ == "__main__":
    city = input("In what city do you want to know a weather? ")

    weather_collect = WeatherDataCollector(city)
    weather = Weather(weather_collect.collect_actual_weather(), 0, "shitty", weather_collect.collect_forecast_data())

    print(weather)
    for i in weather.forecast:
        print(i)