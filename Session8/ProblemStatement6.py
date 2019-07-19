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
