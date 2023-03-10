import random
import numpy
from PIL import Image, ImageEnhance
from numpy import asarray
import numpy as np
import math

class CVC:
    def __init__(self):
        print('')

    def encryption(self, fname):
        img = Image.open(fname)
        r, g, b = img.split()
        share1 = r.load()
        share2 = g.load()
        share3 = b.load()
        for i in range(r.size[0]):
            for j in range(r.size[1]):
                share1[i, j] = math.floor(share1[i, j] / 16)
                share1[i, j] ^= 200
                share2[i, j] = math.floor(share2[i, j] / 16)
                share2[i, j] ^= 200
                share3[i, j] = math.floor(share3[i, j] / 16)
                share3[i, j] ^= 200

        r.save('share1.png')
        g.save('share2.png')
        b.save('share3.png')

    def decryption(self, s1, s2, s3):
        r = Image.open(s1)
        g = Image.open(s2)
        b = Image.open(s3)
        share1 = r.load()
        share2 = g.load()
        share3 = b.load()
        for i in range(r.size[0]):
            for j in range(r.size[1]):
                share1[i, j] ^= 200
                # share1[i, j] = math.ceil(share1[i, j]*(3/4))
                share2[i, j] ^= 200
                # share2[i, j] = math.ceil(share2[i, j]*(3/4))
                share3[i, j] ^= 200
                # share3[i, j] = math.ceil(share3[i, j]*(3/4))
                share1[i, j] *= 16
                share2[i, j] *= 16
                share3[i, j] *= 16

        merged_img = Image.merge('RGB', (r, g, b))
        merged_img.save('decrypted.png')
