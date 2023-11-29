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