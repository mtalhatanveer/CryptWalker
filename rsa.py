import math
import random
import string

arr=""

class RSA:
    p=0
    q=0
    phi=0
    n=0
    e=0
    d=0
    dpub=0
    dpriv=0
    def __init__(self):
        print("Peer Created")

    def checkprime(self, p):
        primebool = False
        while primebool == False:
            if p <= 1:
                primebool = False
            elif p == 2 or p == 3:
                print("Prime")
                primebool = True
            elif p > 2:
                for i in range(2, p):
                    res = p % i
                    if res == 0:
                        primebool = False
                        break
                    else:
                        primebool = True
            if primebool == False:
                return False
            else:
                return True

    def setpq(self):
        #print("No")
        print("Enter two prime values p and q\n")
        primebool = False
        self.p=int(input("P : "))
        while primebool == False:
            if self.p<=1:
                primebool=False
            elif self.p==2 or self.p==3:
                print("Prime")
                primebool=True
            elif self.p>2:
                for i in range(2, self.p):
                    res=self.p%i
                    if res == 0:
                        primebool=False
                        break
                    else:
                        primebool=True
            if primebool == False:
                self.p=int(input("Not a prime number\nPlease enter a prime value : "))

        primebool=False
        self.q = int(input("Q : "))
        while primebool == False:
            if self.q <= 1:
                primebool = False
            elif self.q == 2 or self.q == 3:
                print("Prime")
                primebool = True
            elif self.q > 2:
                for i in range(2, self.q):
                    res = self.q % i
                    if res == 0:
                        primebool = False
                        break
                    else:
                        primebool = True
            if primebool == False:
                self.q = int(input("Not a prime number\nPlease enter a prime value : "))

    def mulinv(self, e, phi):
        mod1=e%phi
        for i in range(1, phi):
            if (mod1*i)%phi==1:
                return i

    def primroot(p):
        r=2
        onecount=0
        while 1:
            for i in range(1, p):
                power=math.pow(r, i)
                if power%p==1:
                    onecount+=1
            if onecount>1:
                r+=1
                onecount=0
            elif onecount==1:
                return r

    # function to encrypt a message using rsa
    def encryptor(self, msg, e, n, fname):
        cipher = []
        temp=''
        for x in msg:
            cipher.append(pow(ord(x), e) % n)
        for i in range(0, len(cipher)):
            temp+=str(cipher[i])
            temp+=' '
        with open(fname, 'w+', encoding="utf-8") as f:
            f.write(temp)
        return cipher

    # fucntion to decrypt the cipher text
    def decryptor(self, cipher, d, n, fname):
        plain = ""
        for x in cipher:
            plain += (chr(pow(x, d) % n))
        with open(fname, 'w+', encoding="utf-8") as f:
            f.write(plain)
        return plain

    def encrypt(self, key, n, pt, fname):
        global arr
        cipher=""
        temp=0
        c=0
        listarr = []
        for i in range(0, len(pt)):
            # if pt[i]!=" ":
                #if ord(pt[i])>=97:
                #    arr+='a'
            temp=ord(pt[i])
            c = pow(temp, key) % n
                # else:
                #     arr+='b'
                #     temp=ord(pt[i])-64
                #     c = pow(temp, key) % n + 64
                #print(temp)
            listarr.insert(i, c)
            # else:
            #     arr+='c'
            #     cipher+=" "
        print(listarr)
        # file = open('test.txt', 'w+')
        # file.write(cipher)
        with open(fname, 'w+', encoding="utf-8") as f:
            f.write(str(listarr))
        return listarr

    def decrypt(self, key, n, ct, fname):
        global arr
        #ct=""
        plain=""
        temp=0
        p=0
        for i in range(0, len(ct)):
            if ct[i]!=" ":
                #if arr[i] == 'a':
                temp=ord(ct[i])-96
            #print(temp)
                p=pow(temp, key)%n+96
            #print(p)
                # elif arr[i] == 'b':
                #     temp=ord(ct[i])-64
                #     p=pow(temp, key)%n+64
                plain+=chr(p)
            else:
                plain+=" "
        print(plain)
        with open(fname, 'w+', encoding="utf-8") as f:
            f.write(plain)
        return plain
