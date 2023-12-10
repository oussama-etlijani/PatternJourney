// Iterator.h

#ifndef ITERATOR_H
#define ITERATOR_H

class Iterator {
public:
    virtual ~Iterator() {}
    virtual Book* next() = 0;
    virtual bool hasNext() = 0;
};

#endif // ITERATOR_H
