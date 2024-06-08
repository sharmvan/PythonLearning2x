class employee:
    def __init__(self, fname, lname, age):
        self.name_1 = fname
        self.name_2 = lname
        self.age = age

    def greet_person(self):
        print("Hello, Welcome to this world", self.name_1, self.name_2)


emp1 = employee("Vandana", "Sharma", 100)
emp2 = employee("Anushka", "Sharma", 50)
print(emp1.name_1)
print(emp2.name_1)
emp1.greet_person()
emp2.greet_person()
