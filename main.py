"""
main.py: A script for reading and sorting a CSV file containing books information.
"""

import os
import csv
from library import (
    read_books, sort_books_by_title,
    sort_books_by_author, sort_books_by_price, sort_books_by_genre
)


def main():
    """
    Main function for executing the book reading and sorting process.
    """
    while True:
        file_path = input("Enter the file path: ")

        if not os.path.exists(file_path):
            print("File not found")
            continue

    assert os.path.exists(file_path), "File not found"

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_data = csv.DictReader(file)
            try:
                assert csv_data.fieldnames is not None, \
                    "CSV file is empty. No data found to be sorted."
            except AssertionError as e:
                print(e)
                return
            books = read_books(csv_data)

    except FileNotFoundError as e:
        print(e)
        return
    except IOError as e:
        print(e)
        return

    print("\nBooks sorted by title:\n")
    print_books(sort_books_by_title(books))
    print("\nBooks sorted by author:\n")
    print_books(sort_books_by_author(books))
    print("\nBooks sorted by price:\n")
    print_books(sort_books_by_price(books))
    print("\nBooks sorted by genre:\n")
    print_books(sort_books_by_genre(books))


def print_books(books):
    """
    Print the details of books in a formatted manner.

    Args:
        books (list): A list of book dictionaries.

    Returns:
        None
    """
    for book in books:
        print(book)


if __name__ == '__main__':
    main()
