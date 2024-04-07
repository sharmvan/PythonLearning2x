# Tuple:
# Collection of items
# Immutable: We can't modify the data items
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[4])
print(type(my_tuple))
# my_tuple[0] = 14 # TypeError: 'tuple' object does not support item assignment
print(len(my_tuple))

# List:
# Collection of items
# mutable: We can modify the data items
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(my_list[0])
print(my_list[4])
print(type(my_list))
my_list[0] = 14
print(my_list)
print(len(my_list))

# can we convert list into tuple? Yes
my_list_1 = [100, 200, 300, 400, 500]
new_tuple = tuple(my_list_1)
print(new_tuple)
my_list_1[1] = 600
print(my_list_1)

# can we convert tuple into list? Yes but data items won't get changed.
my_tuple_1 = (100, 200, 300, 400, 500)
new_list = list(my_tuple_1)
print(new_list)
my_tuple_1[1] = 600 # TypeError: 'tuple' object does not support item assignment
print(my_tuple_1)