import socket
from rsa import generate_keys, decrypt

def server():
    # Generowanie kluczy RSA
    public_key, private_key = generate_keys(128)
    #print("Serwer uruchomiony, klucz publiczny:", public_key)
    print("Serwer uruchomiony")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    
    print("Oczekiwanie na połączenie...")
    client_socket, addr = server_socket.accept()
    print(f"Połączono z {addr}")
    
    client_socket.send(str(public_key).encode())

    # Odbieranie zaszyfrowanej wiadomości
    encrypted_msg = client_socket.recv(4096)
    encrypted_msg = eval(encrypted_msg.decode())
    print("Otrzymano zaszyfrowaną wiadomość")

    # Deszyfrowanie wiadomości
    decrypted_msg = decrypt(private_key, encrypted_msg)
    print("Odszyfrowana wiadomość:", decrypted_msg)
    
    # Wysłanie potwierdzenia
    client_socket.send("Odszyfrowano wiadomosc".encode())
    client_socket.close()

if __name__ == "__main__":
    server()
