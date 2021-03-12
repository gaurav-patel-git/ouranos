import socket
from _thread import *

server = '192.168.43.32'
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
    print('Server started, waiting for connection')

except socket.error as e:
    print(e)


def threaded_recv(client):
    connected = True
    while connected:
        data = client.recv(2048).decode()
        connected = (data=='disconnected')
        if data:
            print(f'[Recived] {data}')
            instruction = data

def threaded_send(client, msg):
    global instruction
    connected = True
    msg = str.encode(msg)
    while connected:
        connected = (msg=='disconnected')
        if msg:
            client.send(msg)
            instruction = None
            print(f'[Sent] {msg}')

instruction = None
def threaded_client(conn):
    global instruction
    name = conn.recv(2048).decode()
    name = 'pi' if name=='pi' else 'android'
    conn.send(str.encode(name))
    print(f'[New Connection] Connected to {name}')
    connected = True
    while connected:
        if name!='pi':
            instruction = conn.recv(2048).decode()
            instruction = instruction.strip()
            if instruction:
                print(f'[Recived] {instruction}')
            else:
                connected = False
        if instruction and name=='pi':
            conn.send(str.encode(instruction))
            print(f'[Sent] {instruction}')
            instruction = None
    conn.close()


def start():
    s.listen()
    while True:
        conn, addr = s.accept()
        start_new_thread(threaded_client, (conn,))

start()