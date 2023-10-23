from book import Book
from user import User


def main():
    books = Book.load_books_from_file()
    users = User.load_users_from_file()

    print("Welcome to the Library!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Check out a book")
        print("2. Return a book")
        print("3. See all books")
        print("4. See all users")
        print("5. Exit")
        choice = input("Enter your choice: ")

        assert choice in ["1", "2", "3", "4", "5"]

        if choice == "1":
            check_out_book(books, users)
        elif choice == "2":
            return_book(users)
        elif choice == "3":
            see_all_books(books)
        elif choice == "4":
            see_all_users(users)
        elif choice == "5":
            print("Goodbye!")
            break

def check_out_book(books, users):
    username = input("Enter your username: ")
    user = find_user(users, username)

    if user is None:
        print("User not found. Please check the username.")
        return

    title = input("Enter the title of the book to check out: ")
    book = find_book(books, title)

    if book is None:
        print("Book not found. Please check the title.")
        return

    if book.checked_out:
        print("Sorry, this book is already checked out.")
    else:
        if user.check_out_book(book):
            book.checked_out = True
            print(f"{user.username} checked out '{book.title}' successfully.")
        else:
            print("You have reached the maximum number of checked-out books.")


def return_book(users):
    username = input("Enter your username: ")
    user = find_user(users, username)

    if user is None:
        print("User not found. Please check the username.")
        return

    if not user.checked_out_books:
        print(f"{user.username}, you haven't checked out any books.")
        return

    print("Books you have checked out:")
    for i, book in enumerate(user.checked_out_books, start=1):
        print(f"{i}. {book.title} by {book.author}")

    try:
        choice = int(input("Enter the number of the book to return: "))
        if 1 <= choice <= len(user.checked_out_books):
            book = user.checked_out_books[choice - 1]
            if user.return_book(book):
                book.checked_out = False
                print(f"You returned '{book.title}' successfully.")
            else:
                print("Failed to return the book.")
        else:
            print("Invalid choice. Please select a valid book number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def find_user(users, username):
    for user in users:
        if user.username == username:
            return user
    return None


def find_book(books, title):
    for book in books:
        if book.title == title:
            return book
    return None


def see_all_books(books):
    print("All books in the library:")
    for book in books:
        print(f"{book.title} by {book.author}")


def see_all_users(users):
    print("All users in the library:")
    for user in users:
        print(user.username)


if __name__ == "__main__":
    main()
