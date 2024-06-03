def create_test_files():
    sizes = [2**30]  # 2, 32, 1024, 1048576 bytes
    for size in sizes:
        with open(f'{size}b.txt', 'wb') as f:
            f.write(b'a' * size)

if __name__ == "__main__":
    create_test_files()