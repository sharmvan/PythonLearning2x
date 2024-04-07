# Example of Multilevel inheritance: Multilevel means when you have one or more. level1, level2, level3 or we can
# say grandfather, father & child relationship.

class GF:  # you have grandfather.
    def home(self):  # He has 5 BHK flat.
        print("5BHK")


class father(GF):  # Father inherit from the Grand father and My father doesn't have anything.
    def home2(self):  # if my father has home2 at Goa.
        print("GOA")


# class son(father):  # As a son, I am getting it from my father. and I also don't have anything.
#     pass
class son(father):
    def home3(self):  # if I have home3 at Bangalore.
        print("Bangalore")


pramod = son()  # Pramod is nothing but a son.
# pramod can access al of them.
# pramod.home()  # pramod can access his GF's home.because son gets from father and father gets from GF.
# pramod.home2()  # pramod as a son can access his father's home.
# pramod.home3() # pramod can access his own home.

myfather = father()  # myfather is nothing but a father.
myfather.home()  # myfather can access my GF's home.
myfather.home2()  # myfather can access his own home.
myfather.home3()  # myfather cannot access his son's home because till my father was present, he doesn't have idea that
# his son now has a home. Father can inherit from only GF. Not from the son.

mygf = GF()  # gf always has access.
mygf.home()  # he can access his own home.
mygf.home2()  # my GF can't access my father's home. GF can access only his home.

# the lower class will access all the properties of the class.
