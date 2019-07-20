#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a python module script that contains fib2() method to calculate the Fibonacci series till 1000 and save it as fibo.py.

Note : The module created as fibo.py has to be placed in lib folder

For linux/ubuntu path = /home/anaconda/lib/python3
For Windows path = C:/Users/Ajit/Anaconda3/Lib
"""
def fibo(n):
    sequence = []
    a, b = 0, 1
    while b < n:
        sequence.append(b)
        a, b = b, a + b

    return sequence

# This file can be saved as fibo.py, Function fibo() can be used generate Fibonacci series after importing file.