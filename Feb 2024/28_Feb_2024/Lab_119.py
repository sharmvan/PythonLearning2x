# Example of hybrid Inheritance:
# Hybrid means multiple types of inheritance in one such as single, multiple, multilevel inheritance
class A:
    def methodA(self):
        return "methodA"


class B(A):
    def methodB(self):
        return "methodB"


class C(
    A):  # Here, Class C is getting from A and Class B is also getting from A then it's a "hierarchical" Inheritance.
    # means 1 parent and 2 children.
    def methodC(self):
        return "methodC"


class D(B, C):  # Here, Class D is getting from both parent B & C then it's a "multiple" Inheritance.
                # In this case, if we have same method in B and C then B will be call first as per MRO (Method Resolution Order)
    def methodD(self):
        return "methodD"


# Now, if we combine all of them then it becomes "Hybrid".
d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())
