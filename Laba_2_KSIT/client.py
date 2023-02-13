import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 9999))

client_name = input("Enter your name: ")
clientsocket.send(client_name.encode())

message = input("Enter your message: ")
clientsocket.send(message.encode())

response = clientsocket.recv(1024).decode()
print("Received response:", response)

clientsocket.close()