x = 'This is in single quotes.'
y = "This is in double quotes."
print(x)
print(y)
print(x[3])
print(x[4])
print(y[9])

a = 'This is in "single" quotes.'
print(a)
b = "This is in 'double' quotes."
print(b)
c = 'This is in \"single\" quotes.'
print(c)
print(c[11])
d = "This is in \'double\' quotes."
print(d)
print(d[12])

# how to define strings in multiline using triple quotes?
# if we don't assign that string to a variable, That becomes a comment and that can be ignored.
z = """This is multiline string"""
print(z)
print(z[3])

m = """This is a comment and we can ignore it."""

# If I want to see a particular word or the character is part of that string, we can use membership operator.
print('comment' in m)  # 'in' is a membership operator
print('comment' not in m)
