# Method Overloading: means same name of a function with different parameters
# Python doesn't support Method Overloading in the traditional sense.
# This concept is not there in python but what can we do? we can create a function. Let's understand by an example.
# Python doesn't support Method Overloading in the traditional sense.However, we can do overloading by using
# default parameters.
class MathUtil:
    def add(self, a, b=0, c=0):  # create a function with default arguments (b=0, c=0). It means Method Overloading
        # can be done by this also.
        return a + b + c

    # def add(self, a, b):  # We cannot create one more method with the "add" in python. This is not advisable in python as
    # Python doesn't support Method Overloading in the traditional sense.
    #     pass


mu = MathUtil()
print(mu.add(1))  # I can call "add" method with one parameter because b=0, c=0 are default values.
print(mu.add(1, 2))  # I can call "add" method with two parameters.
print(mu.add(1, 2, 3))  # I can call "add" method with three parameters also. This is the concept which is called in the
# Method Overloading
# In this example, I can call "add" function by 1 parameter, by 2 parameters and by 3 parameters because of
# default arguments.
