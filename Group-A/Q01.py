"""
Aledutron
SPPU 2019 SE DSL Lab
SPPU Computer Engineering Second Year (SE) Data Structure Lab (DSL) / Fundamentals of Data Structures (FDS) Assignments (2019 Pattern)
Youtube DSL / FDS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&si=u12IYwo93Z7RU4e8

Problem Statement:
Group-A\Q01.py
In second year computer engineering class, group A student’s play cricket, group B students play badminton and group C students play football. Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton 
b) List of students who play either cricket or badminton but not both 
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.(Note- While realizing the group, duplicate entries should be avoided, Do not use SET built-in functions)

Explaination Video Link: https://www.youtube.com/watch?v=oKGftNwy3ZI&list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&index=3&pp=iAQB
"""

# https://excalidraw.com/#json=H9SeEjyjXXQVv8Sx-0mtU,hISpi8v4hePqOnAovl2wpg


def intersection(l1, l2):
    res = []

    for student in l1:
        if student in l2:
            res.append(student)

    return res


def union(l1, l2):
    res = l2.copy()

    for student in l1:
        if not student in l2:
            res.append(student)

    return res


def diff(l1, l2):
    res = []

    for student in l1:
        if not student in l2:
            res.append(student)

    return res


a = [1, 2, 3, 4, 5, 6, 7]
b = [2, 3, 6, 7, 9, 10]
c = [2, 4, 6, 8, 10, 12]


print(__doc__)

print(f"A = {a}\nB = {b}\nC = {c}\n")

print("a.", end=" ")
print(intersection(a, b))
# print(union(a,b))

print("b.", end=" ")
print(diff(union(a, b), intersection(a, b)))
# print(union(diff(b,a),diff(a,b)))


print("c.", end=" ")
print(diff(diff(c, b), a))

print("d.", end=" ")
print(diff(union(a, c), b))
