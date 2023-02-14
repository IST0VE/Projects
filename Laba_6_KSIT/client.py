import socket

HOST, PORT = "localhost", 20001

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    name = input("Enter your name: ")
    message = name.encode()
    client_socket.sendto(message, (HOST, PORT))
    data, server = client_socket.recvfrom(1024)
    response = data.decode()
    print(response)
