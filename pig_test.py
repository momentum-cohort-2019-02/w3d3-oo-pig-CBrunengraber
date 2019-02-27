import pytest

from pig import Human

def test_human():
    my_human = Human()
    assert my_human.score == 0
    # assert human.turn == ""
    # assert human.die_roll == ""
    # assert human.choice == ""

# first three are attributes, the bottom three are methods - need to go to game