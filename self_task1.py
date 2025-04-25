class Student:
    def __init__(self, name, marks):
        # Initializing instance variables using self
        self.name = name
        self.marks = marks

    def display(self):
        # Displaying student details using self
        print(f"Student Name: {self.name} and Marks: {self.marks}")
       
# Creating an instance of the Student class and displaying its details
student1 = Student("Siddiqa Badar", 92)
student2 = Student("Ali Khan", 85)
student3 = Student("Sara Ali", 78)
student1.display()
student2.display()
student3.display()
