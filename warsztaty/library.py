class Library:
    def __init__(self):
        self.books = []

    def addBook(self,book):
        self.books.append(book)

    def show(self):
         if not self.books:
             print("Biblioteka jest pusta")
         else:
             for book in self.books:
                 print(book.describe())
    def borrow_book(self,title):
        for book in self.books:
            if book.title.lower() == book.title:
                return book.borrow()

        return print(f"nie znaleziono ksiazki o tytule {title}")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.return_book()
        return f"Nie znaleziono książki o tytule '{title}'"

