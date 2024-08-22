from book import Book
from user import User
from author import Author

class LibrarySystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.data() # to start with the data base and see if inputs are entered to begin with application

    def data(self):
        author1 = Author("George R.R. Martin", "American author, essayist, and critic.")
        author2 = Author("J.K. Rowling", "British author, best known for the Harry Potter series.")
        self.authors.extend([author1, author2])

        book1 = Book("A Song of Ice and Fire", author1.name, "Medieval Fantasy", "1996")
        book2 = Book("Harry Potter and the Philosopher's Stone", author2.name, "Fantasy", "1997")
        self.books.extend([book1, book2])

        user1 = User("Alice", "U001")
        user2 = User("Roger", "U002")
        self.users.extend([user1, user2])

    def add_book(self, title, author, genre, publication_date):
        book = Book(title, author, genre, publication_date)
        self.books.append(book)
        print(f"Book '{title}' added to the library.")

    def add_user(self, name, library_id):
        user = User(name, library_id)
        self.users.append(user)
        print(f"User '{name}' added to the library.")

    def add_author(self, name, biography):
        author = Author(name, biography)
        self.authors.append(author)
        print(f"Author '{name}' added to the library.")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_user(self, library_id):
        for user in self.users:
            if user.library_id == library_id:
                return user
        return None

    def find_author(self, name):
        for author in self.authors:
            if author.name.lower() == name.lower():
                return author
        return None

    def display_books(self):
        for book in self.books:
            print(book.get_details())

    def display_users(self):
        for user in self.users:
            print(user.get_details())

    def display_authors(self):
        for author in self.authors:
            print(author.get_details())

    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.book_operations()
            elif choice == "2":
                self.user_operations()
            elif choice == "3":
                self.author_operations()
            elif choice == "4":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def book_operations(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                genre = input("Enter book genre: ")
                publication_date = input("Enter publication date: ")
                self.add_book(title, author, genre, publication_date)
            elif choice == "2":
                title = input("Enter book title to borrow: ")
                book = self.find_book(title)
                if book:
                    library_id = input("Enter your Library ID: ")
                    user = self.find_user(library_id)
                    if user:
                        user.borrow_book(book)
                    else:
                        print("User not found.")
                else:
                    print("Book not found.")
            elif choice == "3":
                title = input("Enter book title to return: ")
                book = self.find_book(title)
                if book:
                    library_id = input("Enter your Library ID: ")
                    user = self.find_user(library_id)
                    if user:
                        user.return_book(book)
                    else:
                        print("User not found.")
                else:
                    print("Book not found.")
            elif choice == "4":
                title = input("Enter book title to search: ")
                book = self.find_book(title)
                if book:
                    print(book.get_details())
                else:
                    print("Book not found.")
            elif choice == "5":
                self.display_books()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter user name: ")
                library_id = input("Enter Library ID: ")
                self.add_user(name, library_id)
            elif choice == "2":
                library_id = input("Enter Library ID to view: ")
                user = self.find_user(library_id)
                if user:
                    print(user.get_details())
                else:
                    print("User not found.")
            elif choice == "3":
                self.display_users()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter author name: ")
                biography = input("Enter biography: ")
                self.add_author(name, biography)
            elif choice == "2":
                name = input("Enter author name to view: ")
                author = self.find_author(name)
                if author:
                    print(author.get_details())
                else:
                    print("Author not found.")
            elif choice == "3":
                self.display_authors()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    library_system = LibrarySystem()
    library_system.main_menu()


