import pickle


class User:
    def __init__(self, username):
        self.username = username
        self.checked_out_books = []
        self.save_users_to_file([self])

    def check_out_book(self, book):
        if book.check_out():
            self.checked_out_books.append(book)
            return True
        else:
            return False

    def return_book(self, book):
        if book in self.checked_out_books:
            book.check_in()
            self.checked_out_books.remove(book)
            return True
        else:
            return False

    @staticmethod
    def save_users_to_file(users):
        with open("files/users.txt", 'wb') as file:
            pickle.dump(users, file)

    @staticmethod
    def load_users_from_file():
        try:
            with open("files/users.txt", 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []
