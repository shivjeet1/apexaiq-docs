from .book import Book

class Member:
    """Represents a library member."""
    def __init__(self, name, member_id):
        self.name = str(name)
        self.member_id = str(member_id)
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        self.borrowed_books.append(book)

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def __str__(self):
        return f"{self.name} (Member ID: {self.member_id})"
