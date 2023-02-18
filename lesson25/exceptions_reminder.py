class LibraryError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class CustomerAlreadyExists(LibraryError):
    def __init__(self, msg):
        super().__init__(msg)

class BookAlreadyExists(LibraryError):
    def __init__(self, msg):
        super().__init__(msg)


class Library:

    def __init__(self):
        self.customers = {}
        self.books = {}

    def add_new_customer(self, id, name, email):
        if id in self.customers:
            raise CustomerAlreadyExists(
                f"Customer with provided id {id} already exist")

    def add_new_book(self, id, name, author):
        if id in self.books:
            raise BookAlreadyExists(
                f"The book with provided id {id} already exist")

if __name__ == '__main__':
    library = Library()
    try:
        # a lot of code
        library.add_new_customer(1, "bla", "email")
        # a lot of code
        library.add_new_book(3, "book", "ddfg")
    except LibraryError as e:
        print(e)