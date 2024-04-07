# Continue: means you want to continue.
# It's alternate of break.
# You don't want to break. You want to continue.
# Alternate way to find out even and odd numbers is continue.
for i in range(1, 11):

    if i % 2 == 0:  # from line no 7 to line no 9, code will be executed for even numbers.
        print("Even number", i)
        continue  # Continue is just a keyword to continue some conditions.

    print("Odd number", i)  # This code will execute for odd numbers. This statement is the part of for loop.
