# set is an unordered collection with no duplicate elements. It doesn't accept duplicate items.
set1 = {10, 20, 30, 20, 30, 40, 50}
set2 = {"Vandana", "The Testing Academy", "40.23", "200"}
set3 = {100, "Vandana", 40.33, True}
set4 = set((100, "Vandana", 40.33, True))
print(set1)
print(set2)
print(set3)
print(set4)
print(type(set1))
print(type(set2))
print(type(set3))
print(type(set4))
print(100 in set4)
print("100" in set4)