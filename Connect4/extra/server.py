import socket
import threading

PORT = 5505
SERVER_IP = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER_IP, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"
FORMAT = 'utf-8'
MAX_VAl = 2048

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
recived = []

def getcol():
    recived.reverse()
    return recived[0]

def handel_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.\n")
    connected = True
    while connected:
        msg_length = conn.recv(int(MAX_VAl)).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            recived.append(msg)
            conn.send("Message recevied".encode(FORMAT))

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER_IP}\n")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handel_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] = {threading.active_count() - 1}\n")

print("[STARTING] server is starting...")
start()
