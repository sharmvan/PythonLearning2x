# program of calculator:
class calculator:

    def add_num(self, a, b):
        return a + b

    def sub_num(self, c, d):
        return c - d


add_num_1 = calculator()
sub_num_1 = calculator()

r = add_num_1.add_num(10, 20)
print("Sum of 2 numbers is",r)

r1 = sub_num_1.sub_num(50, 40)
print("Subtraction of 2 numbers is",r1)
