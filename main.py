import os
import csv
from library import *


def main():
    file_path = input("Enter the file path: ")

    assert os.path.exists(file_path), f"File not found at {file_path}"

    with open(file_path, mode='r', newline='') as file:
        csv_data = csv.DictReader(file)
        books = read_books(csv_data)

    print("\nBooks sorted by title:\n")
    print_books(sort_books_by_title(books))
    print("\nBooks sorted by author:\n")
    print_books(sort_books_by_author(books))
    print("\nBooks sorted by price:\n")
    print_books(sort_books_by_price(books))
    print("\nBooks sorted by genre:\n")
    print_books(sort_books_by_genre(books))


def print_books(books):
    for book in books:
        print(book)


if __name__ == '__main__':
    main()
