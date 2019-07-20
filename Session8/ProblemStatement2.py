#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Array out of Bound Exception

Write a Python program to give exception “Array Out of Bound” if the user wants to access the elements beyond the list size (use try and except)
"""
list_random_numbers = [1, 2, 3, 4, 5]

try:
    print(list_random_numbers[0])
    print(list_random_numbers[10])
except IndexError as error:
    print("Exception: Array Out of Bound")