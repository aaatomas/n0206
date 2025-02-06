class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} ({self.author})"

class Library:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def removeBook(self, title):
        book_to_delete = self.findBook(title)
        self.books.remove(book_to_delete)
        print(f"Removed: {book_to_delete}")

    def findBook(self, title):
        for book in self.books:
            if book.title == title:
                return book


library1 = Library()

library1.addBook(Book('Harry Potter 1', 'J.K Rouling'))
library1.addBook(Book('Harry Potter 2', 'J.K Rouling'))
library1.addBook(Book('Harry Potter 3', 'J.K Rouling'))
library1.addBook(Book('Harry Potter 4', 'J.K Rouling'))

library1.removeBook('Harry Potter 2')
foundBook = library1.findBook('Harry Potter 3')
print(f"Found: {foundBook}")
