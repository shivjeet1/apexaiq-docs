from .logger import log_activity
from .exceptions import BookNotFoundError, MemberNotFoundError, BookAlreadyBorrowedError
from .book import Book
from .member import Member

class Library:
    def __init__(self):
        self._books = {}
        self._members = {}
        self._borrowed_books = {}

    @log_activity
    def add_book(self, book: Book):
        if book.book_id in self._books:
            print(f"WARN: Book with ID {book.book_id} already exists.")
            return
        self._books[book.book_id] = book
        print(f"INFO: Book {book} added to the library.")

    @log_activity
    def add_member(self, member: Member):
        if member.member_id in self._members:
            print(f"WARN: Member with ID {member.member_id} already exists.")
            return
        self._members[member.member_id] = member
        print(f"INFO: Member {member} registered.")

    @log_activity
    def borrow_book(self, member_id: str, book_id: str):
        if book_id not in self._books: raise BookNotFoundError(book_id)
        if member_id not in self._members: raise MemberNotFoundError(member_id)

        if book_id in self._borrowed_books:
            borrower_id = self._borrowed_books[book_id]
            raise BookAlreadyBorrowedError(self._books[book_id], self._members[borrower_id])

        book = self._books[book_id]
        member = self._members[member_id]
        member.borrow_book(book)
        self._borrowed_books[book_id] = member_id
        print(f"SUCCESS: {member.name} borrowed {book.title}.")

    @log_activity
    def return_book(self, book_id: str):
        if book_id not in self._books: raise BookNotFoundError(book_id)
        if book_id not in self._borrowed_books:
            print(f"INFO: Book '{self._books[book_id].title}' is already available.")
            return
            
        member_id = self._borrowed_books.pop(book_id)
        member = self._members[member_id]
        book = self._books[book_id]
        member.return_book(book)
        print(f"SUCCESS: {member.name} returned {book.title}.")
        
    @log_activity
    def display_available_books(self):
        print("\n--- Available Books ---")
        available = [b for i, b in self._books.items() if i not in self._borrowed_books]
        if not available: print("No books are currently available.")
        else:
            for book in available: print(f"- {book}")
        print("-----------------------")

    @log_activity
    def display_borrowed_books(self):
        print("\n--- Borrowed Books ---")
        if not self._borrowed_books: print("No books are currently borrowed.")
        else:
            for book_id, member_id in self._borrowed_books.items():
                print(f"- {self._books[book_id]} (By: {self._members[member_id].name})")
        print("----------------------")
