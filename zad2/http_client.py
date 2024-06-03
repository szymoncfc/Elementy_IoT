import requests
import time

def http_client(server_url, message):
    headers = {'Content-Type': 'application/octet-stream'}
    start_time = time.time()
    tot_messages = 0
    while True:
        response = requests.post(server_url, headers=headers, data=message)
        tot_messages += 1 
        if time.time() - start_time >= 1:
            break
        
    print(f"Wyslano {tot_messages} komunikatow")

if __name__ == "__main__":
    message = b'a' * 256 
    http_client('http://127.0.0.1:12345', message)
    
