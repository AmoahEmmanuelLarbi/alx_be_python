"""
Docstring for library_system

Task Description:
Develop two Python scripts: library_system.py and main.py. 
In library_system.py, you’ll define a base class Book and two derived classes, EBook and PrintBook, showcasing inheritance. 
Additionally, implement a Library class demonstrating composition by managing a collection of books.
"""
#create a Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"{__class__.__name__}: {self.title} by {self.author}"
    
    # def __repr__(self):
    #     return f"Book ('{self.title}', '{self.author}')"
    

#create a Ebook class that inherit the Book class
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        # return f"{super().__str__()} and it's file szie of {self.file_size} KB"
        return f"{__class__.__name__}: {self.title} by {self.author}, File Size: {self.file_size}KB"
    
    # def __repr__(self):
    #     # return f"{super().__repr__()}, ('{self.file_size} KB')"
    #     return f"EBook: ('{self.title} by {self.author}, File Size: {self.file_size}KB')"
    

#create a PrintBook class that inherit the Book class
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        # return f"{super().__str__()} and page count is {self.page_count}"
         return f"{__class__.__name__}: {self.title} by {self.author}, Page Count: {self.page_count}"

    
    # def __repr__(self):
    #     # return f"{super().__repr__()}, ('{self.page_count}')"
    #      return f"PrintBook: ('{self.title} by {self.author}, Page Count: {self.page_count}')"

#create a class using composition
class Library:

    
    def __init__(self):
        # self.books = list()
        self.books = []
        # self.book = Book()

    def add_book(self, book):
        #add a book to library
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
        # return self.books
