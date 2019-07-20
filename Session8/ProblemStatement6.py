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

#import os
#os.chdir("C:\\Users\\panda4\\ml-20m")

'''
I. Read the dataset using pandas.
'''
df_ratings = pd.read_csv("./ml-20m/ratings.csv")
df_tags = pd.read_csv("./ml-20m/tags.csv")
df_movies = pd.read_csv("./ml-20m/movies.csv")

'''
II. Extract the first row from tags and print its type.
'''
print(type(df_tags[:1]))

'''
III. Extract row 0, 11, 2000 from tags DataFrame.
'''
print(df_tags.iloc[[0,11,2000],:])

'''
IV. Print index, columns of the DataFrame.
'''
print(df_tags.columns)
print(df_tags.index)

'''
V. Calculate descriptive statistics for the 'ratings' column of the ratings DataFrame. Verify using describe().
'''
print(df_ratings["rating"].describe())

'''
VI. Filter out ratings with rating > 5
'''
print(df_ratings[df_ratings["rating"] > 5]["rating"])

'''
VII. Find how many null values, missing values are present. Deal with them. Print out how many rows have been modified.
'''
print(df_ratings.isnull().sum())

'''
VIII. Filter out movies from the movies DataFrame that are of type 'Animation'.
'''
print(df_movies[df_movies["genres"] == "Animation"])

'''
IX. Find the average rating of movies.
'''
print(df_ratings["rating"].mean())

'''
X. Perform an inner join of movies and tags based on movieId.
'''
movie_tags = pd.merge(df_movies, df_tags, how="inner", on="movieId")
print(movie_tags)

'''
XI. Print out the 5 movies that belong to the Comedy genre and have rating greater than 4.
'''
comedy_rating = pd.merge(df_movies, df_ratings, how="inner", on="movieId")
print(comedy_rating[comedy_rating["genres"] == "Comedy"][comedy_rating["rating"] > 4]["title"].unique()[:5].tolist())

'''
XII. Split 'genres' into multiple columns.
'''
df_movies[["genre1", "genre2", "genre3"]] = df_movies.genres.str.split("|", n=2, expand = True,)
print(df_movies)

'''
XIII. Extract year from title e.g. (1995).
'''
df_movies["year"] = df_movies["title"].str.extract("\s\((\d{4})\)$", expand = True)
print(df_movies)

'''
XIV. Select rows based on timestamps later than 2015-02-01.
'''
import datetime
timestamp_input = datetime.datetime(2015, 2, 1).timestamp()
print(timestamp_input)
print(df_tags[df_tags["timestamp"] > timestamp_input])

'''
XV. Sort the tags DataFrame based on timestamp.
'''
print(df_tags.sort_values(by = "timestamp"))