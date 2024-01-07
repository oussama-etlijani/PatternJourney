// Bookshelf.h

#ifndef BOOKSHELF_H
#define BOOKSHELF_H

#include "Iterator.h"

class Bookshelf {
public:
    Bookshelf(Book** books, int size);
    Iterator* createIterator(const std::string& iteratorType);

private:
    Book** books;
    int size;
};

#endif // BOOKSHELF_H
