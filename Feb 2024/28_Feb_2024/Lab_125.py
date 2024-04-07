# Abstraction: Means Hiding the details and showing what is required.
# For eg: We have a car. do we know which wire is used to start the engine? No, we don't know.
# Whenever you drive a car, do we know how engine started? what is the internal structure of engine? No, we don't know.
# How gear box is managed? No, we don't know.
# This is called as Hiding the implementation and show only the important details by using the Abstraction.
# Abstraction can be done by 2 concepts: 1) Abstract Base class 2) Abstract Base Method
# In JAVA, Abstraction can be done by 1) Abstract class 2) Interface, but we don't have this concept in Python.
# In Python, Abstraction can be done by 1) Abstract Base class 2) Abstract Base Method
from abc import ABC, abstractmethod  # There is already a method know abc (Abstract Base Class) they have a created a class for us.


# From this abc class, we can import ABC and abstractmethod also.
# Let's create a class "Animal" and import ABC. Import means to use the leverage of abstraction. this: "class animal(ABC)" isclass animal(ABC):
# single inheritance. We inherited from class ABC which we imported from abc.
# To use the concept of abstraction, we have to inherit from ABC (imported) class.
class animal(ABC):
    def __init__(self,
                 name):  # --Abstraction means I have defined a parameterized constructor and I can write an incomplete method.
        self.name = name

    @abstractmethod  # an incomplete method which is by using the keyword @abstractmethod
    def sound(self):  # This is incomplete function. Who is going to complete this?
        pass


class dog(
    animal):  # If I create a class dog. dog inherited from animal. If we inherited from the animal, there is an incomplete
    # pass            # method known as sound. So we need to complete "Animal's class" method if we want to use "dog" class.
    def sound(self):
        return "bow bow"


class cat(animal):
    def sound(self):
        return "meow"


d = dog(
    "Rancho")  # If I try to create an object of dog class, it will throw an error like create a sound method for animal class first.
print(
    d.sound())  # TypeError: Can't instantiate abstract class dog without an implementation for abstract method 'sound' means
# We cannot create an object because it inherits from the animal and animal has an incomplete method.
# so, somebody has to write this method. if we see  @abstractmethod and if we inherit from Animal class, we need to give
# a full definition of "sound" function in dog class.
# Note: It means that any class who will get from animal, they have to give the definition of sound.
c = cat("cat")  # pass the name of the cat as a parameter
print(c.sound())

# Abstraction concept in python is very limited. It says that we can use "ABC" class and "abstractmethod" which we both
# imported from abc, we have to inherit to the class "animal", and "abstractmethod" we need to use which will be
# incomplete method in this case.



