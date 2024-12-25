class Event(list):
    # Event class acts as a list of callbacks (subscribers)
    # It implements the observer pattern for event handling

    def __call__(self, *args, **kwargs):
        # When the Event instance is called, all the registered callbacks are triggered
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self):
        # Initialize the game with an Event to handle notifications
        self.events = Event()

    def fire(self, args):
        # Trigger the Event to notify all subscribers
        self.events(args)


class GoalScoredInfo:
    # Class to encapsulate information about a goal being scored
    def __init__(self, who_scored, goals_scored):
        self.goals_scored = goals_scored  # Number of goals scored by the player
        self.who_scored = who_scored  # Name of the player who scored


class Player:
    def __init__(self, name, game):
        self.name = name  # Name of the player
        self.game = game  # Reference to the game for firing events
        self.goals_scored = 0  # Track the number of goals scored by the player

    def score(self):
        # Increment the player's goal count
        self.goals_scored += 1

        # Create a GoalScoredInfo object with details of the goal
        args = GoalScoredInfo(self.name, self.goals_scored)

        # Notify all subscribers about the goal
        self.game.fire(args)


class Coach:
    def __init__(self, game):
        # Subscribe to the game's events
        game.events.append(self.celebrate_goal)

    def celebrate_goal(self, args):
        # Callback method triggered when a goal event is fired
        if isinstance(args, GoalScoredInfo) and args.goals_scored < 3:
            # Celebrate the goal only if the player has scored less than 3 goals
            print(f"Coach says: well done, {args.who_scored}!")


if __name__ == "__main__":
    # Create a Game instance
    game = Game()

    # Create a Player instance associated with the game
    player = Player("Sam", game)

    # Create a Coach instance subscribed to the game's events
    coach = Coach(game)

    # Player scores a goal, triggering an event
    player.score()  # Coach says: well done, Sam!

    # Player scores again, triggering another event
    player.score()  # Coach says: well done, Sam!

    # Player scores a third goal, but the coach ignores it
    player.score()  # (No output, as coach celebrates only the first 2 goals)
