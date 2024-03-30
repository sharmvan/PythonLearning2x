# Multiple parameters class
class mul_para:
    name = 'Vandana'  # class variable

    def print_info(self, last_name, age):
        a = 10  # Local variable and it's scope will be in this method only.
        print("My name is", self.name, last_name, "and my age is",
              age, '.')
        # self is not mandatory with last_name and age in this case as these are normal arguments,
        # and we can access arguments directly
        # If we have added 'name' only as a data member/class variable in class then self would be used.


multiple_parameters = mul_para()
multiple_parameters.print_info(last_name='Sharma', age=65)
