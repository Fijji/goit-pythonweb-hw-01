import logging
from abc import ABC, abstractmethod
from typing import List

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title: str = title
        self.author: str = author
        self.year: int = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: 'Book') -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]

    def show_books(self) -> None:
        if not self.books:
            logger.info("The library is empty.")
        else:
            for book in self.books:
                logger.info(str(book))


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library: LibraryInterface = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        logger.info(f'Book "{title}" added to the library.')

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)
        logger.info(f'Book "{title}" removed from the library.')

    def show_books(self) -> None:
        logger.info("Books in the library:")
        self.library.show_books()


def main() -> None:
    library: Library = Library()
    manager: LibraryManager = LibraryManager(library)

    while True:
        command: str = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title: str = input("Enter book title: ").strip()
                author: str = input("Enter book author: ").strip()
                try:
                    year: int = int(input("Enter book year: ").strip())
                except ValueError:
                    logger.error("Invalid year. Please enter a number.")
                    continue
                manager.add_book(title, author, year)
            case "remove":
                title: str = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                logger.info("Exiting the program.")
                break
            case _:
                logger.error("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
