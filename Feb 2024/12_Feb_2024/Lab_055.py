# Return type function
# how to make a return type function which should return something?
# we need to use "return" keyword
# define the function
def double_my_salary(num):  # 100 with replace with num. Variable also doesn't matter. It can be anything. we can use
    # name also instead of num.
    return num * 2  # 100*2


# Calling the function
result = double_my_salary(100)  # anyone can use this function
print(result)
result = double_my_salary(21.500)  # data type doesn't matter in this case. python interpreter will automatically
# convert into float.
print(result)
result = double_my_salary(5000)
print(result)
# The advantage that you see here is that you can pass anything at all.
