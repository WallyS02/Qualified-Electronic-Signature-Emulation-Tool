from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import os
import xml.etree.ElementTree as ET
from datetime import datetime
from key_decryptor import decrypt_private_key


def generate_signature(document_path, private_key_path, aes_key):
    with open(document_path, 'rb') as f:
        document_data = f.read()
    document_hash = SHA256.new(document_data)
    private_key = RSA.import_key(decrypt_private_key(aes_key, private_key_path))
    signature = pkcs1_15.new(private_key).sign(document_hash)
    return signature


def create_xml_signature(document_path, user_info, private_key_path, aes_key):
    document_info = {
        'size': os.path.getsize(document_path),
        'extension': os.path.splitext(document_path)[1],
        'modification_date': datetime.fromtimestamp(os.path.getmtime(document_path)).isoformat()
    }

    root = ET.Element("DigitalSignature")
    document_info_elem = ET.SubElement(root, "DocumentInfo")
    for key, value in document_info.items():
        ET.SubElement(document_info_elem, key).text = str(value)

    user_info_elem = ET.SubElement(root, "UserInfo")
    for key, value in user_info.items():
        ET.SubElement(user_info_elem, key).text = str(value)

    ET.SubElement(root, "Timestamp").text = datetime.now().isoformat()
    ET.SubElement(root, "Signature").text = generate_signature(document_path, private_key_path, aes_key).hex()

    tree = ET.ElementTree(root)

    xml_file_path = os.path.splitext(document_path)[0] + "_signature.xml"
    tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

    print("Digital signature XML created successfully.")
    return tree
