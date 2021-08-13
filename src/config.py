import sqlite3
database = "./database/persons.sqlite3"

def get_connection():
    try:
        connection = sqlite3.connect(database)
        return connection
    except Exception as e:
        print(e)
