#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1) How-to-count-distance-to-the-previous-zero
For each value, count the difference of the distance from the previous zero (or the start of the Series, whichever is closer) and if there are no previous zeros, print the position

Consider a DataFrame df where there is an integer column {'X'[7, 2, 0, 3, 4, 2, 5, 0, 3, 4]}

The values should therefore be [1, 2, 0, 1, 2, 3, 4, 0, 1, 2]. Make this a new column 'Y'.
import pandas as pd
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

2) Create a DatetimeIndex that contains each business day of 2015 and use it to index a Series of random numbers.

3) Find the sum of the values in s for every Wednesday

4) Average For each calendar month

5) For each group of four consecutive calendar months in s, find the date on which the highest value occurred.
"""

'''
1) How-to-count-distance-to-the-previous-zero
'''
import pandas as pd

df = pd.DataFrame({"X": [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
Y, index = [], 0

for i in range(len(df.X)):
    if df.X[i] == 0:
        index = 0
    else:
        index += 1
    Y.append(index)

df["Y"] = Y
print("count-distance-to-the-previous-zero\n")
print(df)
print("\n", "="*50, "\n", sep="")

'''
2) Create a DatetimeIndex that contains each business day of 2015 and use it to index a Series of random numbers.
'''
import numpy as np

dates = pd.date_range(start="2015-01-01", end="2015-12-31", freq="B") 
s = pd.Series(np.random.rand(len(dates)), index=dates)
print("DatetimeIndex that contains each business day of 2015 and use it to index a Series of random numbers\n")
print(s)
print("\n", "="*50, "\n", sep="")

'''
3) Find the sum of the values in s for every Wednesday
'''
print("Find the sum of the values in s for every Wednesday\n")
print(s[dates.weekday == 2].sum())
print("\n", "="*50, "\n", sep="")

'''
4) Average For each calendar month
'''
print("Average For each calendar month\n")
print(s.resample("M").mean())
print("\n", "="*50, "\n", sep="")

'''
5) For each group of four consecutive calendar months in s, find the date on which the highest value occurred.
'''
print("Group of four consecutive calendar months in s, find the date on which the highest value occurred\n")
print("Jan-Apr = ", s["2015-01-01":"2015-04-30"].idxmax())
print("May-Aug = ", s["2015-05-01":"2015-08-31"].idxmax())
print("Sep-Dec = ", s["2015-09-01":"2015-12-31"].idxmax())
print("\n", "="*50, "\n", sep="")