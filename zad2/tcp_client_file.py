import socket
import time

def tcp_client(host, port, file_path):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    start_time = time.time()
    
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            sock.sendall(data)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"File sent in {elapsed_time:.2f} seconds")
    
    sock.close()

if __name__ == "__main__":
    tcp_client("localhost", 12345, "1024b.txt")
