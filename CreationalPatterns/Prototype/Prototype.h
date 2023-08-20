#pragma once

class Prototype {
public:
    virtual ~Prototype() {}
    virtual Prototype* clone() const = 0;
};
