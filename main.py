import tkinter as tk
from tkinter import font  as tkfont
from tkinter import filedialog as fd
from tkinter import Canvas
import rsa
import aes
import cvc
import svc
import svcII
import grayscale
import math
import random
import string


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, RSA, AES, VISUAL, rsaencrypt,
                  rsadecrypt, rsakey, rsaoptions, RSAf, rsafencrypt,
                  rsakeyf, rsadecryptf, AESecbenc, AESecbdec,
                  visualenc, visualdec, cvcoptions, advoptions,
                  simpleoptions, gvcoptions, cvcenc, cvcdec,
                  cvcoptions, gvcoptions, svcenc, svcdec):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        heading1 = tk.Label(self, text='Crypt Walker Tool',
                            font=('Airstrike Half-Tone', 45, 'bold'), fg='white',
                            background='#25274D')
        heading1.pack(pady=25)

        # space_label = tk.Label(self, height=4, bg='#25274D')
        # space_label.pack()

        menutext = tk.Label(self, text='Main Menu',
                            font=('Game Of Squids', 36), fg='white', bg='#25274D')
        menutext.pack()

        Rsa_Btn = tk.Button(self, text='RSA\nCRYPTOGRAPHY',
                            font=('Airstrike', 40), fg='white', bg='#0d1a26',
                            relief='flat', command=lambda: controller.show_frame('rsaoptions'))
        Rsa_Btn.pack(pady=15)

        Aes_Btn = tk.Button(self, text='AES\nCRYPTOGRAPHY',
                            font=('Airstrike', 40), fg='white', bg='#0d1a26',
                            relief='flat', command=lambda: controller.show_frame('AES'))
        Aes_Btn.pack(pady=15)

        Visual_Btn = tk.Button(self, text='VISUAL\nCRYPTOGRAPHY',
                            font=('Airstrike', 40), fg='white', bg='#0d1a26',
                            relief='flat', command=lambda: controller.show_frame('VISUAL'))
        Visual_Btn.pack(pady=15)


class RSA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        heading1 = tk.Label(self, text='Crypt Walker Tool',
                            font=('Airstrike Half-Tone', 45, 'bold'), fg='white',
                            background='#25274D')
        heading1.pack(pady=25)

        menutext = tk.Label(self, text='Menu',
                            font=('Game Of Squids', 36), fg='white', bg='#25274D')
        menutext.pack()

        space_label = tk.Label(self, height=4, bg='#25274D')
        space_label.pack()

        keybtn = tk.Button(self, text='Key Gen',
                           font=('Airstrike', 36), fg='white', bg='#0d1a26',
                           relief='flat', command=lambda: controller.show_frame('rsakey'))

        keybtn.pack(ipadx=10)

        encryptbtn = tk.Button(self, text='Encrypt',
                               font=('Airstrike', 36), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: controller.show_frame('rsaencrypt'))
        encryptbtn.pack(pady=35)

        decryptbtn = tk.Button(self, text='Decrypt',
                               font=('Airstrike', 36), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: controller.show_frame('rsadecrypt'))
        decryptbtn.pack()

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                             command=lambda: controller.show_frame('StartPage'))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back',
                             command=lambda: controller.show_frame('rsaoptions'))
        back_btn.pack(side='right')


class rsaoptions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        heading1 = tk.Label(self, text='Crypt Walker Tool',
                            font=('Airstrike Half-Tone', 45, 'bold'), fg='white',
                            background='#25274D')
        heading1.pack(pady=25)

        menutext = tk.Label(self, text='Menu',
                            font=('Game Of Squids', 36), fg='white', bg='#25274D')
        menutext.pack()

        space_label = tk.Label(self, height=4, bg='#25274D')
        space_label.pack()

        def setbool(a):
            global boolvar
            if int(a) == 1:
                boolvar = True
                controller.show_frame('RSA')
            else:
                boolvar = False
                controller.show_frame('RSAf')

        txtfiles = tk.Button(self, text='Text Files',
                           font=('Airstrike', 36), fg='white', bg='#0d1a26',
                           relief='flat', command=lambda: setbool(2))

        txtfiles.pack(ipadx=20)

        txt = tk.Button(self, text='Simple Text',
                               font=('Airstrike', 36), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: setbool(1))
        txt.pack(pady=35)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                             command=lambda: controller.show_frame('StartPage'))
        menu_btn.pack(side='right')


