import pytest

from library import read_books, sort_books_by_title, sort_books_by_author, sort_books_by_price, sort_books_by_genre, get_cheapest_book
from decimal import Decimal

CSV_MOCK_DATA = [
    {
        'Title': 'The Pragmatic Programmer',
        'Author': 'Andrew Hunt, David Thomas',
        'Price': '36.00',
        'ISBN': '978-0201616224',
        'Genre': 'Software Development'
    },
    {
        'Title': 'Clean Code',
        'Author': 'Robert C. Martin',
        'Price': '37.99',
        'ISBN': '978-0132350884',
        'Genre': 'Software Development'
    }
]


def test_read_books():
    books = read_books(CSV_MOCK_DATA)
    assert len(books) == 2
    assert books[0].title == 'The Pragmatic Programmer'
    assert books[0].author == 'Andrew Hunt, David Thomas'
    assert books[0].price == Decimal('36.00')
    assert books[0].isbn == '978-0201616224'
    assert books[0].genre == 'Software Development'
    assert books[1].title == 'Clean Code'
    assert books[1].author == 'Robert C. Martin'
    assert books[1].price == Decimal('37.99')
    assert books[1].isbn == '978-0132350884'
    assert books[1].genre == 'Software Development'


def test_sort_books_by_title(benchmark):
    books = read_books(CSV_MOCK_DATA)
    sorted_books = benchmark(sort_books_by_title, books)
    assert sorted_books[0].title == 'Clean Code'
    assert sorted_books[1].title == 'The Pragmatic Programmer'


def test_sort_books_by_author(benchmark):
    books = read_books(CSV_MOCK_DATA)
    sorted_books = benchmark(sort_books_by_author, books)
    assert sorted_books[0].author == 'Andrew Hunt, David Thomas'
    assert sorted_books[1].author == 'Robert C. Martin'


def test_sort_books_by_price(benchmark):
    books = read_books(CSV_MOCK_DATA)
    sorted_books = benchmark(sort_books_by_price, books)
    assert sorted_books[0].price == Decimal('36.00')
    assert sorted_books[1].price == Decimal('37.99')


def test_sort_books_by_genre():
    books = read_books(CSV_MOCK_DATA)
    sorted_books = sort_books_by_genre(books)
    assert sorted_books[0].genre == 'Software Development'
    assert sorted_books[1].genre == 'Software Development'


def test_read_books_with_price_less_than_zero(capfd):
    csv_mock_data = [
        {
            'Title': 'The Pragmatic Programmer',
            'Author': 'Andrew Hunt, David Thomas',
            'Price': '-36.00',
            'ISBN': '978-0201616224',
            'Genre': 'Software Development'
        }
    ]
    read_books(csv_mock_data)
    captured = capfd.readouterr()
    expected_error_message = 'Invalid value type for the price: -36.00 in row'
    assert expected_error_message in captured.out



def mock_that_raises_exception():
    raise Exception('Mock exception')


def test_get_cheapest_book(benchmark):
    books = read_books(CSV_MOCK_DATA)
    cheapest_book = benchmark(get_cheapest_book, books)
    assert cheapest_book.title == 'The Pragmatic Programmer'


def test_read_books_with_invalid_price(capfd):
    csv_mock_data_invalid_price = [
        {
            'Title': 'Fourth Wing',
            'Author': 'Rebecca Yarros',
            'Price': 'xxx',
            'ISBN': '978-1234567890',
            'Genre': 'Fantasy'
        }
    ]
    read_books(csv_mock_data_invalid_price)
    captured = capfd.readouterr()
    expected_error_message = 'Invalid value type for the price: xxx in row'
    assert expected_error_message in captured.out
