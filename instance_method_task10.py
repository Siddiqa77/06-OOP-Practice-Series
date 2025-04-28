# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.


class Dog:
    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed

    def bark(self):
        # Instance method that prints a message including the dog's name
        print(f"{self.name} the {self.breed} says: Woof!")

# Create a Dog object
dog:Dog = Dog("Buddy", "Golden Retriever")

# Calling the instance method
dog.bark()
