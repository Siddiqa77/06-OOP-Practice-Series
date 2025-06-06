# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().


# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()  # Call the actual function
    return wrapper

# Function to be decorated
@log_function_call
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()
