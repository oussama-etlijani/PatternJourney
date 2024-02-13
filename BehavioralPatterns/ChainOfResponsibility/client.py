from concrete_handlers import ConsoleLogger, EmailLogger, FileLogger
from handler_interface import Logger


def main() -> None:
    # Create the chain of loggers
    console_logger = ConsoleLogger(Logger.DEBUG)
    file_logger = FileLogger(Logger.INFO, "app.log")
    email_logger = EmailLogger(Logger.ERROR, "admin@example.com")

    console_logger.set_next_logger(file_logger)
    file_logger.set_next_logger(email_logger)

    # Simulate log messages
    console_logger.log_message("This is a debug message.", Logger.DEBUG)
    console_logger.log_message("This is an info message.", Logger.INFO)
    console_logger.log_message("This is an error message.", Logger.ERROR)


if __name__ == "__main__":
    main()
