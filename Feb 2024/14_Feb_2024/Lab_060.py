# We have seen multiple type of arguments. for eg: max which is a built - in function can take multiple arguments.
# We can pass arguments of any data type but max function won't work if we pass string.
r = max(1, 8, 9, 7, 5, 2, 1.56, 23.2)
print(r)
r1 = max("Vandana", 1, 8, 9, 7, 5, 2, 1.56, 23.2)  # TypeError: '>' not supported between instances of 'int' and 'str'
print(r1)
# Type conversion and data type compatibility we as a programmer have to maintain. Not python will maintain for us.

# **kargs-> This is called as "Keyword arguments" -> Will discuss with the "Dictionary" part.
# **kargs means key value pair like
name: "Vandana"
age: 65
state: Punjab


