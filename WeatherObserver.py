import requests
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

    _api_key = "4d382de40de2b645998c8ab0095e917c"
    _units = "metric"
    
    _actual_weather_data = None
    _forecast_data = None

    def __init__(self, city):
        self._city = city

        self._actual_weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={self._city}&units={self.units}&appid={self.api_key}"
        self._forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={self._city}&units={self.units}&appid={self.api_key}"
        
    @property
    def city(self): return self._city

    @property
    def api_key(self): return self._api_key

    @property
    def units(self): return self._units

    @property
    def actual_weather_data(self): return self._actual_weather_data

    @actual_weather_data.setter
    def actual_weather_data(self, value): self._actual_weather_data = value

    @property
    def forecast_data(self): return self._forecast_data

    @forecast_data.setter
    def forecast_data(self,value): self._forecast_data = value


    def collect_actual_weather_data(self):
        weather_data = requests.get(self._actual_weather_url)

        if weather_data.status_code == 200:

            self.actual_weather_data = [
                weather_data.json()["main"]["temp"],
                weather_data.json()["main"]["feels_like"],
                weather_data.json()["weather"][0]["main"]
            ]

        elif weather_data.status_code == 401:
            print("Unauthorized entrence")

        elif weather_data.status_code == 404:
            print("The page was not found :-/")

    def collect_forecast_data(self):
        whole_forecast_data = requests.get(self._forecast_url)
        computational_forecast_data = []
        
        if whole_forecast_data.status_code == 200:
            for i in whole_forecast_data.json()["list"]:
                computational_forecast_data.append([datetime.datetime.fromtimestamp(i["dt"]),
                                      i["main"]["temp"],
                                      i["weather"][0]["icon"]])

            required_forecast_data = self.get_average_temp(computational_forecast_data)
            self.forecast_data = computational_forecast_data #TODO: 2 - Sem pøijdou required_forecast_data

        elif whole_forecast_data.status_code == 401:
            print("Unauthorized entrence")

        elif whole_forecast_data.status_code == 404:
            print("The page was not found :-/")   
            
    def get_average_temp(self,whole_forecast):
        # TODO: 1 - vypoèítat prùmìry noèní/denní teploty
        # prùmìrná denní teplota: (T7 + T14 + 2xT21)/4
        # prùmìrná noèní teplota: (souèet teplot v rozmezí 22 - 06 a vydìlit jejich poètem)
        pass

if __name__ == "__main__":
    city = input("In what city do you want to know a weather? ")

    weather_collect = WeatherDataCollector(city)
    weather_collect.collect_actual_weather_data()
    weather_collect.collect_forecast_data()

    weather = Weather(
        weather_collect.actual_weather_data[0],
        weather_collect.actual_weather_data[1],
        weather_collect.actual_weather_data[2],
        weather_collect.forecast_data)

    print(weather)
    for forecast in weather.forecast:
        print(forecast)