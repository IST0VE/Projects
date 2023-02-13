import socket

# Задаем хост и порт
host = '127.0.0.1'
port = 20001

# Создаем сокет
with socket.socket() as client_socket:
    # Подключаемся к серверу
    client_socket.connect((host, port))

    # Запрашиваем имя пользователя
    client_name = input("Enter your name: ")

    # Отправляем имя на сервер
    client_socket.sendall(client_name.encode('utf-8'))

    # Выполняем цикл для запроса времени
    while True:
        # Запрашиваем у пользователя время
        request = input("Enter 'Show time': ")

        # Если запрос не соответствует условию, завершаем работу
        if request != 'Show time':
            break

        # Отправляем запрос на сервер
        client_socket.sendall(request.encode('utf-8'))

        # Получаем ответ от сервера
        data = client_socket.recv(1024).decode('utf-8')

        # Выводим полученный ответ
        print(f"Current time is: {data}")