class rsakey(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        p_lbl = tk.Label(self, text='Enter P',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        p_lbl.pack(pady=10)

        p_var = tk.IntVar()
        p_entry = tk.Entry(self, textvariable=p_var,
                           font=('Brothers', 25), width=22)
        p_entry.pack(ipady=7)

        q_lbl = tk.Label(self, text='Enter Q',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        q_lbl.pack(pady=10)

        q_var = tk.IntVar()
        q_entry = tk.Entry(self, textvariable=q_var,
                           font=('Brothers', 25), width=22)
        q_entry.pack(ipady=7)

        def displaykey():
            r = rsa.RSA()
            p = p_entry.get()
            q = q_entry.get()
            if len(p_entry.get())==0 or len(q_entry.get())==0:
                key_lbl['text'] = 'Input fields cannot be empty'
            elif r.checkprime(int(p)) == True and r.checkprime(int(q)) == True:
                r.n = int(p)*int(q)
                r.phi = (int(p)-1)*(int(q)-1)
                # rsa.p = p
                # rsa.q = q
                # rsa.n = n
                # rsa.phi = phi
                r.e=random.randint(2, r.phi-1)
                while math.gcd(r.e, r.phi)!=1:
                    r.e=random.randint(2, r.phi-1)
                inv = r.mulinv(r.e, r.phi)
                r.d = inv%r.phi
                key_lbl['text'] = 'n : ' + str(r.n) + '\nphi : ' + str(r.phi) + '\ne : ' + str(r.e) + '\nd : ' + str(r.d)
            else:
                key_lbl['text'] = 'Non-prime Values Entered!'

        def clearnleave(a):
            p_entry.delete(0, tk.END)
            q_entry.delete(0, tk.END)
            key_lbl['text'] = ''
            if int(a) == 1:
                controller.show_frame('RSA')
            else:
                controller.show_frame('StartPage')

        submit_btn = tk.Button(self, text='Submit',
                               font=('Airstrike', 13), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: displaykey())
        submit_btn.pack(pady=13)

        key_lbl = tk.Label(self, text='',
                              font=('Airstrike', 20), fg='white', bg='#191a34',
                              anchor='n')
        key_lbl.pack(fill='both', expand=True)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                             command=lambda: clearnleave(2))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back',
                             command=lambda: clearnleave(1))
        back_btn.pack(side='right')


class rsaencrypt(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        # heading1 = tk.Label(self, text='Crypt Walker Tool',
        #                     font=('Airstrike', 45, 'bold'), fg='white',
        #                     background='#25274D')
        # heading1.pack(pady=25)

        p_lbl = tk.Label(self, text='Enter P',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        p_lbl.pack(pady=10)

        p_var = tk.IntVar()
        p_entry = tk.Entry(self, textvariable=p_var,
                           font=('Brothers', 25), width=22)
        p_entry.pack(ipady=7)

        q_lbl = tk.Label(self, text='Enter Q',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        q_lbl.pack(pady=10)

        q_var = tk.IntVar()
        q_entry = tk.Entry(self, textvariable=q_var,
                           font=('Brothers', 25), width=22)
        q_entry.pack(ipady=7)

        pub_lbl = tk.Label(self, text='Enter Public Key',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        pub_lbl.pack(pady=10)

        pub_var = tk.IntVar()
        pub_entry = tk.Entry(self, textvariable=pub_var,
                           font=('Brothers', 25), width=22)
        pub_entry.pack(ipady=7)

        pt_lbl = tk.Label(self, text='Enter Plaintext',
                          font=('Airstrike', 25), fg='white', bg='#25274D')
        pt_lbl.pack(pady=10)

        pt_var = tk.StringVar
        pt_entry = tk.Entry(self, textvariable=pt_var,
                            font=('Brothers', 25), width=22)
        pt_entry.pack(ipady=7)

        def display_cipher():
            r = rsa.RSA()
            p = p_entry.get()
            q = q_entry.get()
            if len(p_entry.get())==0 or len(q_entry.get())==0 or len(pub_entry.get())==0:
                cipher_lbl['text'] = 'Input fields cannot be empty'
            elif r.checkprime(int(p)) == True and r.checkprime(int(q)) == True:
                ct = []
                r.n = int(p)*int(q)
                r.phi = (int(p)-1)*(int(q)-1)
                r.e = int(pub_entry.get())
                inv = r.mulinv(r.e, r.phi)
                r.d = inv % r.phi
                pt = pt_entry.get()
                #ct = r.encrypt(int(r.e), int(r.n), str(pt), 'ctfile.txt')
                ct = r.encryptor(str(pt), int(r.e), int(r.n), 'ctfile.txt')
                ctstr=""
                for i in range (0, len(ct)):
                    #cipher_lbl['text'] = 'Cipher : ' + str(ct[i]) + '\nA txt file has been created in the same folder'
                    ctstr += str(ct[i])
                    ctstr += ' '
                cipher_lbl['text'] = 'Cipher : ' + str(ctstr) + '\nA txt file has been created in the same folder'
            else:
                cipher_lbl['text'] = 'Non-prime Values Entered!'

        def clearnleave(a):
            p_entry.delete(0, tk.END)
            q_entry.delete(0, tk.END)
            pub_entry.delete(0, tk.END)
            pt_entry.delete(0, tk.END)
            cipher_lbl['text'] = ''
            if int(a) == 1:
                controller.show_frame('RSA')
            else:
                controller.show_frame('StartPage')

        submit_btn = tk.Button(self, text='Submit',
                               font=('Airstrike', 13), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: display_cipher())
        submit_btn.pack(pady=13)

        cipher_lbl = tk.Label(self, text='',
                              font=('Airstrike', 20), fg='white', bg='#191a34',
                              anchor='n')
        cipher_lbl.pack(fill='both', expand=True)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                            command=lambda: clearnleave(2))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back',
                             command=lambda: clearnleave(1))
        back_btn.pack(side='right')


class RSAf(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        heading1 = tk.Label(self, text='Crypt Walker Tool',
                            font=('Airstrike Half-Tone', 45, 'bold'), fg='white',
                            background='#25274D')
        heading1.pack(pady=25)

        menutext = tk.Label(self, text='Menu',
                            font=('Game Of Squids', 36), fg='white', bg='#25274D')
        menutext.pack()

        space_label = tk.Label(self, height=4, bg='#25274D')
        space_label.pack()

        keybtn = tk.Button(self, text='Key Gen',
                           font=('Airstrike', 36), fg='white', bg='#0d1a26',
                           relief='flat', command=lambda: controller.show_frame('rsakeyf'))

        keybtn.pack(ipadx=10)

        encryptbtn = tk.Button(self, text='Encrypt',
                               font=('Airstrike', 36), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: controller.show_frame('rsafencrypt'))
        encryptbtn.pack(pady=35)

        decryptbtn = tk.Button(self, text='Decrypt',
                               font=('Airstrike', 36), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: controller.show_frame('rsadecryptf'))
        decryptbtn.pack()

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                             command=lambda: controller.show_frame('StartPage'))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back',
                             command=lambda: controller.show_frame('rsaoptions'))
        back_btn.pack(side='right')


class rsakeyf(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        p_lbl = tk.Label(self, text='Enter P',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        p_lbl.pack(pady=10)

        p_var = tk.IntVar()
        p_entry = tk.Entry(self, textvariable=p_var,
                           font=('Brothers', 25), width=22)
        p_entry.pack(ipady=7)

        q_lbl = tk.Label(self, text='Enter Q',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        q_lbl.pack(pady=10)

        q_var = tk.IntVar()
        q_entry = tk.Entry(self, textvariable=q_var,
                           font=('Brothers', 25), width=22)
        q_entry.pack(ipady=7)

        def displaykey():
            r = rsa.RSA()
            p = p_entry.get()
            q = q_entry.get()
            if len(p_entry.get())==0 or len(q_entry.get())==0:
                key_lbl['text'] = 'Input fields cannot be empty'
            elif r.checkprime(int(p)) == True and r.checkprime(int(q)) == True:
                r.n = int(p)*int(q)
                r.phi = (int(p)-1)*(int(q)-1)
                # rsa.p = p
                # rsa.q = q
                # rsa.n = n
                # rsa.phi = phi
                r.e=random.randint(2, r.phi-1)
                while math.gcd(r.e, r.phi)!=1:
                    r.e=random.randint(2, r.phi-1)
                inv = r.mulinv(r.e, r.phi)
                r.d = inv%r.phi
                key_lbl['text'] = 'n : ' + str(r.n) + '\nphi : ' + str(r.phi) + '\ne : ' + str(r.e) + '\nd : ' + str(r.d)
            else:
                key_lbl['text'] = 'Non-prime Values Entered!'

        def clearnleave(a):
            p_entry.delete(0, tk.END)
            q_entry.delete(0, tk.END)
            key_lbl['text'] = ''
            if int(a) == 1:
                controller.show_frame('RSAf')
            else:
                controller.show_frame('StartPage')

        submit_btn = tk.Button(self, text='Submit',
                               font=('Airstrike', 13), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: displaykey())
        submit_btn.pack(pady=13)

        key_lbl = tk.Label(self, text='',
                              font=('Airstrike', 20), fg='white', bg='#191a34',
                              anchor='n')
        key_lbl.pack(fill='both', expand=True)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                             command=lambda: clearnleave(2))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back',
                             command=lambda: clearnleave(1))
        back_btn.pack(side='right')


class rsafencrypt(tk.Frame):
    def __init__(self, parent, controller):
        fname = ""
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        # heading1 = tk.Label(self, text='Crypt Walker Tool',
        #                     font=('Airstrike', 45, 'bold'), fg='white',
        #                     background='#25274D')
        # heading1.pack(pady=25)

        p_lbl = tk.Label(self, text='Enter P',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        p_lbl.pack(pady=10)

        p_var = tk.IntVar()
        p_entry = tk.Entry(self, textvariable=p_var,
                           font=('Brothers', 25), width=22)
        p_entry.pack(ipady=7)

        q_lbl = tk.Label(self, text='Enter Q',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        q_lbl.pack(pady=10)

        q_var = tk.IntVar()
        q_entry = tk.Entry(self, textvariable=q_var,
                           font=('Brothers', 25), width=22)
        q_entry.pack(ipady=7)

        pub_lbl = tk.Label(self, text='Enter Public Key',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        pub_lbl.pack(pady=10)

        pub_var = tk.IntVar()
        pub_entry = tk.Entry(self, textvariable=pub_var,
                           font=('Brothers', 25), width=22)
        pub_entry.pack(ipady=7)

        pt_lbl = tk.Label(self, text='FilePath',
                          font=('Airstrike', 25), fg='white', bg='#25274D')
        pt_lbl.pack(pady=10)

        pt_var = tk.StringVar
        pt_entry = tk.Entry(self, textvariable=pt_var,
                            font=('Brothers', 25), width=22)
        pt_entry.pack(ipady=7)

        def display_cipher():
            r = rsa.RSA()
            p = p_entry.get()
            q = q_entry.get()
            if len(p_entry.get())==0 or len(q_entry.get())==0 or len(pt_entry.get())==0 or len(pub_entry.get())==0:
                cipher_lbl['text'] = 'Input fields cannot be empty'
            elif r.checkprime(int(p)) == True and r.checkprime(int(q)) == True:
                fct=""
                fname = pt_entry.get()
                f = open(fname)
                with open(fname, 'r+') as f:
                    fct += f.read()
                ct = []
                r.n = int(p)*int(q)
                r.phi = (int(p)-1)*(int(q)-1)
                r.e = int(pub_entry.get())
                inv = r.mulinv(r.e, r.phi)
                r.d = inv % r.phi
                pt = pt_entry.get()
                #ct = r.encrypt(int(r.e), int(r.n), str(pt), 'ctfile.txt')
                ct = r.encryptor(str(fct), int(r.e), int(r.n), 'ctfile.txt')
                ctstr=""
                for i in range (0, len(ct)):
                    #cipher_lbl['text'] = 'Cipher : ' + str(ct[i]) + '\nA txt file has been created in the same folder'
                    ctstr += str(ct[i])
                    ctstr += ' '
                cipher_lbl['text'] = 'A txt file has been created in the same folder'
            else:
                cipher_lbl['text'] = 'Non-prime Values Entered!'

        def clearnleave(a):
            p_entry.delete(0, tk.END)
            q_entry.delete(0, tk.END)
            pub_entry.delete(0, tk.END)
            pt_entry.delete(0, tk.END)
            cipher_lbl['text'] = ''
            if int(a) == 1:
                controller.show_frame('RSAf')
            else:
                controller.show_frame('StartPage')

        def selectfile():
            fname = fd.askopenfilename(filetypes=[("Text Files", "*txt")])
            pt_entry.insert(0, str(fname))
            #print(fname)

        file_bt = tk.Button(self, text ='Select File',
                            font=('Airstrike', 13), fg='white', bg='#0d1a26',
                            relief='flat', command=lambda: selectfile())
        file_bt.pack()


        submit_btn = tk.Button(self, text='Submit',
                               font=('Airstrike', 13), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: display_cipher())
        submit_btn.pack(pady=13)

        cipher_lbl = tk.Label(self, text='',
                              font=('Airstrike', 20), fg='white', bg='#191a34',
                              anchor='n')
        cipher_lbl.pack(fill='both', expand=True)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                            command=lambda: clearnleave(2))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back',
                             command=lambda: clearnleave(1))
        back_btn.pack(side='right')


class rsadecrypt(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        p_lbl = tk.Label(self, text='Enter P',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        p_lbl.pack(pady=10)

        p_var = tk.IntVar()
        p_entry = tk.Entry(self, textvariable=p_var,
                           font=('Brothers', 25), width=22)
        p_entry.pack(ipady=7)

        q_lbl = tk.Label(self, text='Enter Q',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        q_lbl.pack(pady=10)

        q_var = tk.IntVar()
        q_entry = tk.Entry(self, textvariable=q_var,
                           font=('Brothers', 25), width=22)
        q_entry.pack(ipady=7)

        privlbl = tk.Label(self, text='Private Key',
                           font=('Airstrike', 25), fg='white', bg='#25274D')
        privlbl.pack()

        privvar = tk.IntVar
        priventry = tk.Entry(self, textvariable=privvar,
                             font=('Brothers', 25), width=22)
        priventry.focus_set()
        priventry.pack()

        def hidepriv(_):
            priventry.configure(fg='black', show='*')

        priventry.bind('<FocusIn>', hidepriv)

        # space_label = tk.Label(self, height=4, bg='#25274D')
        # space_label.pack()

        ctlbl = tk.Label(self, text='Cipher Text',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        ctlbl.pack()

        ctvar = tk.StringVar
        ctentry = tk.Entry(self, textvariable=ctvar,
                           font=('Brothers', 25), width=22)
        ctentry.pack()

        def showpt():
            r = rsa.RSA()
            p = p_entry.get()
            q = q_entry.get()
            cipher_lbl['text'] = ctentry.get()
            if len(p_entry.get())==0 or len(q_entry.get())==0 or len(ctentry.get())==0 or len(priventry.get())==0:
                cipher_lbl['text'] = 'Input fields cannot be empty'
            elif r.checkprime(int(p)) == True and r.checkprime(int(q)) == True:
                r.n = int(p) * int(q)
                r.phi = (int(p) - 1) * (int(q) - 1)
                r.d = int(priventry.get())
                inv = r.mulinv(r.e, r.phi)
                #r.d = inv % r.phi
                cipher = ctentry.get()
                #print(cipher)
                cl = list(map(int, cipher.split()))
                #ct = r.decrypt(int(r.d), int(r.n), str(cipher), 'ptfile.txt')
                ct = r.decryptor(cl, int(r.d), int(r.n), 'ptfile.txt')
                cipher_lbl['text'] = 'Plaintext : ' + str(ct) + '\nA txt file has been created in the same folder'
            else:
                cipher_lbl['text'] = 'Non-prime Values Entered!'

        def clearnleave(a):
            p_entry.delete(0, tk.END)
            q_entry.delete(0, tk.END)
            priventry.delete(0, tk.END)
            ctentry.delete(0, tk.END)
            cipher_lbl['text'] = ''
            if int(a) == 1:
                controller.show_frame('RSA')
            else:
                controller.show_frame('StartPage')

        submit_btn = tk.Button(self, text='Submit',
                               font=('Airstrike', 13), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: showpt())
        submit_btn.pack(pady=13)


        cipher_lbl = tk.Label(self, text='',
                              font=('Airstrike', 20), fg='white', bg='#191a34',
                              anchor='n')
        cipher_lbl.pack(fill='both', expand=True)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                            command=lambda: clearnleave(2))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back', command=lambda: clearnleave(1))
        back_btn.pack(side='right')


class rsadecryptf(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        p_lbl = tk.Label(self, text='Enter P',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        p_lbl.pack(pady=10)

        p_var = tk.IntVar()
        p_entry = tk.Entry(self, textvariable=p_var,
                           font=('Brothers', 25), width=22)
        p_entry.pack(ipady=7)

        q_lbl = tk.Label(self, text='Enter Q',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        q_lbl.pack(pady=10)

        q_var = tk.IntVar()
        q_entry = tk.Entry(self, textvariable=q_var,
                           font=('Brothers', 25), width=22)
        q_entry.pack(ipady=7)

        privlbl = tk.Label(self, text='Private Key',
                           font=('Airstrike', 25), fg='white', bg='#25274D')
        privlbl.pack()

        privvar = tk.IntVar
        priventry = tk.Entry(self, textvariable=privvar,
                             font=('Brothers', 25), width=22)
        priventry.focus_set()
        priventry.pack()

        def hidepriv(_):
            priventry.configure(fg='black', show='*')

        priventry.bind('<FocusIn>', hidepriv)

        # space_label = tk.Label(self, height=4, bg='#25274D')
        # space_label.pack()

        ctlbl = tk.Label(self, text='FilePath',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        ctlbl.pack()

        ctvar = tk.StringVar
        ctentry = tk.Entry(self, textvariable=ctvar,
                           font=('Brothers', 25), width=22)
        ctentry.pack()

        def showpt():
            r = rsa.RSA()
            p = p_entry.get()
            q = q_entry.get()
            cipher_lbl['text'] = ctentry.get()
            if len(p_entry.get())==0 or len(q_entry.get())==0 or len(ctentry.get())==0 or len(priventry.get())==0:
                cipher_lbl['text'] = 'Input fields cannot be empty'
            elif r.checkprime(int(p)) == True and r.checkprime(int(q)) == True:
                fct = ""
                fname = ctentry.get()
                f = open(fname)
                with open(fname, 'r+') as f:
                    fct += f.read()
                r.n = int(p) * int(q)
                r.phi = (int(p) - 1) * (int(q) - 1)
                r.d = int(priventry.get())
                inv = r.mulinv(r.e, r.phi)
                #r.d = inv % r.phi
                cipher = ctentry.get()
                #print(cipher)
                cl = list(map(int, fct.split()))
                #ct = r.decrypt(int(r.d), int(r.n), str(cipher), 'ptfile.txt')
                ct = r.decryptor(cl, int(r.d), int(r.n), 'ptfile.txt')
                cipher_lbl['text'] = 'A txt file has been created in the same folder'
            else:
                cipher_lbl['text'] = 'Non-prime Values Entered!'

        def clearnleave(a):
            p_entry.delete(0, tk.END)
            q_entry.delete(0, tk.END)
            priventry.delete(0, tk.END)
            ctentry.delete(0, tk.END)
            cipher_lbl['text'] = ''
            if int(a) == 1:
                controller.show_frame('RSAf')
            else:
                controller.show_frame('StartPage')

        def selectfile():
            fname = fd.askopenfilename(filetypes=[("Text Files", "*txt")])
            ctentry.insert(0, str(fname))
            #print(fname)

        file_bt = tk.Button(self, text ='Select File',
                            font=('Airstrike', 13), fg='white', bg='#0d1a26',
                            relief='flat', command=lambda: selectfile())
        file_bt.pack()

        submit_btn = tk.Button(self, text='Submit',
                               font=('Airstrike', 13), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: showpt())
        submit_btn.pack(pady=13)


        cipher_lbl = tk.Label(self, text='',
                              font=('Airstrike', 20), fg='white', bg='#191a34',
                              anchor='n')
        cipher_lbl.pack(fill='both', expand=True)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                            command=lambda: clearnleave(2))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back', command=lambda: clearnleave(1))
        back_btn.pack(side='right')


class AES(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        heading1 = tk.Label(self, text='Crypt Walker Tool',
                            font=('Airstrike Half-Tone', 45, 'bold'), fg='white',
                            background='#25274D')
        heading1.pack(pady=25)

        menutext = tk.Label(self, text='Menu',
                            font=('Game Of Squids', 36), fg='white', bg='#25274D')
        menutext.pack()

        space_label = tk.Label(self, height=4, bg='#25274D')
        space_label.pack()

        encryptbtn = tk.Button(self, text='Encrypt',
                               font=('Airstrike', 36), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: controller.show_frame('AESecbenc'))
        encryptbtn.pack()

        decryptbtn = tk.Button(self, text='Decrypt',
                               font=('Airstrike', 36), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: controller.show_frame('AESecbdec'))
        decryptbtn.pack(pady=35)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                             command=lambda: controller.show_frame('StartPage'))
        menu_btn.pack(side='right')

        # back_btn = tk.Button(button_frame, text='Back',
        #                      command=lambda: controller.show_frame('rsaoptions'))
        # back_btn.pack(side='right')


class AESecbenc(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        password_lbl = tk.Label(self, text='Enter Password',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        password_lbl.pack(pady=10)

        p_var = tk.StringVar()
        password_entry = tk.Entry(self, textvariable=p_var,
                           font=('Brothers', 25), width=22)
        #password_entry.pack(ipady=7)

        password_entry.focus_set()
        password_entry.pack()

        def hidepriv(_):
            password_entry.configure(fg='black', show='*')

        password_entry.bind('<FocusIn>', hidepriv)


        pt_lbl = tk.Label(self, text='Enter Plaintext',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        pt_lbl.pack(pady=10)

        pt_var = tk.StringVar()
        pt_entry = tk.Entry(self, textvariable=pt_var,
                           font=('Brothers', 25), width=22)
        pt_entry.pack(ipady=7)

        def showct():
            if len(password_entry.get())==0 or len(pt_entry.get())==0:
                cipher_lbl['text'] = 'Input fields cannot be empty'
            elif len(password_entry.get())!=16:
                cipher_lbl['text'] = 'Password must be 128 bits i.e. 16 char'
            else:
                a = aes.AES()
                inputkey = password_entry.get()
                pt = pt_entry.get()
                a.password = inputkey
                a.pt = pt
                a.genrkeys()
                cipher = a.ptpass(a.pt)
                fname='ctfile.txt'
                with open(fname, 'w+', encoding="utf-8") as f:
                    f.write(cipher)
                cipher_lbl['text'] = 'Text File Created'

        def clearnleave(a):
            password_entry.delete(0, tk.END)
            pt_entry.delete(0, tk.END)
            if a==1:
                controller.show_frame('AES')
            else:
                controller.show_frame('StartPage')

        submit_btn = tk.Button(self, text='Submit',
                               font=('Airstrike', 13), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: showct())
        submit_btn.pack(pady=13)

        cipher_lbl = tk.Label(self, text='',
                              font=('Airstrike', 20), fg='white', bg='#191a34',
                              anchor='n')
        cipher_lbl.pack(fill='both', expand=True)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                            command=lambda: clearnleave(2))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back',
                             command=lambda: clearnleave(1))
        back_btn.pack(side='right')


class AESecbdec(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        password_lbl = tk.Label(self, text='Enter Password',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        password_lbl.pack(pady=10)

        p_var = tk.StringVar()
        password_entry = tk.Entry(self, textvariable=p_var,
                           font=('Brothers', 25), width=22)
        #password_entry.pack(ipady=7)

        password_entry.focus_set()
        password_entry.pack()

        def hidepriv(_):
            password_entry.configure(fg='black', show='*')

        password_entry.bind('<FocusIn>', hidepriv)


        pt_lbl = tk.Label(self, text='Enter Ciphertext',
                         font=('Airstrike', 25), fg='white', bg='#25274D')
        pt_lbl.pack(pady=10)

        pt_var = tk.StringVar()
        pt_entry = tk.Entry(self, textvariable=pt_var,
                           font=('Brothers', 25), width=22)
        pt_entry.pack(ipady=7)

        def showct():
            if len(password_entry.get())==0 or len(pt_entry.get())==0:
                cipher_lbl['text'] = 'Input fields cannot be empty'
            elif len(password_entry.get())!=16:
                cipher_lbl['text'] = 'Password must be 128 bits i.e. 16 char'
            else:
                a = aes.AES()
                inputkey = password_entry.get()
                pt = pt_entry.get()
                a.password = inputkey
                a.pt = pt
                a.genrkeys()
                ciphertemp = a.ctpass(a.pt)
                fname = 'ptfile.txt'
                cipher=''
                for i in range(0, len(ciphertemp)):
                    if ciphertemp[i]=='0':
                        break
                    cipher+=ciphertemp[i]
                with open(fname, 'w+', encoding="utf-8") as f:
                    f.write(cipher)
                cipher_lbl['text'] = 'Text File Created'

        def clearnleave(a):
            password_entry.delete(0, tk.END)
            pt_entry.delete(0, tk.END)
            if a==1:
                controller.show_frame('AES')
            else:
                controller.show_frame('StartPage')

        submit_btn = tk.Button(self, text='Submit',
                               font=('Airstrike', 13), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: showct())
        submit_btn.pack(pady=13)

        cipher_lbl = tk.Label(self, text='',
                              font=('Airstrike', 20), fg='white', bg='#191a34',
                              anchor='n')
        cipher_lbl.pack(fill='both', expand=True)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                            command=lambda: clearnleave(2))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back',
                             command=lambda: clearnleave(1))
        back_btn.pack(side='right')


class VISUAL(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        heading1 = tk.Label(self, text='Crypt Walker Tool',
                            font=('Airstrike Half-Tone', 45, 'bold'), fg='white',
                            background='#25274D')
        heading1.pack(pady=25)

        menutext = tk.Label(self, text='Menu',
                            font=('Game Of Squids', 36), fg='white', bg='#25274D')
        menutext.pack()

        space_label = tk.Label(self, height=4, bg='#25274D')
        space_label.pack()


        encryptbtn = tk.Button(self, text='Simple',
                               font=('Airstrike', 36), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: controller.show_frame('simpleoptions'))
        encryptbtn.pack(ipadx=45)

        decryptbtn = tk.Button(self, text='Advanced',
                               font=('Airstrike', 36), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: controller.show_frame('advoptions'))
        decryptbtn.pack(pady=35)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                             command=lambda: controller.show_frame('StartPage'))
        menu_btn.pack(side='right')

        # back_btn = tk.Button(button_frame, text='Back',
        #                      command=lambda: controller.show_frame('rsaoptions'))
        # back_btn.pack(side='right')


class simpleoptions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        heading1 = tk.Label(self, text='Crypt Walker Tool',
                            font=('Airstrike Half-Tone', 45, 'bold'), fg='white',
                            background='#25274D')
        heading1.pack(pady=25)

        menutext = tk.Label(self, text='Menu',
                            font=('Game Of Squids', 36), fg='white', bg='#25274D')
        menutext.pack()

        space_label = tk.Label(self, height=4, bg='#25274D')
        space_label.pack()


        encryptbtn = tk.Button(self, text='Encrypt',
                               font=('Airstrike', 36), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: controller.show_frame('svcenc'))
        encryptbtn.pack()

        decryptbtn = tk.Button(self, text='Decrypt',
                               font=('Airstrike', 36), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: controller.show_frame('svcdec'))
        decryptbtn.pack(pady=35)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                             command=lambda: controller.show_frame('StartPage'))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back',
                             command=lambda: controller.show_frame('VISUAL'))
        back_btn.pack(side='right')


class advoptions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        heading1 = tk.Label(self, text='Crypt Walker Tool',
                            font=('Airstrike Half-Tone', 45, 'bold'), fg='white',
                            background='#25274D')
        heading1.pack(pady=25)

        menutext = tk.Label(self, text='Menu',
                            font=('Game Of Squids', 36), fg='white', bg='#25274D')
        menutext.pack()

        space_label = tk.Label(self, height=4, bg='#25274D')
        space_label.pack()


        encryptbtn = tk.Button(self, text='Coloured',
                               font=('Airstrike', 36), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: controller.show_frame('cvcoptions'))
        encryptbtn.pack(ipadx=16)

        decryptbtn = tk.Button(self, text='GrayScale',
                               font=('Airstrike', 36), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: controller.show_frame('gvcoptions'))
        decryptbtn.pack(pady=35)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                             command=lambda: controller.show_frame('StartPage'))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back',
                             command=lambda: controller.show_frame('VISUAL'))
        back_btn.pack(side='right')


class cvcoptions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        heading1 = tk.Label(self, text='Crypt Walker Tool',
                            font=('Airstrike Half-Tone', 45, 'bold'), fg='white',
                            background='#25274D')
        heading1.pack(pady=25)

        menutext = tk.Label(self, text='Menu',
                            font=('Game Of Squids', 36), fg='white', bg='#25274D')
        menutext.pack()

        space_label = tk.Label(self, height=4, bg='#25274D')
        space_label.pack()


        encryptbtn = tk.Button(self, text='Encrypt',
                               font=('Airstrike', 36), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: controller.show_frame('cvcenc'))
        encryptbtn.pack()

        decryptbtn = tk.Button(self, text='Decrypt',
                               font=('Airstrike', 36), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: controller.show_frame('cvcdec'))
        decryptbtn.pack(pady=35)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                             command=lambda: controller.show_frame('StartPage'))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back',
                             command=lambda: controller.show_frame('advoptions'))
        back_btn.pack(side='right')


class gvcoptions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        heading1 = tk.Label(self, text='Crypt Walker Tool',
                            font=('Airstrike Half-Tone', 45, 'bold'), fg='white',
                            background='#25274D')
        heading1.pack(pady=25)

        menutext = tk.Label(self, text='Menu',
                            font=('Game Of Squids', 36), fg='white', bg='#25274D')
        menutext.pack()

        space_label = tk.Label(self, height=4, bg='#25274D')
        space_label.pack()


        encryptbtn = tk.Button(self, text='Encrypt',
                               font=('Airstrike', 36), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: controller.show_frame('visualenc'))
        encryptbtn.pack()

        decryptbtn = tk.Button(self, text='Decrypt',
                               font=('Airstrike', 36), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: controller.show_frame('visualdec'))
        decryptbtn.pack(pady=35)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                             command=lambda: controller.show_frame('StartPage'))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back',
                             command=lambda: controller.show_frame('advoptions'))
        back_btn.pack(side='right')


class svcenc(tk.Frame):
    def __init__(self, parent, controller):
        fname = ""
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        # heading1 = tk.Label(self, text='Crypt Walker Tool',
        #                     font=('Airstrike', 45, 'bold'), fg='white',
        #                     background='#25274D')
        # heading1.pack(pady=25)

        def selectfile(a):
            fname = fd.askopenfilename(filetypes=[("jpeg", "*jpg"), ("png", "*png")])
            share2_entry.insert(0, str(fname))
            #print(fname)


        share1_lbl = tk.Label(self, text='Password',
                          font=('Airstrike', 25), fg='white', bg='#25274D')
        share1_lbl.pack(pady=10)

        share1_var = tk.StringVar
        share1_entry = tk.Entry(self, textvariable=share1_var,
                            font=('Brothers', 25), width=22)
        share1_entry.pack(ipady=7)

        share1_entry.focus_set()
        share1_entry.pack(ipady=7)

        def hidepriv(_):
            share1_entry.configure(fg='black', show='*')

        share1_entry.bind('<FocusIn>', hidepriv)

        share2_lbl = tk.Label(self, text='Image',
                          font=('Airstrike', 25), fg='white', bg='#25274D')
        share2_lbl.pack(pady=10)

        share2_var = tk.StringVar
        share2_entry = tk.Entry(self, textvariable=share2_var,
                            font=('Brothers', 25), width=22)
        share2_entry.pack(ipady=7)

        file_bt = tk.Button(self, text='Select File',
                            font=('Airstrike', 13), fg='white', bg='#0d1a26',
                            relief='flat', command=lambda: selectfile(2))
        file_bt.pack()


        def display_cipher():
            if len(share2_entry.get())==0 or len(share1_entry.get())==0:
                cipher_lbl['text'] = 'Input fields cannot be empty'
            else:
                fct=""
                password = share1_entry.get()
                fname = share2_entry.get()
                s = svc.ENC()
                s.mainfunc(fname, password)
                cipher_lbl['text'] = 'A file has been created in the same folder'

        def clearnleave(a):
            share1_entry.delete(0, tk.END)
            share2_entry.delete(0, tk.END)
            cipher_lbl['text'] = ''
            if int(a) == 1:
                controller.show_frame('simpleoptions')
            else:
                controller.show_frame('StartPage')

        submit_btn = tk.Button(self, text='Submit',
                               font=('Airstrike', 13), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: display_cipher())
        submit_btn.pack(pady=13)

        cipher_lbl = tk.Label(self, text='',
                              font=('Airstrike', 20), fg='white', bg='#191a34',
                              anchor='n')
        cipher_lbl.pack(fill='both', expand=True)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                            command=lambda: clearnleave(2))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back',
                             command=lambda: clearnleave(1))
        back_btn.pack(side='right')


class svcdec(tk.Frame):
    def __init__(self, parent, controller):
        fname = ""
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        # heading1 = tk.Label(self, text='Crypt Walker Tool',
        #                     font=('Airstrike', 45, 'bold'), fg='white',
        #                     background='#25274D')
        # heading1.pack(pady=25)

        def selectfile(a):
            fname = fd.askopenfilename(filetypes=[("jpeg", "*jpg"), ("png", "*png")])
            share2_entry.insert(0, str(fname))
            #print(fname)


        share1_lbl = tk.Label(self, text='Password',
                          font=('Airstrike', 25), fg='white', bg='#25274D')
        share1_lbl.pack(pady=10)

        share1_var = tk.StringVar
        share1_entry = tk.Entry(self, textvariable=share1_var,
                            font=('Brothers', 25), width=22)
        #share1_entry.pack(ipady=7)

        share1_entry.focus_set()
        share1_entry.pack(ipady=7)

        def hidepriv(_):
            share1_entry.configure(fg='black', show='*')

        share1_entry.bind('<FocusIn>', hidepriv)

        share2_lbl = tk.Label(self, text='Encrypted Image',
                          font=('Airstrike', 25), fg='white', bg='#25274D')
        share2_lbl.pack(pady=10)

        share2_var = tk.StringVar
        share2_entry = tk.Entry(self, textvariable=share2_var,
                            font=('Brothers', 25), width=22)
        share2_entry.pack(ipady=7)

        file_bt = tk.Button(self, text='Select File',
                            font=('Airstrike', 13), fg='white', bg='#0d1a26',
                            relief='flat', command=lambda: selectfile(2))
        file_bt.pack()


        def display_cipher():
            if len(share2_entry.get())==0 or len(share1_entry.get())==0:
                cipher_lbl['text'] = 'Input fields cannot be empty'
            else:
                fct=""
                password = share1_entry.get()
                fname = share2_entry.get()
                s = svcII.DEC()
                s.mainfunc(fname, password)
                cipher_lbl['text'] = 'A file has been created in the same folder'

        def clearnleave(a):
            share1_entry.delete(0, tk.END)
            share2_entry.delete(0, tk.END)
            cipher_lbl['text'] = ''
            if int(a) == 1:
                controller.show_frame('simpleoptions')
            else:
                controller.show_frame('StartPage')

        submit_btn = tk.Button(self, text='Submit',
                               font=('Airstrike', 13), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: display_cipher())
        submit_btn.pack(pady=13)

        cipher_lbl = tk.Label(self, text='',
                              font=('Airstrike', 20), fg='white', bg='#191a34',
                              anchor='n')
        cipher_lbl.pack(fill='both', expand=True)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                            command=lambda: clearnleave(2))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back',
                             command=lambda: clearnleave(1))
        back_btn.pack(side='right')


