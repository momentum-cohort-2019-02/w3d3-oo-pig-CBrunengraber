class Human:
    """
    This class represents the human player and everything needed for player to take a turn, score points, make choices, and win or lose
    """
    def __init__(self):
        self.score = 0

#take those to game

class Game:
    def __init__(self, turn, die_roll, choice):
        self.turn = turn
        self.dice_roll = die_roll
        self.choice = choice


class Computer_player:
    def __init__(self):
        self.score = 0