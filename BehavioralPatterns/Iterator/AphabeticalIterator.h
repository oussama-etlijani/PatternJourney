// AlphabeticalIterator.h

#ifndef ALPHABETICAL_ITERATOR_H
#define ALPHABETICAL_ITERATOR_H

#include "Iterator.h"
#include <algorithm>

class AlphabeticalIterator : public Iterator {
public:
    AlphabeticalIterator(Book** books, int size);
    Book* next() override;
    bool hasNext() override;

private:
    Book** books;
    int size;
    int currentIndex;
};

#endif // ALPHABETICAL_ITERATOR_H
