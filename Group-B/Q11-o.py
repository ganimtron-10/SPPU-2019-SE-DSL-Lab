"""Write a python program to store roll numbers of student in array who attended 
training program in random order. Write function for searching whether particular 
student attended training program or not, using Linear search and Sentinel search."""

print(__doc__)

stud_list = [10, 40, 45, 67, 89, 34, 56, 78, 73, 90, 1, 37]


def linear_search(l, key):
    # (3n + n)
    for i in range(len(l)):
        if l[i] == key:
            return i

    return -1


index = linear_search(stud_list, 87)
if index == -1:
    print("Student is not present (Linear Search)")
else:
    print("Student is present at position", index, "(Linear Search)")


def sentinel_search(l, key):
    # (2n + 7)
    last = l[-1]
    l[-1] = key
    i = 0
    while l[i] != key:
        i += 1

    if i != len(l) - 1:
        return i
    if last == key:
        return len(l) - 1

    return -1


index = sentinel_search(stud_list, 87)
if index == -1:
    print("Student is not present (Sentinel Search)")
else:
    print("Student is present at position", index, "(Sentinel Search)")
