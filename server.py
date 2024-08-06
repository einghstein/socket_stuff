import socket, json, threading

"""
dont question most of the technicall stuff its not my code :D
but hey it works (kinda)
"""

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISS = "[DISSCONNECT]"

data_add = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

class is_running:
    run = True


def handle_clients(conn, addr):
    print("[SERVER] New thread started")
    print(f"[SERVER] {addr} connected")
    while is_running.run:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
        else:
            break
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISS:
            break
        
        data_add.append(f"{addr}:{msg}")
        print(f"[{addr}]: {msg}")


    conn.close()
    print(f"[SERVER] {addr} DISSconnected cleanly")

def consol():
    while is_running.run:
        pass

def start():
    server.listen()
    print(f"[LISTENNING] at {ADDR}")
    thread = threading.Thread(target=consol)
    thread.start()
    while is_running.run:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clients, args=(conn, addr))
        thread.start()
        print(f"[SERVER] New client connected ({threading.active_count() - 2})")

print("[SERVER] Server is starting...")
start()