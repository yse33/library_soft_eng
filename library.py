from book import Book
from decimal import Decimal


def read_books(csv_data):
    books = []

    for row in csv_data:
        title = row['Title']
        author = row['Author']
        if Decimal(row['Price']) <= Decimal('0.00'):
            raise ValueError("Price cannot be negative or zero")
        price = Decimal(row['Price'])
        isbn = row['ISBN']
        genre = row['Genre']
        books.append(Book(title, author, price, isbn, genre))

    return books


def sort_books_by_title(books):
    return sorted(books, key=lambda book: book.title)


def sort_books_by_author(books):
    return sorted(books, key=lambda book: book.author)


def sort_books_by_price(books):
    return sorted(books, key=lambda book: book.price)


def sort_books_by_genre(books):
    return sorted(books, key=lambda book: book.genre)


def get_cheapest_book(books):
    return min(books, key=lambda book: book.price)