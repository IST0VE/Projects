import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 9999))
server_socket.listen()

print("Server is listening...")

client_socket, client_address = server_socket.accept()
print("Accepted connection from", client_address)

client_name = client_socket.recv(1024).decode()
print("Client name:", client_name)

while True:
    request = client_socket.recv(1024).decode()
    if request == "Покажи время":
        response = time.ctime() + " " + client_name
        client_socket.send(response.encode())
    else:
        print("Closing connection with", client_name)
        client_socket.close()
        break

server_socket.close()
