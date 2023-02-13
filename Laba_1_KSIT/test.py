# Импортируем модуль socket
import socket
# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Получаем локальный адрес хоста и порт
host = socket.gethostname()
port = 20001
# Связываем сокет с адресом и портом
server_socket.bind((host, port))
# Устанавливаем максимальное количество одновременных подключений
server_socket.listen(5)

print("Waiting for a client to connect...")
# Ожидаем подключения клиента
connection, address = server_socket.accept()

print("Connected to client with address", address)

# Получаем данные от клиента
data = connection.recv(4096)
# Декодируем данные
message = data.decode("utf-8")
    
# Send message to client with the original message, reversed message, number of letters, and upper case message
original_message = 'Original message: {}'.format(message)
reversed_message = 'Reversed message: {}'.format(message[::-1])
count_message = 'Number of letters: {}'.format(len(message))
upper_case_message = 'Uppercase message: {}'.format(message.upper())
response = '{}\n{}\n{}\n{}'.format(original_message, reversed_message, count_message, upper_case_message)
server_socket.sendto(response.encode())

# Закрываем соединение
connection.close()
# Закрываем сокет
server_socket.close()