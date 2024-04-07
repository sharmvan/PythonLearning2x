# Lambda Expression: It is just to help us. It means we can convert any function in one-liner in python.
# This is just to save the length of the file.

# def greet():
#     print("Hello World!")
#
#
# greet()


# Above - mentioned is a simple function. let's take another below example.
# def double_my_salary(salary):
#     return salary * 2
#
#
# result = double_my_salary(10000)
# print(result)

# Above-mentioned program has multiple no. of lines, and we can convert into lambda expression by using below:
# result = lambda salary: salary * 2
# print(result(20))

# below more 3 examples with lambda functions:
pow = lambda num: num ** 2
print(pow(3))

sum_of_2_num = lambda x, y, z: x + y + z
print(sum_of_2_num(1, 2, 3))

my_name = lambda name, age: print(f"my name is {name} and I am {age} years old.")
my_name("Vandana", 90)
