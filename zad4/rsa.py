import random
from sympy import isprime
from sympy import mod_inverse
import time

def generate_prime_candidate(length):
    p = 1
    while not isprime(p):
        p = random.getrandbits(length)
    return p

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generate_keys(key_size):
    p = generate_prime_candidate(key_size // 2)
    q = generate_prime_candidate(key_size // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    aux = [str(pow(char, key, n)) for char in ciphertext]
    # Return the array of bytes as a string
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)



def measure_encryption_time(message, key_size):
    public_key, private_key = generate_keys(key_size)
    start_time = time.time()
    encrypted_msg = encrypt(public_key, message)
    end_time = time.time()
    encryption_time = end_time - start_time
    return encryption_time

def measure_decryption_time(encrypted_msg, private_key):
    start_time = time.time()
    decrypted_msg = decrypt(private_key, encrypted_msg)
    end_time = time.time()
    decryption_time = end_time - start_time
    return decryption_time

message = "A" * 64  # Example message of 64 bytes
key_sizes = [64, 128, 256]

for key_size in key_sizes:
    public_key, private_key = generate_keys(key_size)
    encryption_time = measure_encryption_time(message, key_size)
    encrypted_msg = encrypt(public_key, message)
    decryption_time = measure_decryption_time(encrypted_msg, private_key)
    print(f"Rozmiar klucza: {key_size} bitów")
    print(f"Czas enkrypcji: {encryption_time} sekund")
    print(f"Czas dekrypcji: {decryption_time} sekund")


