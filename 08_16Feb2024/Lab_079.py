x = 10  # Single assignment
x, y = 10, 20  # Multiple assignment
x, y, z = (10, 20, 30)  # We can assign in the tuple also
print(x)
print(x, y)
print(x, y, z)
# Nested Tuples/Nested list: Tuple inside Tuple/list inside list
x = ("London", "Japan")
y = ("Brazil", "China")
z = (x, y)
print(z)
print(z[0])  # We have 0 i.e. ('London', 'Japan') and
print(z[1])  # We have 1 i.e. (('Brazil', 'China') means there is a tuple inside tuple then how to print "london" only then Japan etc
print(z[0][0])
print(z[0][1])
print(z[1][0])
print(z[1][1])
# Search in Tuple: for search we can use "in" operator
Cities = ("Delhi", "Chennai", "Mumbai", "Kolkata")
print("Delhi" in Cities)
print("Moscow" in Cities)