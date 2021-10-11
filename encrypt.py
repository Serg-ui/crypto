from cryptography.fernet import Fernet
import base64
import hashlib
from tkinter.filedialog import askopenfilename
import webbrowser


def set_key(string: str):
    return base64.urlsafe_b64encode(hashlib.sha256(string.encode('utf-8')).digest())


def encrypt(data, keyword):
    f = Fernet(keyword)
    encrypted_data = f.encrypt(data)

    return encrypted_data


def decrypt(data, keyword):
    f = Fernet(keyword)
    return f.decrypt(data)


if __name__ == '__main__':
    command = input("Type '1' to encrypt, or '2' to decrypt: ")

    if command == '1':
        pass

    elif command == '2':
        filename = askopenfilename()
        encrypted_file = open(filename, 'rb')
        encrypted_data = encrypted_file.read()

        keyword = input('keyword: ')
        decrypted_data = decrypt(encrypted_data, set_key(keyword))
        encrypted_file.close()

        decr_file = open('decr', 'wb')
        decr_file.write(decrypted_data)
        decr_file.close()

        webbrowser.open(decr_file.name)

    else:
        print('wrong command')
