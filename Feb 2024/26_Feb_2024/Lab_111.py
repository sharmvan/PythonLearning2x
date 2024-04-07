# Inheritance means you get something from your father as well as your grandfather.
# Different types of Inheritance:

# Single Inheritance --> 80% we will be using this type of Inheritance in API & We Automation.
# Rest we will be rarely use, but it's important to understand.
# Multilevel inheritance
# Hierarchical inheritance
# Multiple inheritance
# Hybrid inheritance


# Example of Single Inheritance:
class father: # Suppose this is my father
    gold = 5  # Father has 5kg gold as a data variables and will be inherited by son also.  inheritance means you
    # can use the variables as well as functions.
    __private_villa = "GOA"  # Son won't be able to access it.

    def drive_car(self):  # my father has lambo car.
        print("lambo")

    def threebhkflat(self):  # he has 3bhk flat also.
        print("3BHK flat")

    # There is one condition If I want to allow private variables/functions by using encapsulation
    def private_villa_access(self, is_my_son):
        print(self.__private_villa)


class son(father):  # To inherit from father, in curly brackets, just need mention Father.
    pass


# Note: If I don't  add (father or inheritance) and just mention class son(),
# then son wouldn't able to access anything from father. Make sure you add inheritance in brackets like son(Father)

pramod = son()  # This is called single inheritance where son can access Father's properties.
# This is also called parent/sub (father) and child/super (son) class.
# Also known as
pramod.drive_car()  # pramod can drive the car. He doesn't have, but he inherited it from father. Pramod has nothing
# but his son. There is a relationship. it has inherited from the father.
pramod.threebhkflat()  # same explanation for 3bhk flat also.
# This is called as single inheritance. inheritance means you can use the variables as well as functions .
# The Properties and the functions can be accessed by the son object.
print(pramod.gold)
# pramod.__private_villa # Son wouldn't be able to access as private things of father will not be allowed to son.
print(pramod.private_villa_access(True))  # There is one condition If I want to allow private variables/functions
# by using encapsulation

print("----------")

myfather = father()
myfather.drive_car()  # Father can drive his own car.
myfather.threebhkflat()  # Father can use 3bhk flat.
print(myfather.gold)  # Father can use own gold also.
