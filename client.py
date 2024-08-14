import socket, threading

HEADER = 64
PORT = 5050
SERVER = input("server address")
FORMAT = "utf-8"
DISS = "[DISSCONNECT]"
ADDR = (SERVER, PORT)

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Socket.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b" " * (HEADER - len(send_len))
    Socket.send(send_len)
    Socket.send(message)

def listen():
    while True:
        msg_length = Socket.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
        else:
            break
        msg = Socket.recv(msg_length).decode(FORMAT)
        if msg == DISS:
            break
        print(msg)

thread = threading.Thread(target=listen)
thread.start()

while True:
    inp = input()
    if inp == "EXIT":
        break
    send(inp)

send(DISS)
