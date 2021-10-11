from cryptography.fernet import Fernet
import base64
import hashlib
from tkinter.filedialog import askopenfilename, asksaveasfile
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
        filename = askopenfilename()
        keyword = input('keyword: ')

        with open(filename, 'rb') as f:
            data = f.read()

        encrypt_data = encrypt(data, set_key(keyword))

        with asksaveasfile(mode='wb') as f:
            f.write(encrypt_data)

    elif command == '2':
        filename = askopenfilename()

        with open(filename, 'rb') as f:
            encrypted_data = f.read()

        keyword = input('keyword: ')
        decrypted_data = decrypt(encrypted_data, set_key(keyword))

        with open('decr', 'wb') as f:
            f.write(decrypted_data)
            webbrowser.open(f.name)

    else:
        print('wrong command')
