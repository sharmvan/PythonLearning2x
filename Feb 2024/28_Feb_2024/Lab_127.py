# In filexyz we have 2 classes and 1 method, and we can call in other class also by
# using "from package(xyz) import (filexyz)"
from xyz import filexyz, utilis

a = filexyz.A() # We can directly use class A, and we can create an object for this.
a.print()

b = filexyz.B()

c = filexyz.C()
c.print()

utilis.vandana_read_excel()

# This concept basically means we can reuse the utilities.
# Suppose I will create an "utilis" file and in this file I will create a method.
# then I can directly import utilis and call the methods which comes under utilis.
# This is called as importing of the modules.




