# Multilevel inheritance
class GF:  # you have grandfather.
    def __init__(self):  # Constructors are automatically called.
        print("Automatically called when object is created")


class father(GF):  # Father inherit from the Grand father and My father doesn't have anything.
    def home2(self):  # if my father has home2 at Goa.
        print("GOA")


# class son(father):  # As a son, I am getting it from my father. and I also don't have anything.
#     pass
class son(father):
    def home3(self):  # if I have home3 at Bangalore.
        print("Bangalore")


pramod = son()  # in this case, I have just created a object and not calling the __init function but automatically it's called,
# when object was being craeted.
pramod.home2()  # But if we want to call function with home2 then we need to call it by using object.
