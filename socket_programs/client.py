import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5555
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT = 'DISCONNECT'


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_msg(msg):
    message = msg.encode()
    client.send(message)
    print(client.recv(2084).decode(FORMAT))

client.send(str.encode('pi'))
while True:
    instruction = client.recv(2048).decode()
    if instruction:
        print(f'[Received] {instruction}')
client.close()    
