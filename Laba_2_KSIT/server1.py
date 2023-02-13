# Код для сервера
import socket
import time
# создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# связываем сокет с локальным адресом
server_socket.bind(("localhost", 20001))
# начинаем прослушивание сокета
server_socket.listen()

print("Server is listening...")
# ждем подключения клиента
client_socket, client_address = server_socket.accept()
print("Accepted connection from", client_address)
# принимаем данные от клиента
client_name = client_socket.recv(1024).decode()
print("Client name:", client_name)

while True:
    # принимаем данные от клиента
    request = client_socket.recv(1024).decode()
    # проверяем полученные данные на правду
    if request == "Покажи время":
        # если это правда, отправляем клиенту текущее время
        response = time.ctime() + " " + client_name
        client_socket.send(response.encode('utf-8'))
    else:
        # если это не правда, закрываем связь с клиентом
        print("Closing connection with", client_name)
        client_socket.close()
        break
# закрываем сокет
server_socket.close()
