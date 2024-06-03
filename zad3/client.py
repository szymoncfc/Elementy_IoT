import socket
import threading
import time

def send_message(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    
    # Wyślij wiadomość do serwera
    client_socket.send(message.encode())

    # Czekaj na odpowiedź serwera z zatrzaskiem (Latch)
    response_latch = threading.Event()
    
    def receive_response():
        response = client_socket.recv(1024)
        print("Otrzymano od serwera:", response.decode())
        response_latch.set()

    # Utwórz wątek do odbioru odpowiedzi od serwera
    receiver_thread = threading.Thread(target=receive_response)
    receiver_thread.start()

    # Czekaj na odpowiedź lub timeout (timeout na 5 sekund)
    if response_latch.wait(timeout=5):
        print("Odpowiedź otrzymana w wyznaczonym czasie.")
    else:
        print("Przekroczono czas oczekiwania na odpowiedź od serwera.")
    
    client_socket.close()

# Testowanie klienta
for i in range(10):
    send_message("Hello!")