class cvcenc(tk.Frame):
    def __init__(self, parent, controller):
        fname = ""
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        # heading1 = tk.Label(self, text='Crypt Walker Tool',
        #                     font=('Airstrike', 45, 'bold'), fg='white',
        #                     background='#25274D')
        # heading1.pack(pady=25)

        pt_lbl = tk.Label(self, text='FilePath',
                          font=('Airstrike Half-Tone', 25), fg='white', bg='#25274D')
        pt_lbl.pack(pady=10)

        pt_var = tk.StringVar
        pt_entry = tk.Entry(self, textvariable=pt_var,
                            font=('Brothers', 25), width=22)
        pt_entry.pack(ipady=7)

        def display_cipher():
            if len(pt_entry.get())==0:
                cipher_lbl['text'] = 'Input fields cannot be empty'
            else:
                fct=""
                fname = pt_entry.get()
                c = cvc.CVC()
                c.encryption(fname)
                cipher_lbl['text'] = 'Three files have been created in the same folder'

        def clearnleave(a):
            pt_entry.delete(0, tk.END)
            cipher_lbl['text'] = ''
            if int(a) == 1:
                controller.show_frame('cvcoptions')
            else:
                controller.show_frame('StartPage')

        def selectfile():
            fname = fd.askopenfilename(filetypes=[("jpeg", "*jpg"), ("png", "*png")])
            pt_entry.insert(0, str(fname))
            #print(fname)

        file_bt = tk.Button(self, text ='Select File',
                            font=('Airstrike', 13), fg='white', bg='#0d1a26',
                            relief='flat', command=lambda: selectfile())
        file_bt.pack()


        submit_btn = tk.Button(self, text='Submit',
                               font=('Airstrike', 13), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: display_cipher())
        submit_btn.pack(pady=13)

        cipher_lbl = tk.Label(self, text='',
                              font=('Airstrike', 20), fg='white', bg='#191a34',
                              anchor='n')
        cipher_lbl.pack(fill='both', expand=True)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                            command=lambda: clearnleave(2))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back',
                             command=lambda: clearnleave(1))
        back_btn.pack(side='right')


