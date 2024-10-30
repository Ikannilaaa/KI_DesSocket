import socket
from des import encrypt

def send_data(data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    
    key = b'secretky'  # Hardcoded key (must be 8 bytes for DES)
    encrypted_data = encrypt(key, data)  # Encrypt the data
    client_socket.send(encrypted_data)  # Send encrypted data
    client_socket.close()

if __name__ == "__main__":
    data = input("Enter the string to send: ")
    send_data(data)
