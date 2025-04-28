
# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.


class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        self.current = self.start  # Reset for new iteration
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Use the Countdown class
cd = Countdown(5)

# Iterate using a for loop
for num in cd:
    print(num)
