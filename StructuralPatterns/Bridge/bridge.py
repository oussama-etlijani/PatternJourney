from __future__ import annotations

from abc import ABC, abstractmethod


class MusicPlayer:
    """
    The MusicPlayer class acts as the Abstraction in this example. It contains
    a reference to a Device object and delegates the actual audio playback to it.
    """

    def __init__(self, device: Device) -> None:
        self.device = device

    def play(self) -> str:
        """Perform the play action by calling the device's playback method."""
        return f"Playing music on {self.device.play_audio()}"


class AdvancedMusicPlayer(MusicPlayer):
    """
    AdvancedMusicPlayer is an Extended Abstraction that might offer advanced
    features like equalizers. It inherits from the base MusicPlayer class.
    """

    def play(self) -> str:
        """Perform advanced play action, for example, with equalizer settings."""
        return f"Playing music with equalizer on {self.device.play_audio()}"


class Device(ABC):
    """
    The Device class serves as the Implementation interface. It provides a contract
    for concrete device classes to fulfill for actual audio playback.
    """

    @abstractmethod
    def play_audio(self) -> str:
        """Abstract method to play audio. To be implemented by concrete classes."""


class Speaker(Device):
    """
    The Speaker class is a Concrete Implementation that fulfills the contract
    defined by the Device interface for speaker-based audio playback.
    """

    def play_audio(self) -> str:
        """Implement the play audio functionality for Speaker."""
        return "the Speaker"


class Headphones(Device):
    """
    The Headphones class is another Concrete Implementation that fulfills the
    contract defined by the Device interface, this time for headphone-based audio
    playback.
    """

    def play_audio(self) -> str:
        """Implement the play audio functionality for Headphones."""
        return "the Headphones"


def client_code(music_player: MusicPlayer) -> None:
    """
    The client code works with an instance of the MusicPlayer (or an extended
    version of it), unaware of the specific Device implementation in use.
    """
    print(music_player.play())


if __name__ == "__main__":
    # Client code to demonstrate functionality
    device1 = Speaker()
    basic_player = MusicPlayer(device1)
    client_code(basic_player)

    print("\n")

    device2 = Headphones()
    advanced_player = AdvancedMusicPlayer(device2)
    client_code(advanced_player)
