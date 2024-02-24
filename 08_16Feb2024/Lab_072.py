# There is basically a Map() If we want ot work on every element. This function called as Map.
# This is a Map function not a Map. Map in JAVA that is key value pair. In Python, Map is a function.
# How to use this function?
# First lets say I have a function which will basically do double.
# def double(num):
#     r = pow(num, 2)  # we can use: r=num**2
#     print(f"The square of {num} is:", r)
#     return r
#
#
# result = double(2)
# print("returned value", result)
# ---------------------------------------------------------

def double(num):
    r = pow(num, 2)  # we can use: r=num**2
    # print(f"The square of {num} is:", r)
    return r


# Now Suppose I have some numbers in a list and for each item/number I want to execute double (function name)
# We can use for loop. But in this case, instead of using for loop, we can use Map().
# Map() means it will give you double of your numbers. It says that which function you want to apply for each number?
# Hence, in this program, name of the function is "double" with def keyword.
# Map() will pick one item from numbers list and it will execute as double
numbers = [1, 2, 3, 4, 5]
# Map()-
# - It takes each item from the list.
# - Execute the function on it.
# - Return same number of elements (list). Length will remain for the list.
result = list(map(double,numbers)) # 1,4,9,16,25-> This result will get displayed in the form of list and we
# converted into list.
print(result)
