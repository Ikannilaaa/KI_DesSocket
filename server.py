# server.py

import socket
from des import encrypt, decrypt

def start_server(host='127.0.0.1', port=65432, key="mysecret"):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                encrypted_message = list(data)
                decrypted_message = decrypt(encrypted_message, key)
                print("Decrypted message:", decrypted_message)

                response = "Message received"
                encrypted_response = encrypt(response, key)
                conn.sendall(bytes(encrypted_response))

if __name__ == "__main__":
    start_server()
