# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.




class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_employee(self):
        print(f"Employee: {self.name}, Position: {self.position}")

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: Department stores a reference to an Employee

    def display_department(self):
        print(f"Department: {self.department_name}")
        self.employee.display_employee()  # Access Employee's method from Department

# Create an Employee object
employee1 = Employee("John Doe", "Software Engineer")

# Create a Department object and pass the Employee object to it
department1 = Department("IT", employee1)

# Display department details along with employee details
department1.display_department()
