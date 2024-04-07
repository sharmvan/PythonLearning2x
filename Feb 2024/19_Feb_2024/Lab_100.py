class car:
    color = None
    model = None

    def car_details(self):  # If I want to create a Method.
        print("you car details is:", self.color, self.model)  # then I need self in this case.
    # Note: To access the class type variable, we need self.


# We can get the color of the car and model from the user also:
car_color = input("Enter the color of car\n")
car_model = input("Enter the model of the car\n")

car_obj_ref = car()  # Created an obj reference by using car()
car_obj_ref.color = car_color  # We can set the value of the color by using obj reference.
car_obj_ref.model = car_model  # We can set the value of the model by using obj reference.
car_obj_ref.car_details()  # call the method "car_details" also and details will get printed in the console.

# If We don't want to get the color of the car and model from the user:
car_obj_ref.color = 'Red'
car_obj_ref.model = 'V3'
car_obj_ref.car_details()
