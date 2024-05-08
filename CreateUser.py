import sqlite3

def create_user(name, age):
     connection = sqlite3.connect('.db')
     cursor = connection.cursor()
     cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''')
     connection.commit()
     connection.close()   