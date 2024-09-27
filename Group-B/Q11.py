"""
Aledutron
SPPU 2019 SE DSL Lab
SPPU Computer Engineering Second Year (SE) Data Structure Lab (DSL) / Fundamentals of Data Structures (FDS) Assignments (2019 Pattern)
Youtube DSL / FDS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&si=u12IYwo93Z7RU4e8

Problem Statement:
Group-B\Q11.py
a) Write a pythonprogram to store roll numbers of student in array who attended training program in random order. Write function for searching whether particular student attended training program or not, using Linear search and Sentinel search.
b) Write a python program to store roll numbers of student array who attended training program in sorted order. Write function for searching whether particular student attended training program or not, using Binary search and Fibonacci search

Explaination Video Link: https://www.youtube.com/watch?v=5g84mMMFcMU&list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&index=9&pp=iAQB
"""

import random

student_list = [random.randint(-100, 100) for i in range(10)]
print(student_list)


def linear_search(l, key):
    # O(n)
    for i in range(len(l)):
        if l[i] == key:
            return i
    return -1


def sentinel_search(l, key):
    # O(n)
    last_element = l[-1]
    l[-1] = key
    i = 0
    while l[i] != key:
        i += 1  # i = i+1

    if i != len(l) - 1:
        return i
    elif last_element == key:
        return len(l) - 1
    else:
        return -1


key = random.choice(student_list)
print(key)

print(sentinel_search(student_list, student_list[-1]))
