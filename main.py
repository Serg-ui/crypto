from abc import ABC, abstractmethod
from cryptography.fernet import Fernet, InvalidToken
from tkinter.filedialog import askopenfilename, asksaveasfile
import base64
import hashlib
import sys


class Cipher(ABC):
    lib: Fernet

    @staticmethod
    def set_key(string: str):
        return base64.urlsafe_b64encode(
            hashlib.sha256(
                string.encode('utf-8')
            ).digest()
        )

    @staticmethod
    def file_reader():
        filename = askopenfilename()
        with open(filename, 'rb') as f:
            data = f.read()
        return data

    @abstractmethod
    def action(self):
        pass


class Encrypt(Cipher):
    def action(self):
        print('choose file')
        data = self.file_reader()
        keyword = input('keyword: ')

        self.lib = Fernet(self.set_key(keyword))
        encrypted_data = self.lib.encrypt(data)

        with asksaveasfile(mode='wb') as f:
            f.write(encrypted_data)


class Decrypt(Cipher):
    attempts_counter = 0
    attempts_limit = 3

    def action(self):
        print('choose file')
        encrypted_data = self.file_reader()
        data = self._decrypt(encrypted_data)
        print(data)

    def _decrypt(self, data):
        key = input('keyword: ')
        self.lib = Fernet(self.set_key(key))

        try:
            decrypted_data = self.lib.decrypt(data)
        except InvalidToken:
            self.attempts_counter += 1
            print(f'wrong key, attempts left {self.attempts_limit - self.attempts_counter}')

            if self.attempts_counter == self.attempts_limit:
                sys.exit('too match')

            return self._decrypt(data)

        return decrypted_data


class Dialog:
    menu = {
        '1': Encrypt(),
        '2': Decrypt()
    }

    @classmethod
    def start(cls):
        value = input('type 1 to encrypt, or 2 to decrypt: ')
        try:
            cls.menu[value].action()
        except KeyError:
            print('wrong command')
            cls.start()


if __name__ == '__main__':
    Dialog.start()
