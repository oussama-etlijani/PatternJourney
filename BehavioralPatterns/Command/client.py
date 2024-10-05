# Command pattern client code.
from command import LightOffCommand, LightOnCommand, CompositeCommand
from light import Light
from remote_control import RemoteControl

# Command pattern client code.
if __name__ == "__main__":
    living_room_light = Light()

    # Create concrete command instances
    light_on = LightOnCommand(living_room_light)
    light_off = LightOffCommand(living_room_light)

    # Create a composite command
    morning_routine = CompositeCommand()
    morning_routine.add(light_on)  # Turn the light on as part of the routine
    # You can add more commands here, such as turning on other devices

    # Create an invoker (Remote Control) and associate commands
    remote = RemoteControl()
    remote.set_on_button(morning_routine)  # Using composite command for ON button
    remote.set_off_button(light_off)

    # Press the buttons on the remote control
    print("Executing morning routine:")
    remote.press_on_button()

    print("Turning light off:")
    remote.press_off_button()
