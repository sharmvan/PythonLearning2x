# To create a class we need to type a keyword name as class, and then you can give a name.
# Whatever the class name that you give, the first letter of the class should be capital. That is advisable to everyone.
# and good practice that you should create it.
class Person:
    # Class Variables/Instance Variables.
    # empty class variables we cannot enter. For eg: empty name without assigning anything we can't enter.
    # We have to assign some value to them.
    # name = None
    name = 'Amit'  # If I assign "Amit", it will become hard coded. This value is hard coded which is a problem.
    # This value is same for all, both the objects.
    age = None

    # people generally add None value which basically means we have no idea. They have none value right now. None
    # means their value is empty as of now that we have. All theses are nothing but class variables/Instance Variables.

    def walk(
            self):  # We can have functions also. Self is nothing but instance of this ("Person") class to access
        # class variables.
        a = 10  # Local variable
        print("Hi, your name is:", self.name)
        print("Hi, your age is:", self.age)
        print(a)


# amit = Person()  # To create an object we need to use () with class name. It will create an object.
# amit.walk()
pramod = Person()  # If I create Person as pramod means If I create another object, then still It will say "your name is
# Amit".
pramod.walk()
# name = 'Amit' is hardcoded value means this value is for both the objects. This value is not getting changed based
# on the objects that we have created. And I want to change the values of class variables. If we want to change these
# values, then we have to use "Constructors".Constructors basically can change the values. How to use constructor?
# see next lab i.e.Lab_103.
