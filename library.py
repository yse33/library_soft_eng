import decimal

from book import Book
from decimal import Decimal


def read_books(csv_data):
    books = []

    for row in csv_data:
        title = row['Title']
        author = row['Author']
        try:
            price = Decimal(row['Price'])
            if price <= Decimal('0.00'):
                raise ValueError("Price cannot be negative or zero")
        except (decimal.InvalidOperation, ValueError) as e:
            print(f"Invalid value type for the price: {row['Price']} in row {row}. Skipping this row.")
            continue

        isbn = row['ISBN']
        genre = row['Genre']
        books.append(Book(title, author, price, isbn, genre))

    return books



def sort_books_by_title(books):
    assert isinstance(books, list), "Invalid argument type. Expected list of books."
    assert all(isinstance(book, Book) for book in books), "Invalid element in the list. Expected Book instance."
    return sorted(books, key=lambda book: book.title)


def sort_books_by_author(books):
    assert isinstance(books, list), "Invalid argument type. Expected list of books."
    assert all(isinstance(book, Book) for book in books), "Invalid element in the list. Expected Book instance."
    return sorted(books, key=lambda book: book.author)


def sort_books_by_price(books):
    assert isinstance(books, list), "Invalid argument type. Expected list of books."
    assert all(isinstance(book, Book) for book in books), "Invalid element in the list. Expected Book instance."
    return sorted(books, key=lambda book: book.price)


def sort_books_by_genre(books):
    assert isinstance(books, list), "Invalid argument type. Expected list of books."
    assert all(isinstance(book, Book) for book in books), "Invalid element in the list. Expected Book instance."
    return sorted(books, key=lambda book: book.genre)


def get_cheapest_book(books):
    assert isinstance(books, list), "Invalid argument type. Expected list of books."
    assert all(isinstance(book, Book) for book in books), "Invalid element in the list. Expected Book instance."
    return min(books, key=lambda book: book.price)