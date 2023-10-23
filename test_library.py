from unittest import mock


from main import (
    User,
    Book,
    find_user,
    find_book,
    see_all_books,
    see_all_users,
)


def exception_mock():
    return mock.Mock(side_effect=Exception("Boom!"))


def expect_exception(self):
    users = [
        mock.Mock(username="user1")
    ]

    with self.assertRaises(Exception):
        find_user(users, "user2")


def test_find_user():
    users = [
        mock.Mock(username="user1"),
        mock.Mock(username="user2"),
        mock.Mock(username="user3"),
    ]
    assert find_user(users, "user1") == users[0]
    assert find_user(users, "user2") == users[1]
    assert find_user(users, "user3") == users[2]
    assert find_user(users, "user4") is None


def test_find_book():
    books = [
        mock.Mock(title="book1"),
        mock.Mock(title="book2"),
        mock.Mock(title="book3"),
    ]
    assert find_book(books, "book1") == books[0]
    assert find_book(books, "book2") == books[1]
    assert find_book(books, "book3") == books[2]
    assert find_book(books, "book4") is None


def test_see_all_books(capsys):
    books = [
        mock.Mock(title="book1", author="author1"),
        mock.Mock(title="book2", author="author2"),
        mock.Mock(title="book3", author="author3"),
    ]
    see_all_books(books)
    captured = capsys.readouterr()
    assert captured.out == "All books in the library:\nbook1 by author1\nbook2 by author2\nbook3 by author3\n"


def test_see_all_users(capsys):
    users = [
        mock.Mock(username="user1"),
        mock.Mock(username="user2"),
        mock.Mock(username="user3"),
    ]
    see_all_users(users)
    captured = capsys.readouterr()
    assert captured.out == "All users in the library:\nuser1\nuser2\nuser3\n"


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
