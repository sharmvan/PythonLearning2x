# Set: won't accept duplicate values. It accept unique value with unordered (not sorted values)
my_set = {1, 22, 33, 44, 56, 7, 7, 7, 56}
print(len(my_set))
print(my_set)

# We can create empty set by using the set function or by using the {} braces only.
e_m = {}
e_m1 = set()
print(e_m)
print(e_m1)

# Can we convert list into set? Yes
my_list = [1, 2, 5, 6, 8, 9, 10, 10, 10]
print(len(my_list))
print(set(my_list))
#
# Can we convert set into list? Yes
my_set = {4, 5, 6, 8, 9, 9}
print(len(my_set))
print(list(my_set))
