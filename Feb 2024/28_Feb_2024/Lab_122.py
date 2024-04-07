# Polymorphism: Poly means-"Many", Morphism means-"Forms": Different forms Whatever the Object or Method we create,
# It tells you they can serve different purpose. Simple example to remember: I have Mother. For me, she is a mother.
# For my maternal uncle, she is sister. For parents, she is child. Hence, one person i.e. Mother, She has multiple
# roles in real life. Even I (Vandana) am performing a different roles. like: Sister, cousin, niece, Wife,
# Mentor. We all serve multiple purposes.
# Similarly, Object or Method that we create,they can also serve for multiple purpose.
# Same case is allowed in Polymorphism.
# There are 2 concepts: 1) Method Overloading 2) Overriding
# Example of Polymorphism:
class shape:  # Suppose we have shape class
    def area(self):  # In shape class, we have area
        print("Area of shape")  # And it will print the "Area of shape"


class rectangle(shape):  # Let's create a "rectangle" class which will inherited from shape.
    def __init__(self, length, width):  # It has a default private constructor.
        self.length = length  # It has length and width, and We have set length and width
        self.width = width

    def area(self):  # It also has a function/Method i.e. area.
        return self.length * self.width  # To calculate the area of ractangle.


class circle(shape):  # Let's create another "circle" class which will also inherited from shape.
    def __init__(self, radius):  # We have one more constructor, and we will give as radius
        self.radius = radius

    def area(self):  # Circle has also one more function/method known as "area"
        return 3.14 * self.radius * self.radius  # To calculate the area of circle.


rec = rectangle(2, 3)  # created an object of "rectangle" class and which "area" will be called?
print(rec.area())  # Automatically area will be called of "rectangle" class.

cir = circle(4)  # If I create another object of "circle" class, pass radius as 4 then which "area" will be called?
print(cir.area())  # Automatically area will be called of "circle" class.
# It means same function i.e. "area" behaves differently.
# If I create an object of rectangle, It gives an area of rectangle.
# If I create an object of circle, It gives an area of circle.
# It (area) has many forms. The name (area) is same but purpose is different.
# Name (area) remains same but purpose is different.
# when "pramod" is called at home then he is a brother.
# when "pramod" is called by wife then he is a husband.
# "Pramod" behaves different in both cases.
sha = shape()
print(sha.area())
# If "None" is getting visible in console. It means we print the message in console but didn't return anything.
