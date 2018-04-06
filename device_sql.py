import sqlite3

def createDeviceTable():
    con = sqlite3.connect("devices.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS MY_DEVICES (id INTEGER PRIMARY KEY AUTOINCREMENT,create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,DEVICE_UNIQUE_IDENTIFIER TEXT,RSSI INT,last_update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,IS_ACTIV INT DEFAULT 1)")

def addBeaconValue(cursor, rssi, dev_id, existance_table):
    params = (dev_id, rssi)
    sql ="INSERT INTO MY_DEVICES (device_id, rssi) VALUES (?,?)"
    cursor.execute(sql,params)
    existance_table[dev_id] = True

def update(cursor, device_id, rssi):
   params = (device_id, rssi)
   query  = ("UPDATE MY_DEVICES SET rssi={}, last_update_date=GETDATE() where device_id={};".format(rssi, device_id))
   cursor.execute(query)s

def readTable(database_name):
    existance_table = {}
    con = sqlite3.connect(database_name)
    c = con.cursor()
    c.execute('SELECT * FROM MY_DEVICES')
    for row in c.fetchall():
        curr_dev_id = row[2]
        existance_table[curr_dev_id] = True
        print(row)
    return existance_table

'''
existance_table = readTable("devices.db")
existance_table.get(dev_id) == NULL
insert
else
update
'''
if __name__ == "__main__":
#read_from_db()
    con = sqlite3.connect("devices.db")
    createtable()

    con.commit()
    con.close()
