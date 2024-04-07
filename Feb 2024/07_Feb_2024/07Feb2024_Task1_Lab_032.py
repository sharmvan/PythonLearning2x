# Que1: Explain the difference between the = (single equal) operator and the == (double equal) operator in Python.
# VS_Ans:
# Single Operator i.e. = is used for when we provide value to some variable.
# for eg:
a = 10
print(a)
# Double equal i.e. == is a comparison operator to compare values.
# for eg:
b = 20
print(a == b)
# PD_Ans:
# Single equal basically means assignment. We assign some value. It doesn't return anything.
# It just assigns the value.
# For eg:
a = 10
b = 12
# Double equal is comparison operator which compares the value. It returns boolean i.e. True and False only.
# For eg:
result = (a == b)
print(result)


# Que2: What does the ** operator do in Python, and how is it used?
# VS_Ans: it's an Arithmetic operator which is used for power.
# For eg:
x = 10
b = 2
print(b ** x)
# PD_Ans: It is basically a power operator.
# For eg:
print(2**3)


# Que3: What does the ^ operator do in Python, and in what context is it commonly used?
# VS_Ans: This operator will convert into binary operator and give the result
# For eg:
x = 5
y = 4
print(x ^ y)

x = True
y = False
print(x ^ y)
# PD_Ans: this (^) is bitwise XOR operator. Means If both the values are False then result is False. If both values
# are True then result is False. Rest of them It will be True. This use in electronics and communication only.
a = True
b = False
print(a ^ b)
