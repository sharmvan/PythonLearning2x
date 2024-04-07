class bankaccount:

    def __init__(self):  # default constructor created # __init (in double underscore) is also a private function.
        self.balance = 0  # Suppose initially we have zero balance.
        self.__private_var = 100

    def public_func(self):
        print(
            self.__private_var)  # There is one bad practice if you want to access private variable by using a public
        # function. This public function is within the vicinity. That's why it is able to access the private
        # variable. Now anyone has a key because of this public function. # Encapsulation means that your data
        # variables can be accessed only through functions. and we will tell you which function, not all the functions.
        # If it's a private function, we can't access.
        # If it's a protected function, we can't access.
        # If it's fulfill all the conditions, only then it's allowed.

    def deposit(self, amount):  # this is function public function called as deposit. you will give me the amount.
        self.balance = + amount  # whatever the balance you have I will add with the amount.

    def _withdraw(self,
                  amount):  # I have added one protected which is withdraw. we can withdraw a certain amount if we want.
        self.balance = - amount  # when someone withdraws we can subtract from the balance

    def __show_balance(self):  # show balance should be private. not everyone can see. who should see the balance?
        print("your balance", self.balance)

# Encapsulation says only one thing that private variables and protected variables can be access only through functions.
# Public variables can be access by everyone.
# if you want to access pramod's private toilet, you have to call function.
# if you want to access pramod's protective toilet, you have to call function.
# Function will decide it is allowed to access or not.

# In below case, this function i.e.,"if_you_are_auth" will decide if you are allowed to access the private things or not.
# We will not decide.
    def if_you_are_auth(self, flag):  # if you are authenticated, i will send a flag.
        if flag:  # If flag is true,
            self.__show_balance()  # then you are allowed to see the balance
        else:
            print("Not allowed")

    def do_with_by_bank_manager(self, amount):  # Bank manager can also withdraw.
        self._withdraw(amount=amount)  # bank manager is within the class. So, he can call protected function also.
# amount=amount-- This is just to showcase. we can also do the same thing self._withdraw(amount). In the functions, we can also give
# arguments=arguments. we can give default arguments in functions.

bank = bankaccount()
bank.deposit(1000)  # via a public function, anyone can deposit
# bank._withdraw()  # I can't withdraw (Protected)
bank.do_with_by_bank_manager(999)  # Only bank manager can withdraw because it is protected in nature
# bank.__show_balance # I am not allowed to see the balance.
bank.if_you_are_auth(True)  # only called if you are authenticated. this is a private function.
# bank.if_you_are_auth(False) # not allowed.
bank.public_func()  # This public function is within the vicinity

# We have encapsulated the functions means "deposit" is a public function. Anyone can use it.
# But python is very lenient in nature. Still we can access a couple of private variables.
# there is one bad practice if you want to access private variable by using a public function.
