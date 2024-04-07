class myclass:
    def __init__(self):  # init function
        self.name = "Amit"  # access for name variable is public

    def publicfunction(self):  # This is also public function
        print("public function")

    def __private_fun(self):  # This is a private function
        print("This is private")

    def pub_fn_pri_fn(self): # this is a public function which can access private function because this function is within the class.
        self.__private_fun() # hence, this is allowed to access the private function. This is the concept of encapsulation which means
# if you are encapsulated in the class, you are allowed to access the private functions as well as private variables but above direct private
# functions are not allowed.

# Reason of using private and public function--> they provide security. and not everyone can access your variables and functions.


a = myclass()
# a.publicfunction()  # I can directly call the public function.
# a.__pr  # We can't access private. It's not allowed because private functions are always part of this class ans they are only allowed in the
# functions of class.
a.pub_fn_pri_fn()

