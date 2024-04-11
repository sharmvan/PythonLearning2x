# One more concept i.e. try, except and finally
try:
    num1 = int(input("Enter 1st number:\n"))
    num2 = int(input("Enter 2nd number:\n"))
    result = num1 / num2
except ValueError as v:  # I've handled te "ValueError" which was getting appeared in "try" block
    print(v)
except ZeroDivisionError as z:  # there's one more error i.e. "ZeroDivisionError".
    # Both exceptions: "ValueError" and "ZeroDivisionError" we have added.
    print(z)
else:  # If both exceptions are not there then we can use else condition also.
    print(f"result is {result}")
finally:  # In the end, we can also add a block i.e. "finally"
    print("I will be executed anyhow!!")

# we know line no: 4 will create a problem if we divide something by zero.
# but instead of entering the number, if I enter string like "vandana" as a user,
# then this will also an error i.e. ValueError: invalid literal for int() with base 10: 'vandana' It means line no: 2
# has also an error because we're expecting an integer value but user can enter a string also.
# It means we have multiple problems in this case.
# We have 2 below errors in this case:
# 1.ValueError: invalid literal
# 2.Zero division error
# Hence, we will have multiple errors but how can we handle this? by using "try" and "except".


# After adding both exceptions, now we have handled this program very well. there are 2 types of problems
# we have figured it out i.e. 1.ValueError: invalid literal and 2.Zero division error
# So, what we need to do is:
# we need to put our code, whatever is the vulnerable code, we will put into try.
# then we will handle something called as "ValueError" which is our first error because instead of integer,
# if we put str, it will give you a value error.
# If this is not a value error suppose if somebody enters number as a zero in num2 then "z" will handle.
# --> if there is a problem in line 3 or line 4, then "ValueError as v" will handle.
# --> if there is a problem in line 5, then "ZeroDivisionError as z" will handle.
# --> if there is no problem in all 3 lines i.e. line 3,4,5 then "else" part will execute and result will be printed.
# --> And "finally" block will always be executed. This will always execute. There is no condition to execute this.


# Please Note: In this case, "finally" isn't mandatory, but it can be added. "finally" is something that we can always
# add.
