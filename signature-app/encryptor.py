import base64
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def aes_pad(data, block_size):
    padding_length = block_size - len(data) % block_size
    padding = bytes([padding_length]) * padding_length
    return data + padding


def aes_encrypt(aes_key, file_path):
    with open(file_path, "wb") as file:
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(aes_key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(aes_pad(file, AES.block_size))
        file.write(base64.b64encode(iv + ciphertext))


def rsa_encrypt(public_key_path, file_path):
    with open(public_key_path, "rb") as public_key_file:
        public_key = RSA.import_key(public_key_file.read())

    cipher_rsa = PKCS1_OAEP.new(public_key)
    with open(file_path, "rb") as plaintext_file:
        plaintext = plaintext_file.read()

    encrypted_data = cipher_rsa.encrypt(plaintext)
    with open(file_path, "wb") as file_out:
        file_out.write(encrypted_data)
