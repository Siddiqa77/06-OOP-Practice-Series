# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.



class Car: 
    def __init__(self, brand):
        # Public variable
        self.brand = brand
    # Public method
    def start(self):
        print(f"The {self.brand} car is starting...")

# Instantiate the class
my_car:Car = Car("Toyota")

# Access the public variable from outside the class
print("Car Brand:", my_car.brand)

# Call the public method from outside the class
my_car.start()