class cvcdec(tk.Frame):
    def __init__(self, parent, controller):
        fname = ""
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        # heading1 = tk.Label(self, text='Crypt Walker Tool',
        #                     font=('Airstrike', 45, 'bold'), fg='white',
        #                     background='#25274D')
        # heading1.pack(pady=25)

        def selectfile(a):
            fname = fd.askopenfilename(filetypes=[("jpeg", "*jpg"), ("png", "*png")])
            if a==1:
                share1_entry.insert(0, str(fname))
            elif a==2:
                share2_entry.insert(0, str(fname))
            else:
                share3_entry.insert(0, str(fname))
            #print(fname)


        share1_lbl = tk.Label(self, text='Share 1',
                          font=('Airstrike', 25), fg='white', bg='#25274D')
        share1_lbl.pack(pady=10)

        share1_var = tk.StringVar
        share1_entry = tk.Entry(self, textvariable=share1_var,
                            font=('Brothers', 25), width=22)
        share1_entry.pack(ipady=7)

        file_bt1 = tk.Button(self, text='Select File',
                            font=('Airstrike', 13), fg='white', bg='#0d1a26',
                            relief='flat', command=lambda: selectfile(1))
        file_bt1.pack()

        share2_lbl = tk.Label(self, text='Share 2',
                          font=('Airstrike', 25), fg='white', bg='#25274D')
        share2_lbl.pack(pady=10)

        share2_var = tk.StringVar
        share2_entry = tk.Entry(self, textvariable=share2_var,
                            font=('Brothers', 25), width=22)
        share2_entry.pack(ipady=7)

        file_bt2 = tk.Button(self, text='Select File',
                            font=('Airstrike', 13), fg='white', bg='#0d1a26',
                            relief='flat', command=lambda: selectfile(2))
        file_bt2.pack()

        share3_lbl = tk.Label(self, text='Share 3',
                          font=('Airstrike', 25), fg='white', bg='#25274D')
        share3_lbl.pack(pady=10)

        share3_var = tk.StringVar
        share3_entry = tk.Entry(self, textvariable=share3_var,
                            font=('Brothers', 25), width=22)
        share3_entry.pack(ipady=7)

        file_bt3 = tk.Button(self, text='Select File',
                            font=('Airstrike', 13), fg='white', bg='#0d1a26',
                            relief='flat', command=lambda: selectfile(3))
        file_bt3.pack()


        def display_cipher():
            if len(share2_entry.get())==0 or len(share1_entry.get())==0 or len(share3_entry.get())==0:
                cipher_lbl['text'] = 'Input fields cannot be empty'
            else:
                fct=""
                fname = share1_entry.get()
                fname2 = share2_entry.get()
                fname3 = share3_entry.get()
                c = cvc.CVC()
                c.decryption(fname, fname2, fname3)
                cipher_lbl['text'] = 'A file has been created in the same folder'

        def clearnleave(a):
            share1_entry.delete(0, tk.END)
            share2_entry.delete(0, tk.END)
            share3_entry.delete(0, tk.END)
            cipher_lbl['text'] = ''
            if int(a) == 1:
                controller.show_frame('cvcoptions')
            else:
                controller.show_frame('StartPage')

        submit_btn = tk.Button(self, text='Submit',
                               font=('Airstrike', 13), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: display_cipher())
        submit_btn.pack(pady=13)

        cipher_lbl = tk.Label(self, text='',
                              font=('Airstrike', 20), fg='white', bg='#191a34',
                              anchor='n')
        cipher_lbl.pack(fill='both', expand=True)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                            command=lambda: clearnleave(2))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back',
                             command=lambda: clearnleave(1))
        back_btn.pack(side='right')


