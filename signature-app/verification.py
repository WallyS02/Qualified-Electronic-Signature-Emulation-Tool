from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15


def verify_signature(xml, public_key_path, document):
    root = xml.getroot()

    encrypted_signature_hex = root.find("Signature").text
    signature = bytes.fromhex(encrypted_signature_hex)

    document_hash = SHA256.new(document)

    public_key = RSA.import_key(open(public_key_path).read())

    try:
        pkcs1_15.new(public_key).verify(document_hash, signature)
        return True
    except (ValueError, TypeError):
        return False
