import socket
# создаем сокет
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# связываем сокет с локальным адресом
clientsocket.connect(('localhost', 20001))
# вводим имя
client_name = input("Enter your name: ")
clientsocket.send(client_name.encode())

while True:
    # вводим строку
    request = input("Enter your request: ")
    # если строка равна "Покажи время"
    if request == "Покажи время":
        # отправляем запрос серверу
        clientsocket.send(request.encode())
        # получаем ответ от сервера
        response = clientsocket.recv(1024).decode()
        # выводим ответ
        print(response)
    else:
        # если строка не равна "Покажи время", выходим из цикла
        print("Closing connection...")
        clientsocket.close()
        break
# закрываем сокет
clientsocket.close()