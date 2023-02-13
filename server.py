#Создаем UDP серверный сокет
# ждем дейтарамму от клиента
# принимаем одну UDP дейтарамму
# закрываем серверный сокет
import socket # данные сервера
host = 'localhost'
port = 20001 
serverAddressPort = (host, port)
print('serverAddressPort=',serverAddressPort,type(serverAddressPort))
# serverAddressPort= ('localhost', 20001) <class 'tuple'>
bufferSize=1024
UDPServerSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDPServerSocket.bind(serverAddressPort)
print('Сервер запущен! Запустите клиента!')
bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
print('bytesAddressPair=', bytesAddressPair,type(bytesAddressPair))
# bytesAddressPair= (b'Hello', ('127.0.0.1', 58141))# <class 'tuple'>
clientIP = bytesAddressPair [1]
print('clientIP=',clientIP, type(clientIP))
# clientIP= ('127.0.0.1', 61384) <class 'tuple'>
print('bytesAddressPair [0]=', bytesAddressPair [0])
# bytesAddressPair [0]= b'Hello'
message=bytesAddressPair [0].decode()
print('clientMessage=',message)
# clientMsg= Hello
data=message
print('data=',data)
Hellodata=data[::-1]
print('data=',Hellodata)
x = len(data)
print('data = ', x)
big = data.upper()
print('data = ', big)
# data= olleH
UDPServerSocket.sendto(data.encode(),clientIP)
UDPServerSocket.close()