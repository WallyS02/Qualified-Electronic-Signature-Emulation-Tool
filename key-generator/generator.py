import base64
import sys
import os
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES


KEY_SIZE = 4096


def pad(data, block_size):
    padding_length = block_size - len(data) % block_size
    padding = bytes([padding_length]) * padding_length
    return data + padding


def generate_keys(aes_key, pendrive_path):
    key = RSA.generate(KEY_SIZE)
    private_key_path = os.path.join(pendrive_path, "private_key")
    public_key_path = os.path.join(os.path.join(os.path.dirname(os.getcwd()), "public-rsa-key"), "public_key.pem")

    with open(private_key_path, "wb") as private_key_file:
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(aes_key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(key.export_key(format="PEM"), AES.block_size))
        private_key_file.write(base64.b64encode(iv + ciphertext))

    with open(public_key_path, "wb") as public_key_file:
        public_key_file.write(key.publickey().export_key(format="PEM"))


def main():
    if len(sys.argv) != 3:
        print("Usage: python generator.py aes_key pendrive_path")
        return "failure"

    generate_keys(bytes(sys.argv[1], 'utf-8'), sys.argv[2])
    return "success"


if __name__ == '__main__':
    main()
