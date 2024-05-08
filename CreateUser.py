import sqlite3

def create_user(id, name, age):
     connection = sqlite3.connect('database.db')
     cursor = connection.cursor()
     cursor.execute('''INSERT INTO user (id, name, age) VALUES (?, ?, ?)''', ('id 123', 'John', 26))
     connection.commit()
     connection.close()   