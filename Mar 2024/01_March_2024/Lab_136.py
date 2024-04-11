# Custom exceptions:
# Custom Exception should inherit from the "Exception" class. We can create Custom exceptions by using
# inheriting a class i.e. Exception
class MyCustomException(Exception):
    # We can call this init method.
    def __init__(self, message):  # This is the message you want.
        self.message = message  # "self.message" means what is the message you want? Whatever the message we send,
        # it will be = message
        super.__init__(message)  # I want to call a message by using super function. We have to use super because we
        # have to call the message of exception.


# super means "MyCustomException" parent i.e.Exception. Whatever the message you are telling via
# "def __init__(self, message):", this message will pass to "super.__init__(message)--Exception constructor".
# It is getting passed to the exception constructor.

balance = 100  # Suppose I have 100rs balance.

# Somebody wants to withdraw amount. so, I can ask user, How much you can withdraw?
withdraw_amount = int(input("Enter the amount you can withdraw\n"))
if withdraw_amount > balance:  # What is the maximum amount I can withdraw? If withdraw_amount is more than balance,
    # then you need to raise an Exception.
    raise MyCustomException("balance is low!!") # This message is getting passed to Exception constructor in this case.
else:
    print("Total after withdraw", balance - withdraw_amount)
