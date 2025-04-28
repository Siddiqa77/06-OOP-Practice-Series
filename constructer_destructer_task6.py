# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

#constructor and destructor in python
# In Python, the constructor is defined using the __init__ method and the destructor is defined using the __del__ method.



class Logger:
    def __init__(self):
        print("Logger object has been created.")

    def __del__(self):
        print("Logger object has been destroyed.")

# Creating an object
log:Logger = Logger()

# You can explicitly delete it (or wait for the program to end)
del log
