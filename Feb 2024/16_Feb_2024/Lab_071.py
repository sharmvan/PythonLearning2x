# Suppose I have a below list:
my_list = [1, 2, 3, 4]
# and I want to double each element. we will use for loop.
# first create empty list.
d_list = []
# Does the syntax of for loop change as per the requirement?
# No, for loop is basically means i in any list. If we use range, range(1,10) is also a type of list.
# We can convert that in list also. Both (list &  range) will work with for loop.
for i in my_list:
    # Whatever item I have picked, I have to double it and storing in temp variable, and then I am appending.
    # append means it will keep adding/append in the end.
    temp = i * 2
    d_list.append(temp)
print(d_list)

# If we're done with above-mentioned way, this is too long process. There is a way in very short form.
# We can use lamda
my_list = [1, 2, 3, 4]
d_list = lambda x: x * 2  # But each element we have to make it double in this case. lambda works like a function.
# How we should use it?
d_list(1)  # not possible to use it.

# We can use something a very logical thing. and above program will work in a logical manner way.
# We will use Map() function.

