import socket
from rsa import encrypt


def client():
    # Generowanie kluczy RSA
    #public_key, private_key = generate_keys(128)
    #print("Klucz publiczny klienta:", public_key)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    public_key = client_socket.recv(4096)
    public_key = eval(public_key.decode())
    # Wiadomość do wysłania
    message = "Test message"
    encrypted_msg = encrypt(public_key, message)
    #print("Zaszyfrowana wiadomość:", encrypted_msg)
    
    # Wysyłanie zaszyfrowanej wiadomości
    client_socket.send(str(encrypted_msg).encode())
    
    # Odbieranie potwierdzenia
    response = client_socket.recv(4096)
    print("Odpowiedź od serwera:", response.decode())
    
    client_socket.close()

if __name__ == "__main__":
    client()

