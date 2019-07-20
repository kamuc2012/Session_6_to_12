#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Read the following data set:
https://archive.ics.uci.edu/ml/machine-learning-databases/adult/

Rename the columns as per the description from this file:
https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.names

Task:

Create a sql db from adult dataset and name it sqladb
1. Select 10 records from the adult sqladb
2. Show me the average hours per week of all men who are working in private sector
3. Show me the frequency table for education, occupation and relationship, separately
4. Are there any people who are married, working in private sector and having a master’s degree
5. What is the average, minimum and maximum age group for people working in different sectors
6. Calculate age distribution by country
7. Compute a new column as 'Net-Capital-Gain' from the two columns 'capitalgain' and 'capitalloss'
"""
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import sqlite3 as db

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data", header=None)
df.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']
print(df.head())
print("="*50)
print()

'''
Create a sql db from adult dataset and name it sqladb
'''
sqladb = db.connect("./adult_data.db")

cursor = sqladb.cursor()
df.to_sql("adult_data", sqladb, if_exists="replace", index=False)

'''
1. Select 10 records from the adult sqladb
'''
query = "SELECT * FROM adult_data LIMIT 10"
print(pd.read_sql_query(query, sqladb))
print("="*50)
print()

'''
2. Show me the average hours per week of all men who are working in private sector
'''
query = "SELECT AVG(hours_per_week) AS average_hours_per_week FROM adult_data WHERE sex = 'Male' AND workclass = 'Private'"
print(pd.read_sql_query(query, sqladb))
print("="*50)
print()

'''
3. Show me the frequency table for education, occupation and relationship, separately
'''
query = "SELECT  education, COUNT(education) AS frequency FROM adult_data GROUP BY education ORDER BY frequency DESC"
print(pd.read_sql_query(query, sqladb))
print()

query = "SELECT  occupation, COUNT(occupation) AS frequency FROM adult_data GROUP BY occupation ORDER BY frequency DESC"
print(pd.read_sql_query(query, sqladb))
print()

query = "SELECT  relationship, COUNT(relationship) AS frequency FROM adult_data GROUP BY relationship ORDER BY frequency DESC"
print(pd.read_sql_query(query, sqladb))
print("="*50)
print()

'''
4. Are there any people who are married, working in private sector and having a master’s degree
'''
query = "SELECT COUNT(age) AS records FROM adult_data WHERE marital_status LIKE '%Married%' AND workclass = 'Private' AND education = 'Masters'"
print(pd.read_sql_query(query, sqladb))
print("="*50)
print()

'''
5. What is the average, minimum and maximum age group for people working in different sectors
'''
query = "SELECT workclass, AVG(age) AS average, MIN(age) AS minimum, MAX(age) AS maximum FROM adult_data GROUP BY workclass"
print(pd.read_sql_query(query, sqladb))
print("="*50)
print()

'''
6. Calculate age distribution by country
'''
query = "SELECT native_country, ROUND(ROUND((COUNT(age)*100),5)/ROUND((SELECT COUNT(age) FROM adult_data),5),5) AS age_destribution FROM adult_data GROUP BY native_country ORDER BY COUNT(age) DESC"
print(pd.read_sql_query(query, sqladb))
print("="*50)
print()

'''
7. Compute a new column as 'Net-Capital-Gain' from the two columns 'capitalgain' and 'capitalloss'
'''
query = "SELECT capital_gain, capital_loss, (capital_gain - capital_loss) AS 'Net-Capital-Gain' FROM adult_data"
print(pd.read_sql_query(query, sqladb))
print("="*50)

sqladb.close()