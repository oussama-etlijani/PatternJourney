# In this example, TemperatureAdapter is serving as the bridge between WeatherInCelsius and WeatherInFahrenheit.
# It adapts the interface of WeatherInFahrenheit to match that of WeatherInCelsius, allowing them to work together seamlessly.
# Existing interface
class WeatherInCelsius:
    def get_temperature(self) -> float:
        return 25.0  # returns temperature in Celsius


# Third-party library with incompatible interface
class WeatherInFahrenheit:
    def fetch_temperature(self) -> float:
        return 77.0  # returns temperature in Fahrenheit


# Adapter class
class TemperatureAdapter:
    def __init__(self, weather_in_fahrenheit: WeatherInFahrenheit) -> None:
        self.weather_in_fahrenheit = weather_in_fahrenheit

    def get_temperature(self) -> float:
        temp_fahrenheit = self.weather_in_fahrenheit.fetch_temperature()
        temp_celsius = (temp_fahrenheit - 32) * 5 / 9
        return temp_celsius  # converts Fahrenheit to Celsius


# Client code
def display_temperature(weather_source):
    print(f"The current temperature is {weather_source.get_temperature()}°C.")


if __name__ == "__main__":
    # Using the existing interface
    celsius_weather = WeatherInCelsius()
    display_temperature(celsius_weather)

    # Using the third-party library through the adapter
    fahrenheit_weather = WeatherInFahrenheit()
    adapter = TemperatureAdapter(fahrenheit_weather)
    display_temperature(adapter)
