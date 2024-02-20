# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal),
# or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 = side 3

# My own solution:
side_1 = int(input("Enter 1st side of triangle: "))
side_2 = int(input("Enter 2nd side of triangle: "))
side_3 = int(input("Enter 3rd side of triangle: "))
if side_1 == side_2 == side_3:
    print("triangle is equilateral")
elif side_1 == side_2 or side_2 == side_3 or side_3 == side_1:
    print("triangle is isosceles")
elif side_1 != side_2 or side_2 != side_3 or side_3 != side_1:
    print("triangle is scalene")
else:
    print("Invalid Input")

# Pramod's solution:
side1 = float(input("Enter the side 1\n"))
side2 = float(input("Enter the side 2\n"))
side3 = float(input("Enter the side 3\n"))
if side1 == side2 == side3:
    print("EQ")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("ISO")
else:
    print("Scalene")



