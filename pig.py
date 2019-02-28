class Human:
    """
    This class represents the human player. They must enter user input, 
    chose to roll die or hold, and keep track of score for this player, and keep track of turn.   
    """
    def __init__(self):
        self.score = 0


class Computer_player:
    """
    This class represents the computer opponent. It will automatically decide to 
    roll or hold, and will keep track of the score for this player. It will also have a function to keep rolling until 20 points are reached, and keep track of turn.
    """
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

