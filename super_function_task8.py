# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.




class Person:
    def __init__(self, name):
        self.name = name
        

class Teacher(Person):
    def __init__(self, name, subject):
        # Call the constructor of the base class using super()
        super().__init__(name)
        self.subject = subject
       

# Create a Teacher object
t1: Teacher = Teacher("Siddiqa", "Computer Science")
print(f"Teacher Name: {t1.name}, Subject: {t1.subject}")
