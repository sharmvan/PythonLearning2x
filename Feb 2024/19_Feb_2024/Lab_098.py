# program of calculator:
class calculator:

    def add_num(self, a, b):
        return a + b

    def sub_num(self, c, d):
        return c - d

    def mul_num(self, a, b):
        return a * b

    def div_mul(self, c, d):
        return c / d


obj_ref = calculator()
r = obj_ref.add_num(2, 5)  # same obj ref we can use to perform all operations.
r1 = obj_ref.sub_num(10, 20)
r2 = obj_ref.mul_num(5, 6)
r3 = obj_ref.div_mul(20, 10)
print(r, r1, r2, r3)
