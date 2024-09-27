"""Write a python program to store names and mobile numbers of your friends in sorted 
order on names. Search your friend from list using binary search (recursive and non-recursive). 
Insert friend if not present in phonebook"""


def binary_search_nr(a, key):
    l = 0
    h = len(a) - 1

    while l <= h:
        mid = (l+h)//2
        # print(l,h,mid)

        if a[mid][0] == key:
            return mid
        elif a[mid][0] < key:
            l = mid + 1
        elif a[mid][0] > key:
            h = mid - 1

    a.append((key, -1))
    return len(a)-1


def binary_search_r(a, key, l, h):
    if l <= h:
        a.append((key, -1))
        return len(a) - 1

    mid = (l + h)//2
    if a[mid][0] == key:
        return mid

    elif a[mid][0] < key:
        l = mid + 1
        return binary_search_r(a, key, l, h)

    elif a[mid][0] > key:
        h = mid - 1
        return binary_search_r(a, key, l, h)


array = [("a", 10), ("aa", 17), ("ad", 89), ("ai", 1),
         ("as", 87), ("aw", 90), ("az", 18)]

print(__doc__, end="\n\n")
index = binary_search_nr(array, "z")
print("Binary Search recursive - ", index, array[index])

index = binary_search_nr(array, "z")
print("Binary Search iterative - ", index, array[index])
