from math import pi


class AreaOfRectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def calculateareaofrectangle(self):
        return self.l * self.b


ar1 = AreaOfRectangle(20, 30)
print(ar1.calculateareaofrectangle())
ar2 = AreaOfRectangle(63, 51)
print(ar2.calculateareaofrectangle())

