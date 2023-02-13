# Передаем русский текст от клиента к серверу
import socket

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
server_address = ('localhost',20001)
client_socket.connect(server_address)

# Отправляем текстовое сообщение
message = input('Enter your message: ')
client_socket.sendall(message.encode('utf-8'))

# Получаем ответ от сервера
data = client_socket.recvfrom(4096)

# Распечатываем ответ
print("Обычное сообщение:", data.decode())

client_socket.close()
