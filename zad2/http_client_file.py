import requests
import time

def upload_file(server_url, file_path):
    with open(file_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(server_url, files=files)
    return response

if __name__ == "__main__":
    server_url = 'http://127.0.0.1:12345/upload'
    file_path = '2_25b.txt'  # Replace with your file path
    start_time = time.time()
    response = upload_file(server_url, file_path)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"File sent in {elapsed_time:.2f} seconds")
    print(response.json())

