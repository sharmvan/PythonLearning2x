try:
    x = int(input("Enter 1st number "))
    y = int(input("Enter 2nd number "))
    if y == 0:
        raise Exception("The denominator is 0")
    print(x / y)
except Exception as e:
    print(e)
    print("In except block")
else:
    print("In else block")
finally:
    print("This will always executed")
