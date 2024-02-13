from abc import ABC, abstractmethod


# Define the Book class representing individual books in the collection
class Book:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre


# Define the Iterator interface
class Iterator(ABC):
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass


# Define the ConcreteIterators
class RandomSelectionIterator(Iterator):
    def __init__(self, books):
        self.books = books
        self.current_index = -1

    def next(self):
        if self.has_next():
            book = self.books[self.current_index]
            self.current_index += 1
            return book
        else:
            return None

    def has_next(self):
        return self.current_index + 1 < len(self.books)


class AlphabeticalIterator(Iterator):
    def __init__(self, books):
        self.books = sorted(books, key=lambda x: x.title)
        self.current_index = -1

    def next(self):
        if self.has_next():
            book = self.books[self.current_index]
            self.current_index += 1
            return book
        else:
            return None

    def has_next(self):
        return self.current_index + 1 < len(self.books)


# Define the Bookshelf class
class Bookshelf:
    def __init__(self, books):
        self.books = books

    def create_iterator(self, iterator_type):
        if iterator_type == "random":
            return RandomSelectionIterator(self.books)
        elif iterator_type == "alphabetical":
            return AlphabeticalIterator(self.books)
        else:
            raise ValueError("Invalid iterator type")


# Example Usage
if __name__ == "__main__":
    # Create a collection of books
    books = [
        Book("The Great Gatsby", "Fiction"),
        Book("To Kill a Mockingbird", "Fiction"),
        Book("1984", "Dystopian"),
        # Add more books as needed
    ]

    # Create a bookshelf
    bookshelf = Bookshelf(books)

    # Use different iterators to explore the bookshelf
    random_iterator = bookshelf.create_iterator("random")
    alphabetical_iterator = bookshelf.create_iterator("alphabetical")

    print("Randomly Selected Books:")
    for _ in range(len(books)):
        book = random_iterator.next()
        print(book.title if book else "No more books")

    print("\nAlphabetically Sorted Books:")
    for _ in range(len(books)):
        book = alphabetical_iterator.next()
        print(book.title if book else "No more books")
