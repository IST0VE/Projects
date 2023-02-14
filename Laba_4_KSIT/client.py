import socket

HOST = '127.0.0.1'  # localhost
PORT = 20001        # порт по умолчанию

# Создаем сокет TCP/IP, используя семейство адресов IPv4 (AF_INET) и протокол TCP (SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Устанавливаем соединение с сервером, используя адрес сервера (хост и порт)
    s.connect((HOST, PORT))
    # Запросить у пользователя ввод сообщения
    message = input("Введите сообщение: ")
    # Кодируем строку в байты (для отправки на сервер)
    encoded_message = message.encode('utf-8')
    # Отправляем данные на сервер, используя соединение s
    s.sendall(encoded_message)
    # Принимаем ответ от сервера, максимальный размер буфера - 1024 байта
    data = s.recv(1024)
    # Декодируем байты в строку (ответ от сервера)
    response = data.decode('utf-8')
    # Выводим ответ от сервера
    print(response)
