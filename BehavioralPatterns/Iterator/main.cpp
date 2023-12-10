// Main.cpp

#include "Book.h"
#include "Bookshelf.h"
#include "RandomSelectionIterator.h"
#include "AlphabeticalIterator.h"

int main() {
    // Create a collection of books
    Book* books[] = {
        new Book("The Great Gatsby", "Fiction"),
        new Book("To Kill a Mockingbird", "Fiction"),
        new Book("1984", "Dystopian"),
        // Add more books as needed
    };
    int numBooks = sizeof(books) / sizeof(books[0]);

    // Create a bookshelf
    Bookshelf bookshelf(books, numBooks);

    // Use different iterators to explore the bookshelf
    Iterator* randomIterator = bookshelf.createIterator("random");
    Iterator* alphabeticalIterator = bookshelf.createIterator("alphabetical");

    // Print randomly selected books
    std::cout << "Randomly Selected Books:" << std::endl;
    while (randomIterator->hasNext()) {
        Book* book = randomIterator->next();
        std::cout << (book ? book->getTitle() : "No more books") << std::endl;
    }

    // Print alphabetically sorted books
    std::cout << "\nAlphabetically Sorted Books:" << std::endl;
    while (alphabeticalIterator->hasNext()) {
        Book* book = alphabeticalIterator->next();
        std::cout << (book ? book->getTitle() : "No more books") << std::endl;
    }

    // Clean up allocated memory
    for (int i = 0; i < numBooks; ++i) {
        delete books[i];
    }

    return 0;
}
