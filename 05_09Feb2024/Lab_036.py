x = 10
y = 20
if x > y:
    print("x > y")
elif x < y:
    print("x < y")
else:
    print("both are equal")

a = 10
b = 45
x = 10
y = 67
result = (a > b) and (x < y)
print(result)

# we can also solve this with below:
result1 = a > b
result2 = x < y
f_result = result1 and result2
print(f_result)
