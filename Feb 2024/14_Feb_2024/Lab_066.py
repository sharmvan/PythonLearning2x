# sorting is not allowed on heterogeneous data (different type of data)
# sorting is allowed on homogeneous data (same type of data)

# sorting_with_diff_data_types = ["Vandana", 100, 56.89]
# sorting_with_diff_data_types.sort()
# print(sorting_with_diff_data_types)  # TypeError: '<' not supported between instances of 'int' and 'str'

sorting_with_same_data_types = ["Vandana", "Sharma", '56.89']  # this list contains strings only
sorting_with_same_data_types.sort()
print(sorting_with_same_data_types)
