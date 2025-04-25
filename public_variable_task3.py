class Car:
    # Public variable
    brand = "Toyota"

    # Public method
    def start(self):
        print(f"The {self.brand} car is starting...")

# Instantiate the class
my_car = Car()

# Access the public variable from outside the class
print("Car Brand:", my_car.brand)

# Call the public method from outside the class
my_car.start()
