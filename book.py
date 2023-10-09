import pickle


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False
        self.save_books_to_file([self])

    def __str__(self):
        return f"{self.title} by {self.author}"

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return True
        else:
            return False

    def check_in(self):
        if self.checked_out:
            self.checked_out = False
            return True
        else:
            return False

    @staticmethod
    def save_books_to_file(books):
        with open("files/books.txt", 'wb') as file:
            pickle.dump(books, file)

    @staticmethod
    def load_books_from_file():
        try:
            with open("files/books.txt", 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []
