# Write a Python program to calculate the area of a circle given its radius using
# the formula area=π×r^2 ( Take pie as 3.14)
# VS_Ans:
r = int(input("Enter the value of radius:\n"))
pi = 3.14
print(pi * r * r)
# PD_Ans:
import math
print(math.pi)
radius = float(input("Enter the radius: "))
area = math.pi * pow(radius, 2)  # Base is radius, 2 is power
print(area)

# Create a program that takes two numbers as input and prints
# whether the first number is greater than, less than, or equal to the second number.
# VS_Ans:
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print(a > b)
print(a < b)
print(a == b)
# PD_Ans: It wil cover with conditions & loops chapter


# Develop a Python script that calculates the square and cube of a given number.
#VS_Ans:
a = int(input("Enter any number: "))
print(f"The square of {a} is:", a * a)
print(f"The cube of {a} is:", a * a * a)
# PD_Ans:
import math
num = float(input("Enter any number: "))
square = num ** 2  # To find the square
print(square)
sqrt = math.sqrt(2)  # To find the sqrt
print(sqrt)
# 1st way to find cube:
cube = num ** 3
print(cube)
# 2nd way to find cube:
cube1 = math.pow(num, 3)
print(cube1)
result = math.sin(90)
print(result)
