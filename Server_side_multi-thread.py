import socket  # Import socket module for network communication
import threading  # Import threading module for handling multiple clients concurrently

# Server configuration
IP = socket.gethostbyname(socket.gethostname())  # Get the IP address of the server
PORT = 12348  # Define the port number for the server
ADDR = (IP, PORT)  # Combine IP and port into a tuple for socket binding
SIZE = 1024  # Define the size of the message buffer
FORMAT = "utf-8"  # Set the encoding format for communication
DISCONNECT_MSG = "quit"  # Define a message for disconnecting the client

def handle_client(conn, addr):
    """Handle communication with a single client."""
    print(f"[NEW CONNECTION] {addr} connected.")  # Log new client connection
    connected = True  # Maintain connection state

    while connected:  # Loop until the client disconnects
        msg = conn.recv(SIZE).decode(FORMAT)  # Receive and decode a message from the client
        if msg == DISCONNECT_MSG:  # Check if the disconnect message is received
            connected = False  # Update connection state to terminate the loop

        print(f"[{addr}] {msg}")  # Print the client's message with their address

        # Respond back to the client
        response = "Hi, you've connected to the server."
        conn.send(response.encode(FORMAT))  # Send the response message to the client

    conn.close()  # Close the client connection when the loop ends

def main():
    """Main function to start the server and listen for connections."""
    print("[STARTING] Server is starting...")  # Log server startup
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
    server.bind(ADDR)  # Bind the socket to the IP and port
    server.listen()  # Start listening for incoming connections
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")  # Log listening state

    while True:  # Continuously accept new client connections
        conn, addr = server.accept()  # Accept a new client connection
        # Create a new thread to handle the connected client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()  # Start the thread
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")  # Log active connections count

if __name__ == "__main__":  # Check if the script is run directly
    main()  # Call the main function to start the server
