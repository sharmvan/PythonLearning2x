# Encapsulation: It means whatever the data members or class variables and functions or methods we have,
# they are closed within a single blueprint/class.
# or we can say in alternate way: wrapping or binding the data variables with the methods
# Encapsulation we are already doing.
class car:
    name = None  # class/data variable

    # password = "123" # This is bad practice. To access the password, in method we will make it as private by using __

    # 3 different types of data members/class variables.

    # def __init__(self, name):  # initialize constructor
    #     self.name = name
    def __init__(self):
        self.public_var = 'Public'  # Public--> Anyone can access it.
        self._protected_var = 'protected123'
        self.__private_var = 'pass@123'
        self.__password = "pass@123"  # Instead of above metioned bad practice, we can access this by making as private. This is a

    # special type of function. Advantage is : this is not allowed outside.

    # by using different methods, we can access protected and private variables.
    def _protected_method(
            self):  # Protected method with 1 underscore. Underscore is mandatory. rest name can be anything.
        print("Protected!")

    def __private_method(self):  # Protected method with double underscores.
        print("Privated!")

    # Note: In Python, don't use underscore randomly in the class methods as they have special meaning. for eg: __init. It is a
    # private constructor of class: car. We can't call __init method as this is private in nature.
    def printname(self):  # Normal Method/Functions
        print(self.name)  # car("XUV car") will be used by this method.

    def printname1(self):
        print(
            "I am allowed to use the private variable because I am in the class" + self.__password)  # This is called encapsulation.


# xuv = car("XUV car")  # This value will be changed with "def __init__(self, name)"
# xuv.printname()

# lambo = car("Lambo car")
# lambo.printname()
# Note: In the above program, we are binding the data variables and Functions together.

# If I try to print below, it will get printed:
# print(xuv.name)

# Encapsulation means this is your data variables, this is your functions in a single class but every variable should
# not be available outside. for eg: I have password as a data variable which should not be allowed outside.
# Anyone can print my password. but here we can see it's allowed
# print(xuv.password)
# Encapsulation was used so that we can bind the data variables and methods. Reason of biding is to hide the important
# variables like password I want to hide. Nobody should have access.
# In this case, they have introduced 3 different types of data members/class variables.
xuv = car()
print(xuv.public_var)  # we are able to access the public variable outside.
# print(xuv.) # but we are not able to access private and protected variables outside. They are not available. So, we have
# successfully encapsulated the data members.
# Question is: How to access Protected and Private variables? we have these variables as hidden right now but there is a way
# how we can access them. --> by using different methods, we can access them.

# Official definition of Encapsulation is that whatever the data variables are there and whatever the functions are there
# in the calss, those variables/data members should not be allowed to access directly. Only public variable should be allowed.
# print(xuv.password)  # we should not be able to access this password.
# print(xuv.__password)  # with __password, it is not coming with . because this is not allowed outside as this is private
# in nature and properly encapsulated.
# but without constructor method, simple method i.e. printname1 is allow to access private variables.
print(xuv.printname1())
