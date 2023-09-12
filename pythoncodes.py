import serial
import time
import string
import pynmea2
import requests
import datetime
import pytz


url = "https://backend-for-sih.onrender.com/save_location"
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=4)
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0:
            newdata = ser.readline()
            print(newdata)
            if newdata[1:6] == bytes("GPGGA",'utf-8'):
                print(newdata)
                newmsg=pynmea2.parse(newdata.decode('utf-8'))
                lat= newmsg.latitude
                lng= newmsg.longitude
                timestamp= newmsg.timestamp
                today = datetime.datetime.now(tz=pytz.utc)
                localT = datetime.datetime(today.year, today.month, today.day, newmsg.timestamp.hour, newmsg.timestamp.minute, newmsg.timestamp.second, tzinfo=pytz.utc)
                altitude = newmsg.altitude
                sendobj = {"latitude":lat, "longitude":lng, "time": (str(localT.astimezone().isoformat())), "altitude":altitude}
                x = requests.post(url, json = sendobj)
                gps = "Time = "+str(newmsg.timestamp)+" altitude = "+str(newmsg.altitude)+" Latitude = " + str(lat) + " and Longitude = " + str(lng)
                print(sendobj)








import serial
import time
import string
import pynmea2
import requests
import datetime
import pytz


url = "https://backend-for-sih.onrender.com/save_location"

while True:
        port="/dev/ttyUSB0"
        ser=serial.Serial(port, 9600, timeout=0.2)
        ser.reset_input_buffer()
        dataout = pynmea2.NMEAStreamReader()
        newdata=ser.readline()
        print(newdata)
        if newdata[0:5] == bytes("$GPRMC",'utf-8'):
                print(newdata)
                newmsg=pynmea2.parse(newdata.decode('utf-8'))
                lat= newmsg.latitude
                lng= newmsg.longitude
                timestamp= newmsg.timestamp
                today = datetime.datetime.now(tz=pytz.utc)
                localT = datetime.datetime(today.year, today.month, today.day, newmsg.timestamp.hour, newmsg.timestamp.minute, newmsg.timestamp.second, tzinfo=pytz.utc)
                altitude = newmsg.altitude
                sendobj = {"latitude":lat, "longitude":lng, "time": (str(localT.astimezone().isoformat())), "altitude":altitude}
                x = requests.post(url, json = sendobj)
                gps = "Time = "+str(newmsg.timestamp)+" altitude = "+str(newmsg.altitude)+" Latitude = " + str(lat) + " and Longitude = " + str(lng)
                print(sendobj)


import serial
import time
import string
import pynmea2

while True:
        port="/dev/ttyAMA0"
        ser=serial.Serial(port, baudrate=9600, timeout=0.5)
        dataout = pynmea2.NMEAStreamReader()
        newdata=ser.readline()

        if newdata[0:6] == "$GPRMC":
                newmsg=pynmea2.parse(newdata)
                lat=newmsg.latitude
                lng=newmsg.longitude
                gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
                print(gps)
