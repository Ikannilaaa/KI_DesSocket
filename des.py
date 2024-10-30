from Crypto.Cipher import DES

# Function to pad the input data to ensure it's a multiple of 8 bytes
def pad(data):
    # Calculate how many bytes are needed for padding
    padding_size = 8 - len(data) % 8
    return data + (chr(padding_size) * padding_size)

# Function to unpad the input data
def unpad(data):
    padding_size = ord(data[-1])  # Get the size of padding
    return data[:-padding_size]  # Remove padding

# Function to encrypt the data
def encrypt(key, data):
    des = DES.new(key, DES.MODE_CBC, iv=b'12345678')  # Use a fixed IV for simplicity
    padded_data = pad(data)
    encrypted_data = des.encrypt(padded_data.encode())
    return encrypted_data

# Function to decrypt the data
def decrypt(key, encrypted_data):
    des = DES.new(key, DES.MODE_CBC, iv=b'12345678')
    decrypted_data = des.decrypt(encrypted_data)
    return unpad(decrypted_data.decode())
