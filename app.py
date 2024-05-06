import sqlite3

def create_table():
    connection = sqlite3.connect('.db')
    cursor = connection.cursor()
    cursor.execute('''''')
    connection.commit()
    connection.close()
    

def create_user(name, age):
     connection = sqlite3.connect('.db')
     cursor = connection.cursor()
     cursor.execute('''''')
     connection.commit()
     connection.close()   


def update_user(id, name, age):
    connection = sqlite3.connect('.db')
    cursor = connection.cursor()
    cursor.execute('''''')
    connection.commit()   
    connection.close()     