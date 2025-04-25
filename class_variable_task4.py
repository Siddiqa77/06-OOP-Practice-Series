class Bank:
    # Class variable
    bank_name = "National Bank"

    def __init__(self, customer_name):
        self.customer_name = customer_name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Customer: {self.customer_name}, Bank: {Bank.bank_name}")

# Create instances
acc1 = Bank("Siddiqa")
acc2 = Bank("Batool")

# Display original bank name
acc1.display()
acc2.display()

# Change bank name using class method
Bank.change_bank_name("Global Bank")

# Display updated bank name (should reflect in all instances)
acc1.display()
acc2.display()
