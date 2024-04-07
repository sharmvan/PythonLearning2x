# Another example with *args
# without using for loop:
def make_pizza(*toppings):  # *toppings means list
    print(toppings)
    # for topping in toppings: # toppings is actually a range, kind of a list. So this list we can print by using the for loop.
    #     print(topping)


make_pizza("Maze")
make_pizza("Maze", "Mashroom")  # This will automatically replace with the list (*toppings)
make_pizza("Maze", "Mashroom", "Pineapple")  # This will automatically replace with the list (*toppings)
make_pizza("Maze", "Mashroom", "Pineapple", "Paneer")  # This will automatically replace with the list (*toppings)


# with using for loop:
def make_pizza(*toppings):  # *toppings means list
    for topping in toppings:  # toppings is actually a range, kind of a list. So this list we can print by using the for loop.
        print(topping)


make_pizza("Maze")
make_pizza("Maze", "Mashroom")  # This will automatically replace with the list (*toppings)
make_pizza("Maze", "Mashroom", "Pineapple")  # This will automatically replace with the list (*toppings)
make_pizza("Maze", "Mashroom", "Pineapple", "Paneer")  # This will automatically replace with the list (*toppings)

# Can we use same function with a and arguments in this case? Yes.
# For eg:
def make_pizza_base(*toppings, base):
    print(toppings, base)
    for topping in toppings:
        print(topping)


# We need to mention base properly otherwise it "thin" will consider as "toppings"
make_pizza_base("Maze", "Mashroom", "Pineapple", "Paneer", base='thin')


# Multiple * arguments are not allowed. Only one can be multiple. in this case, either toppings or base
def make_pizza_base(*toppings, *base):
    print(toppings, base)
    for topping in toppings:
        print(topping)