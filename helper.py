import pynmea2 
import RPi.GPIO as GPIO
import time
import serial, time, threading
from geographiclib.geodesic import Geodesic
import haversine as hs
from haversine import Unit
import py_qmc5883l

# baud_rate = 9600
# timeout = 1
# heading = 0

# def sanetize_heading(head):
#     global heading
#     try:
#         heading = int(head)
#     except ValueError: 
#         heading = int(head[0:2])
#     except: 
#         heading = int(head[0])
# def get_mag_bearing():
#     global heading
#     while True:
#         num = 0
#         try:
#             ser =  serial.Serial(f'/dev/ttyUSB{num}', baud_rate)
#         except: 
#             num += 1
#             ser =  serial.Serial(f'/dev/ttyUSB{num}', baud_rate)
#         try:
#             line = str(ser.readline())
#             print(line)
#             head = line[2:5]
#             # print(head, 'head')
#             sanetize_heading(head)
#             # heading = int(heading) if heading[0] != ':' else int(heading[1:])                
#             print(heading)
#         except: 
#             print('Problem in getting degree')
#             time.sleep(0.1)
#         ser.close()
#         time.sleep(0.1)




class Agrobot:
    
    def __init__(self, dest_pos):
        GPIO.setwarnings(False)
        self.heading = None
        self.position = None
        self.dest_pos = dest_pos
        
        # setting pins
        self.in1 = 15
        self.in2 = 13
        self.in3 = 37
        self.in4 = 29
        self.pwm1 = 32
        self.pwm2 = 33


        self.set_pins(self.in1, self.in2, self.in3, self.in4, self.pwm1, self.pwm2)

        # magnetometer and gps thread
        gps_thread = threading.Thread(target=self.get_position)
        gps_thread.start()
        mag_thread = threading.Thread(target=self.get_mag_bearing)
        mag_thread.start()
        print('Threads have been started hope to get data')
        # while self.position and self.heading is None:
        #     print(f'Postion is {self.position} and Heading is {self.heading}.\nWaiting for 2 sec')
        time.sleep(2)

    def set_pins(self, in1, in2, in3, in4, pwm1, pwm2):    
        print(f'input pins are {in1}, {in2}, {in3} and {in4}')
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)
        GPIO.setup(in3, GPIO.OUT)
        GPIO.setup(in4, GPIO.OUT)
        GPIO.setup(pwm1, GPIO.OUT)
        GPIO.setup(pwm2, GPIO.OUT)

        GPIO.output(in1, True)
        GPIO.output(in2, True)
        GPIO.output(in3, True)
        GPIO.output(in4, True)
        GPIO.output(pwm1, True)
        GPIO.output(pwm2, True)

        self.mtr1_pwm = GPIO.PWM(pwm1, 1023)
        self.mtr2_pwm = GPIO.PWM(pwm2, 1023)        

        self.move('s')

    def get_mag_bearing(self):
        mag_sensor = py_qmc5883l.QMC5883L()
        while True:
            try:
                self.heading = mag_sensor.get_bearing()
                # print(self.heading, 'get_mag_bearing func call')
            except: 
                print('problem in getting degree')
                time.sleep(0.1)

    def get_distance(self, unit=Unit.METERS):
        while self.position is None:
            pass
        distance = hs.haversine(self.position, self.dest_pos, unit=unit)
        # print(f'Distance from cur pos to desination is {distance} meters')
        return distance


    def dest_bearing(self):
        while self.position is None:
            time.sleep(0.1)
        lat1, lat2 = self.position[0], self.dest_pos[0]
        long1, long2 = self.position[1], self.dest_pos[1]
        brng = Geodesic.WGS84.Inverse(lat1, long1, lat2, long2)['azi1']
        return brng
    
    def get_position(self):
        while True: 
            try:       
                port="/dev/ttyAMA0"
                ser=serial.Serial(port, baudrate=9600) 
                newdata=ser.readline() 
                newdata = str(newdata)[2:-5]
                if newdata[0:5] == "GPGGA":  
                    newmsg=pynmea2.parse(newdata)  
                    lat=newmsg.latitude 
                    lng=newmsg.longitude
                    # print(lat,lng)
                    self.position = (lat,lng)
            except: time.sleep(0.1)
    
    def align(self, error):
        desired_heading = abs(self.dest_bearing())
        print(f'Aliging bot cureent heading {self.heading} and destation heading is {desired_heading} ')
        print(self.heading)
        while not desired_heading-error <= self.heading <= desired_heading+error:
            self.move('l')
        self.move('s')
        print('bot aligned')
        return True

    

    def move(self, instruction):
        self.mtr1_pwm.start(30)
        self.mtr2_pwm.start(30)
        if instruction:
            # print(instruction)
            #d=int(input())
            if instruction=='f':
                GPIO.output(self.in1, True)
                GPIO.output(self.in2, False)
                GPIO.output(self.in3, True)
                GPIO.output(self.in4, False)
                
            elif  instruction=='b':
                GPIO.output(self.in1, False)
                GPIO.output(self.in2, True)
                GPIO.output(self.in3, False)
                GPIO.output(self.in4, True)
                
            elif  instruction=='s':
                GPIO.output(self.in1, True)
                GPIO.output(self.in2, True)
                GPIO.output(self.in3, True)
                GPIO.output(self.in4, True)
                self.mtr1_pwm.start(0)
                self.mtr2_pwm.start(0)
                
            elif  instruction=='r':
                GPIO.output(self.in1, True)
                GPIO.output(self.in2, False)
                GPIO.output(self.in3, True)
                GPIO.output(self.in4, True)
            
            elif  instruction=='br':
                GPIO.output(self.in1, False)
                GPIO.output(self.in2, True)
                GPIO.output(self.in3, True)
                GPIO.output(self.in4, True)
                
            elif instruction=='l':
                GPIO.output(self.in1, True)
                GPIO.output(self.in2, True)
                GPIO.output(self.in3, True)
                GPIO.output(self.in4, False)
            
            elif instruction=='bl':
                GPIO.output(self.in1, True)
                GPIO.output(self.in2, True)
                GPIO.output(self.in3, False)
                GPIO.output(self.in4, True)
        else: print('Cannot understand instruction sorry...')

    def navigate(self, radius, error):
        while True:
            distance = self.get_distance()
            if distance <= radius:
                print('Hurray we have reached to destination!!!!')
                break
            else:
                desired_heading = abs(self.dest_bearing())
                if desired_heading-10 <= self.heading <= desired_heading+10:
                    self.align(error)
                self.move('f')


dest_pos = (23.129831833333334, 79.87441966666667)
print('bot object created')
bot = Agrobot(dest_pos)

def distance_left():
    while True:
        print(f' {bot.get_distance()} meters left to destination')
        time.sleep(1)

dis_thread = threading.Thread(target=(distance_left))
dis_thread.start()
radius, head_error = 2, 12
# bot.navigate(radius, head_error)
while True:
    bot.move('f')
    print('forward for 2sec')
    time.sleep(10)
    bot.move('s')
    time.sleep(5)
    bot.move('b')
    print('back for 2 sec')
    time.sleep(10)
    bot.move('s')
    time.sleep(5)
