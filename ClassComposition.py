class BookShelf:
    def __init__(self, *book):
        self.books = book

    def __str__(self):
        return f"Bookshelf has: {len(self.books)} books"
    
class Book:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return f"Book Name: {self.name}"

book = Book("Harry Potter")
book2 = Book("Harry Potter 2")
bookShelf = BookShelf(book, book2)
print(bookShelf)
print(bookShelf.books[0])
