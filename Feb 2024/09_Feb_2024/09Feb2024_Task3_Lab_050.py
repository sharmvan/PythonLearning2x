# Fibonacci series
# 0,0+1, 0+1+1,
# n = 7
# 0, 1, 2, 3, 5, 8, 13 -- when we add last/previous 2 numbers
# a = 10
# b = 20
# a, b = a, a + b
# print(a,b)
# 0 1 1 2 3 5 8 13 21
a = 0
b = 1
while a < 10:
    print(a, end=' ')
    a, b = b, a + b
