# Command pattern client code.
from command import LightOffCommand, LightOnCommand
from light import Light
from remote_control import RemoteControl

if __name__ == "__main__":
    living_room_light = Light()

    # Create concrete command instances
    light_on = LightOnCommand(living_room_light)
    light_off = LightOffCommand(living_room_light)

    # Create an invoker (Remote Control) and associate commands
    remote = RemoteControl()
    remote.set_on_button(light_on)
    remote.set_off_button(light_off)

    # Press the buttons on the remote control
    remote.press_on_button()
    remote.press_off_button()
