import socket
import random
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Tworzenie gniazda klienta
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Odbieranie wartości p i g od serwera
data = client_socket.recv(1024).decode()
p, g = map(int, data.split(','))
print(f"Odebrano p={p} i g={g} od serwera")

# Generowanie prywatnego klucza klienta
client_private_key = random.randint(2, p - 2)
A = pow(g, client_private_key, p)
#print(f"Prywatny klucz klienta: {client_private_key}, A: {A}")

# Wysłanie wartości A do serwera
client_socket.send(str(A).encode())

# Odbieranie wartości B od serwera
B = int(client_socket.recv(1024).decode())
#print(f"Odebrano B={B} z serwera")

# Obliczanie wspólnego sekretu
shared_secret = pow(B, client_private_key, p)
print(f"Wspolny sekret: {shared_secret}")

# Konwersja wspólnego sekretu na 32-bajtowy klucz AES
key = shared_secret.to_bytes(32, 'big')[:32]

# Szyfrowanie wiadomości przy użyciu AES
def encrypt_message(message, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(message.encode()) + encryptor.finalize()
    return iv + encrypted_message

# Szyfrowanie i wysyłanie wiadomości do serwera
message = "Test message"
encrypted_message = encrypt_message(message, key)
client_socket.send(encrypted_message)

client_socket.close()
