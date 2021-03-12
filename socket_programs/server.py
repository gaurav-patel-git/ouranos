import socket
from _thread import *

server = socket.gethostbyname(socket.gethostname())
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
    print('Server started, waiting for connection')

except socket.error as e:
    print(e)



def client_name(conn):
    name = ""
    while not name:
        conn.send(str.encode('Who are you??'))
        name = conn.recv(2048).decode()
    conn.send(str.encode('connected'))
    return name
    
instruction = ""
def threaded_client(conn):
    global instruction
    name = client_name(conn)
    print(f'[Connected] {name}')
    connected = True
    while connected:
        if name=='android':
            instruction = conn.recv(2048).decode()
            print(f'[Recived] {instruction}')
        if instruction == "disconnect":
            connected = False
        if name=='pi' and instruction:
            conn.send(str.encode(instruction))
            print(f'[Sent] {instruction}')
            instruction = ""
    conn.close()

def start():
    s.listen()
    while True:
        conn, addr = s.accept()
        start_new_thread(threaded_client, (conn,))

start()