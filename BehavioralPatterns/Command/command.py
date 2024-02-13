# Command pattern separates the receiver from the invoker.
from abc import ABC, abstractmethod

from light import Light


class Command(ABC):
    """The Command interface declares a method for executing a command."""

    @abstractmethod
    def execute(self) -> None:
        """Execute the command."""


class LightOnCommand(Command):
    """Concrete command class for turning the light on."""

    def __init__(self, light: Light) -> None:
        """Initialize with a Light instance."""
        self._light = light

    def execute(self) -> None:
        """Execute the command to turn the light on."""
        self._light.turn_on()


class LightOffCommand(Command):
    """Concrete command class for turning the light off."""

    def __init__(self, light: Light) -> None:
        """Initialize with a Light instance."""
        self._light = light

    def execute(self) -> None:
        """Execute the command to turn the light off."""
        self._light.turn_off()
