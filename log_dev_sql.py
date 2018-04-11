import sqlite3

def createLogTable():
    con = sqlite3.connect("devices.db")
    cursor =con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS MY_DEVICE_LOGS (id INTEGER PRIMARY KEY AUTOINCREMENT,uuid TEXT,create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,DEVICE_UNIQUE_IDENTIFIER TEXT,mac_id TEXT,cpu_id TEXT,distance FLOAT,last_update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,FEED_FLAG INT DEFAULT 0)")



def addLogsValue (cursor, uuid, dev_id, mac, cpuserial, distance):
    params = (uuid, dev_id, mac, cpuserial, distance)
    sql = "INSERT INTO MY_DEVICE_LOGS (uuid, device_id, mac, cpuserial, distance) VALUES (?,?,?,?,?)"
    cursor.execute(sql,params)


def updateLogValues(cursor, device_id, distance):
    params = (device_id, distance)
    query  = ("UPDATE MY_DEVICES SET distance={}, last_update_date=GETDATE() where device_id={};".format(distance, device_id))
    cursor.execute(query)
