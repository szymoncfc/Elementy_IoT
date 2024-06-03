import socket

def udp_server(host, port, file_path):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print("Serwer UDP nasłuchuje na porcie", host, port)

    with open(file_path, 'wb') as f:
        while True:
            data, addr = sock.recvfrom(1024)
            if data == b'END':
                break
            f.write(data)
    
    sock.close()
    print("Plik odebrano i zapisano jako", file_path)

if __name__ == "__main__":
    udp_server("localhost", 12345, "received_file_udp.txt")
