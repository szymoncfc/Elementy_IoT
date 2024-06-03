import socket
import time

HOST = 'localhost'

def tcp_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, port))
    server_socket.listen(5)
    print(f"TCP serwer nasłuchuje na porcie {port}")

    total_messages = 0
    total_bytes = 0

    client_socket, addr = server_socket.accept()
    print('Połączono z', addr)

    start_time = time.time()
    while True:
        data = client_socket.recv(256)
        if not data:
            break
        total_messages += 1
        total_bytes += len(data.decode('utf-8'))
    client_socket.close()
    end_time = time.time()
    elapsed_time = end_time - start_time


    print(f"Odebrano {total_messages} komunikatow w {elapsed_time} sekundy")
    print(f"Ilosc bajtow: {total_bytes}")

if __name__ == "__main__":
    tcp_server(12345)  