class visualenc(tk.Frame):
    def __init__(self, parent, controller):
        fname = ""
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        # heading1 = tk.Label(self, text='Crypt Walker Tool',
        #                     font=('Airstrike', 45, 'bold'), fg='white',
        #                     background='#25274D')
        # heading1.pack(pady=25)

        pt_lbl = tk.Label(self, text='FilePath',
                          font=('Airstrike Half-Tone', 25), fg='white', bg='#25274D')
        pt_lbl.pack(pady=10)

        pt_var = tk.StringVar
        pt_entry = tk.Entry(self, textvariable=pt_var,
                            font=('Brothers', 25), width=22)
        pt_entry.pack(ipady=7)

        def display_cipher():
            if len(pt_entry.get())==0:
                cipher_lbl['text'] = 'Input fields cannot be empty'
            else:
                fct=""
                fname = pt_entry.get()
                g = grayscale.GVC()
                g.viscrypt(fname)
                cipher_lbl['text'] = 'The files have been created in the same folder'

        def clearnleave(a):
            pt_entry.delete(0, tk.END)
            cipher_lbl['text'] = ''
            if int(a) == 1:
                controller.show_frame('gvcoptions')
            else:
                controller.show_frame('StartPage')

        def selectfile():
            fname = fd.askopenfilename(filetypes=[("jpeg", "*jpg"), ("png", "*png")])
            pt_entry.insert(0, str(fname))
            #print(fname)

        file_bt = tk.Button(self, text ='Select File',
                            font=('Airstrike', 13), fg='white', bg='#0d1a26',
                            relief='flat', command=lambda: selectfile())
        file_bt.pack()


        submit_btn = tk.Button(self, text='Submit',
                               font=('Airstrike', 13), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: display_cipher())
        submit_btn.pack(pady=13)

        cipher_lbl = tk.Label(self, text='',
                              font=('Airstrike', 20), fg='white', bg='#191a34',
                              anchor='n')
        cipher_lbl.pack(fill='both', expand=True)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                            command=lambda: clearnleave(2))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back',
                             command=lambda: clearnleave(1))
        back_btn.pack(side='right')


