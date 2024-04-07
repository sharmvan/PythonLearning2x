def fun(name):
    print("Hi", name)


fun("Vandana")


# This is a function definition with return type function.
def fun():
    name = 'Vandana'
    return name


result = fun()
print(result)


# If we don't type "return" then it will return as "None" because this function is not returning anything.
def fun():
    name = 'Vandana'
    name


result = fun()
print(result)
