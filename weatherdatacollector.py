import requests
from datetime import datetime

class WeatherDataCollector:

    _api_key = "4d382de40de2b645998c8ab0095e917c"
    _units = "metric"
    
    _actual_weather_data = None
    _forecast_data = None

    def __init__(self,city):
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
    def actual_weather_data(self,value): self._actual_weather_data = value

    @property
    def forecast_data(self): return self._forecast_data

    @forecast_data.setter
    def forecast_data(self,value): self._forecast_data = value


    def collect_actual_weather_data(self):
        weather_data = requests.get(self._actual_weather_url)

        if self.status_code_check(weather_data.status_code):

            self.actual_weather_data = [
                weather_data.json()["main"]["temp"],
                weather_data.json()["main"]["feels_like"],
                weather_data.json()["weather"][0]["icon"]
                ]

    def collect_forecast_data(self):
        whole_forecast_data = requests.get(self._forecast_url)
        computational_forecast_data = []
        
        if self.status_code_check(whole_forecast_data.status_code):
            for hourly_weather_data in whole_forecast_data.json()["list"]:
                computational_forecast_data.append(
                    [hourly_weather_data["dt_txt"].strip(),
                     hourly_weather_data["main"]["temp"],
                     hourly_weather_data["weather"][0]["icon"]]
                    )

            self.forecast_data = self.get_max_min_temps(computational_forecast_data)
           
    def get_max_min_temps(self,whole_forecast):
        daily_max_min_temps = []
        max_daily_temps = self.get_max_daily_temps(whole_forecast)
        min_daily_temps = self.get_min_daily_temps(whole_forecast)
        
        for weather_data_order in range(len(max_daily_temps)):
            daily_max_min_temps.append(
                [max_daily_temps[weather_data_order][0],              #date
                 max_daily_temps[weather_data_order][1],              #highest daily temperature
                 max_daily_temps[weather_data_order][2],              #index of the highest temperature condition
                 min_daily_temps[weather_data_order][1],              #lowest daily temperature
                 min_daily_temps[weather_data_order][2]]              #index of the lowest temperature condition
                )
        return daily_max_min_temps

    def get_max_daily_temps(self,whole_forecast):
        daily_max_temps = []
        max_temp_weather = [whole_forecast[0][1], whole_forecast[0][2]]
        day = whole_forecast[0][0][:10]

        for hourly_data in whole_forecast:
            if hourly_data[0][:10] == day:
                if max_temp_weather[0] < hourly_data[1]:
                    max_temp_weather = [hourly_data[1], hourly_data[2]]      
            else:
                daily_max_temps.append(
                    [day,
                    max_temp_weather[0],
                    max_temp_weather[1]]
                    )
                day = hourly_data[0][:10]
                max_temp_weather = [hourly_data[1], hourly_data[2]]

        daily_max_temps = self.remove_today(daily_max_temps)

        return daily_max_temps

    def get_min_daily_temps(self,whole_forecast):
        daily_min_temps = []
        min_temp_weather = [whole_forecast[0][1], whole_forecast[0][2]]
        day = whole_forecast[0][0][:10]

        for hourly_data in whole_forecast:
            if hourly_data[0][:10] == day:
                if min_temp_weather[0] > hourly_data[1]:
                    min_temp_weather = [hourly_data[1], hourly_data[2]]
            else:
                daily_min_temps.append(
                    [day,
                    min_temp_weather[0],
                    min_temp_weather[1]]
                    )
                day = hourly_data[0][:10]
                min_temp_weather = [hourly_data[1], hourly_data[2]]

        daily_min_temps = self.remove_today(daily_min_temps)

        return daily_min_temps

    def remove_today(self,weather_data):
        if weather_data[0][0] == datetime.today().strftime("%Y-%m-%d"):
            weather_data.pop(0)
        return weather_data

    def status_code_check(self,status_code):
        if status_code == 200:
            return True

        elif status_code == 400:
            raise Exception("No location has been entered")

        elif status_code == 401:
            raise Exception("Access denied")

        elif status_code == 404:
            raise Exception("Resource not found")

        else:
            raise Exception(f"HTTP error occured: {status_code}")