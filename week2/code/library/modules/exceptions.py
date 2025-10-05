class BookAlreadyBorrowedError(Exception):
    """Exception raised when a book is already checked out."""
    def __init__(self, book, member):
        super().__init__(f"Action failed: Book '{book.title}' is already borrowed by {member.name}.")

class BookNotFoundError(Exception):
    """Exception raised when a book ID does not exist."""
    def __init__(self, book_id):
        super().__init__(f"Action failed: No book found with ID '{book_id}'.")

class MemberNotFoundError(Exception):
    """Exception raised when a member ID does not exist."""
    def __init__(self, member_id):
        super().__init__(f"Action failed: No member found with ID '{member_id}'.")
