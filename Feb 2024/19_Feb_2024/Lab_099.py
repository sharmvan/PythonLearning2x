# Multiple parameters class
class mul_para:
    name = 'Vandana'  # class variable. And also instance variable because we can access this by using self.name
    # through instance only. All the variables which are kind of class variables, they are instance variables.
    # This name is available throughout the class then it's a instance variable.

    def print_info(self, last_name, age):
        a = 10  # Local variable and it's scope will be in this method only.
        # This isn't instance variable because this a is available only in this method.

        print("My name is", self.name, last_name, "and my age is",
              age, '.')
        # self is not mandatory with last_name and age in this case as these are normal arguments,
        # and we can access arguments directly
        # If we have added 'name' only as a data member/class variable in class then self would be used.

    print(a)  # we can't access the value of "a" here because it's locally available within above "print_info" function.


multiple_parameters = mul_para()
multiple_parameters.print_info(last_name='Sharma', age=65)

# Note: We cannot map single object to multiple classes.
# One class can have multiple objects.
# One object will have one class.

