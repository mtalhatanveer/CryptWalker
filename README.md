# CryptWalker

CryptWalker was my semester project for the Information Security.
CryptWalker was the name my group members and I came up for an all-in-one gui-based 
cryptography application that would be capable of encrypting and decrypting text and files using:

~ AES 128-bit in ECB mode

~ RSA

~ Visual Cryptography


AES and RSA don't really need any introduction or explanation due to their wide use and fame globally.
Visual Cryptography, however, was described in our report as follows:

   "For Visual Cryptography, the simplest and most basic form of this technique was implemented
   using 256-bit AES cbc mode in which we used the cryptographic module for python.
   Furthermore, we attempted to implement more advanced techniques of Visual Cryptography
   which includes 2n visual cryptography for grayscale images and also colour visual cryptography.
   The main aim of all three of these “sub-divisions” of Visual Cryptography is to somehow
   obscure the details of the original message (in this case it is an image) so that any unknowing
   person may not make out what it is supposed to be." 
   

# Implementation Details

~ The language used to implement this project was Python

~ The gui was made using the widely used Python library known as "Tkinter"

~ AES was implemented from scratch 

~ RSA was implemented using the crypto library in Python

~ The visual cryptography module was done via matrix manipulation to change 
  the pixels
  

# Screenshots

Main Menu
![mainmenu](https://user-images.githubusercontent.com/34996639/224276532-11d18069-f0bb-4227-824f-a628f863d4b2.png)


AES
![aesmenu](https://user-images.githubusercontent.com/34996639/224276596-16e86b26-93e1-4181-8537-bc7aa1cf7e19.png)
![aesencrypt](https://user-images.githubusercontent.com/34996639/224277103-0af77d17-88c1-4302-80a7-021a8b0307dd.png)
![aesdecrypt](https://user-images.githubusercontent.com/34996639/224277110-fd1bc390-3bf7-470e-8eee-4e95e6e22a0c.png)


RSA
![rsamenu1](https://user-images.githubusercontent.com/34996639/224276772-8cbaa13c-df7b-445f-8fed-965225e55185.png)
![rsaencrypt](https://user-images.githubusercontent.com/34996639/224277153-0be36751-08ff-4e9d-a283-55581add5007.png)
![rsadecrypt](https://user-images.githubusercontent.com/34996639/224277156-69eccdd5-86ef-47ee-8b89-1082c3d151a2.png)


Visual Cryptography
![vcmenu](https://user-images.githubusercontent.com/34996639/224276799-d65e9c6c-71d8-4127-a2ca-935fe726d21e.png)
![vcdecrypt](https://user-images.githubusercontent.com/34996639/224277234-6c222072-2d4a-4bd2-9c6f-7151fd00b7c3.png)
![vcencrypt](https://user-images.githubusercontent.com/34996639/224277224-67cb6a13-80be-4055-8951-acdf3b60f26d.png)

