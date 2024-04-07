# String Concatenation
str1 = "Hello"
str2 = 'World'
print(str1 + str2)

# for space
print(str1 + '\t' + str2)

name = 'Vandana'
age = 96
# print(name + age) # TypeError: can only concatenate str (not "int") to str [Different data type, we can't concatenate]
# We can fix this problem by converting int to str by using str function. This is called kind of type casting
print(name + str(age))

# for space
print(name + '\t' + str(age))

# += is also an operator. This is same as a=a+"World". We can write in both ways either a=a+"World or a += "World"
a = 'Hello'
a += "World"
print(a)

# increment (++) and decrement (--)operator
x = 5
x += 1
print(x)

y = 6
y -= 5
print(y)

# There is no pre-operators and post-operators in python like below. These operators used in JAVA only.
# we have to use x=x+1 or x+=1
x = 10
y = ++x
y = --x