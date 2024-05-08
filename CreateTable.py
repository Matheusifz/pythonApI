import sqlite3


def create_table():
    connection = sqlite3.connect("database.db")
    print(connection.total_changes)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE user(id, name, age)")
    connection.commit()
    connection.close()