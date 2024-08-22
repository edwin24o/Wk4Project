class Book:
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self._availability = True

    def borrow(self):
        if self._availability:
            self._availability = False
            print(f"Book '{self.title}' has been borrowed.")
        else:
            print(f"Book '{self.title}' is currently unavailable.")

    def return_book(self):
        self._availability = True
        print(f"Book '{self.title}' has been returned.")

    def get_details(self):
        availability = "Available" if self._availability else "Not Available"
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Published: {self.publication_date}, Availability: {availability}"
    
