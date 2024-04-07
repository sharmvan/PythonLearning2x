my_tuple = tuple(["Vandana", "Shweta", "Pooja", 123, 8.23, True, 'K'])
print(my_tuple[2])
print(my_tuple[5])

x = ("Delhi", "Punjab", "Chennai", "Bangalore", 'Hyderabad')
y = ("India", "Sydney", "Brazil", "China")
print(x[1])
print(y[2])
z = x + y  # Concatenation of the tuples
print(z)
print(list(z))

# Convert tuple to list. Yes we can convert by using "list" operator
my_tuple = (1, 2, 3)
print(list(my_tuple))
