class Book:
    """Represents a single book in the library."""
    def __init__(self, title, author, book_id):
        self.title = str(title)
        self.author = str(author)
        self.book_id = str(book_id)

    def __str__(self):
        return f"'{self.title}' by {self.author} (ID: {self.book_id})"
