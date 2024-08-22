class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self._borrowed_books = []

    def borrow_book(self, book):
        if book._availability:
            book.borrow()
            self._borrowed_books.append(book.title)
        else:
            print(f"Sorry, {book.title} is unavailable.")

    def return_book(self, book):
        if book.title in self._borrowed_books:
            book.return_book()
            self._borrowed_books.remove(book.title)
        else:
            print(f"{self.name} does not have the book '{book.title}' borrowed.")

    def get_details(self):
        return f"Name: {self.name}, Library ID: {self.library_id}, Borrowed Books: {', '.join(self._borrowed_books) if self._borrowed_books else 'None'}"