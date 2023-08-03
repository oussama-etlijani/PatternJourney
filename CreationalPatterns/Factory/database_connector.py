from abc import ABC, abstractmethod


class DatabaseConnector(ABC):
    @abstractmethod
    def connect(self):
        pass


class MySQLConnector(DatabaseConnector):
    def connect(self):
        return "MySQL Database connection established"


class PostgreSQLConnector(DatabaseConnector):
    def connect(self):
        return "PostgreSQL Database connection established"
