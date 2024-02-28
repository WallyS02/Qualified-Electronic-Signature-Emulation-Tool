import base64
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from key_decryptor import decrypt_private_key


def aes_unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]


def aes_decrypt(aes_key, file_path):
    with open(file_path, "rb") as file:
        ciphertext = file.read()
    iv_key = base64.b64decode(ciphertext)
    iv = iv_key[:AES.block_size]
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    decrypted_file = aes_unpad(cipher.decrypt(iv_key[AES.block_size:]))
    print(decrypted_file)
    return decrypted_file


def rsa_decrypt(aes_key, private_key_path, file_path):
    private_key = RSA.import_key(decrypt_private_key(aes_key, private_key_path))

    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted_data = cipher_rsa.decrypt(encrypted_data)

    with open(file_path, "wb") as file_out:
        file_out.write(decrypted_data)
