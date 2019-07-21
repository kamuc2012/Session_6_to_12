#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Get Data from the following link:
http://files.grouplens.org/datasets/movielens/ml-20m.zip

We will be using the following files for this exercise:
ratings.csv : userId,movieId,rating, timestamp
tags.csv : userId,movieId, tag, timestamp
movies.csv : movieId, title, genres

I. Read the dataset using pandas.
II. Extract the first row from tags and print its type.
III. Extract row 0, 11, 2000 from tags DataFrame.
IV. Print index, columns of the DataFrame.
V. Calculate descriptive statistics for the 'ratings' column of the ratings DataFrame. Verify using describe().
VI. Filter out ratings with rating > 5
VII. Find how many null values, missing values are present. Deal with them. Print out how many rows have been modified.
VIII. Filter out movies from the movies DataFrame that are of type 'Animation'.
IX. Find the average rating of movies.
X. Perform an inner join of movies and tags based on movieId.
XI. Print out the 5 movies that belong to the Comedy genre and have rating greater than 4.
XII. Split 'genres' into multiple columns.
XIII. Extract year from title e.g. (1995).
XIV. Select rows based on timestamps later than 2015-02-01.
XV. Sort the tags DataFrame based on timestamp.
"""
import pandas as pd

'''
I. Read the dataset using pandas.
'''
df_ratings = pd.read_csv("./ml-20m/ratings.csv")
df_tags = pd.read_csv("./ml-20m/tags.csv")
df_movies = pd.read_csv("./ml-20m/movies.csv")

'''
II. Extract the first row from tags and print its type.
'''
print("Extract the first row from tags and print its type\n")
print(type(df_tags[:1]))
print("\n", "="*50, "\n", sep="")

'''
III. Extract row 0, 11, 2000 from tags DataFrame.
'''
print("Extract row 0, 11, 2000 from tags DataFrame\n")
print(df_tags.iloc[[0,11,2000],:])
print("\n", "="*50, "\n", sep="")

'''
IV. Print index, columns of the DataFrame.
'''
print("Print index, columns of the DataFrame\n")
print(df_tags.columns)
print(df_tags.index)
print("\n", "="*50, "\n", sep="")

'''
V. Calculate descriptive statistics for the 'ratings' column of the ratings DataFrame. Verify using describe().
'''
print("Calculate descriptive statistics for the 'ratings' column of the ratings DataFrame. Verify using describe()\n")
print(df_ratings["rating"].describe())
print("\n", "="*50, "\n", sep="")

'''
VI. Filter out ratings with rating > 5
'''
print("Filter out ratings with rating > 5")
print(df_ratings[df_ratings["rating"] > 5]["rating"])
print("\n", "="*50, "\n", sep="")

'''
VII. Find how many null values, missing values are present. Deal with them. Print out how many rows have been modified.
'''
print("Find how many null values, missing values are present. Deal with them. Print out how many rows have been modified.\n")
print(df_ratings.isnull().sum())
print("\n", "="*50, "\n", sep="")

'''
VIII. Filter out movies from the movies DataFrame that are of type 'Animation'.
'''
print("Filter out movies from the movies DataFrame that are of type 'Animation'\n")
print(df_movies[df_movies["genres"] == "Animation"])
print("\n", "="*50, "\n", sep="")

'''
IX. Find the average rating of movies.
'''
print("Find the average rating of movies\n")
print(df_ratings["rating"].mean())
print("\n", "="*50, "\n", sep="")

'''
X. Perform an inner join of movies and tags based on movieId.
'''
print("Perform an inner join of movies and tags based on movieId\n")
movie_tags = pd.merge(df_movies, df_tags, how="inner", on="movieId")
print(movie_tags)
print("\n", "="*50, "\n", sep="")

'''
XI. Print out the 5 movies that belong to the Comedy genre and have rating greater than 4.
'''
print("Print out the 5 movies that belong to the Comedy genre and have rating greater than 4\n")
comedy_rating = pd.merge(df_movies, df_ratings, how="inner", on="movieId")
print(comedy_rating[comedy_rating["genres"] == "Comedy"][comedy_rating["rating"] > 4]["title"].unique()[:5].tolist())
print("\n", "="*50, "\n", sep="")

'''
XII. Split 'genres' into multiple columns.
'''
print("Split 'genres' into multiple columns\n")
df_movies[["genre1", "genre2", "genre3"]] = df_movies.genres.str.split("|", n=2, expand = True,)
print(df_movies)
print("\n", "="*50, "\n", sep="")

'''
XIII. Extract year from title e.g. (1995).
'''
print("Extract year from title e.g. (1995)\n")
df_movies["year"] = df_movies["title"].str.extract("\s\((\d{4})\)$", expand = True)
print(df_movies)
print("\n", "="*50, "\n", sep="")

'''
XIV. Select rows based on timestamps later than 2015-02-01.
'''
print("Select rows based on timestamps later than 2015-02-01\n")
import datetime
timestamp_input = datetime.datetime(2015, 2, 1).timestamp()
print(timestamp_input)
print(df_tags[df_tags["timestamp"] > timestamp_input])
print("\n", "="*50, "\n", sep="")

'''
XV. Sort the tags DataFrame based on timestamp.
'''
print("Sort the tags DataFrame based on timestamp\n")
print(df_tags.sort_values(by = "timestamp"))
print("\n", "="*50, "\n", sep="")