#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Read the following data set:
https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data

Task:
1. Create an sqlalchemy engine using a sample from the data set
2. Write two basic update queries
3. Write two delete queries
4. Write two filter queries
5. Write two function queries
"""
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data", header=None)
df.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']
print(df.head())
print("="*50)
print()

'''
1. Create an sqlalchemy engine using a sample from the data set
'''
engine = create_engine("sqlite:///adult_data_new.db")
df.to_sql("adult_data_new", engine)

'''
2. Write two basic update queries
'''
query1 = "UPDATE adult_data_new SET hours_per_week = 40 WHERE education = 'Bachelors'"
engine.execute(query1)

query2 = "UPDATE adult_data_new SET income = '>=100K' WHERE age >= 50"
engine.execute(query2)
print("\n", "="*50, "\n", sep="")

'''
3. Write two delete queries
'''
query3 = "DELETE FROM adult_data_new WHERE age = 50"
engine.execute(query3)

query4 = "DELETE FROM adult_data_new WHERE education = '9th'"
engine.execute(query4)
print("\n", "="*50, "\n", sep="")

'''
4. Write two filter queries
'''
query5 = "SELECT * FROM adult_data_new WHERE age > 35"
print(engine.execute(query5).fetchall())

query6 = "SELECT * FROM adult_data_new WHERE education = 'Masters' AND workclass = 'Private'"
print(engine.execute(query6).fetchall())
print("\n", "="*50, "\n", sep="")

'''
5. Write two function queries
'''
query7 = "SELECT MAX(age) FROM adult_data_new"
print(engine.execute(query7).fetchone())

query8 = "SELECT COUNT(age) FROM adult_data_new WHERE education = 'Masters' AND workclass = 'Private'"
print(engine.execute(query8).fetchone())
print("\n", "="*50, "\n", sep="")