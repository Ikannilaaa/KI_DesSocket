import socket
from des import decrypt

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is listening on port 12345...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} established.")
        
        encrypted_data = client_socket.recv(1024)  # Receive encrypted data
        key = b'secretky'  # Hardcoded key (must be 8 bytes for DES)
        
        decrypted_data = decrypt(key, encrypted_data)
        print(f"Decrypted data: {decrypted_data}")

        client_socket.close()

if __name__ == "__main__":
    start_server()
