# list: Collection of items (duplicate is allowed)
my_list = [34, 1, 8, 278, "Vandana", "Brazil"]
print(my_list)

# Indexing:
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
print(my_list[5])
# print(my_list[6])  # IndexError: list index out of range

# Changing an element:
my_list[2] = 'Australia'
print(my_list)

# append() means in the end, value will get added automatically. append means single item will get added only.
# If you append me, behind me.
my_list.append("Sharma")
print(my_list)

# extend() means you can add a list also to a list. Extend is list. It will extend by list.
my_list.extend("India")  # Result will come as a list. one more item added as a list
my_list.extend([500, 1000])  # Result will come as a list. 2 more items added as a list
print(my_list)

# insert() # Inserted value at index 1 as 'Punjab'.
# Now my list will become heterogeneous. It contains different type of elements.
my_list.insert(1, 'Punjab')
print(my_list)

# remove() # I am removing "I" from the list
my_list.remove("I")
print(my_list)

# copy() # We can opy the list by using copy() method. It will create a copy of the list.
copy_my_list = my_list.copy()
print(copy_my_list)

# clear() # clear basically means gone but the copy of list will still present after performing clear method also.
# because we have take up the backup.
my_list.clear()
print(my_list)
print(copy_my_list)

print("index of Australia in the list:", copy_my_list.index("Australia"))

# sort() # sorting is possible if list contains all str values or int values
# in both (int and str type of list) cases, it will throw an error:
# TypeError: '<' not supported between instances of 'str' and 'int'
# sorting is not allowed on heterogeneous (different type) data. It allows on homogeneous (same type of data) data.
# copy_my_list.sort()
# print(copy_my_list())

# sort() # we can sorting the list by using sort()
list1 = [450, 200, 8, 9, 7, 4]
list1.sort()
print(list1)
list1.reverse() # reverse() # we can reverse the list by using reverse()
print(list1)

