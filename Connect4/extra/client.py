import socket

PORT = 5505
SERVER_IP = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER_IP, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"
FORMAT = 'utf-8'
MAX_VAl = 2048

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def snd(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (MAX_VAl - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(MAX_VAl).decode(FORMAT))

# while True:
#     print("Enter the choice :")
#     print("1. send message")
#     print("2. exit")
#     choice = int(input())
#     if choice == 1:
#         print("Enter the message: ")
#         snd(str(input()))
#     if choice == 2:
#         snd(DISCONNECT_MESSAGE)
#         break
#     else:
        # continue