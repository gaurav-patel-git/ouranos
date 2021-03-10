import RPi.GPIO as GPIO
import time

in1 = 16
in2 = 18
in3 = 13
in4 = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

GPIO.output(in1, True)
GPIO.output(in2, True)
GPIO.output(in3, True)
GPIO.output(in4, True)
        
while True:
    d=int(input())
    if d == 8:
        GPIO.output(in1, True)
        GPIO.output(in2, False)
        GPIO.output(in3, True)
        GPIO.output(in4, False)
        
    elif d == 2:
        GPIO.output(in1, False)
        GPIO.output(in2, True)
        GPIO.output(in3, False)
        GPIO.output(in4, True)
        
    elif d == 5:
        GPIO.output(in1, True)
        GPIO.output(in2, True)
        GPIO.output(in3, True)
        GPIO.output(in4, True)
        
    elif d == 4:
        GPIO.output(in1, False)
        GPIO.output(in2, True)
        GPIO.output(in3, True)
        GPIO.output(in4, True)
        
    elif d == 6:
        GPIO.output(in1, True)
        GPIO.output(in2, True)
        GPIO.output(in3, False)
        GPIO.output(in4, True)