# There is a Condition
# age > 18 -> you are allowed to go the club
# age < 18 -> you are not allowed
# Now above condition can be converted into Python
age = int(input("Enter you age: "))  # This will return into string so, we need to convert int integer.
# We will use a syntax know as loop or a condition based which is if.
# if condition: -> return True or False
if age > 18:  # This should return True or False
    print("you are allowed to go the club.")
else:
    print("you are not allowed to go the club.")

# Can we do like this below? No because it's not a condition. It will throw an error as it's not a comparison operator
# if a=5: Single equal (=) won't work

# Correct way is to initialize the condition is:
a = 5
if a == 8:  # This is a comparison operator, and it will return True or False
    print("Hi")
else:
    print("bye")
