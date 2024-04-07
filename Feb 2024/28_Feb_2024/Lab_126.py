# In Real life, how we will use this abstraction method? What are the advantages of abstraction?

# We will import the methods.
from abc import ABC, abstractmethod


class ATB(ABC):  # We all are part of ATB Batch. I will give you classes, and you all have to perform task1 and task2.

    @abstractmethod
    def perform_task_1(self):
        pass

    @abstractmethod
    def perform_task_2(self):
        pass


class amit(ATB):
      # Now if amit comes in and if he wants to get ATB, he has to perform these 2 tasks. Only then amit's instance
           # will be created.
    # def perform_task_1(self):
    #     return "bow bow"
    #
    # def perform_task_2(self):
    #     return "meow meow"
    pass


amit = amit() # now we can create an object for amit.
print(amit.perform_task_1())
print(amit.perform_task_2())

# If amit doesn't perform any task, he will get an error:
# TypeError: Can't instantiate abstract class amit without an implementation for abstract methods 'perform_task_1', 'perform_task_2'
# So, Whenever you want to enforce something, then we can use abstraction.