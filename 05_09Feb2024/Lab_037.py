# Problem find the max between 3 numbers
# 1st way by using max function
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
print(max(num1, num2, num3))
# 2nd way suppose if we don't have max function
if (num1 > num2) and (num1 > num3):
    print(num1)
elif (num2 > num1) and (num2 > num3):
    print(num2)
else:
    print(num3)
