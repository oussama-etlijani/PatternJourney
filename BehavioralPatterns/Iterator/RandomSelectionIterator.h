// RandomSelectionIterator.h

#ifndef RANDOM_SELECTION_ITERATOR_H
#define RANDOM_SELECTION_ITERATOR_H

#include "Iterator.h"

class RandomSelectionIterator : public Iterator {
public:
    RandomSelectionIterator(Book** books, int size);
    Book* next() override;
    bool hasNext() override;

private:
    Book** books;
    int size;
    int currentIndex;
};

#endif // RANDOM_SELECTION_ITERATOR_H
