# filter():
# It can filter the items from the list based on the logic.
# It returns less number of items.
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want to get only even numbers.
# To get all even numbers, we need to use filter. Also, we can one linar function i.e. lambda.
# if num (It can be num, x anything) is divide by 2 and that num is from which list? number list.
# x ix just alias. This can be anything.
even_number = list(filter(lambda x: x % 2 == 0, number))
print(even_number)

# Instead of lambda function, we can use function also.
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def even_num(num):
    return num % 2 == 0


result = list(filter(even_num, number))
print(result)

# Also, If we know it's a one linear we can convert above function in one line also by using lambda.

# Example list
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers using lambda function
even_number = list(filter(lambda x: x % 2 == 0, number))

# Print even numbers
print(even_number)
