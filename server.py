import socket  # For creating socket objects and handling connections
import threading  # For handling multiple clients concurrently

PORT = 5050  # Port the server listens on
SERVER = socket.gethostbyname(socket.gethostname())  # Automatically get the server's IP
print(SERVER)  # Print the server's IP for debugging
ADDR = (SERVER, PORT)  # Combine server IP and port into a tuple for binding
HEADER = 64  # Fixed size for the header containing the message length
FORMAT = 'utf-8'  # Encoding format for strings
DISCONNECT_MESSAGE = "!DISCONNECT"  # Command to signal client disconnection

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
server.bind(ADDR)  # Bind the socket to the specified address

def handle_client(conn, addr):
    """
    Handles communication with a connected client.
    """
    print(f"[NEW CONNECTION] {addr} connected")  # Log new connection
    connected = True  # Connection status
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)  # Receive and decode the header
        if msg_length:  # Ensure we received data
            msg_length = int(msg_length)  # Convert the header to an integer
            msg = conn.recv(msg_length).decode(FORMAT)  # Receive and decode the actual message
            if msg == DISCONNECT_MESSAGE:  # Check if the message is a disconnect command
                connected = False  # Break the loop and close the connection
            print(f"[{addr}] {msg}")  # Log the received message
            conn.send("Message received".encode(FORMAT))  # Send acknowledgment
    conn.close()  # Close the connection when done

def start():
    """
    Starts the server and listens for incoming connections.
    """
    server.listen()  # Begin listening for clients
    print(f"[LISTENING] Server is listening on {SERVER}")  # Log server status
    while True:
        conn, addr = server.accept()  # Accept a new connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))  # Create a new thread for the client
        thread.start()  # Start the client thread
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")  # Log active connections

print("[STARTING] Server is starting...")  # Log server startup
start()  # Start the server
