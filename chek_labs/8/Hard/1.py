class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def find_books_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def find_books_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def sort_books_by_title(self):
        return sorted(self.books, key=self.sort_by_title)

    def sort_books_by_author(self):
        return sorted(self.books, key=self.sort_by_author)

    def sort_books_by_year(self):
        return sorted(self.books, key=self.book.year)

    def sort_by_title(self, book):
        return book.title

    def sort_by_author(self, book):
        return book.author

    def sort_by_year(self, book):
        return book.year

library = Library()

library.add_book(Book("Война и мир", "Лев Толстой", 1869))
library.add_book(Book("Преступление и наказание", "Федор Достоевский", 1866))
library.add_book(Book("Мастер и Маргарита", "Михаил Булгаков", 1928))

books_by_author = library.find_books_by_author("Лев Толстой")
print("Книги Льва Толстого:")
for book in books_by_author:
    print(book)

sorted_books_by_year = library.sort_books_by_year()
print("\nКниги, отсортированные по году издания:")
for book in sorted_books_by_year:
    print(book)
