from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]

    def show_books(self) -> None:
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        print(f'Book "{title}" added to the library.')

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)
        print(f'Book "{title}" removed from the library.')

    def show_books(self) -> None:
        print("Books in the library:")
        self.library.show_books()


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                try:
                    year = int(input("Enter book year: ").strip())
                except ValueError:
                    print("Invalid year. Please enter a number.")
                    continue
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                print("Exiting the program.")
                break
            case _:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()