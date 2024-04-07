t = ("TheTestingAcademy", "for", "TheTestingAcademy")  # Data type of t is tuple
print(t)
print(type(t))

# Can we convert tuple into set? Yes
print(set(t))  # Because it will accept only unique values.

# Set has a couple of features. For eg: Union, intersection, difference
# Union means all the items between set1 and set2.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.union(set2))  # they will be merged, concatenate
print(set2.union(set1))

# Intersection means common values
set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}
print(set3.intersection(set4))
print(set4.intersection(set3))

# difference means minus
set5 = {1, 2, 3, 4, 5}
set6 = {4, 5, 6, 7, 8}
print(set5.difference(set6))  # from the set5, remove the duplicates which are present in set6
print(set6.difference(set5))  # from the set6, remove the duplicates which are present in set5
