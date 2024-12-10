import socket  # Import socket module for network communication

# Client configuration
IP = socket.gethostbyname(socket.gethostname())  # Get the server's IP address
PORT = 12348  # Define the port number of the server to connect to
ADDR = (IP, PORT)  # Combine IP and port into a tuple for connection
SIZE = 1024  # Define the size of the message buffer
FORMAT = "utf-8"  # Set the encoding format for communication
DISCONNECT_MSG = "quit"  # Define a message for disconnecting the client

def main():
    """Main function to connect to the server and handle communication."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
    client.connect(ADDR)  # Connect to the server using the defined address
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")  # Log successful connection

    connected = True  # Maintain connection state
    while connected:  # Loop until the client decides to disconnect
        msg = input("> ")  # Take input from the user
        client.send(msg.encode(FORMAT))  # Encode and send the message to the server

        if msg == DISCONNECT_MSG:  # Check if the user wants to disconnect
            connected = False  # Update connection state to terminate the loop
        else:
            # Receive and decode the server's response
            response = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] {response}")  # Print the server's response

if __name__ == "__main__":  # Check if the script is run directly
    main()  # Call the main function to start the client
