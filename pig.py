class Human:
    """This class represents the human player """
    def __init__(self):
        self.score = 0


class Computer_player:
    """This class represents the computer opponent"""
    def __init__(self):
        self.score = 0

class Game:
    """This class will deal with game flow, functions within the game, and scoring, start, and end of game"""
    def __init__(self, human, computer_player):
        self.human = human
        self.computer_player = computer_player




        # self.turn = turn
        # self.dice_roll = die_roll
        # self.choice = choice

