# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.




class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Calling the static method without creating an object
print("Sum:", MathUtils.add(5, 7))

