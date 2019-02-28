import pytest


from pig import Human, Computer_player, Game

def test_human():
    my_human = Human()
    assert my_human.score == 0

def test_computer_player():
    my_computer_player = Computer_player()
    assert my_computer_player.score == 0    



def test_game():
    my_test_game = Game(Human, Computer_player) #this test should assert if this is true, but self not defined and i cant pass the test an argument above
    assert self.human == Human()
    assert self.computer_player == Computer_player()

#three are methods - need to go to game
    # assert new_game.turn = turn()
    # assert new_game.die_roll = die_roll()
    # assert new_game.choice = choice()

