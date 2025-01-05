# This code demonstrates the State design pattern using a light switch example.
# The state of the light (on/off) is managed dynamically by switching between different state classes.

from abc import ABC


# The Switch class acts as the context in the State pattern.
# It delegates its behavior to the current state (initially OffState).
class Switch:
    def __init__(self):
        self.state = OffState()  # Start with the light in the off state

    def on(self):
        # Delegates the 'on' behavior to the current state
        self.state.on(self)

    def off(self):
        # Delegates the 'off' behavior to the current state
        self.state.off(self)


# The State class is an abstract base class (ABC) defining the interface for states.
# It provides default behavior for 'on' and 'off' methods.
class State(ABC):
    def on(self, switch):
        print(
            "Light is already on"
        )  # Default behavior when turning on from an already on state

    def off(self, switch):
        print(
            "Light is already off"
        )  # Default behavior when turning off from an already off state


# OnState represents the "on" state of the light.
class OnState(State):
    def __init__(self):
        print("Light turned on")  # Indicate that the light has been turned on

    def off(self, switch):
        # Transition from OnState to OffState
        print("Turning light off...")
        switch.state = OffState()  # Change the state of the switch to OffState


# OffState represents the "off" state of the light.
class OffState(State):
    def __init__(self):
        print("Light turned off")  # Indicate that the light has been turned off

    def on(self, switch):
        # Transition from OffState to OnState
        print("Turning light on...")
        switch.state = OnState()  # Change the state of the switch to OnState


# Main block for testing the behavior of the Switch and its states
if __name__ == "__main__":
    sw = Switch()  # Create a switch, initially in the OffState

    sw.on()  # Trigger the 'on' method
    # Output: Turning light on...
    #         Light turned on

    sw.off()  # Trigger the 'off' method
    # Output: Turning light off...
    #         Light turned off

    sw.off()  # Trigger the 'off' method again while already off
    # Output: Light is already off
