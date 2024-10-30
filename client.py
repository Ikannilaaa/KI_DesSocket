# client.py

import socket
from des import encrypt, decrypt

def start_client(host='127.0.0.1', port=65432, key=[0x13, 0x34, 0x57, 0x79, 0x9B, 0xBC, 0xDF, 0xF1]):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        
        message = "Hello, this is a test message!"
        # Convert message to bytes and encrypt
        encrypted_message = encrypt(key, message.encode())
        
        # Convert the list to bytes for transmission
        client_socket.sendall(bytes(encrypted_message))
        
        # Receive the encrypted response
        data = client_socket.recv(1024)
        encrypted_response = list(data)  # Convert bytes back to a list of integers
        decrypted_response = decrypt(key, encrypted_response)
        
        # Decode the decrypted bytes back to a string for printing
        print("Decrypted response from server:", decrypted_response.decode())

if __name__ == "__main__":
    start_client()
