#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>

class CharacterMemento {
public:
    virtual ~CharacterMemento() = default;
    virtual int getHealth() const = 0;
    virtual int getMana() const = 0;
};

class ConcreteCharacterMemento : public CharacterMemento {
private:
    int health;
    int mana;

public:
    ConcreteCharacterMemento(int h, int m) : health(h), mana(m) {}

    int getHealth() const override {
        return health;
    }

    int getMana() const override {
        return mana;
    }
};

class GameCharacter {
private:
    int health;
    int mana;

public:
    GameCharacter(int h, int m) : health(h), mana(m) {
        std::cout << "Character created with health: " << health << ", mana: " << mana << std::endl;
    }

    void performAction() {
        std::cout << "Character is performing an action." << std::endl;
        health -= 10;
        mana += 5;
        std::cout << "Updated attributes - health: " << health << ", mana: " << mana << std::endl;
    }

    CharacterMemento* saveState() const {
        return new ConcreteCharacterMemento(health, mana);
    }

    void restoreState(const CharacterMemento* memento) {
        const ConcreteCharacterMemento* concreteMemento = dynamic_cast<const ConcreteCharacterMemento*>(memento);
        if (concreteMemento) {
            health = concreteMemento->getHealth();
            mana = concreteMemento->getMana();
            std::cout << "Character attributes restored - health: " << health << ", mana: " << mana << std::endl;
        }
    }
};

class GameStateCaretaker {
private:
    std::vector<CharacterMemento*> mementos;
    GameCharacter* gameCharacter;

public:
    GameStateCaretaker(GameCharacter* character) : gameCharacter(character) {}

    ~GameStateCaretaker() {
        for (auto memento : mementos) {
            delete memento;
        }
    }

    void saveState() {
        std::cout << "\nCaretaker: Saving character state..." << std::endl;
        mementos.push_back(gameCharacter->saveState());
    }

    void undo() {
        if (!mementos.empty()) {
            CharacterMemento* memento = mementos.back();
            mementos.pop_back();
            std::cout << "Caretaker: Restoring character state - health: " << memento->getHealth()
                      << ", mana: " << memento->getMana() << std::endl;
            gameCharacter->restoreState(memento);
            delete memento;
        }
    }

    void showHistory() const {
        std::cout << "Caretaker: Character state history:" << std::endl;
        for (const auto& memento : mementos) {
            std::cout << "Health: " << memento->getHealth() << ", Mana: " << memento->getMana() << std::endl;
        }
    }
};

int main() {
    srand(static_cast<unsigned>(time(nullptr)));

    GameCharacter character(100, 50);
    GameStateCaretaker caretaker(&character);

    caretaker.saveState();
    character.performAction();

    caretaker.saveState();
    character.performAction();

    caretaker.saveState();
    character.performAction();

    std::cout << std::endl;
    caretaker.showHistory();

    std::cout << "\nClient: Undo once!\n";
    caretaker.undo();

    std::cout << "\nClient: Undo again!\n";
    caretaker.undo();

    return 0;
}
