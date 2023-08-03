from abc import ABC, abstractmethod
from database_connector import DatabaseConnector, MySQLConnector, PostgreSQLConnector


class Application(ABC):
    def __init__(self):
        self.connector = self.create_connector()

    @abstractmethod
    def create_connector(self) -> DatabaseConnector:
        pass

    def connect_to_database(self):
        return self.connector.connect()


class MySQLApplication(Application):
    def create_connector(self) -> DatabaseConnector:
        return MySQLConnector()


class PostgreSQLApplication(Application):
    def create_connector(self) -> DatabaseConnector:
        return PostgreSQLConnector()
