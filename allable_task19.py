# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.


class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Store the multiplication factor

    def __call__(self, number):
        return number * self.factor  # Makes the object callable like a function

# Create a Multiplier object
times3 = Multiplier(3)

# Test if the object is callable
print(callable(times3))  # Output: True

# Call the object like a function
result = times3(10)
print(f"3 times 10 is: {result}")  # Output: 3 times 10 is: 30
