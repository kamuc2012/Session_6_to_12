#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a Python program which accepts a list named : randomList = ['a', 0, 2]. Use exception handling using try-catch which gives the output as:

Output:

1) If the List element is a alphabet or string, the output will be
The entry is a
Oops! <class 'ValueError'> occured.
Next entry.

2) If the List element is “0”,the output will be
The entry is 0
Oops! <class '  '> occured.
Next entry.

3) If the List element is and integer except 0,then output will be:
The entry is 2
The reciprocal of 2 is 0.5 // reciprocal of an integer
"""
import sys

randomList = ["a", 0, 2]

for i in randomList:
    try:
        print("The entry is", i)
        r = 1/int(i)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occured.")
        print("Next entry.")
        print()

print("The reciprocal of", i, "is", r)