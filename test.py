from beacon import *
from beacon_features import *
from device_sql import *

if __name__ == "__main__":
    #f.close()
    #DISTANCE OPERATIONS
    con = sqlite3.connect("devices.db")
    cursor = con.cursor()
    existance_table = readTable("devices.db")
    try:
        _thread.start_new_thread(INSERTorUPDATE, (existance_table, cursor))
    except Exception as e:
        print("Error : {}".format(e))

    #BEACON SEARCH
    firstTime = time.time()
    read_from_db()

    scan()
    '''con = sqlite3.connect("/home/pi/Desktop/beaconnn.db")
    cursor = con.cursor()
    res = cursor.execute("Select * from beacontime")
    for row in res:
        print(row)'''
