#include <iostream>
#include <string>

class AquaticAnimal {
public:
    virtual ~AquaticAnimal() {}
    virtual std::string interact() = 0;
};

class TerrestrialAnimal {
public:
    virtual ~TerrestrialAnimal() {}
    virtual std::string interact() = 0;
};

class AvianAnimal {
public:
    virtual ~AvianAnimal() {}
    virtual std::string interact() = 0;
};

class Shark : public AquaticAnimal {
public:
    std::string interact() override {
        return "The shark swims around.";
    }
};

class Lion : public TerrestrialAnimal {
public:
    std::string interact() override {
        return "The lion roars.";
    }
};

class Eagle : public AvianAnimal {
public:
    std::string interact() override {
        return "The eagle soars high.";
    }
};
