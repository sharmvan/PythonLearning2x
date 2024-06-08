# used to iterate block of code as long as test expression is true.
# test expression is checked first, if expression is evaluated true then body of loop will execute.
# conditions are used to stop the loops.
# can iterate on list, strings, tuples, dictionary

# Syntax of while loop-
# while test_expression: -- while is a keyword and test expression will be evaluated prior to getting into body of the loop.
#    body of while loop

# i = 0
# while i <= 100:
#     print(i)
#     i += 1
#     print("inside the loop")
# print("out of loop")

# city = 'London'
# i = 0
# while i <= len(city):
#     print(city[i])
#     i = i + 1

list_1 = [10, 20, 30]
print(len(list_1))
i = 0
while i < len(list_1):
    print(list_1[i])
    i = i + 1
