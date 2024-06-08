# class rateofinterest:
#     def __init__(self, name, loan, interest):
#         self.name = name
#         self.loan = loan
#         self.interest = interest
#
#     def calculate_interest(self):
#         return self.loan * self.interest
#
#
# obj1 = rateofinterest("Vandana", 500000, 0.06)
# print(obj1.calculate_interest())
# obj2 = rateofinterest("Anushka", 400000, 0.06)
# print(obj2.calculate_interest())


# class rateofinterest:
#     interest = 0.06  # Class Variable
#
#     def __init__(self, name, loan):
#         self.name = name  # instance variable
#         self.loan = loan  # instance variable
#
#     def calculate_interest(self):
#         return self.loan * self.interest
#
#
# obj1 = rateofinterest("Vandana", 500000)
# obj1.interest = 0.2
# print(obj1.calculate_interest())
#
# obj2 = rateofinterest("Anushka", 400000)
# obj2.interest = 0.3
# print(obj2.calculate_interest())

# class rateofinterest:
#     interest = 0.06  # Class Variable
#
#     def __init__(self, name, loan):
#         self.name = name  # instance variable
#         self.loan = loan  # instance variable
#
#     def calculate_interest(self):
#         return self.loan * rateofinterest.interest
#
#
# obj1 = rateofinterest("Vandana", 500000)
# obj1.interest = 0.2
# print(obj1.calculate_interest())
#
# obj2 = rateofinterest("Anushka", 400000)
# obj2.interest = 0.3
# print(obj2.calculate_interest())

class rateofinterest:
    interest = 0.07  # Class Variable

    def __init__(self, name, loan):
        self.name = name  # instance variable
        self.loan = loan  # instance variable

    def calculate_interest(self):
        return self.loan * rateofinterest.interest


obj1 = rateofinterest("Vandana", 500000)
rateofinterest.interest = 0.9
print(obj1.calculate_interest())

obj2 = rateofinterest("Anushka", 400000)
obj2.interest = 0.15
print(obj2.calculate_interest())