import sqlite3

def delete_user(id):
    connection = sqlite3.connect("database.db")   
    cursor = connection.cursor()
    cursor.execute('''DELETE FROM user WHERE id = ?''',("1") )
    connection.commit()
    connection.close()  