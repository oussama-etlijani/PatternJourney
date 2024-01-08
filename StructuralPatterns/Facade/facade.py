# Subsystem components
class CPU:
    def start(self) -> str:
        """
        Start the CPU.

        Returns:
            str: A message indicating the CPU has started.
        """
        return "CPU started"


class Memory:
    def load(self) -> str:
        """
        Load memory.

        Returns:
            str: A message indicating that memory has been loaded.
        """
        return "Memory loaded"


class HardDrive:
    def read(self) -> str:
        """
        Read from the hard drive.

        Returns:
            str: A message indicating the hard drive has been read.
        """
        return "Hard Drive read"


# Facade
class ComputerFacade:
    def __init__(self):
        """
        Initialize the ComputerFacade with CPU, Memory, and HardDrive instances.
        """
        self.cpu: CPU = CPU()
        self.memory: Memory = Memory()
        self.hard_drive: HardDrive = HardDrive()

    def start(self) -> list[str]:
        """
        Start the computer by orchestrating the startup sequence.

        Returns:
            list[str]: A list of messages indicating each step of the startup sequence.
        """
        result: list[str] = [self.cpu.start(), self.memory.load(), self.hard_drive.read()]
        return result


# Client code
if __name__ == "__main__":
    # Using the Facade to start the computer
    computer_facade: ComputerFacade = ComputerFacade()
    result: list[str] = computer_facade.start()

    # Displaying the result
    print("Computer Starting Sequence:")
    for step in result:
        print(step)
