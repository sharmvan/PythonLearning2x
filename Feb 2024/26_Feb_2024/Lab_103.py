class car:
    # If we hardcoded this then all the objects will have a name = Lambo. This is what we don't want. In this case,
    # we can mention this as None.

    #     name = "Lambo"
    name = None
    make = None
    model = None

    # In this case, we will use a special function called as "init". init is basically initialization. This function
    # is a special function.

    # This (init) is a special function which will automatically called when object is created.
    # It means if I pass arguments like name,make,model,I can set the values of name, make, model (class variables) with
    # whatever the name that constructor has sent.

    # Non parameterized constructor. But in this case it will throw below error:
    # TypeError: car.__init__() missing 3 required positional arguments: 'o_name', 'o_make', and 'o_model'
    # Error says No, you need to use parameterized constructor. Hence, this empty constructor is not allowed.
    # def __init_(self):
    #     print("Hi I will be called when an object is created.")

    # This is called as parameterized constructors.
    def __init__(self, o_name, o_make, o_model):
        self.name = o_name  # =lambo
        self.make = o_make  # =v2
        self.model = o_model  # =2024

    def start_engine(self):
        print("Starting a car with the name: " + self.name)
        print("Starting a car with the make: " + self.make)
        print("Starting a car with the model: " + self.model)


# Here I can pass arguments which car I want to see. As per init method, it will take 3 arguments. The moment we
# create an object in line 30, method i.e. "def __init__" will get called automatically means the values of car(
# "lambo", "v2", "2024") will be available at def __init__(self, lambo, v2, 2024) and also available at the below:
# self.name = o_name = lambo, self.make = o_make = v2, self.model = o_model = 2024. This is the special property of
# constructor.
lambo = car("lambo", "v2", "2024")  # for this "lambo" reference, the values become like below
# self.name = o_name  =lambo
# self.make = o_make  =v2
# self.model = o_model   =2024
lambo.start_engine()  # If I call method start engine, then values will become like this:
# print("Starting a car with the name: " + self.name)  =lambo
# print("Starting a car with the make: " + self.make)  =v2
# print("Starting a car with the model: " + self.model)  =2024
print("-----------------------------------")
xuv = car("xuv", "v5", "2025")  # We have created 2nd type of object and for this "xuv" reference,
# the values become like below
# self.name = o_name  =xuv
# self.make = o_make  =v5
# self.model = o_model   =2025
xuv.start_engine()  # If I call method start engine, then values will become like this:
# print("Starting a car with the name: " + self.name)  =xuv
# print("Starting a car with the make: " + self.make)  =v5
# print("Starting a car with the model: " + self.model)  =2025
alto = car() # Non parameterized constructor. But in this case it will throw below error:
# TypeError: car.__init__() missing 3 required positional arguments: 'o_name', 'o_make', and 'o_model'
# Error says No, you need to use parameterized constructor. Hence, this empty constructor is not allowed.
# def __init_(self):
# print("Hi I will be called when an object is created.")
alto.start_engine()

# Note: In Python, if we are already using a parameterized constructor where you have all the parameters,
# then please use that only in this case.

