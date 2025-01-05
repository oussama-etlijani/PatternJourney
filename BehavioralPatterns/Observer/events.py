class Event(list):
    def __call__(self, *args, **kwargs):
        # Call each function (callback) stored in the Event list
        for item in self:
            item(*args, **kwargs)


# A class to represent a thermostat
class Thermostat:
    def __init__(self, temperature=22):
        self.temperature = temperature
        self.temperature_changed = (
            Event()
        )  # Create an event to notify temperature changes

    def set_temperature(self, new_temperature):
        if self.temperature != new_temperature:
            self.temperature = new_temperature
            # Trigger the event, notifying all subscribers of the new temperature
            self.temperature_changed(self.temperature)


# Example usage
def display_temperature_change(new_temp):
    print(f"The temperature is now {new_temp}°C.")


def alert_if_too_hot(new_temp):
    if new_temp > 25:
        print("Warning: It's getting too hot!")


def alert_if_too_cold(new_temp):
    if new_temp < 18:
        print("Warning: It's getting too cold!")


# Create a thermostat instance
thermostat = Thermostat()

# Subscribe functions to the 'temperature_changed' event
thermostat.temperature_changed.append(display_temperature_change)
thermostat.temperature_changed.append(alert_if_too_hot)
thermostat.temperature_changed.append(alert_if_too_cold)

# Change the temperature to trigger the event
thermostat.set_temperature(26)  # Triggers all callbacks
# Output:
# The temperature is now 26°C.
# Warning: It's getting too hot!

thermostat.set_temperature(16)  # Triggers all callbacks
# Output:
# The temperature is now 16°C.
# Warning: It's getting too cold!

thermostat.set_temperature(22)  # No warnings; only the display callback runs
# Output:
# The temperature is now 22°C.
