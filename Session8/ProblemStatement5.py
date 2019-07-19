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
