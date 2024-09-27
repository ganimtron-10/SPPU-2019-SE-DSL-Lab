"""
Aledutron
SPPU 2019 SE DSL Lab
SPPU Computer Engineering Second Year (SE) Data Structure Lab (DSL) / Fundamentals of Data Structures (FDS) Assignments (2019 Pattern)
Youtube DSL / FDS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&si=u12IYwo93Z7RU4e8

Problem Statement:
Group-B\Q12.py
a) Write a python program to store names and mobile numbers of your friends in sorted order on names. Search your friend from list using binary search (recursive and non☻recursive). Insert friend if not present in phonebook
b) Write a python program to store names and mobile numbers of your friends in sorted order on names. Search your friend from list using Fibonacci search. Insert friend if not present in phonebook.

Explaination Video Link: https://www.youtube.com/watch?v=_rKyFEmH5Ww&list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&index=10&pp=iAQB
"""

import random


def return_max(l):
    max_val = l[0]
    for i in l:
        if max_val < i:
            max_val = i
    return max_val


def return_min(l):
    min_val = l[0]
    for i in l:
        if min_val > i:
            min_val = i
    return min_val


def find_saddle_point(matrix):
    row_min = []
    col_max = []

    row_count = len(matrix)
    col_count = len(matrix[0])

    for i in range(row_count):
        row_min.append(return_min(matrix[i]))

    for col in range(col_count):
        max_col_value = matrix[0][col]
        for row in range(row_count):
            if matrix[row][col] > max_col_value:
                max_col_value = matrix[row][col]
        col_max.append(max_col_value)

    print(row_min, col_max)

    for row in range(row_count):
        for column in range(col_count):
            if row_min[row] == col_max[column]:
                return (
                    f"Saddle point at {row} {column} for value {matrix[row][column]}."
                )
        return "No Saddle point exist!"


m = [[random.randint(-10, 10) for i in range(2)] for i in range(3)]

print(m)

print(find_saddle_point(m))
