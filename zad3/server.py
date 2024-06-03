import socket
import threading
import time

# Definicja semafora
mutex = threading.Semaphore(1)

# Zatrzask do synchronizacji (Lock)
response_latch = threading.Event()

def handle_client(client_socket):
    while True:
        try:
            request = client_socket.recv(1024)  # Odbierz dane od klienta
            if not request:
                break  # Jeśli brak danych, zakończ pętlę

            # Sekcja krytyczna - dostęp do współdzielonych zasobów
            mutex.acquire()
            print("Otrzymano od klienta:", request.decode())
            
            # Przykładowa odpowiedź do klienta
            response = "Serwer otrzymał: " + request.decode()
            time.sleep(2)  # Symulacja przetwarzania

            # Wyślij odpowiedź do klienta
            client_socket.send(response.encode())
            
            # Uwolnij zatrzask po wysłaniu odpowiedzi
            response_latch.set()

            # Sekcja krytyczna - koniec
            mutex.release()
            
        except socket.timeout:
            print("Przekroczono czas oczekiwania na dane od klienta.")
            break

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Serwer nasłuchuje na porcie 12345...")

    while True:
        client_socket, addr = server_socket.accept()
        print("Nawiązano połączenie z", addr)
        # Ustaw timeout dla socketu
        client_socket.settimeout(10)
        # Utwórz nowy wątek dla każdego klienta
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

start_server()
