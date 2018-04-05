import sqlite3

def createtable():
    con = sqlite3.connect("device_logs.db")
    cursor =con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS MY_DEVICE_LOGS (id INTEGER PRIMARY KEY AUTOINCREMENT,,create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,DEVICE_UNIQUE_IDENTIFIER TEXT,mac TEXT,)")
