# Task - Factorial number
# Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24
# 1st way
num = int(input("Enter a number: "))
if num == 0 or num == 1:
    print(f"Factorial of {num} is", 1)
elif num < 0:
    print("Factorial is not applicable for -ve numbers")
else:
    f = 1
    for i in range(1, num + 1):  # (num+1) As it takes below 1 value like 1 to 8 it will print till 7 numbers
        f = f * i
print(f"The factorial of {num} is:", f)

# 2nd way
import math

n = int(input("Enter a number: "))
print(f"Factorial of {n} is: ", math.factorial(n))
