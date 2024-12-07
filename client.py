import socket  # For creating the client socket

HEADER = 64  # Fixed size for the header containing the message length
PORT = 5050  # Port number matching the server's port
SERVER = "192.168.154.194"  # Replace with the server's IP if not running locally
ADDR = (SERVER, PORT)  # Combine server IP and port into a tuple
FORMAT = "utf-8"  # Encoding format for strings
DISCONNECT_MESSAGE = "!DISCONNECT"  # Command to signal disconnection to the server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP client socket
client.connect(ADDR)  # Connect to the server

def send(msg):
    """
    Sends a message to the server.
    """
    message = msg.encode(FORMAT)  # Encode the message to bytes
    msg_length = len(message)  # Calculate the length of the message
    send_length = str(msg_length).encode(FORMAT)  # Encode the length as bytes
    send_length += b' ' * (HEADER - len(send_length))  # Pad the length to fit the header size
    client.send(send_length)  # Send the header
    client.send(message)  # Send the actual message
    print(client.recv(2048).decode(FORMAT))  # Receive and print the server's response

send("Hello World")  # Send a test message
send("Testing Socket Communication")  # Send another test message
send(DISCONNECT_MESSAGE)  # Signal the server to close the connection
