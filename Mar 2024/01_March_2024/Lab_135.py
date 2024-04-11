class XYZ:  # Create a class
    def f1(self):
        try:
            a = int(input("Enter a number\n"))
        except Exception as e:  # bad coder
            print("Enter int only value of a")  # If we don't want to print e, we can use "enter int only".
        else:  # If there's no problem in this case, then use "else" block.
            print(a)
        finally:  # It will always get printed.
            print("Anyhow I will be printed")


x = XYZ()  # Create an object
x.f1()  # and call f1 function directly
