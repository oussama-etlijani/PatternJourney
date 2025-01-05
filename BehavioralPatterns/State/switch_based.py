from enum import Enum, auto


class State(Enum):
    IDLE = auto()
    WAITING_FOR_PAYMENT = auto()
    DISPENSING_ITEM = auto()


if __name__ == "__main__":
    items = {"A1": 1.50, "B2": 2.00, "C3": 2.50}  # Items with their prices
    selected_item = None
    state = State.IDLE
    balance = 0.0

    print("Welcome to the vending machine!")
    print("Available items:")
    for code, price in items.items():
        print(f"{code}: ${price:.2f}")

    while True:
        if state == State.IDLE:
            selected_item = input("\nSelect an item (e.g., A1): ").upper()
            if selected_item in items:
                state = State.WAITING_FOR_PAYMENT
                print(f"Selected {selected_item}. Price: ${items[selected_item]:.2f}")
            else:
                print("Invalid selection. Try again.")

        elif state == State.WAITING_FOR_PAYMENT:
            try:
                payment = float(input("Insert payment (e.g., 1.50): "))
                balance += payment
                print(f"Current balance: ${balance:.2f}")
                if balance >= items[selected_item]:
                    state = State.DISPENSING_ITEM
                else:
                    print("Insufficient funds. Please insert more money.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

        elif state == State.DISPENSING_ITEM:
            change = balance - items[selected_item]
            print(f"\nDispensing {selected_item}...")
            if change > 0:
                print(f"Returning change: ${change:.2f}")
            print("Thank you for your purchase!")
            balance = 0.0
            state = State.IDLE
