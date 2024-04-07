class password:
    # encapsulation is nothing but this variable i.e. ".__password" we want to hide and they will
    # only access through the functions.
    def __init__(self,
                 password):  # Created initialized constructor. Whatever the password you will give me, I will set with
        self.__password = password  # this = password. this is a private variable
        self.public_var = 10  # This is a public variable

    def get_password(self, is_auth):  # we can use get (or public function) function to access private functions.
        if is_auth:  # make sure, whenever you get, you are authenticated. means we have provided the security.
            print(self.__password)
        else:
            print("invalid password")  # Not everyone can access even by using the public functions.

    def set_password(self, password):  # we can use set (or public function) function to access private functions.
        if len(password) > 10:
            self.__password = password
            print("set to correct", self.__password)
        else:
            print("Not allowed,week password")


# Note: encapsulation says that whatever the variables that we have these variables can be access with the public
# functions. means this private variable i.e. "self.__password = password" can be access through public (get and set)
# functions. and we can restrict this functions. we have restricted them.

pas = password("123")
# print(pas.public_var)  # I can access public variable.
# print(pas.__password)  # I can't access private variable. encapsulation doesn't allow to access private variables.then
# how can we access private variables. encapsulation says you can use functions to access them. to GET them and to
# SET them. we can use some public functions. we can use getter and setters.
# print(pas.get_password(True))  # If you want to get the password, you have to be authenticated. only then you
# # will be able to get this.
# print(pas.get_password(False))  # If you are not authenticated, then you are not allowed.
print(pas.set_password("230@"))
print(pas.set_password("van45465545"))
