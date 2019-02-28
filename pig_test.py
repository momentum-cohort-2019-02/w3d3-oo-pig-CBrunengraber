import pytest

from pig import Human, Computer_player, Game

def test_human():
    my_human = Human()
    assert my_human.score == 0

def test_computer_player():
    my_computer_player = Computer_player()
    assert my_computer_player.score == 0    


# how do i get the init method to work with this test - check the video from the morning at 11:20 - shapes.py & testshapes references from Clinton

def test_game(self):
    my_test_game = Game(Human, Computer_player) 
    assert self.human == Human()
    assert self.computer_player == Computer_player()

#three are methods - need to go to game
    # assert new_game.turn = turn()
    # assert new_game.die_roll = die_roll()
    # assert new_game.choice = choice()

