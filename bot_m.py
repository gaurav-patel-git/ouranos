import socket
import RPi.GPIO as GPIO
import time, threading


def connect_to_server():      
    SERVER = "52.66.240.187"
    PORT = 5555
    ADDR = (SERVER, PORT)
    HEADER = 64
    FORMAT = 'utf-8'
    DISCONNECT = '!DISCONNECT'


    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    client.send(str.encode("pi"))
    # strating welcome message
    msg = client.recv(2048).decode()
    print(msg)
    if msg=='pi': 
        print(f'You are connected to server as {msg}')
        return client
    else: print('Unable to connect to server')


# def set_pins():
# motor pins
in1 = 12
in2 = 16
in3 = 18
in4 = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

GPIO.output(in1, True)
GPIO.output(in2, True)
GPIO.output(in3, True)
GPIO.output(in4, True)

# piston pins
pst1, pst2 = 40, 32
GPIO.setup(pst1, GPIO.OUT)
GPIO.setup(pst2, GPIO.OUT)

GPIO.output(pst1, True)
GPIO.output(pst2, True)

# hover

in1_hvr = 37
in2_hvr = 35
en_hvr = 33
speed = 100

GPIO.setup(in1_hvr,GPIO.OUT)
GPIO.setup(in2_hvr,GPIO.OUT)
GPIO.setup(en_hvr,GPIO.OUT)

GPIO.output(in1_hvr,GPIO.LOW)
GPIO.output(in2_hvr,GPIO.LOW)
p=GPIO.PWM(en_hvr,1000)
p.start(speed)

def recv_msg(clt):
    while True:

        msg = clt.recv(2048).decode()
        msg = msg.strip()
        msg = msg.split()

        if msg:
            ins_type = msg[0].upper()
            instruction = msg[1]
            print(f'>> Type {ins_type} and msg {instruction}')
            if ins_type == 'PPST':
                plnt_pst(instruction)
            elif ins_type == 'MPST':
                mouth_pst(instruction)                
            elif ins_type=='HOVER':
                hover_cntrl(instruction)
            else:
                motor_cntrl(instruction)

                
def send_msg(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' *  (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2084).decode(FORMAT))


def motor_cntrl(instruction):
        # instruction = client.recv(2048).decode()
        # instruction = instruction.strip()
    if instruction:
        # print(instruction)
        #d=int(input())
        if instruction=='f':
            GPIO.output(in1, True)
            GPIO.output(in2, False)
            GPIO.output(in3, True)
            GPIO.output(in4, False)
            
        elif  instruction=='b':
            GPIO.output(in1, False)
            GPIO.output(in2, True)
            GPIO.output(in3, False)
            GPIO.output(in4, True)
            
        elif  instruction=='s':
            GPIO.output(in1, True)
            GPIO.output(in2, True)
            GPIO.output(in3, True)
            GPIO.output(in4, True)
            
        elif  instruction=='r':
            GPIO.output(in1, True)
            GPIO.output(in2, False)
            GPIO.output(in3, True)
            GPIO.output(in4, True)
        
        elif  instruction=='br':
            GPIO.output(in1, False)
            GPIO.output(in2, True)
            GPIO.output(in3, True)
            GPIO.output(in4, True)
            
            
        elif instruction=='l':
            GPIO.output(in1, True)
            GPIO.output(in2, True)
            GPIO.output(in3, True)
            GPIO.output(in4, False)
        elif instruction=='bl':
            GPIO.output(in1, True)
            GPIO.output(in2, True)
            GPIO.output(in3, False)
            GPIO.output(in4, True)




def mouth_pst(instruction, rly_pin=32):
    # rly_pin = 32
    if instruction=='o':
        GPIO.output(rly_pin, GPIO.LOW)
        print("Mouth of planter is opend")
    else:
        GPIO.output(rly_pin, GPIO.HIGH)
        print("Mouth of planter is closed")

def plnt_pst(instruction, rly_pin=40):
    if instruction=='f':
        GPIO.output(rly_pin, GPIO.LOW)
        print('Hurry!! We have planted')
    else:
        GPIO.output(rly_pin, GPIO.HIGH)
        print('Planter piston backward')

def hover_cntrl(instruction, in1=37, in2=35):
    if instruction=='r':
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        print('Hover right')
    elif instruction=='l':
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        print('Hover left')
    else: 
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        print('Hover stop')



delay = 1
def main():
    client = connect_to_server()
    time.sleep(delay)
    # set_pins()
    # time.sleep(delay)
    msg_thread = threading.Thread(target=recv_msg, args=(client,))
    msg_thread.start()


main()











# def motor_cntrl():
#     while True:
#         instruction = client.recv(2048).decode()
#         instruction = instruction.strip()
#         if instruction:
#             print(instruction)
#             #d=int(input())
#             if instruction=='f':
#                 GPIO.output(in1, True)
#                 GPIO.output(in2, False)
#                 GPIO.output(in3, True)
#                 GPIO.output(in4, False)
                
#             elif  instruction=='b':
#                 GPIO.output(in1, False)
#                 GPIO.output(in2, True)
#                 GPIO.output(in3, False)
#                 GPIO.output(in4, True)
                
#             elif  instruction=='s':
#                 GPIO.output(in1, True)
#                 GPIO.output(in2, True)
#                 GPIO.output(in3, True)
#                 GPIO.output(in4, True)
                
#             elif  instruction=='r':
#                 GPIO.output(in1, True)
#                 GPIO.output(in2, False)
#                 GPIO.output(in3, True)
#                 GPIO.output(in4, True)
            
#             elif  instruction=='br':
#                 GPIO.output(in1, False)
#                 GPIO.output(in2, True)
#                 GPIO.output(in3, True)
#                 GPIO.output(in4, True)
                
                
#             elif instruction=='l':
#                 GPIO.output(in1, True)
#                 GPIO.output(in2, True)
#                 GPIO.output(in3, True)
#                 GPIO.output(in4, False)
#             elif instruction=='bl':
#                 GPIO.output(in1, True)
#                 GPIO.output(in2, True)
#                 GPIO.output(in3, False)
#                 GPIO.output(in4, True)


