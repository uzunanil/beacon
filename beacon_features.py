import subprocess
import time
import os
from beacon import *
from device_sql import *
import _thread
import uuid
from log_dev_sql import *
#subprocess.call('sudo btmgmt find',shell=True)

#print(output)
#*********************CPU_ID*************************
def getserial()
    cpuserial = "0000000000000000"
    try:
        with open('/proc/cpuinfo','r')as f:
            for line in f.readlines():

                if line[0:6]=='Serial'
                    cpuserial = line[10:26]
                    print(cpuserial)
            f.close()
    except:
        cpuserial = "ERROR000000000"

    return cpuserial

#************************UUID************************
#*****************RSSI & DEV_ID**********************
def get_rssi_and_dev_id():
    output = subprocess.check_output('sudo btmgmt find',shell=True)
    lines = output.splitlines()
    dev2rssi = {}
    for i, line in enumerate(lines):
        line = str(line)
        if line.find( "Beacon" )!=-1:
            print ( line )
            print(lines[i-2])
            beacon_infoline = lines[i-2].split()
            print(beacon_infoline)
            rssi = int(beacon_infoline[7])
            device_id = beacon_infoline[3]
            print (rssi)
            print(device_id)
            dev2rssi[device_id] = rssi
    return dev2rssi
#*********************DISTANCE***********************
def calculate_accuracy(txpower, rssi):
    if rssi == 0:
        return -1
    else:
        ratio = rssi/txpower
        if ratio < 1:
            return ratio**10
        else:
            return 0.89976 * ratio**7.7095 + 0.111

def INSERTorUPDATE (existance_table, cursor):
    while True:
        print("**************************")
        dev2rssi = get_rssi_and_dev_id()
        for dev_id, rssi in dev2rssi.items():
            print("rssi : {} txpower : {}".format(rssi, txpower))
            distance = calculate_accuracy(txpower, rssi)
            print("Distance(meter): {}".format(distance/10000))
            if existance_table.get(dev_id) == None:
                existance_table[dev_id] = True
                addBeaconValue(cursor, rssi, dev_id, existance_table)
                uuid = uuid.uuid4()
                mac = get_mac()
                cpuserial = getserial()
                addLogsValue (cursor, uuid, dev_id, mac, cpuserial, distance)
            else:
                update(cursor, dev_id, rssi)
                updateLogValues(distance, dev_id)
        con.commit()
        #Distance Computation

        time.sleep(10)

def sampleThreadFunc(x, y):
    while True:
        print("{} = {} GOOD JOB MAN".format(x,y))
        time.sleep(10)

if __name__ == '__main__':
    createDeviceTable()

    existance_table = readTable("devices.db")
    con = sqlite3.connect("devices.db")
    cursor = con.cursor()
    #_thread.start_new_thread(sampleThreadFunc, ("x", "2"))

    while True:
        print("normal")
        time.sleep(2)#INSERTorUPDATE(existance_table, cursor)
    con.close()
