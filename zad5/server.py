import socket
import random
from sympy import isprime
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Generowanie liczb pierwszych p i g
def generate_prime_candidate(length):
    p = random.getrandbits(length)
    # zapewnienie liczby nieparzystej
    p |= (1 << length - 1) | 1
    return p

def generate_large_prime(length=128):
    p = 4
    while not isprime(p):
        p = generate_prime_candidate(length)
    return p

p = generate_large_prime()
g = random.randint(2, p - 2)

# Tworzenie gniazda serwera
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print(f"Serwer nasłuchuje na porcie 12345 z p={p} i g={g}")

client_socket, address = server_socket.accept()
print(f"Połączono z {address}.")

# Wysłanie wartości p i g do klienta
client_socket.send(f"{p},{g}".encode())

# Odbieranie wartości A od klienta
A = int(client_socket.recv(1024).decode())
print(f"Odebrano A={A} od klienta")

# Generowanie prywatnego klucza serwera
server_private_key = random.randint(2, p - 2)
B = pow(g, server_private_key, p)
#print(f"Prywatny kluc serwera: {server_private_key}, B: {B}")

# Wysłanie wartości B do klienta
client_socket.send(str(B).encode())

# Obliczanie wspólnego sekretu
shared_secret = pow(A, server_private_key, p)
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

# Odbieranie i odszyfrowanie wiadomości od klienta
encrypted_message = client_socket.recv(1024)
iv = encrypted_message[:16]
cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
decryptor = cipher.decryptor()
decrypted_message = decryptor.update(encrypted_message[16:]) + decryptor.finalize()
print(f"Odszyfrowana wiadomosc od klienta: {decrypted_message.decode()}")

client_socket.close()
server_socket.close()
