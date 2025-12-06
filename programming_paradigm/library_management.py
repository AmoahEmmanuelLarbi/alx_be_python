"""
Objective: Solidify understanding of basic OOP concepts in Python by implementing a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.

Your Task: library_management.py
Implement a Book class with public attributes title and author, and a private attribute _is_checked_out to track its availability.
Implement a Library class with a private list _books to store instances of Book. Include methods to add_book, check_out_book(title), return_book(title), and list_available_books.
"""
#class implementation
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def __repr__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return True
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                return True
        return False

    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        # available_books = [book for book in self._books]
        for book in available_books:
            print(book)



#test
# test1 = Book("Brave New World", "Aldous Huxley")
# library = Library()
# library.add_book(test1)
# library.add_book(Book("1984", "George Orwell"))
# library.list_available_books()
# library.check_out_book("1984")
# library.list_available_books()