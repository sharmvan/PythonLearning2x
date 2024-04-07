# There are numbers in squares. So, how indexation is done?
squares = [1, 4, 8, 19, 23]
# index=[0,1,2,3,4]
# reverse indexation=[-5,-4,-3,-2,-1]
print(squares[0])
print(squares[1])
print(squares[2])
print(squares[3])
print(squares[4])
print("-----------")
print(squares[-1])
print(squares[-2])
print(squares[-3])
print(squares[-4])
print(squares[-5])
print(type(squares))

# how to check if list is empty?
my_list = []
if not my_list: # not means it's empty
    print("Empty list")
else:
    print("Not empty")
