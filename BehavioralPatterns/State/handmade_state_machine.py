from enum import Enum, auto


class State(Enum):
    RED = auto()
    GREEN = auto()
    YELLOW = auto()


class Trigger(Enum):
    TIMER = auto()
    EMERGENCY = auto()


if __name__ == "__main__":
    # Define the state transition rules
    rules = {
        State.RED: [
            (Trigger.TIMER, State.GREEN),  # Transition from RED to GREEN after a timer
            (Trigger.EMERGENCY, State.RED),  # Remain RED in case of emergency
        ],
        State.GREEN: [
            (
                Trigger.TIMER,
                State.YELLOW,
            ),  # Transition from GREEN to YELLOW after a timer
            (Trigger.EMERGENCY, State.RED),  # Transition to RED in case of emergency
        ],
        State.YELLOW: [
            (Trigger.TIMER, State.RED),  # Transition from YELLOW to RED after a timer
            (Trigger.EMERGENCY, State.RED),  # Transition to RED in case of emergency
        ],
    }

    state = State.RED  # Initial state
    exit_state = None  # No specific exit state for this traffic light system

    print("Traffic Light State Machine")
    print("---------------------------")

    while True:
        print(f"The traffic light is currently {state.name}")
        print("Available triggers:")

        # Display the available triggers for the current state
        for i in range(len(rules[state])):
            trigger = rules[state][i][0]
            print(f"{i}: {trigger.name}")

        # Get user input for the trigger
        try:
            idx = int(input("Select a trigger (or type -1 to exit): "))
            if idx == -1:
                print("Exiting traffic light simulation.")
                break
            if idx < 0 or idx >= len(rules[state]):
                print("Invalid selection. Try again.")
                continue

            # Perform the state transition based on the selected trigger
            state = rules[state][idx][1]
        except ValueError:
            print("Invalid input. Please enter a number.")
