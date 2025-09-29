class Book:
    def __init__(self, title, author,year):
        self.title = title
        self.author = author
        self.year = year
        self.available= True

    def describe(self):
        status="dostepna" if self.available else "wypożyczona"
        return f"{status} {self.title} {self.author} {self.year}"

    def borrow(self):
        if self.available:
            self.available = False
            return f"Ksiazka {self.title} zostala wypożyczona"
        else:
            return f"Ksiazka juz jest wypozyczona"

    def return_book(self):
        if  not self.available:
            self.available= True
            return f"Ksiazka {self.title} zostala zwrocona"
        else:
            return f"Ksiazka  {self.title} nie byla wypozyczona"