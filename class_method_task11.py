class Book:
    # Class variable
    total_books = 0

    def __init__(self, title):
        self.title = title
        # Increment the total_books count whenever a new book is created
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        # Increase the class variable total_books
        cls.total_books += 1

    @classmethod
    def display_book_count(cls):
        # Display the current total count of books
        print(f"Total books: {cls.total_books}")

# Adding books
book1 = Book("The Great Gatsby")
book2 = Book("1984")
book3 = Book("To Kill a Mockingbird")

# Display total number of books
Book.display_book_count()
