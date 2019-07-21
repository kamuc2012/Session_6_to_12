#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Read the dataset from the below link
https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv

Questions:
1) Delete unnamed columns
2) Show the distribution of male and female
3) Show the top 5 most preferred names
4) What is the median name occurrence in the dataset
5) Distribution of male and female born count by states
"""
import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv")
print("Top 5 rows from dataset\n")
print(df.head())
print("\n", "="*50, "\n", sep="")

'''
1) Delete unnamed columns
'''
print("Delete unnamed columns\n")
df.drop("Unnamed: 0", axis=1, inplace=True)
print(df.head())
print("\n", "="*50, "\n", sep="")

'''
2) Show the distribution of male and female
'''
print("Show the distribution of male and female\n")
print(df.groupby("Gender").count())
print()
print(df["Gender"].value_counts("F"))
print("\n", "="*50, "\n", sep="")

'''
3) Show the top 5 most preferred names
'''
print("Show the top 5 most preferred names\n")
print(df["Name"].value_counts().head())
print("\n", "="*50, "\n", sep="")

'''
4) What is the median name occurrence in the dataset
'''
print("What is the median name occurrence in the dataset\n")
data_median =  (np.where(df["Id"] == df["Id"].median()))
print(df.loc[data_median])
print("\n", "="*50, "\n", sep="")

'''
5) Distribution of male and female born count by states
'''
print("Distribution of male and female born count by states\n")
print(df.groupby(["State", "Gender"]).count()["Count"])
print("\n", "="*50, "\n", sep="")