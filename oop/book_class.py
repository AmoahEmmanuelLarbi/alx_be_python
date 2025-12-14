"""
Docstring for alx_be_python.oop.book_class

Task Description:
Create a Python script named book_class.py. 
In this script, define a Book class that uses specific magic methods to enhance its functionality. 
This class will model a book with attributes for the title, author, and publication year.
"""

class Book:
    #constructor
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    #destructor
    def __del__(self):
        print(f"Deleting {self.title}")
    
    #string representation
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    #official representation
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"



def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()