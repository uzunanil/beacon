from beacon import *
if __name__ == "__main__":
    #f.close()
    
    firstTime = time.time()
    read_from_db()
    
    scan()
    '''con = sqlite3.connect("/home/pi/Desktop/beaconnn.db")
    cursor = con.cursor()
    res = cursor.execute("Select * from beacontime")
    for row in res:
        print(row)''' 
    