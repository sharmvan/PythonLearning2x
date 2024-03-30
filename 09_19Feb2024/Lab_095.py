# We have discussed Class and Objects in python.
# Class contains "Attributes/Data members" and "Behaviour/Member functions/Methods".
# If I want to create a "Person" class, and real world objects will be "Vandana", "Vani", "Amit"

# We should create a class first. Keyword should be class.
class Person:
    pass  # This is an empty class with pass. Nothing is there. No attribute, No behaviour then what is the point of
    # this class?


# If I create an object lets say "Vandana" = person(). Object is created when we type class name with () round
# brackets like a function(()).
# Vandana has no attribute. nothing is there.
# vandana = Person()
# vandana.

# It means we need to add something.
class Person:
    # Attributes is also called as "Data Members"
    name = None
    age = None
    phone_number = None
    id = None

    # Behaviour is also called as "Methods" (not the functions) because functions are something which aren't used in
    # the classes. Whenever a function is used in the class, It's called as "Method".

    # Self means that It's a own instance. Self will be the 1st argument of every method within the class.
    # Whenever we call any method with the instance variable, self will automatically have all their functions.
    # within the class "Self" will automatically call. Self basically means instance reference. It's not a keyword. It
    # refers to as instance of a class. Instance means creation of class.
    def talk(self):  # Methods are part of classes. Within classes, Methods remains not functions.
        print("I can talk")

    def sleep(self):  # Methods are part of classes.
        print("I am a Method")
        print("Sleep")

    def walk(self):  # Methods are part of classes.
        return "I am walking"


# This is another function.
def another():  # This is an independent function. Not a part of class. Functions can be independent.
    # Functions are not generally part of classes. This is the only difference between Functions and Methods.
    # If we create functions in class, they will become methods.
    print("I am a Function")


# object creation
# To create an object, we need to add classname followed by function (())
# difference between below 3 is:
vandana = Person() # This is different object
vandana.name = "My name is Vandana Sharma." # We have assigned a value and printing on the console. How they are store in memory?
print(vandana.name)
vandana.talk() # this belongs to Vandana.

anjum = Person()  # another function which is Anjum  # This is different object.

sonam = Person()  # Can we create unlimited number of objects? Yes. # This is different object.
# Nothing is there, So, clean the memory.
# Exit the program.