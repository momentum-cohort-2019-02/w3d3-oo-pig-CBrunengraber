import pytest

from pig import Human, Computer_player, Game

def test_human():
    my_human = Human()
    assert my_human.score == 0

def test_computer_player():
    my_computer_player = Computer_player()
    assert my_computer_player.score == 0    


# first three are attributes, the bottom three are methods - need to go to game
def test_game():
    assert new_game.turn == ""
    assert new_game.die_roll == ""
    assert new_game.choice == ""