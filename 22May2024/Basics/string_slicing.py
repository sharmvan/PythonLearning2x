# string is an array in python so, we will use the indexes.
# s[i:j] - slice of s from i to j
# s[i:j:k] - slice of s from i to j with step k
# s[startindex:endindex:step]
s = "Welcome to The Testing Academy"
print(s)
print(s[0])
print(s[0:])
print(s[:])
print(s[:12])
print(s[0:9])
print(s[5:15:2])
print(s[-1])
print(s[23:])
print(s[-7:])
print(s[-7:-2])
print(
print(s[::-1]))  # To get a reverse string. :: means from starting from beginning to end but mention -1 to make it reverse.

s1 = "1234567891011121314151617181920"
print(s1[0:15:3])

# Suppose below are the 3 values with comma separated and i want to push in the Excel file by using slicing.
# delimiter means comma
s = 'name, age, city'
print(s.index(","))  # index of comma (,) is 4
print(s[0:s.index(",")])