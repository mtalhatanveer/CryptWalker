from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode
import os
import random


class ENC:
    def __init__(self):
        print('')

    def key_generator(self):
        character_pool = ''
        key = ''
        for i in range(20, 126):
            character_pool += chr(i)
        for i in range(16):
            key += random.choice(character_pool)
        return key


    def encrypt(self, file, key):
        print(f'encrypting {file}')
        try:
            aes = AES.new(key, AES.MODE_CBC)
            # with open(file, 'rb') as f:
            #     data = f.read()
            # f.close()
            fin = open(file, 'rb')
            data = fin.read()
            fin.close()
            data = bytearray(data)
            ciphertext = aes.encrypt(pad(data, AES.block_size))
            aes_iv = b64encode(aes.iv).decode('utf-8')
            ciphertext = b64encode(ciphertext).decode('utf-8')
            written = aes_iv+ciphertext
            with open(file, 'w') as f:
                f.write(written)
            f.close()
            print(f'{file} encrypted successfully.')
        except:
            print(f'could not encrypt {file}')

    def mainfunc(self, fname, k):
        file = fname
        key = k
        key = key.encode('utf-8')
        key = pad(key, AES.block_size)
        # print(key)

        self.encrypt(file, key)
        with open('key.txt', 'w') as file:
            key = unpad(key, AES.block_size)
            key = key.decode('utf-8')
            file.write(key)
        file.close()

#
# if __name__ == "__main__":
#     e = ENC()
#     e.mainfunc('button_4.png', 'hello')