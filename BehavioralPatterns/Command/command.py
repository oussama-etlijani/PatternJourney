# Command pattern separates the receiver from the invoker.
from abc import ABC, abstractmethod
from typing import List

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


class CompositeCommand(Command):
    """A composite command to execute multiple commands sequentially."""

    def __init__(self) -> None:
        """Initialize with an empty list of commands."""
        self._commands: List[Command] = []

    def add(self, command: Command) -> None:
        """Add a command to the list."""
        self._commands.append(command)

    def execute(self) -> None:
        """Execute all commands in sequence."""
        for command in self._commands:
            command.execute()
