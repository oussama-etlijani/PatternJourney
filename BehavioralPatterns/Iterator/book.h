// Book.h

#ifndef BOOK_H
#define BOOK_H

#include <string>

class Book {
public:
    Book(const std::string& title, const std::string& genre);
    std::string getTitle() const;
    std::string getGenre() const;

private:
    std::string title;
    std::string genre;
};

#endif // BOOK_H
