import RPi.GPIO as GPIO
from time import sleep



in1 = 15
in2 = 13
in3 = 37
in4 = 29
pwm1 = 33
pwm2 = 32

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#mtr 1
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(pwm1, GPIO.OUT)

GPIO.output(in1, True)
GPIO.output(in2, False)
GPIO.output(pwm1, True)

mtr1_pwm = GPIO.PWM(pwm1, 1023)
mtr1_pwm.start(100)



# mtr 2
# GPIO.setup(in3, GPIO.OUT)
# GPIO.setup(in4, GPIO.OUT)
# GPIO.setup(pwm2, GPIO.OUT)

# GPIO.output(in3, True)
# GPIO.output(in4, False)
# GPIO.output(pwm2, True)

# mtr2_pwm = GPIO.PWM(pwm2, 1023)
# mtr2_pwm.start(30)


while True:
    pass
    # for duty in range(100,0,-1):
    #     print(f'motor 1 {duty}')
    #     mtr1_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
    #     sleep(0.1)
    # sleep(0.5)
    
    # for duty in range(100,-1,-1):
    #     print(f'motor 2 {duty}')
    #     mtr2_pwm.ChangeDutyCycle(duty)
    #     sleep(0.1)
    # sleep(0.5)