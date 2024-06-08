# 1.len(s): Return the number of items in an object, if object is string it will return the length of the string.
a = 'van san'
print(len(a))

# 2.str(): converts specified value into a String.
b = 123456
print(str(b))

# 3.find (sub[, start[, end]]): Searches the string for a specified value and returns the position. start and end are optional.
x = 123456789
# print(x.find("45"))  # AttributeError: 'int' object has no attribute 'find'
y = str(x) # The value of x which is int has been converted into str and str is an array. Array's index value starts from "0".
print(y.find("45"))
print(y.index("45"))

# 4.upper(): converts a string into upper case
x = 'vandana'
print(x.upper())

# 5.count(sub[, start[, end]]): Returns the number of items a specified value is found in the string. start and end are optional.
a = "The Testing Academy The Testing Academy The Testing Academy The Testing Academy The Testing Academy"
print(a.count("Testing"))
print(a.count("Testing", 5, 200))

# 6.isupper(): Returns True if all characters in the string are upper case.
x = 'vandana'
print(x.isupper())
y = 'VANDANA'
print(y.isupper())

# 7.islower(): Returns True if all characters in the string are lower case.
x = 'vandana'
print(x.islower())
y = 'VANDANA'
print(y.islower())

# 8.split(sep=None, maxsplit=-1): split() method in python is used to split the string into substring if it finds instances of the separator and give output as "list" of substrings.
# it splits the string at the specified separator and returns a list.
# If sep is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if
# the string has leading or trailing whitespace.
a = "The Testing Academy The Testing Academy The Testing Academy The Testing Academy The Testing Academy"
print(a.split())  # It will spilt the string on the basis of white spaces.

# 9.rsplit: splits a string into a list, starting from the right.
a = "&&^ The Testing Academy The Testing Academy The Testing Academy The Testing Academy The Testing Academy &&^"
print(a.rsplit("&&^"))

# 10.strip(): strip() method in python is used to remove whitespaces form the beginning or end of a string.
# it returns a trimmed version of the string.
a = "       ---*(&(*&*The Testing Academy The Testing Academy The Testing Academy The Testing Academy The Testing Academy  454       "
print(a.split())
print(a.strip()) # It will remove the whitespaces.
print(a.strip('---*(&(*&* \''))
print(a.lstrip('---*(&(*&* \'')) # lstrip([chars]): Remove any leading characters from the left side.
print(a.rstrip('---*(&(*&* \'')) # rstrip([chars]): Remove any trailing characters from the right side.

# replace(old, new[, count]): Replaces a specified phrase with another specified phrase
a = "       ---*(&(*&*The Testing Academy The Testing Academy The Testing Academy The Testing Academy The Testing Academy  454       "
print(a.replace("Academy","Strategy"))
print(a.replace("Academy","Strategy", 2))