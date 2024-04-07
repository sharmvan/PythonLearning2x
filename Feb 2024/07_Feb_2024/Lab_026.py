# Assignment operator: It will store the value of variable literal to the identifier.
name = 'Vandana'
age = 65
print(name)
print(age)

# Urinary operator:
age1 = 65
age2 = +65
age3 = -65
print(age1)
print(age2)
print(age3)

# Not operator - unary operator
is_married = True
print(is_married)
print(not is_married)

# is operator - Identity operator
a = 5
b = 5
print(a is b)
a = 5
b = 6
print(a is b)
a = 5
b = False
print(a is b)
a = True
b = False
print(a is b)

mylist1 = [1, 2, 3]
mylist2 = [1, 2, 3]
print(mylist1 is mylist2)

mylist1 = [1, 2, 3]
mylist2 = ['Apple', 5.6, 20]
print(mylist1 is mylist2)
