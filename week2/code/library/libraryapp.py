
from modules.logger import ActivityLogger
from modules.library import Library
from modules.book import Book
from modules.member import Member

def main():
    """The main entry point for the library application."""
    logger = ActivityLogger("library_log.txt")
    my_library = Library()
    
    try:    
        my_library.add_book(Book("Hidden Hindu", "Akshad Gupta", "B001"))
        my_library.add_book(Book("The War of Art", "Steven Press Field", "B002"))
        my_library.add_book(Book("Factfullness", "Hans Rosling", "B003"))
        my_library.add_book(Book("The Alchemist", "Paulo Coelho", "B004"))
        my_library.add_member(Member("Piyanshu Kale", "M01"))
        my_library.add_member(Member("Aditya Dhengre", "M03"))
    
        while True:
            print("\n===== Library Management System =====")
            print("1. Borrow a Book\n2. Return a Book\n3. Show Available Books\n4. Show Borrowed Books\n5. Show Available members\n6. Exit")
            print("===================================")
            choice = input("Enter your choice (1-6): ")

            try:
                if choice == '1':
                    member_id = input("Enter your Member ID: ").strip()
                    book_id = input("Enter the Book ID to borrow: ").strip()
                    my_library.borrow_book(member_id, book_id)
                elif choice == '2':
                    book_id = input("Enter the Book ID to return: ").strip()
                    my_library.return_book(book_id)
                elif choice == '3':
                    my_library.display_available_books()
                elif choice == '4':
                    my_library.display_borrowed_books()
                elif choice == '5':
                    my_library.display_members()
                elif choice == '6':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except Exception as e:
                print(f"USER ERROR: {e}")
    finally:
        print(f"\nFull activity log has been saved to '{logger._filename}'")
        logger.close()

if __name__ == "__main__":
    main()


