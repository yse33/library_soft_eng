from main import (
    User,
    Book,
    find_user,
    find_book,
    see_all_books,
    see_all_users,
)


def test_check_out_book():
    user = User("User1")
    book = Book("Book1", "Author1", "ISBN1")
    assert not user.checked_out_books
    assert not book.checked_out


def test_return_book():
    user = User("User1")
    book = Book("Book1", "Author1", "ISBN1")
    user.check_out_book(book)
    assert user.checked_out_books == [book]
    assert book.checked_out


def test_find_user():
    users = [User("User1"), User("User2")]
    assert find_user(users, "User1").username == "User1"
    assert find_user(users, "User3") is None


def test_find_book():
    books = [Book("Book1", "Author1", "ISBN1"), Book("Book2", "Author2", "ISBN2")]
    assert find_book(books, "Book1").title == "Book1"
    assert find_book(books, "Book3") is None


def test_see_all_books(capsys):
    books = [Book("Book1", "Author1", "ISBN1"), Book("Book2", "Author2", "ISBN2")]
    see_all_books(books)
    captured = capsys.readouterr()
    assert "All books in the library:" in captured.out
    assert "Book1 by Author1" in captured.out
    assert "Book2 by Author2" in captured.out


def test_see_all_users(capsys):
    users = [User("User1"), User("User2")]
    see_all_users(users)
    captured = capsys.readouterr()
    assert "All users in the library:" in captured.out
    assert "User1" in captured.out
    assert "User2" in captured.out
