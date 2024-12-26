class Subject:
    """Subject interface for managing observers."""

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """Attach an observer to the subject."""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """Detach an observer from the subject."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        """Notify all observers of a change."""
        for observer in self._observers:
            observer.update(self)


class Observer:
    """Observer interface to be implemented by concrete observers."""

    def update(self, subject):
        raise NotImplementedError("Subclass must implement abstract method.")


class WeatherStation(Subject):
    """Concrete subject that stores weather data."""

    def __init__(self):
        super().__init__()
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self.notify()


class TemperatureDisplay(Observer):
    """Concrete observer that displays the temperature."""

    def update(self, subject):
        if isinstance(subject, WeatherStation):
            print(
                f"TemperatureDisplay: The current temperature is {subject.temperature}°C."
            )


class TemperatureLogger(Observer):
    """Concrete observer that logs the temperature changes."""

    def update(self, subject):
        if isinstance(subject, WeatherStation):
            print(f"TemperatureLogger: Logging temperature {subject.temperature}°C.")


# Example usage
if __name__ == "__main__":
    # Create a weather station (subject)
    weather_station = WeatherStation()

    # Create observers
    display = TemperatureDisplay()
    logger = TemperatureLogger()

    # Attach observers to the weather station
    weather_station.attach(display)
    weather_station.attach(logger)

    # Change the temperature, observers will be notified
    print("Setting temperature to 25°C.")
    weather_station.temperature = 25

    print("\nSetting temperature to 30°C.")
    weather_station.temperature = 30

    # Detach one observer and change temperature again
    print("\nDetaching TemperatureLogger.")
    weather_station.detach(logger)

    print("Setting temperature to 35°C.")
    weather_station.temperature = 35
