class parent:
    def flat(self):
        print("Parent has 3 BHK flat.")

    def gold(self):
        print("Parent has 5Kg gold.")


class child(parent):
    def car(self):
        print("Child has Innova.")


c = child()
c.flat()
c.gold()
c.car()
# p = parent()
# p.flat()
# p.gold()

print("--------------------")


class parent_rateofinterest:
    interest = 0.07  # Class Variable

    def __init__(self, name, loan):
        self.name = name  # instance variable
        self.loan = loan  # instance variable

    def calculate_interest(self):
        return self.loan * self.interest


class child(parent_rateofinterest):
    interest = 0.02


s = child("Vandana", 500000)
print(s.calculate_interest())
