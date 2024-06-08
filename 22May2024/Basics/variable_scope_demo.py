# variable scope in python - boundary of variables within a program
# Local Scope
# Global Scope
# global keyword
# LEGB rule: Local -> Enclosing-> Global-> Built-in


# def fun3():
#     print(x)
#
#
# def fun1():
#     global x
#     x = 20
#     print(x)
#
#
# def fun2():
#     print(x)
#
#
# fun1()
# fun2()
# fun3()
x = 500


def parent():
    print(x)

    def child():
        print(x)

        def grandchild():
            print(x)

        grandchild()

    child()


parent()
