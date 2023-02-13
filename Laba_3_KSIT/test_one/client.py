# Client code
import socket
# Using the "with" statement to ensure that the socket is properly closed after the work is done
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect to the server
    client_socket.connect(('localhost', 20001))

    # Loop to continuously ask for the current time
    while True:
        # Get the user's input
        user_input = input("Enter 'Show time' to get the current time: ")

        # Check if the user's input is "Show time"
        if user_input == "Show time":
            # Send the user's request to the server
            client_socket.send(user_input.encode())

            # Receive the server's response
            server_response = client_socket.recv(1024).decode()
            print(f"The current time is: {server_response}")
        else:
            # Break the loop if the user's input is not " Show time"
            print("Invalid input. Closing connection...")
            break

