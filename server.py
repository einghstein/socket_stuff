import socket, json, threading

"""
dont question most of the technicall stuff its not my code :D
but hey it works (kinda)
sphaggeti
"""

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISS = "[DISSCONNECT]"

everyone = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
run = True
def handle_clients(conn, addr):
    global run
    print("[SERVER] New thread started")
    print(f"[SERVER] {addr} connected")
    while True:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
        else:
            break
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISS:
            break
        print(f"{addr}: {msg}")
        send_to_everyone(msg,addr,conn)

    conn.close()
    print(f"[SERVER] {addr} DISSconnected cleanly")
    everyone.remove(conn)
    send_to_everyone(f"{addr} DISSconnected cleanly","[SERVER]")

def send_to_everyone(msg, author, exc=None):
    for i in everyone:
        if i != exc:
            send(f"{author}: {msg}",i)

def main():
    server.listen()
    print(f"[LISTENNING] at {ADDR}")
    while True:
        conn, addr = server.accept()
        everyone.append(conn)
        thread = threading.Thread(target=handle_clients, args=(conn, addr))
        thread.setDaemon(True)
        thread.start()
        print(f"[SERVER] New client connected ({threading.active_count() - 2})")

def send(msg,connection):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b" " * (HEADER - len(send_len))
    connection.send(send_len)
    connection.send(message)

print("[SERVER] Server is starting...")
thread = threading.Thread(target=main)
thread.setDaemon(True)
thread.start()

print("[CONSOLE] ready")
while run:
    command = input()
    if command == "EXIT":
            exit()
