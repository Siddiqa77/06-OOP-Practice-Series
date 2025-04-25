class Logger:
    def __init__(self):
        print("Logger object has been created.")

    def __del__(self):
        print("Logger object has been destroyed.")

# Creating an object
log = Logger()

# You can explicitly delete it (or wait for the program to end)
del log
