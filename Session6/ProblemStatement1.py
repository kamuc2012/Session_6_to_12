#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a function so that the columns of the output matrix are powers of the input vector.

The order of the powers is determined by the increasing boolean argument. 
Specifically, when increasing is False, the i-th output column is the input vector raised element-wise to the power of N - i - 1.

HINT: Such a matrix with a geometric progression in each row is named for AlexandreTheophile Vandermonde.
"""
import numpy as np

# Function which works similar to np.vander()
def generate_matrix(input_vector, columns, increasing):
    start = 0
    stop = columns
    step = 1

    if increasing:
        start = columns - 1
        stop = -1
        step = -1

    return np.column_stack([input_vector ** (columns - 1 - i) for i in range(start, stop, step)])

input_vector = np.array([1, 2, 3, 4, 5])
columns = 5
increasing = True

print(generate_matrix(input_vector, columns, increasing))