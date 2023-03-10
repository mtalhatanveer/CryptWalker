from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode
import os


class DEC:
    def __init__(self):
        print('')

    def decrypt(self, file, key):
        #for file in files:
        print(f'decrypting {file}...')
        try:
            with open(file, 'r') as f:
                data = f.read()
                aes_iv = data[:24]
                aes_iv = b64decode(aes_iv)
                ciphertext = data[24:]
                ciphertext = b64decode(ciphertext)
                aes = AES.new(key, AES.MODE_CBC, aes_iv)
                plaintext = aes.decrypt(ciphertext)
                plaintext = unpad(plaintext, AES.block_size)
                f.close()
                with open(file, 'wb') as f:
                    f.write(plaintext)
                f.close()
                print("Decrypted successfully.")
        except:
            print(f'Could not decrypt {file}')
        #continue

    def mainfunc(self, fname, k):
        file = fname
        #get_files('C:/Users/Zakariya Shahid/Downloads/Video/', files)

        key = k
        key = key.encode('utf-8')
        key = pad(key, AES.block_size)

        self.decrypt(file, key)
#
# if __name__ == "__main__":
#     d = DEC()
#     d.mainfunc('button_4.png', 'hello')
