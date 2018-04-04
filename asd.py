import subprocess
import time
import os
from beacon import *
from device_sql import *
#subprocess.call('sudo btmgmt find',shell=True)

#print(output)


def main():
    output = subprocess.check_output('sudo btmgmt find',shell=True)
    lines = output.splitlines()
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
           return rssi

def calculate_accuracy(txpower, rssi):
    if rssi == 0:
        return -1
    else:
        ratio = rssi/txpower
        if ratio < 1:
            return ratio**10
        else:
            return 0.89976 * ratio**7.7095 + 0.111

if __name__ == '__main__':
    while True:
        print("**************************")
        
        rssi = main()
        print("rssi : {} txpower : {}".format(rssi, txpower))
        distance = calculate_accuracy(txpower, rssi)
    
        print("Distance: {}".format(distance/100))
    
    
    