#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a program in Python with one class called Cipher. Within the constructor of this class, ask user for a string and store it. 
Use a static variable, key to store a randomly generated integer between 1 and 50 inclusive. 
Implement two methods, encrypt and decrypt within this class. 
Encrypt generates and prints a cipher text using the user-entered string and the key and ecrypt generates decrypted string from ciphertext. 
The cipher only encrypts alpha and numeric (A-Z, a-z, 0-9). All Symbols, such as - , ; %, remain unencrypted.
The cipher text can have special characters. Use generator expression to filter out alpha and numeric characters of the input string and to generate cipher text. 
Create an instance of this class, encrypt and decrypt back the user entered string.
"""
import random

class Cipher():
    key = random.randint(1,51)

    def __init__(self, text):
        self.text = text
        self.encrypted_text = ""

    def encrypt(self):
        result = ""
        for i in range(len(self.text)):
            char = self.text[i]
            if (char.isupper()):
                result += chr((ord(char) + Cipher.key - 65) % 26 + 65)
            else:
                result += chr((ord(char) + Cipher.key - 97) % 26 + 97)

        self.encrypted_text = result
        return self.encrypted_text

    def decrypt(self):
        result = ""
        for i in range(len(self.encrypted_text)):
            char = self.encrypted_text[i]
            if (char.isupper()):
                result += chr((ord(char) - Cipher.key - 65) % 26 + 65)
            else:
                result += chr((ord(char) - Cipher.key - 97) % 26 + 97)

        return result

text = input("Input any string: ")
print("\nText = ", text)

c = Cipher(text)
print("Encrypted = ", c.encrypt())
print("Decrypted = ", c.decrypt())