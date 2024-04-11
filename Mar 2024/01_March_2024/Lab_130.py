# In Python, we have very simple mecahnism to handle the exception. because if yoy are coming from JAVA.
# background, Exception is like lot of topics in the exception but it's very simple in python.
# If you want to handle any exception, you can use something called as "try" and "catch" block.
# In Python, we don't have "try" and "catch" block.
# we have "try" and "except" block in python.
# "try" means try the code but if there is an error, execute the "except" code if there is problem in try.
# So, how can we handle in this case?
# Let's understand with below example:
a = int(input("Enter no 1:\n"))
b = int(input("Enter no 2:\n"))

try:  # If there is an error, then we can use "except" in this case.
    c = a / b  # Here, we have problem at this line. so, we can put this into a "try" block.
    print("Division is:", c)
except Exception as e:  # After "except", we can basically give "Exception as e" and if we want we can print e also.
    print(e)
    print("Zero division, Please don't use B as zero!")  # This is the proper message I'm going to show to the user.
print("This is important message that we need to show user")  # This statement is outside as this is an imp message that
# we need to show to the user.

# Whatever the code, which gives certain kind of problems, we will add this into a "try" block. And whatever we want,
# we add into the exception block. When we will divide suppose 100/10. we won't get any red error but will get a
# proper message: which is "division by zero" which is coming from line no:16 -- print(e) and your personal message
# is also coming "Zero division, Please don't use B as zero!". Hence , now user will understand I don't have to use
# the zero as a value of B. And after this line no: 18 is also printed which is very important. In previous case,
# it was not executed.
