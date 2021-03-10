import serial
import time 
import string   
import pynmea2 

# lat,lng = 0,0
# def get_cord():
#     global lat, lng
#     while True: 
#         try:       
#             port="/dev/ttyAMA0"
#             ser=serial.Serial(port, baudrate=9600, timeout=0.5) 
#             # dataout =pynmea2.NMEAStreamReader() 
#             newdata=ser.readline() 
#             # print(newdata, 1)
#             newdata = str(newdata)[2:-5]
#             # print(newdata, 2)
#             if newdata[0:5] == "GPGGA":  
#                 newmsg=pynmea2.parse(newdata)  
#                 lat=newmsg.latitude 
#                 lng=newmsg.longitude 
#                 return (lat,lng)
#         except: time.sleep(0.1)


    
def get_position():
    while True: 
        try:       
            port="/dev/ttyAMA0"
            ser=serial.Serial(port, baudrate=9600, timeout=0.5) 
            # dataout =pynmea2.NMEAStreamReader() 
            newdata=ser.readline() 
            # print(newdata, 1)
            newdata = str(newdata)[2:-5]
            # print(newdata, 2)
            if newdata[0:5] == "GPGGA":  
                newmsg=pynmea2.parse(newdata)  
                lat=newmsg.latitude 
                lng=newmsg.longitude 
                return (lat,lng)
        except: time.sleep(0.1)
while True: 
    print(get_position()) []