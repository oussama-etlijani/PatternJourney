# Purpose: Implementation of the remote control class.
from command import Command


class RemoteControl:
    """
    The Invoker is associated with one or several commands.
    It sends a request to the command.
    """

    _on_button: Command | None = None
    _off_button: Command | None = None

    def set_on_button(self, command: Command) -> None:
        """Set the command for the 'on' button."""
        self._on_button = command

    def set_off_button(self, command: Command) -> None:
        """Set the command for the 'off' button."""
        self._off_button = command

    def press_on_button(self) -> None:
        """Press the 'on' button."""
        if self._on_button is not None:
            self._on_button.execute()

    def press_off_button(self) -> None:
        """Press the 'off' button."""
        if self._off_button is not None:
            self._off_button.execute()
