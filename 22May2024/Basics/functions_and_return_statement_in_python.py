def add(x=5, y=10):
    print(x + y)


add()
add(20, 30)
add(40)
add(y=13)


def addition(x=5, y=10):
    return x + y


# Doc string
'''
This is the sample function of adding of 2 numbers
:param x: integer
:param y: integer
:return: It will return the sum of 3 numbers
'''

result = addition()
print(result)
print(addition())
