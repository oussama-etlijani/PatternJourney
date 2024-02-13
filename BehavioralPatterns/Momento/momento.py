from __future__ import annotations

from abc import ABC, abstractmethod


class GameCharacter:
    def __init__(self, health: int, mana: int) -> None:
        self._health = health
        self._mana = mana
        print(f"Character created with health: {self._health}, mana: {self._mana}")

    def perform_action(self) -> None:
        print("Character is performing an action.")
        self._health -= 10
        self._mana += 5
        print(f"Updated attributes - health: {self._health}, mana: {self._mana}")

    def save_state(self) -> CharacterMemento:
        return ConcreteCharacterMemento(self._health, self._mana)

    def restore_state(self, memento: CharacterMemento) -> None:
        self._health = memento.get_health()
        self._mana = memento.get_mana()
        print(f"Character attributes restored - health: {self._health}, mana: {self._mana}")


class CharacterMemento(ABC):
    @abstractmethod
    def get_health(self) -> int:
        pass

    @abstractmethod
    def get_mana(self) -> int:
        pass


class ConcreteCharacterMemento(CharacterMemento):
    def __init__(self, health: int, mana: int) -> None:
        self._health = health
        self._mana = mana

    def get_health(self) -> int:
        return self._health

    def get_mana(self) -> int:
        return self._mana


class GameStateCaretaker:
    def __init__(self, game_character: GameCharacter) -> None:
        self._mementos = []
        self._game_character = game_character

    def save_state(self) -> None:
        print("\nCaretaker: Saving character state...")
        self._mementos.append(self._game_character.save_state())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(
            f"Caretaker: Restoring character state - health: {memento.get_health()}, mana: {memento.get_mana()}"
        )
        self._game_character.restore_state(memento)

    def show_history(self) -> None:
        print("Caretaker: Character state history:")
        for memento in self._mementos:
            print(f"Health: {memento.get_health()}, Mana: {memento.get_mana()}")


if __name__ == "__main__":
    character = GameCharacter(100, 50)
    caretaker = GameStateCaretaker(character)

    caretaker.save_state()
    character.perform_action()

    caretaker.save_state()
    character.perform_action()

    caretaker.save_state()
    character.perform_action()

    print()
    caretaker.show_history()

    print("\nClient: Undo once!\n")
    caretaker.undo()

    print("\nClient: Undo again!\n")
    caretaker.undo()
