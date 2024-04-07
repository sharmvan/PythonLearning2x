# To create a function: step 1-> Define function, Step 2 -> Call the function
# How to define a function? by using "def" keyword
# Define-> Call
def say_hello():  # Non - return type function with no parameter/argument
    # Arguments means It doesn't take any inputs in this case.
    # write the code
    print("Hello")


say_hello()  # Calling part

def say_hello_arg(name):  # Non - return type function with parameter/argument
    # write the code
    print("Hello",name)


say_hello_arg("Vandana")  # Calling part
def say_hello_args(name, age):  # Non - return type function with parameter/argument
    # write the code
    print(f"Hello, my name is {name} and my age is {age}.")


say_hello_args("Vandana", 98)  # Calling part
say_hello_args("123", True)

def say_hello(name="Vandana"):  # Define function with default value then no need to pass the arguments while calling function
    # Arguments means It doesn't take any inputs in this case.
    # write the code
    print("Hello", name)


say_hello()  # Calling part

def say_hello(name):  # If we define a function with parameter and don't provide value while calling the function,
    # then it will throw an error: TypeError: say_hello() missing 1 required positional argument: 'name'
    # Arguments means It doesn't take any inputs in this case.
    # write the code
    print("Hello", name)


say_hello()  # Calling part TypeError: say_hello() missing 1 required positional argument: 'name'

def say_hello(name="Vandana"):  # : If I pass the value while calling a function, default value will get replaced with
# The passing value.
    # write the code
    print("Hello", name)


say_hello("Sharma")  # Calling part

# Return type function with arguments
def sum_number_argument_return(a, b):
    return a + b


result1 = sum_number_argument_return(7, 1)
print(result1)
result2 = sum_number_argument_return("Vandana", "Sharma")
print(result2)

# While calling the functions, Specifically we can mention for which argument I want to give the value?
def greet(name="Vandana"):
    print(f"Hello, my name is {name}.")


greet(name='Anjum')

