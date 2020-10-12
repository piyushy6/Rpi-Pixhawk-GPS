# Rpi-Pixhawk-GPS
This script is used to store GPS and other Data from Pixhawk to a CSV file in RPi via Mavlink

Use dronekit to conenct pixhawk and Rpi with -

vehicle= connect('udpin:127.0.0.1:14550', wait_ready=False) ; vehicle.wait_ready(True, timeout=300)
