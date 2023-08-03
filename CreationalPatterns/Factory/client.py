from application import MySQLApplication, PostgreSQLApplication


def client_code(app):
    print(app.connect_to_database())


if __name__ == "__main__":
    app = MySQLApplication()
    client_code(app)

    app = PostgreSQLApplication()
    client_code(app)
