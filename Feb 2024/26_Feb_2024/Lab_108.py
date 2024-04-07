# Real time example
class secure:
    def submit(self):
        self.__username = "admin"  # This is private variable
        self.__password = "123"  # This is private function
        self.heading = "VWO login"  # Heading is normal public.


s = secure()
s.heading # I want to show heading as publically.
# s.__password  # not to allow password as I want to hide it.
# s.__username  # not to allow password as I want to hide it.
