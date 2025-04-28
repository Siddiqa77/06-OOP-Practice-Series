# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.


class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price  # Getter to return the price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value  # Setter to update the price

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price  # Deleter to delete the price

# Create a Product object
product1 = Product(100)

# Access the price using the property
print(f"Price: {product1.price}")

# Update the price using the setter
product1.price = 120
print(f"Updated Price: {product1.price}")

# Try setting a negative price
product1.price = -50

# Delete the price
del product1.price

# Try accessing the price after deletion
# print(product1.price)  # This will raise an error because the price is deleted
