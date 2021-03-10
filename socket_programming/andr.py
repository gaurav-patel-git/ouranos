from os import name
import socket
from _thread import *
from time import sleep

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5555
ADDR = (SERVER, PORT)

NAME = 'android'
BUFFER_SIZE = 1024

def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(ADDR) 
    client_socket.send(NAME.encode())    
    msg = client_socket.recv(BUFFER_SIZE).decode()
    print(msg)
    return client_socket


def threaded_recv(client_socket):
    connected = True
    while connected:
        data = client_socket.recv(BUFFER_SIZE).decode()
        connected = (data=='disconnected')
        if data:
            print(f'\n [Recived] {data}') 

m = 'MOTOR'
h = 'HOVER'
p1, p2 = 'PPST', 'MPST'
motor_ctrl = ['', 'bl', 'b', 'br', 'l', 's', 'r', 'fl', 'f', 'fr']
print("""**********
1-9 for motor
"f" and "b" for piston1
"o" and "c" for piston2 
"l" and "r" for hover motor
**********""")
def send_ins(instruction, client):
    ins = None
    try:
        # motor instruction if integer
        ins = int(instruction)
        if 1 <= ins <= 9:
            ins = f'{m} {motor_ctrl[ins]}'
        else: 
            print('Only 1-9 numbers are allowed')
    except:
        # other instruction
        if instruction=='f' or instruction=='b':
            ins = f'{p1} {instruction}'
        elif instruction=='o' or instruction=='c':
            ins = f'{p2} {instruction}'
        elif instruction=='r' or instruction=='l':
            ins = f'{h} {instruction}'
    
    if ins: 
        print(f'[SENT] {ins}')
        client.send(ins.encode())
    else: print(f'Unable to understand instruction {instruction}')


def start():
    client_socket = connect_to_server()
    start_new_thread(threaded_recv, (client_socket,))
    while True:
        instruction = input("Enter the instruction: ")
        send_ins(instruction, client_socket)
        if instruction=="d":
            client_socket.close()
            print('[Connection closed]')
            break

start()        