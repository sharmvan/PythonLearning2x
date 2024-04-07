# Car-> can be a class
# Objects-> Tesla, Lamborghini
# Why we aren't creating objects in class?
# because if I give you blueprint of a building, are we going to make building in that blueprint? No not at all.
class car:
    name = None
    color = None
    model = None
    speed = None
    engine = None

    # self is a special variable that is used within the context of object-oriented programming (Oops)
    # It is reference to the instance of a class
    # We can use this to access and manipulate the attributes and methods of that instance/object.
    # different type of methods created below:
    def start_engine(self):
        print("Starting engine")

    def drive(self):
        print("Drive")

    def car_break(self):
        print("Break")

    def who_is_driving(self):
        print("I am driving", self.name)
        print("which is in color:", self.color)  # meaning of self is If we want to access variable: "name". This is a
        # instance of a class then we can use self with variable name. It is basically used myself name (variable_name)


# Creation of objects: Outside the class,
# Object reference = object
tesla = car()
lamborghini = car()

# everyone has different attributes
tesla.name = 'tesla'
lamborghini.name = 'Lamborghini'

# everyone has different attributes
tesla.color = 'Red'
lamborghini.color = 'Blue'

# everyone has different functions. This function i.e. "who_is_driving" is same in both of them.
# name of te function is same in both of them, but it behaves based on the reference.

# It behaves differently whenever we use tesla, this i.e. below
# def who_is_driving(self):
# print("I am driving", self.name) It will use the name of tesla.


# It behaves differently whenever we use Lambo, this i.e. below
# def who_is_driving(self):
# print("I am driving", self.name) It will use the name of Lamborghini.
tesla.who_is_driving()
lamborghini.who_is_driving()
