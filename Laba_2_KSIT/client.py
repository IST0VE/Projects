import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 9999))

client_name = input("Enter your name: ")
clientsocket.send(client_name.encode())

while True:
    request = input("Enter your request: ")
    if request == "Покажи время":
        clientsocket.send(request.encode())
        response = clientsocket.recv(1024).decode()
        print(response)
    else:
        print("Closing connection...")
        clientsocket.close()
        break
clientsocket.close()