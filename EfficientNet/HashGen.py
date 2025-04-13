import os
import hashlib
from blake3 import blake3
from Crypto.Hash import keccak
from PIL import Image

# Function to read image and convert to bytes
def image_to_bytes(image_path):
    with open(image_path, 'rb') as f:
        return f.read()

# Function to calculate SHA-256
def sha256_hash(data):
    return hashlib.sha256(data).hexdigest()

# Function to calculate BLAKE3
def blake3_hash(data):
    return blake3(data).hexdigest()

# Function to calculate Keccak-256
def keccak256_hash(data):
    k = keccak.new(digest_bits=256)
    k.update(data)
    return k.hexdigest()

# Directory containing biometric images
image_folder = "E:/Biometrics/Dataset/Train/Real/"  # <-- change this to your folder path

# Supported image extensions
image_extensions = {'.png', '.jpg', '.jpeg'}

# Loop through images and compute hashes
for filename in os.listdir(image_folder):
    if os.path.splitext(filename)[1].lower() in image_extensions:
        image_path = os.path.join(image_folder, filename)
        image_data = image_to_bytes(image_path)

        sha256 = sha256_hash(image_data)
        blake = blake3_hash(image_data)
        keccak_hash = keccak256_hash(image_data)

        print(f"\nImage: {filename}")
        print(f"SHA-256 : {sha256}")
        print(f"BLAKE3  : {blake}")
        print(f"Keccak-256: {keccak_hash}")
