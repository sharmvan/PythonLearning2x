# add(elem) - Add element elem to the set.
# remove(elem) - Remove element elem from the set. Raises keyError if elem is not contained.
# discard(elem) - Remove element elem from the set if it's present.
# pop() - Remove and return an arbitrary element from the set.4
# clear() - Remove all elements from the set.

# Joining two sets
# union()
# update()

# keep only duplicates
# intersection()
# intersection_update()

# keep all excluding duplicates
# symmetric_difference
# symmetric_difference_update()

# Returns set containing difference between two or more sets
# difference()
# difference_update()

# issubset()
# issuperset()

cities = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad'}
print(cities)

cities.add("New York")
print(cities)

cities.remove("New York")
print(cities)

cities.discard("Nagpur")
print(cities)

cities.pop()  # set doesn't accept index value as set doesn't have any sequence.
print(cities)

cities.clear()
print(cities)

print("--------------------------------------------")

cities1 = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad'}
cities2 = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad', 'London', 'Cyprus'}
cities3 = cities1.union(cities2)
print(cities3)
cities3 = cities2.union(cities1)
print(cities3)

print("--------------------------------------------")

cities1 = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad'}
cities2 = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad', 'London', 'Cyprus'}
cities3 = cities1.update(cities2)
print(cities3)
cities3 = cities2.update(cities1)
print(cities3)
cities1.update(cities2)
print(cities1)
cities2.update(cities1)
print(cities2)

print("--------------------------------------------")

cities1 = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad'}
cities2 = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad', 'London', 'Cyprus'}
cities3 = cities1.intersection(cities2)
print(cities3)
cities3 = cities2.intersection(cities1)
print(cities3)

print("--------------------------------------------")

cities1 = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad'}
cities2 = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad', 'London', 'Cyprus'}
cities3 = cities1.intersection_update(cities2)
print(cities3)
cities3 = cities2.intersection_update(cities1)
print(cities3)
cities1.intersection_update(cities2)
print(cities1)
cities2.intersection_update(cities1)
print(cities2)

print("--------------------------------------------")

cities1 = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad'}
cities2 = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad', 'London', 'Cyprus'}
cities3 = cities1.symmetric_difference(cities2)
print(cities3)
cities3 = cities2.symmetric_difference(cities1)
print(cities3)

print("--------------------------------------------")

cities1 = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad'}
cities2 = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad', 'London', 'Cyprus'}
cities3 = cities1.symmetric_difference_update(cities2)
print(cities3)
cities3 = cities2.symmetric_difference_update(cities1)
print(cities3)
cities1.symmetric_difference_update(cities2)
print(cities1)
cities2.symmetric_difference_update(cities1)
print(cities2)

print("--------------------------------------------")

cities1 = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad'}
cities2 = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad', 'London', 'Cyprus'}
cities3 = cities1.difference(cities2)
print(cities3)
cities3 = cities2.difference(cities1)
print(cities3)
cities1.difference_update(cities2)
print(cities1)
cities2.difference_update(cities1)
print(cities2)

print("--------------------------------------------")

cities1 = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad'}
cities2 = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad', 'London', 'Cyprus'}
cities3 = cities1.issubset(cities2)
print(cities3)
cities3 = cities2.issubset(cities1)
print(cities3)

print("--------------------------------------------")

cities1 = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad'}
cities2 = {'delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad', 'London', 'Cyprus'}
cities3 = cities1.issuperset(cities2)
print(cities3)
cities3 = cities2.issuperset(cities1)
print(cities3)
cities1.issuperset(cities2)
print(cities1)
cities2.issuperset(cities1)
print(cities2)

print("--------------------------------------------")
