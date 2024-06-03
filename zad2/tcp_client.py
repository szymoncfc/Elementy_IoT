import socket
import time

HOST = 'localhost'

def tcp_client(server_ip, port, message, duration):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))
      

    tot_messages = 0
    start_time = time.time()
    while True:
        client_socket.sendall(message)
        tot_messages +=1 
        if time.time() - start_time >= duration:  # Wysyłamy przez 1 sekundę
            break
    client_socket.close()
    print(f"Wyslano {tot_messages} komunikatow")
if __name__ == "__main__":
    duration = 1   
    
    # Test
    message_256 = b'a' * 256
    message_271 = b'a' * 271
    #tcp_client(HOST, 12345, message_256, duration)
    tcp_client(HOST, 12345, message_271, duration)


