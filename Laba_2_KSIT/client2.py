import socket

# Создание сокета UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Получение имени клиента
name = input("Введите ваше имя: ")
# Отправка имени на сервер
sock.sendto(name.encode('utf-8'), ('localhost', 20001))
print("Вы подключены к серверу")

while True:
    # Запрос времени у сервера
    message = "time"
    sock.sendto(message.encode('utf-8'), ('localhost', 20001))
    data, addr = sock.recvfrom(1024)
    print(data.decode('utf-8'))

