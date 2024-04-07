# Example of Multilevel Inheritance:
class grandparent():  # we have grandparent and they have a function.
    def grandparent_method(self):
        return "grandparent's method"


class parent(grandparent):  # we have parent and they have a function.
    def parent_method(self):
        return "parent's method"


class child(parent):  # we have child and they have a function
    def child_method(self):
        return "child's method"


# this is how the relationship is. in the () we give who is basically I am getting inherited.
# This is the reference of child object = child object I have created
# Child ref = child object()
Child = child()  # we have created a child object. reference of child object can access all 3 methods.
print(Child.grandparent_method())  # If I call "grandparent_method()" function, it will print "grandparent's method"
print(Child.parent_method())  # If I call "grandparent_method()" function, it will print "parent's method"
print(Child.child_method())  # If I call "child_method()" function, it will print "child's method"

# Parent ref = parent object()
Parent = parent()  # This parent reference can only access 1) parent and 2) grandparent methods and it doesn't know
# about child has his own function or not.
Parent.parent_method()
Parent.grandparent_method()

# Grandparent ref = grandparent object()
Grandparent = grandparent()
Grandparent.grandparent_method()  # Grandparent knows about his own method only.