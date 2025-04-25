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
