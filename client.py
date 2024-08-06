import socket, threading

HEADER = 64
PORT = 5050
SERVER = "10.0.0.5" #local ip :D
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

send("hail hitler")
send("I hate communism")
send("I need drugs")

send(DISS)
