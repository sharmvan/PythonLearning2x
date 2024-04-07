# Example of Hierarchical Inheritance:
# Hierarchical means
class vehical():  # this is parent, and it has 2 children i.e. car and bicycle. like father and 2 sons
    # and they both have their own methods.
    def info(self):
        return "this is a vehicle"


class car(vehical):  # car is also a type of vehicle. 1st child
    pass
    # def info(self):  # Local function-> If car class doesn't have any method.function then it's object will call it's parent.
    #     return "this is a car"


class bicycle(vehical):  # bicycle is also a type of vehicle. 2nd child
    def info(self):
        return "this is a bicycle"


Car = car()  # I can create an object reference of Car.
Bicycle = bicycle()  # I can create an object reference of Bicycle
print(Car.info())  # If I call "Car.info()" method, which method will call? It will call car method i.e."this is a
# car" only because local functions always have the higher preferences. we have created object of "car" class at line
# no: 19. so, function will be called by only this information i.e.Car.info().

# If car class doesn't have any method.function then it's object will call its parent.
# it is similar to that for eg: I have 2 bhk flat and my father also have 2 bhk flat. I will say to my friend to use my 2bhk
# flat. he will use mine as of now. If I don't have, he will use my father's 2bhk.

