#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a python module script that contains ispalindrome() method to calculate the input string as palindrome string or not and save it as palindrome.py.
"""
def ispalindrome(s):
    if s[::-1] == s:
        return True
    else:
        return False

# This file can be saved as palindrome.py, Function ispalindrome() can be used to check palindrome string after importing file.