from handler_interface import Logger


class ConsoleLogger(Logger):
    def write(self, message: str) -> None:
        print("Console Logger:", message)


class FileLogger(Logger):
    def __init__(self, level: int, filename: str) -> None:
        super().__init__(level)
        self.filename = filename

    def write(self, message: str) -> None:
        with open(self.filename, 'a') as file:
            file.write(f"File Logger: {message}\n")


class EmailLogger(Logger):
    def __init__(self, level: int, email: str) -> None:
        super().__init__(level)
        self.email = email

    def write(self, message: str) -> None:
        print(f"Email Logger: Sending email to {self.email} with message: {message}")
