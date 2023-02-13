import socket
import time

# Server code

# Using the "with" statement to ensure that the socket is properly closed after the work is done
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to a specific address and port
    server_socket.bind(('localhost', 20001))
    # Set the maximum number of queued connections
    server_socket.listen(2)

    # Wait for incoming connections
    while True:
        # Accept the connection
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Receive the client's message
        client_message = client_socket.recv(1024).decode()

        # Check if the client's message is "Show time"
        if client_message == "Show time":
            # Send the current time to the client
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            client_socket.send(current_time.encode())
        else:
            # Close the connection if the client's message is not "Show time"
            client_socket.close()