# Till now, we have discussed "Core Programming", "OOPs" and "Exceptions"
# suppose there are 2 functions and how can we identify which one is main function?

def f1():
    print("f1")


def f2():
    f1()  # f2() is also calling f1() then I can run only f2() which will call both functions
    print("f2")


def f3():
    f1()
    f2()
    print("f3")


# f1()
# f2()

# if __name__ == "__main__":  # we can tell python interpreter which one is our main method by using this.
#     f2()
#     f1()
#     f3()
# Suppose all of them are not main function. only below one is my main function. Then we can specifically that main
# function is this and rest all of above functions are normal.
def main():
    print("main")


if __name__ == "__main__":  # -- is private method
    main()
