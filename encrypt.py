from cryptography.fernet import Fernet
import base64
import hashlib

# Set key word
key = base64.urlsafe_b64encode(hashlib.sha256(b'key').digest())


def encrypt(data, key):
    """
    Given a data (bytes) and key (bytes), it encrypts the data and return it
    """
    f = Fernet(key)

    encrypted_data = f.encrypt(data)

    return encrypted_data


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and return data
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    return f.decrypt(encrypted_data)
