"""
Aledutron
SPPU 2019 SE DSL Lab
SPPU Computer Engineering Second Year (SE) Data Structure Lab (DSL) / Fundamentals of Data Structures (FDS) Assignments (2019 Pattern)
Youtube DSL / FDS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&si=u12IYwo93Z7RU4e8

Problem Statement:
Group-B\Q14.py
Write a pythonprogram to store first year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using
a) Selection Sort
b) Bubble sort and display top five scores.

Explaination Video Link: https://www.youtube.com/watch?v=hYzQO5Jkn74&list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&index=11&pp=iAQB
"""


def selection_sort(a):

    # O(n^2)

    for i in range(len(a) - 1):
        min_index = i
        for j in range(i, len(a)):
            if a[min_index] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]

        print(a)


def bubble_sort(a):

    # O(n^2)

    for j in range(len(a)):
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
            print(a)


a = [7, 5, 4, 9, 2, 10, 3]

print("Unsorted Array: ", a)
bubble_sort(a)
print("Sorted Array: ", a)
