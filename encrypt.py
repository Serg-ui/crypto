from cryptography.fernet import Fernet
import base64
import hashlib


def set_key(string: str):
    return base64.urlsafe_b64encode(hashlib.sha256(string.encode('utf-8')).digest())


def encrypt(data, keyword):
    f = Fernet(keyword)
    encrypted_data = f.encrypt(data)

    return encrypted_data


def decrypt(data, keyword):
    f = Fernet(keyword)
    return f.decrypt(data)
