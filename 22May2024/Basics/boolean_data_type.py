# bool() is allowed to evaluate any of the value and return the boolean data type True or False.
# sometime in other languages, it will return 0 and 1 but in python, It will return True or False only.
# x = 10
# y = 5
# print(x > y)
# print(x < y)
#
# print(bool(x > y))
# print(bool(x < y))
#
# print(bool(x))
# print(bool(y))

a = 0  # F
b = 2  # T
c = ""  # F
d = "vandana"  # T
print(bool(a), bool(b), bool(c), bool(d))