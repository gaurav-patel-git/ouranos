import socket
from _thread import *


def start_server(port=5555):
    server = socket.gethostbyname(socket.gethostname())    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((server, port))
        print('Server started, waiting for connection')
        return s

    except socket.error as e:
        print(e)



instruction = None
def threaded_client(conn):
    global instruction
    name = conn.recv(2048).decode()
    name = 'pi' if name=='pi' else 'android'
    conn.send(str.encode(f' You are connected as {name}'))
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
        elif instruction and name=='pi':
            conn.send(str.encode(instruction))
            print(f'[Sent] {instruction}')
            instruction = None

    conn.close()


def start():
    server_socket = start_server()
    server_socket.listen()
    while True:
        conn, addr = server_socket.accept()
        start_new_thread(threaded_client, (conn,))

start()



# def threaded_recv(client):
#     connected = True
#     while connected:
#         data = client.recv(2048).decode()
#         connected = (data=='disconnected')
#         if data:
#             print(f'[Recived] {data}')
#             instruction = data

# def threaded_send(client, msg):
#     global instruction
#     connected = True
#     msg = str.encode(msg)
#     while connected:
#         connected = (msg=='disconnected')
#         if msg:
#             client.send(msg)
#             instruction = None
#             print(f'[Sent] {msg}')