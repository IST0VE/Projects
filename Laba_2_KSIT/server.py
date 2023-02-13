# Server side code

import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 9999))
serversocket.listen(5)

print("Server is ready to receive requests")

while True:
    (clientsocket, client_address) = serversocket.accept()
    print("Received a connection from {}".format(client_address))

    client_name = clientsocket.recv(1024).decode()
    print("Client {} is connected".format(client_name))

    message = clientsocket.recv(1024).decode()
    if message == "Покажи время":
        current_time = time.ctime()
        response = "{} says: {}".format(client_name, current_time)
        clientsocket.send(response.encode('utf-8'))
    else:
        response = "Invalid request"
        clientsocket.send(response.encode('utf-8'))
        clientsocket.close()
        break

serversocket.close()