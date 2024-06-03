import socket
import time

# Adres i port serwera
HOST = 'localhost'
PORT = 1234

# Dane do wysłania

def udp_client(message, duration):
    # Tworzenie gniazda
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.connect((HOST, PORT))
    server_address = (HOST, PORT)

    # Pętla wysyłająca dane do serwera przez 1 sekundę
    tot_messages = 0

    start_time = time.time()
    while True:
        client_socket.sendall(message)
        tot_messages +=1 
        if time.time() - start_time >= duration:
            break
    print(f"Wyslano {tot_messages} komunikatow")
    client_socket.sendto(b'END', server_address)        
    # Zamykanie gniazda
    client_socket.close()

if __name__ == "__main__":
    duration = 1 
    
    # Test
    message_256 = b'a' * 256
    message_271 = b'a' * 271

    #udp_client(message_256, duration)
    udp_client(message_271, duration)
    
    # Test for 271 bytes message
    #message_271 = b'a' * 271
    #udp_client(HOST, 12345, message_271, duration)

