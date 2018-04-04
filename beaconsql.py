import sqlite3

def createtable():
    con = sqlite3.connect("beaconnn.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS beacontime (id INTEGER PRIMARY KEY AUTOINCREMENT,t TIMESTAMP DEFAULT CURRENT_TIMESTAMP,mac TEXT,ipAddress TEXT,SignalTime FLOAT,Namespace TEXT,Instance TEXT)")
##       c.execute("alter table beacontime add column 'ipAdress' integer")

    
def addvalue(cursor, con, m, ip, st, nam, ins):
    params = (m , ip, st, nam, ins)
    sql ="INSERT INTO beacontime (mac, ipAddress, SignalTime, Namespace, Instance) VALUES (?,?,?,?,?)"
    cursor.execute(sql,params)
   


def read_from_db():
    con = sqlite3.connect("beaconnn.db")
    c = con.cursor()
    c.execute('SELECT * FROM beacontime ')
    for row in c.fetchall():
        print (row)
    
if __name__ == "__main__":
#read_from_db()
    con = sqlite3.connect("beaconnn.db")
    createtable()
        
    con.commit()
    con.close()