class visualdec(tk.Frame):
    def __init__(self, parent, controller):
        fname = ""
        tk.Frame.__init__(self, parent, bg='#25274D')

        self.controller = controller

        self.controller.title('CryptWalker')

        self.controller.state('zoomed')

        self.controller.iconphoto(False, tk.PhotoImage(file='crypt-key.png'))

        # heading1 = tk.Label(self, text='Crypt Walker Tool',
        #                     font=('Airstrike', 45, 'bold'), fg='white',
        #                     background='#25274D')
        # heading1.pack(pady=25)

        def selectfile(a):
            fname = fd.askopenfilename(filetypes=[("jpeg", "*jpg"), ("png", "*png")])
            if a==1:
                share1_entry.insert(0, str(fname))
            else:
                share2_entry.insert(0, str(fname))
            #print(fname)


        share1_lbl = tk.Label(self, text='Share 1',
                          font=('Airstrike', 25), fg='white', bg='#25274D')
        share1_lbl.pack(pady=10)

        share1_var = tk.StringVar
        share1_entry = tk.Entry(self, textvariable=share1_var,
                            font=('Brothers', 25), width=22)
        share1_entry.pack(ipady=7)

        file_bt1 = tk.Button(self, text='Select File',
                            font=('Airstrike', 13), fg='white', bg='#0d1a26',
                            relief='flat', command=lambda: selectfile(1))
        file_bt1.pack()

        share2_lbl = tk.Label(self, text='Share 2',
                          font=('Airstrike', 25), fg='white', bg='#25274D')
        share2_lbl.pack(pady=10)

        share2_var = tk.StringVar
        share2_entry = tk.Entry(self, textvariable=share2_var,
                            font=('Brothers', 25), width=22)
        share2_entry.pack(ipady=7)

        file_bt = tk.Button(self, text='Select File',
                            font=('Airstrike', 13), fg='white', bg='#0d1a26',
                            relief='flat', command=lambda: selectfile(2))
        file_bt.pack()


        def display_cipher():
            if len(share2_entry.get())==0 or len(share1_entry.get())==0:
                cipher_lbl['text'] = 'Input fields cannot be empty'
            else:
                fct=""
                fname = share1_entry.get()
                fname2 = share2_entry.get()
                g = grayscale.GVC()
                g.videcrypt(fname, fname2)
                cipher_lbl['text'] = 'A file has been created in the same folder'

        def clearnleave(a):
            share1_entry.delete(0, tk.END)
            share2_entry.delete(0, tk.END)
            cipher_lbl['text'] = ''
            if int(a) == 1:
                controller.show_frame('gvcoptions')
            else:
                controller.show_frame('StartPage')

        submit_btn = tk.Button(self, text='Submit',
                               font=('Airstrike', 13), fg='white', bg='#0d1a26',
                               relief='flat', command=lambda: display_cipher())
        submit_btn.pack(pady=13)

        cipher_lbl = tk.Label(self, text='',
                              font=('Airstrike', 20), fg='white', bg='#191a34',
                              anchor='n')
        cipher_lbl.pack(fill='both', expand=True)

        button_frame = tk.Frame(self, relief='raised', borderwidth=3)
        button_frame.pack(fill='x', side='bottom')

        menu_btn = tk.Button(button_frame, text='Main Menu',
                            command=lambda: clearnleave(2))
        menu_btn.pack(side='right')

        back_btn = tk.Button(button_frame, text='Back',
                             command=lambda: clearnleave(1))
        back_btn.pack(side='right')


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()