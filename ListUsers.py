import sqlite3 

def list_users(id, name, age):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM user''')
    users = cursor.fetchall()
    for user in users:
        print(user)
    connection.close()    