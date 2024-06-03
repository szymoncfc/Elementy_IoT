import socket

def tcp_server(host, port, file_path):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)
    print("TCP serwer nasłuchuje na porcie", host, port)

    conn, addr = sock.accept()
    print("Połączono z", addr)
    
    with open(file_path, 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
    
    conn.close()
    sock.close()
    print("Plik odebrano i zapisano jako", file_path)

if __name__ == "__main__":
    tcp_server("localhost", 12345, "received_file_tcp.txt")
