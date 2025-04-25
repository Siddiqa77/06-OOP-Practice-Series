class Dog:
    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed

    def bark(self):
        # Instance method that prints a message including the dog's name
        print(f"{self.name} the {self.breed} says: Woof!")

# Create a Dog object
dog1 = Dog("Buddy", "Golden Retriever")

# Calling the instance method
dog1.bark()
