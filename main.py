from abc import ABC, abstractmethod
from cryptography.fernet import Fernet, InvalidToken
from tkinter.filedialog import askopenfilename, asksaveasfile
import base64
import hashlib


class Cipher(ABC):
    lib: Fernet

    @staticmethod
    def set_key(string: str):
        return base64.urlsafe_b64encode(
            hashlib.sha256(
                string.encode('utf-8')
            ).digest()
        )

    @abstractmethod
    def action(self):
        pass


class Encrypt(Cipher):
    def action(self):
        print('choose file')
        filename = askopenfilename()
        keyword = input('keyword: ')

        with open(filename, 'rb') as f:
            data = f.read()

        self.lib = Fernet(self.set_key(keyword))
        encrypted_data = self.lib.encrypt(data)

        with asksaveasfile(mode='wb') as f:
            f.write(encrypted_data)


class Decrypt(Cipher):
    def action(self):
        print('choose file')
        filename = askopenfilename()

        with open(filename, 'rb') as f:
            encrypted_data = f.read()

        key = input('keyword: ')

        self.lib = Fernet(self.set_key(key))
        try:
            print(self.lib.decrypt(encrypted_data))
        except InvalidToken:
            print('wrong key')


class Dialog:
    menu = {
        '1': Encrypt(),
        '2': Decrypt()
    }

    def start(self):
        value = input('type 1 to encrypt, or 2 to decrypt: ')
        try:
            self.menu[value].action()
        except KeyError:
            print('wrong command')
            self.start()


d = Dialog()
d.start()
