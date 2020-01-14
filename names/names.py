import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open("names_1.txt", "r")
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open("names_2.txt", "r")
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# O(n ^ 2)
def defaultFunction():
    for name_1 in names_1:
        for name_2 in names_2:
            if name_1 == name_2:
                duplicates.append(name_1)


# O(n log n)
def bst():
    names_2_tree = BinarySearchTree(names_2[0])
    for name in names_2[1:]:
        names_2_tree.insert(name)
    for name_1 in names_1:
        contains = names_2_tree.contains(name_1)
        if contains:
            duplicates.append(name_1)


# O(n)
def dicts():
    # name_dict = dict.fromkeys(names_1)
    # name_dict2 = dict.fromkeys(names_2)
    name_dict = {}
    name_dict2 = {}
    for name in names_1:
        name_dict[name] = 0
    for name in names_2:
        name_dict2[name] = 0
    dupes = name_dict.keys() & name_dict2.keys()
    [duplicates.append(dupe) for dupe in dupes]


def norules():
    a = set(names_1)
    b = set(names_2)
    duplicates = a & b
    # duplicates = set(names_1) & set(names_2)


def compren():
    duplicates = [i for i in set(names_1) if i in set(names_2)]


# defaultFunction()
# bst()  # runtime: 0.11512303352355957 seconds
# dicts()  # runtime: 0.0046770572662353516 seconds
norules()  # runtime: 0.00410914421081543 seconds
# compren() #runtime: 3.0023200511932373 seconds


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

# def norules():
#     list(set(names_1+names_2))
