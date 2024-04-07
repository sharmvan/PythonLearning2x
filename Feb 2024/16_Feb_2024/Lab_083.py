# Subset:
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}
print(set2.issubset(set1))  # is 2,3,4 (set2) subset of set1? Yes then result will be true
print(set1.issubset(set2))  # is 2,3,4 (set1) subset of set2? No then result will be false

# que1: What's the output of below?
set1 = set(['TheTestingAcademy', 'for', 'TheTestingAcademy.'])
print(set1)  # {"TheTestingAcademy", "for", "TheTestingAcademy."} due to .

for i in set1:
    print(i)

set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9,
            10, 11, 12, 13, 14, 15]) # All elements are unique.
print(set1)
set1.remove(5)
set1.remove(4)
print(len(set1))
print(set1)
