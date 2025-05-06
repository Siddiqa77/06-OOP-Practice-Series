
# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        # Initializing instance variables using self
        self.name = name
        self.marks = marks
      
# Creating an instance of the Student class and displaying its details
student1 = Student("Siddiqa Badar", 98)
student2 = Student("Ali Khan", 85)
student3 = Student("Sara Ali", 78)

print(f"Student Name: {student1.name}, Marks: {student1.marks}")
print(f"Student Name: {student2.name}, Marks: {student2.marks}")
print(f"Student Name: {student3.name}, Marks: {student3.marks}")