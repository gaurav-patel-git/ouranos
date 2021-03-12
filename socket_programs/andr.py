import socket
from _thread import *
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5555
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT = '!DISCONNECT'
NAME = 'android'
def connect_as(name, ADDR):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    connected = False
    while not connected:
        client.send(str.encode(name))
        print(f'[Sent] {name} as name')
        reply = client.recv(2048).decode()
        if reply==name:
            print(f'[Connected]')
            connected = True
    return client

client = connect_as(NAME, ADDR)

def send_msg(msg):
    message = msg.encode()
    client.send(message)
    print(client.recv(2084).decode(FORMAT))

def threaded_recv(client):
    connected = True
    while connected:
        data = client.recv(2048).decode()
        connected = (data=='disconnected')
        if data:
            print(f'\n [Recived] {data}') 

while True:
    if NAME == 'pi':
        instruction = client.recv(2048).decode()
        if instruction:
            print(f'[Reciced] {instruction}')
    else:
        instruction = input("Enter the instruction: ")
        client.send(str.encode(instruction))
        start_new_thread(threaded_recv, (client,))
        print(f'[Sent] {instruction}')
    if instruction=="disconnect":
        client.close()
        break