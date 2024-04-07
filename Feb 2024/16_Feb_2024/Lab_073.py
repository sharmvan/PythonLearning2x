# Let's do one more example with map() Find cube root for the element in the list map() is created for : list, set,
# tuple, dictionary especially when we have a couple of elements. map() is created when we have list of items. We
# have list of items in list, set, tuple, dictionary. They contain a bunch of items. String is not a bunch of item.
# String is only one item.
import math


def cube_root(num):
    return math.cbrt(num)
    # return math.sqrt(num)


my_list = [1, 3, 5, 7, 9]
# If we want to cube root of all the list, we need to execute "cube_root" function on my_list
result = list(map(cube_root, my_list))
print(result)
