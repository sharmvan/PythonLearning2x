# Match case
# Match is similar to switch.
# This is a program to guess the number from 1 to 6. Which number you have selected
# It is inbuilt conditions.
numbers = int(input("Enter a number 1 to 6:\n"))
match numbers:
    case 1:  # No need to mention break in this case like JAVA. Break will automatically happen for you.
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case 3:
        print("You have entered 3")
    case 4:
        print("You have entered 4")
    case 5:
        print("You have entered 5")
    case 6:
        print("You have entered 6")
    case _:  # This is default case in case nothing matches
        print("No idea")
