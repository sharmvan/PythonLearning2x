# Dict: A dictionary is an unordered collection of data in a key value pair format.
name = 'Vandana'  # This is not a dictionary. This is a normal string.
# key-> name
# value-> Vandana

# How to create an empty dictionary:
# 1st way:
my_dict = {}  # with empty curly braces
print(my_dict)
print(type(my_dict))
# 2nd way:
my_dict1 = dict()  # with dict keyword and open brackets
print(my_dict1)
print(type(my_dict))

# Dictionary looks like below:
my_dict12 = {"name": "Vandana", "age": 96, "Contact_no": 789456122}  # keys will be in string format
print(my_dict12)
print(type(my_dict12))
print(len(my_dict12))
# How to get the value of keys?
print(my_dict12["name"])  # In this case, "keys" will be given as an index; not 0 , 1 something like that.
print(my_dict12.get("name"))  # by using get function

my_dict12 = dict(name="Vandana", age=96, Contact_no=789456122)
print(my_dict12)  # keys without double quotes which is also possible
print(len(my_dict12))

# How to get the value of keys?
print(my_dict12["age"])  # with double quotes
print(my_dict12['age'])  # with single quotes also possible and will produce the same result
print(my_dict12.get('age'))  # with get function and single quotes
print(my_dict12.get("age"))  # with get function and double quotes

# If we "dict" keyword then we don't need to use keys in the double quotes
vandana_details1 = dict(name='Vandana', age=34, isFemale=True, Address='KA')
# If we don't use "dict" keyword then we need to use keys in the double quotes
vandana_details2 = {"name": 'Vandana', "90": 34.34, "isFemale": True, "Address": 'KA'}

# None will get print as this was not a string, and it's searching for an integer value and 90 doesn't exist. string
# "90" exists. and we have to use double quotes to get the result.
print(vandana_details2.get(90))
print(vandana_details2.get("90"))

my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 95}
# len is 3 because keys can't be duplicate but values can be duplicate.
# Keys must be unique. It will pick last 'a': 95 not 'a': 1. a will replace with last.
print(len(my_dict))
print(my_dict)  # keys can't be duplicate but values can be duplicate.