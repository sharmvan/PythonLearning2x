# suppose I want to print: "Welcome to python class from the testing Academy."
x = "python class"
y = "testing Academy"
print("Welcome to", x, "from the", y, '.')  # traditional approach
print("Welcome to " + x + " from the " + y + ".")  # traditional approach
print("Welcome to %s from the %s" % ("JAVA Class", y), ".")  # Not recommended
print("Welcome to {0} from the {1}".format(x, y))
print("Welcome to {classname} from the {academyname}".format(classname=x, academyname=y))
print("Welcome to {classname} from the {academyname}".format(classname='Perl', academyname=y))  # more readable
print(f"Welcome to {x} from the {y}.")  # This is correct format method
