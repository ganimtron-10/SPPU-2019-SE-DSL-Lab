"""
Aledutron
SPPU 2019 SE DSL Lab
SPPU Computer Engineering Second Year (SE) Data Structure Lab (DSL) / Fundamentals of Data Structures (FDS) Assignments (2019 Pattern)
Youtube DSL / FDS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&si=u12IYwo93Z7RU4e8

Problem Statement:
Group-A\Q02.py
Write a Python program to store marks scored in subject “Fundamental of Data Structure” by N students in the class. Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency

Explaination Video Link: https://www.youtube.com/watch?v=WwJspzHmqEI&list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&index=4&pp=iAQB
"""

marklist = [10, 27, None, 94, 20, None, 67, 20, 10,
            94, 20, 89, 0, 90, None, 57, 28, 20, None, 90, 56]

# n = int(input("Enter Number of students: "))

# # Taking marks as input
# for i in range(n):
# 	mark = int(input(f"Enter Marks for {i+1} student: "))
# 	marklist.append(mark)

# print(marklist)

# Calculating Average
total = 0

# Calculate Max and Min
max_val = marklist[0]
min_val = marklist[0]

# Counting Absent Student
absent_student = 0

# Calculating Frequency
freq = {}

for mark in marklist:
    if mark == None:
        absent_student += 1
    else:
        total += mark

        if mark < min_val:
            min_val = mark
        if max_val < mark:
            max_val = mark

        if freq.get(mark) == None:
            freq[mark] = 1
        else:
            freq[mark] += 1


print(__doc__)
print(f"a. Average Score of the Class = {total/len(marklist)}")
print(f"b. Highest Score = {max_val} and Lowest Score = {min_val}")
print(f"c. Number of Absent Student = {absent_student}")

highest_freq = 0
highest_freq_mark = 0

for mark in freq:
    if freq[mark] > highest_freq:
        highest_freq = freq[mark]
        highest_freq_mark = mark

print(f"d. Mark with Highest Frequency = {highest_freq_mark}")
