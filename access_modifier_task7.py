class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name           # Public
        self._salary = salary      # Protected (by convention)
        self.__ssn = ssn           # Private

# Create an object
emp = Employee("Siddiqa", 50000, "123-45-6789")

# Accessing public variable
print("Name (Public):", emp.name)

# Accessing protected variable
print("Salary (_Protected):", emp._salary)

# Accessing private variable (will raise AttributeError)
try:
    print("SSN (__Private):", emp.__ssn)
except AttributeError as e:
    print("Error accessing private variable:", e)

# Accessing private variable using name mangling
print("SSN (Accessed via name mangling):", emp._Employee__ssn)
