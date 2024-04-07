# Python - Vast - Not all the functions are required to built your frameworks
my_dict = {'b': 2, 'a': 1, 'c': 3}
print(len(my_dict))
print(my_dict)

# If we want to find the item,like key or value exist or not then we can use: "for" loop or "in" operator
# 1st way with "for" loop:
for k, v in my_dict.items():
    if k == 'b':
        print("b is found")
    if v == 2:
        print("2 is found")
# 2nd way with "in" operator:
op = 'b' in my_dict  # in basically used for keys only
print(op)
op = '2' in my_dict  # in basically not used for values
print(op)
