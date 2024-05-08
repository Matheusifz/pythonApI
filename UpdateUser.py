import sqlite3 

def update_user(id, name, age):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''''')
    connection.commit()   
    connection.close()   