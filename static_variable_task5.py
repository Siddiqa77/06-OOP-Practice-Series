class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Calling the static method without creating an object
result = MathUtils.add(5, 7)
print("Sum:", result)
