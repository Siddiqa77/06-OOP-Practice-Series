# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.


class Counter:
    # Class variable to keep track of the number of objects
    count = 0

    def __init__(self):
        # Increment the class variable when a new object is created
        Counter.count += 1

    @classmethod
    def display_count(cls):
        # Display total count using cls
        print(f"Total objects created: {cls.count}")

# Example usage
c1 = Counter()
c2 = Counter()
c3 = Counter()

# Display count
Counter.display_count()
