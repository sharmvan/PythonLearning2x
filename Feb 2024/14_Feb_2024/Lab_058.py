# *agrs and **args
# Suppose if we define function with 3 arguments and while calling just we are providing single value then it will throw an error.
# def sum(a, b, c):
#     return a + b + c
#
#
# sum(2)

# To overcome this problem, either we need to give default value, and we can use any values while calling the functions.
# def sum(a, b=1, c=3):
#     return a + b + c
#
#
# result1 = sum(2)
# print(result1)
# result2 = sum(5,2.5,1)
# print(result2)
# result3 = sum("Vandana", "Sharma", "True")
# print(result3)
# result3 = sum(c="Vandana", a="Sharma", b="True") # It will produce correct result but not recommended to maintain the order.
# print(result3)

# *agrs
# In the below, everytime we need to pass values while calling a function with same number of arguments.
# def sum(a, b, c):
#     return a + b + c
#
#
# result = sum(2, 3, 4)
# print(result)

# *args-> nothing but a list. Means any number of arguments, we can give multiple arguments and call them.
def print_arguments(*args):
    for i in args:
        print(i, end=" ")


print_arguments(1)  # With the help of args, we can call "print_arguments" function with 1 value
print_arguments(1, 2)  # With the help of args, we can call "print_arguments" function with 2 values
print_arguments("Vandana", "Sharma","Anjum")  # With the help of args, we can call "print_arguments" function with 3 values
print_arguments("True", "True", "True",
                "False")  # With the help of args, we can call "print_arguments" function with 4 values
print_arguments(1.42, 2.35, 8.96,6,5)  # With the help of args, we can call "print_arguments" function with 5 values
