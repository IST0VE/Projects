# Код для сервера
import socket

# Создание сокета сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязка сокета к адресу и порту
server_address = ('localhost', 20001)
server_socket.bind(server_address)

# Начало прослушивания
server_socket.listen(1)

# Ожидание подключения клиента
print("Waiting for a client to connect...")
connection, client_address = server_socket.accept()

# Получение сообщения от клиента
message = connection.recv(1024).decode()

# Обработка сообщения
reversed_message = message[::-1]
uppercase_message = message.upper()
letter_count = len(message)

# Отправка обработанного сообщения клиенту
response = f"Reversed Message: {reversed_message}\nUppercase Message: {uppercase_message}\nLetter Count: {letter_count}"
connection.sendall(response.encode())

# Закрытие сокета сервера
connection.close()
server_socket.close()
