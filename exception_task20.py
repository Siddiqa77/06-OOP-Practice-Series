# Define a custom exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18."):
        super().__init__(message)

# Function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError()  # Raise the custom exception
    else:
        print("Age is valid. Access granted.")

# Use try...except to handle the exception
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
