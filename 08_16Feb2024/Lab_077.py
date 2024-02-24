# We can create empty tuple like below:
my_tuple_1 = ()  # empty tuple
my_tuple_2 = (1, 2, 3, 4, 5)  # We can also create tuple with the values
my_tuple_3 = list(my_tuple_2)  # We can also convert tuple into the list

# Tuple can be heterogeneous (it contains different data types values). This will convert list into tuple.
my_tuple_4 = tuple(["Vandana", 123, True, 93.2, 'V'])

print(my_tuple_1)
print(my_tuple_2)
print(my_tuple_3)
print(my_tuple_4)

del my_tuple_4  # We can also delete the tuple by using "del" function.
print(my_tuple_4)  # This will throw an error as we have already delete it. NameError: name 'my_tuple_4' is not defined. Did you mean: 'my_tuple_1'?
