import sqlite3

def fectch_db():
    connection = sqlite3.connect("data/Account.db") 
    cursor = connection.cursor()
    cursor.execute()
    