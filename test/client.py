# Код для клиента
import socket

# Создание сокета клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение к серверу
server_address = ('localhost', 20001)
client_socket.connect(server_address)

# Отправка сообщения
message = input("Enter a message to send to the server: ")
client_socket.sendall(message.encode())

# Получение ответа от сервера
response = client_socket.recv(1024).decode()

# Вывод результатов на экран
print("Reversed message: ", response)

# Закрытие сокета клиента
client_socket.close()
