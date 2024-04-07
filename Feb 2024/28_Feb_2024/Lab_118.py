# Example of Multiple Inheritance: 2 parent and 1 child
# we have father and mother. and son is getting everything from both.
class father(object):  # This is father # Object means father of all the classes. Hence, by default it is getting object.
    # If we write "(object)" or not, by default object is father of all the classes.
    def father_money(self):  # father's money
        return "5"

    def home(self):  # father has home also
        # print("this is from father") # lets change it to return instead of print.
        return "this is from father"


class mother:  # this is mother and mother also have same functions
    def mother_money(self):
        return "2"

    def home(self):
        # print("this is from mother") # lets change it to return instead of print.
        return "this is from mother"


class son(mother, father):  # son can get from both of them by using comma (,). Whatever we have inherited first,
    # That method will call first.
    # if we inherited father. It will return "This is from father".
    # If we do reverse, It will return "This is from mother".
    # pass -- if son has also the function/method.
    def home(self):
        return "this is from son"


Son = son()  # created son reference outside the class.
print(Son.father_money())  # If I call father's money, then output wil be 5
print(Son.mother_money())  # If I call mother's money, then output wil be 2
print(Son.home())  # If I call home, which will be call as both father
# and mother have a home? This is a confusion and a problem. this problem is not sorted by JAVA. If I run it,
# it will get confusion which one should I call and user will get None. but this problem is sorted in python.
# They have sorted like this: Whatever we have inherited first, That method will call first. This concept is calles as MRO.
# if we inherited father. It will return "This is from father".
# If we do reverse, It will return "This is from mother".
# MRO (Method Resolution Order): It says that whoever is the first inherited, that method will be call first.
print(son.mro())  # by using "classname.mro" function you will get an order. It will tell you what will be call first.
print(Son.home())
