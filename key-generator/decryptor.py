import base64
import sys
from Crypto.Cipher import AES


def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]


def decrypt_private_key(aes_key, key_path):
    with open(key_path, "rb") as key_file:
        ciphertext = key_file.read()
    iv_key = base64.b64decode(ciphertext)
    iv = iv_key[:AES.block_size]
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    decrypted_key = unpad(cipher.decrypt(iv_key[AES.block_size:])).decode()
    print(decrypted_key)
    return decrypted_key


def main():
    if len(sys.argv) != 3:
        print("Usage: python decryptor.py aes_key key_path")
        return "failure"

    return decrypt_private_key(bytes(sys.argv[1], 'utf-8'), sys.argv[2])


if __name__ == '__main__':
    main()
