# Another example of Hierarchical Inheritance:
class Father:
    def home(self):
        return "this is father"


class son_1(Father):
    pass
    # def home(self): # If son_1 doesn't have function then it will call father's home.
    #     return "this is son_1 home"


class son_2(Father):
    def home(self):
        return "this is son_2 home"


Son = son_1()
print(Son.home())  # It will always call son_1 home. If son_1 doesn't have function then it will call father's home.
