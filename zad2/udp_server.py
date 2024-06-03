import socket
import time

# Adres i port serwera
HOST = 'localhost'
PORT = 1234

def udp_server():
    # Tworzenie gniazda
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))

    print('Serwer nasłuchuje na porcie', PORT)

    # Pętla odbierająca dane od klienta i zliczająca je
    total_messages = 0
    total_bytes = 0
    start_time = time.time()

    while True:
        data, addr = server_socket.recvfrom(256)
        #print(f'{addr} udp {data.decode()}')
        total_messages += 1
        total_bytes += len(data.decode('utf-8'))

        if data == b'END':
            print(f"Odebrano {total_messages} komunikatow")
            print('Odebrano', total_bytes, 'bajtów')  
            break
    

    # Zamykanie gniazda
    server_socket.close()

if __name__ == "__main__":
    udp_server()  # test

