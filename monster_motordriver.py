import RPi.GPIO as GPIO
from time import sleep



# dir1 = 15
# dir2 = 13
# in3 = 37
# in4 = 29

dir1 = 12
pwm1 = 32

dir2 = 16
pwm2 = 33

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(dir1, GPIO.OUT)
GPIO.setup(pwm1, GPIO.OUT)

GPIO.setup(dir2, GPIO.OUT)
GPIO.setup(pwm2, GPIO.OUT)


mtr1_pwm = GPIO.PWM(pwm1, 1023)
mtr2_pwm = GPIO.PWM(pwm2, 1023)

def mtr_cntrl(instruction, speed=70):
    mtr1_pwm.start(0)
    mtr2_pwm.start(0)
    if instruction=='f':
        GPIO.output(dir1, True)
        GPIO.output(dir2, True)
        mtr1_pwm.ChangeDutyCycle(speed)
        mtr2_pwm.ChangeDutyCycle(speed)
    
    elif instruction=='b':
        GPIO.output(dir1, False)
        GPIO.output(dir2, False)
        mtr1_pwm.ChangeDutyCycle(speed)
        mtr2_pwm.ChangeDutyCycle(speed)

    elif instruction=='l':
        GPIO.output(dir1, True)
        GPIO.output(dir2, False)
        mtr1_pwm.ChangeDutyCycle(speed)
        mtr2_pwm.ChangeDutyCycle(speed)
        mtr1_pwm.ChangeDutyCycle(speed)
        mtr2_pwm.ChangeDutyCycle(speed)

    elif instruction=='r':
        GPIO.output(dir1, False)
        GPIO.output(dir2, True)
        mtr1_pwm.ChangeDutyCycle(speed)
        mtr2_pwm.ChangeDutyCycle(speed)
    
    elif instruction=='fl':
        GPIO.output(dir1, True)
        mtr1_pwm.ChangeDutyCycle(speed)
        mtr2_pwm.ChangeDutyCycle(0)

    elif instruction=='br':
        GPIO.output(dir2, False)
        mtr1_pwm.ChangeDutyCycle(0)
        mtr2_pwm.ChangeDutyCycle(speed)

    elif instruction=='fr':
        GPIO.output(dir2, True)
        mtr1_pwm.ChangeDutyCycle(0)
        mtr2_pwm.ChangeDutyCycle(speed)

    elif instruction=='bl':
        GPIO.output(dir1, False)
        mtr1_pwm.ChangeDutyCycle(speed)
        mtr2_pwm.ChangeDutyCycle(0)
    
    elif instruction=='s':
        mtr1_pwm.ChangeDutyCycle(0)
        mtr2_pwm.ChangeDutyCycle(0)
    elif instruction=='++' and speed<100:
        speed+=10
    elif instruction=='--' and speed>10:
        speed-=10
    else:
        print('not able to unsderstand instruction')
        


while True:
    ins = input('Enter instruction: ')
    mtr_cntrl(ins)