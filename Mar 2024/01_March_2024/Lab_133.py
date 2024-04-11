# How can we see syntax error?
try:  # Run this, and you will get IndentationError: expected an indented block after 'try' statement on line 2.
    # 1st it will give you IndentationError: that you don't have Indentation
    pass  # even if you fix the IndentationError then it will throw SyntaxError: expected 'except' or 'finally' block
    # Why syntax error because try always followed by the except
except Exception as e:
    print(e)

# IndentationError
# SyntaxError
# Value Error--> we have already seen in lab_132. It means when we add a different value.
# Zero Division error--> we have already seen in lab_132. It means when we divide something by zero.


# Exception with capital E is the parent for all the exception.
try:
    c = 10 / 0  # If I use c=10/0 --> We will get "Division by Zero" error.
except Exception as e:
    print(e)

# I can specifically mention "ZeroDivisionError" instead of "Exception"
try:
    c = 10 / 0  # If I use c=10/0 --> We will get "Division by Zero" error.
except ZeroDivisionError as e:
    print(e)

# Exception--> Parent for all the exception
# Good coding and Bad coding
# If we know the exception which can come, use that specific exception.
a = int(input("Enter a number only\n"))  # ValueError-> with experience, we will get to the exception.
# If we use "Exception"--> Bad Coding experience

try:
    a = int(input("Enter a number only\n"))
except ValueError as v:  # I can use both of exception "specific" and "parent".
    print(v)
except Exception as e:  # There can be a problem which I have no idea, then I can mention 2nd exception also with Exception.
    print(e)
# I have use both of them. First I will use smaller basket. If this basket will not able to handle then it will be
# handled by big basket i.e. big "Exception".
