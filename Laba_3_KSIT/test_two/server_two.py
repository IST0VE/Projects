import socket
import datetime

# Создаем сокет
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Устанавливаем связь сервера с адресом и портом
    s.bind(("127.0.0.1", 20001))
    # Слушаем клиентов до 5 в числе
    s.listen(5)
    print("Server is ready to receive requests...")
    while True:
        # Ждем подключения клиента
        conn, addr = s.accept()
        # Получаем имя клиента
        client_name = conn.recv(1024).decode()
        print(f"Received request from {client_name}")
        # Получаем запрос клиента
        request = conn.recv(1024).decode()
        # Проверяем, что запрос равен "Покажи время"
        if request == "Покажи время":
            # Отправляем клиенту текущее время
            current_time = str(datetime.datetime.now().time())
            conn.send(f"{client_name}, текущее время: {current_time}".encode())
        else:
            # Если запрос неверный, закрываем соединение с клиентом
            print(f"Incorrect request from {client_name}, closing connection...")
            conn.close()