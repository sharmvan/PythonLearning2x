# Calculate the sum of two numbers by using function
def sum_of_4_num(a, b, c, d):
    return a + b + c + d


result = sum_of_4_num(5, 11, 2, 3)
print(result)
result = sum_of_4_num(5.6, 11.2, 2.3, 3.9)
print(result)
result = sum_of_4_num("Vandana", "sharma", "SAQ",
                      'Engineer')  # In string, concatenation happens whenever we do + operator
print(result)
result = sum_of_4_num('Vandana', 123, 'c', 42.3)  # TypeError: can only concatenate str (not "int") to str
print(result)
# Interesting thing is that we can use float numbers also. Python is very flexible.This can work with any type of
# data type.
# The advantage of python that same function without data type, we can use it.
