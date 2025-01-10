class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.year}"
    
    def __lt__(self, other):
        return self.title < other.title

if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
    book3 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)

    books = [book1, book2, book3]

    sorted_books = sorted(books, key=lambda book: book.title)
    print("Books sorted by title:")
    for book in sorted_books:
        print(book)

    sorted_books = sorted(books, key=lambda book: book.author)
    print("Books sorted by title:")
    for book in sorted_books:
        print(book)

    sorted_books = sorted(books, key=lambda book: book.year)
    print("Books sorted by title:")
    for book in sorted_books:
        print(book)
