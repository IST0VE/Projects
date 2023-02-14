import socketserver
import datetime

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].decode().strip()
        socket = self.request[1]
        print(f"Received data from {self.client_address}: {data}")
        today = datetime.datetime.now()
        response = f"Hello, {data}! Today is {today.strftime('%Y-%m-%d')}".encode()
        socket.sendto(response, self.client_address)

HOST, PORT = "localhost", 20001

with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
    print(f"Server started on {HOST}:{PORT}")
    server.serve_forever()
