from book import Book


def read_books(csv_data):
    books = []

    assert csv_data is not None, "CSV data is empty"

    for row in csv_data:
        title = row['Title']
        author = row['Author']
        assert float(row['Price']) > 0, "Price must be greater than 0"
        price = float(row['Price'])
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