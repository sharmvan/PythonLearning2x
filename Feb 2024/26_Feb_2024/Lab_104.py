# Till now we have two type of concepts and where it will be used?
# This concept will be used when we will work on Selenium web automation.
# In Selenium, every page that we are going to automate. For eg: we have VSO application, and we want to log in.
class VWOloginpage():
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def loginconfirm(self):
        if self.password == "Pass123":
            print("you are allowed to enter")
        else:
            print("Invalid User")


amit = VWOloginpage("amit.amit@gmail.com", "123")
amit.loginconfirm()

print("______")

pramod = VWOloginpage("pramod@gmail.com", "Pass123")
pramod.loginconfirm()

# By using the Parameterized constructor, we can set the value of correct
# email and password whatever the class variable we have and parameterized constructor will help you to set
# the value of class variables based on the object.
# for amit, the value of email and password is different.
# for pramod, value of email and password is different.
# even the "loginconfirm" is also different.
# but they created with same class. the blueprint to create objects i.e. amit and pramod is same.
# If we want to see these are really different. you can check by using a function i.e. id
print(id(amit))
print(id(pramod))
# id means their location where they are stored. even there references are different.
# amit is available at 2387866934624
# pramod is available at 2387866934672

