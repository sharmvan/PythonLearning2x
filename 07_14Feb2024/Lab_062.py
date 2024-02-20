# Task : Factorial program by using the function
# default=1
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24
# 1st way
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     elif num < 0:
#         print("Factorial is not applicable for -ve numbers")
#     else:
#         f = 1
#         for i in range(1, num + 1):  # (num+1) As it takes below 1 value like 1 to 8 it will print till 7 numbers
#             f = f * i
#     print(f"Factorial of {num} is:", f)
#
# factorial(4)
# factorial(5)
# factorial(6)

# 2nd way
# import math
#
#
# def factorial(num):
#     print(f"Factorial of {num} is:", math.factorial(num))
#
#
# factorial(4)
# factorial(5)
# factorial(6)


# Fibonacci series program by using the function
# 0,0+1, 0+1+1,
# n = 7
# 0, 1, 2, 3, 5, 8, 13 -- when we add last/previous 2 numbers
# a = 10
# b = 20
# a, b = a, a + b
# print(a,b)
# 0 1 1 2 3 5 8 13 21
def fibonacci(num):
    return num


a = 0
b = 1
while a <= 300:
    print(a, end=' ')
    a, b = b, a + b

fibonacci(200)

