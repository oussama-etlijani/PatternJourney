class Logger:
    DEBUG = 1
    INFO = 2
    ERROR = 3

    def __init__(self, level: int) -> None:
        self.level = level
        self.next_logger: "Logger" = None

    def set_next_logger(self, next_logger: "Logger") -> None:
        self.next_logger = next_logger

    def log_message(self, message: str, message_level: int) -> None:
        if self.level <= message_level:
            self.write(message)
        if self.next_logger is not None:
            self.next_logger.log_message(message, message_level)

    def write(self, message: str) -> None:
        pass