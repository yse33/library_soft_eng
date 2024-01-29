import os
import csv
from library import (
    read_books, sort_books_by_title,
    sort_books_by_author, sort_books_by_price, sort_books_by_genre
)

def main():
    try:
        while True:
            file_path = input("Enter the file path: ")

            if not os.path.exists(file_path):
                print("File not found")
                continue

            try:
                with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                    csv_data = csv.DictReader(file)
                    if csv_data.fieldnames is None:
                        print("CSV file is empty. No data found to be sorted.")
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

    except Exception as e:
        print("An unexpected error has occurred: " + str(e))


def print_books(books):
    for book in books:
        print(book)

if __name__ == '__main__':
    main()
