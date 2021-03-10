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

def threaded_client(conn):
    print(f'[Connected] New connection established')
    connected = True
    while connected:
        data = conn.recv(2048).decode()
        print(f'[Recived] {data}')
        reply = ''
        if data:
            reply = data
        if not data:
            connected = False

        conn.send(str.encode(reply))
        print(f'[Sent] {reply}')
    conn.close()


def start():
    s.listen()
    while True:
        conn, addr = s.accept()
        start_new_thread(threaded_client, (conn,))

start()