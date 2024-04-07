# Automation Tester blueprint with python system
# Class - Student, Course, Payments- Razorpay, Stipe, Instamojo
# Objects

# For student class (Attributes & Behaviours)-> vandana, pankaj, anmol (Every student belongs to a course also)
# For course class (Attributes & Behaviours)-> PyATB, MTB, ATBJ, APIAT
# For payment class (Attributes & Behaviours)-> Razorpay, Stipe, Instamojo

# It means everything online, real world that we see, can be converted into Classes and Objects.
# Every problem statement can be converted into classes and objects.
# Class 1#
class Python_ATB:
    # pass
    name = 'Vandana Sharma'
    id = 123
    age = 85
    address = 'India'
    email = 'www.gmail@123'
    course_taken = 'Python Automation'

    def add_student(self):
        print("Data has been added for", "name")

    def delete_student(self):
        print("Data has been deleted for", "Vandana Sharma")


# below 3 objects, we are creating:
# 3 objects with one empty class as of now.
# Suppose vandana, pankaj and anmol are the part of Python Automation batch. So, instance also has created.
vandana = Python_ATB()

pankaj = Python_ATB

anmol = Python_ATB


# class 2#
class student:
    name = None
    phone_no = None

    def watch_recording(self):
        print("Recodings")

    def do_assignment(self):
        print("assignments")

    def do_coding(self):
        print("Recording")


vandana = student()

pankaj = student()

anmol = student()


# class 3#
class course:
    course_id = None
    course_name = None
    def couse_added(self):
        print("course has been added")
    def cousre_deleted(self):
        print("course has been deleted")

Py_ATB=course()
M_TB=course()
AT_BJ=course()
API_T=course()

# class 4#
class payment:
    payment_id=None
    payment_type=None
    def payment_done(self):
        print("payment made successful")
    def payment_cancel(self):
        print("payment has been cancel")

razorpay=payment()
stipe=payment()
instamojo=payment()