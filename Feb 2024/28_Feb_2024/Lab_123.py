# Method Overriding: means same function/method name in the parent and child. So, whoever object is created, only that
# function will be called.
# If you create an object of dog, dog's method will be called.
# If you create an object of Animal, Animal's method will be called.
# Child always override the parent functions
# Super means call my parent function
class animal:  # Create an animal class
    def __init__(self):
        pass

    def sound(self):  # Animal can create sound
        print("Animal sound!")


class dog(animal):  # create a dog class which will inherit from animal
    def __init__(self):
        super().__init__()

    def sound(self):  # dog also has a sound
        super().sound()  # We can call Animal sound as well, If we use a "super()" keyword,
        # super means my parent. who is my super?-> Animal (parent) in this case.
        print("Dog sound!")

    # Both classes have same function i.e. "sound"


# a = animal()  # if I create an object of animal class then which method it will call?
# print(a.sound())  # It will call Animal method.

d = dog()  # if I create an object of dog class then which method it will call?
print(d.sound())  # It will call dog method.
