#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Matplotlib:
This assignment is for visualization using matplotlib.

data to use:
url=https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv
titanic = pd.read_csv(url)

Charts to plot:
1. Create a pie chart presenting the male/female proportion
2. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

titanic = pd.read_csv("https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv")
print(titanic.head())
print("="*50)

'''
1. Create a pie chart presenting the male/female proportion
'''
distribution = titanic["sex"].value_counts()

fig = plt.figure(figsize=(10,6))
plt.pie(distribution)
plt.xlabel("Female")
plt.ylabel("Male")
plt.show()

'''
2. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender
'''
print(titanic.isnull().sum())

titanic["sex"].fillna(method="ffill", inplace=True)
titanic["age"].fillna(method="ffill", inplace=True)
titanic["fare"].fillna(method="ffill", inplace=True)

print(titanic.isnull().sum())

fig = plt.figure(figsize=(18,6))
plt.scatter(titanic["age"], titanic["fare"], alpha=0.5, c=pd.factorize(titanic["sex"])[0])
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()