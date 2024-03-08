import hashlib

def calculate_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def check_file_integrity(file_path, expected_hash):
    file_hash = calculate_file_hash(file_path)
    if file_hash == expected_hash:
        print(f"The file {file_path} is intact.")
    else:
        print(f"The file {file_path} has been modified.")
        print(f"Expected hash: {expected_hash}")
        print(f"Actual hash: {file_hash}")

file_path = "main.py"
expected_hash = "your_expected_hash"

check_file_integrity(file_path, expected_hash)