"""
Range is built in function
It generates the sequence of numbers.
"""
# till now, we have used below:
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # which consumes a lot of memory
for x in list_1:
    print(x)

# instead of using above, we can use below:
for x in range(1, 11):
    print(x)

for x in range(1, 11, 3):
    print(x)
