# list.append(x)   Note: x=item and i=index
# list.insert(i,x)
# list.remove(x)
# list.pop(i)
# list.clear()
# list.index(x[, start[, end]])
# list.count(x)
# list.sort(*, key=None, reverse=False)
# list.reverse()
# list.copy()
cities = ['delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad']
print(cities)

cities.append('Goa')
print(cities)

cities.insert(1, "Lucknow")
print(cities)

cities.remove('Lucknow')
print(cities)

cities.pop(3)
print(cities)

print(cities.index("Amritsar"))

print("----------------------------------------")

cities = ['Delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad']
print(cities.count("Mumbai"))

cities.sort()
print(cities)

cities.reverse()
print(cities)

print("----------------------------------------")

cities = ['Delhi', 'Amritsar', 'Mumbai', 'Mumbai', 'Nagpur', 'Hyderabad']
print(cities)

new_cities = cities.copy()
print(new_cities)

new_cities.clear()
print(new_cities)

updated_list = new_cities.clear()
print(updated_list)

print(new_cities.clear())
