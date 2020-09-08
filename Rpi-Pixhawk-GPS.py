from dronekit import connect, Command, LocationGlobal
from pymavlink import mavutil
import time, sys, argparse, math
import csv, datetime, os
from time import sleep

vehicle= connect('udpin:127.0.0.1:14550', wait_ready=False) ; vehicle.wait_ready(True, timeout=300)




def logfilename():
    now = datetime.datetime.now()
    return 'gps_%0.4d-%0.2d-%0.2d_%0.2d-%0.2d-%0.2d.csv' % \
                (now.year, now.month, now.day,
                 now.hour, now.minute, now.second)


path='GPS CSV'  #To save CSV in GPS CSV folder


csv_file = os.path.join(path,logfilename())
csv_file = open(csv_file, mode='w')

fieldnames = ["time", "latitude","longitude","altitude"]


writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
writer.writeheader()
         

#print ("gps: %s") %vehicle.gps_0

#print ("Altitude: %s") %vehicle.location.global_relative_frame.alt
#print ("gps: %s") %vehicle.location.global_frame
#print ("gps: %s") %vehicle.location.global_frame.alt
    
print("Gps Values Getting stored in CSV")    
while True:
    
    #data = vehicle.location.global_frame
    latitude = vehicle.location.global_frame.lat
    longitude= vehicle.location.global_frame.lon
    altitude= vehicle.location.global_frame.alt
                     
    sleep(1) #This SLEEP is used to change the GPS Mavlink Frequency stored in Rpi
    
    #print("gps %s") % longitude
    #print("gps %s") % latitude 
    writer.writerow({'time':str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                        'latitude':latitude,'longitude':longitude,'altitude':altitude})
    

    csv_file.flush()



  
  

    
    
