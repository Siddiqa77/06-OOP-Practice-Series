class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created with name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        # Call the constructor of the base class using super()
        super().__init__(name)
        self.subject = subject
        print(f"Teacher teaches: {self.subject}")

# Create a Teacher object
t1 = Teacher("Siddiqa", "Computer Science")
