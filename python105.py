import random
import pytest

from unittest.mock import patch
from guess import get_random_number, Game

@patch.object(random, 'randint')
def test_get_random_number(n):
    n.return_value = 17
    assert get_random_number == 17
    
@patch('bulletins.input', side_effect=[11, '12', 'Bob', 12, 5, -1, 21, 7, None])

def test_guess(inputs):
    game = Game()
    assert game.guess() == 11 # 11
    assert game.guess() == 12 # '12'
    with pytest.raises(ValueError): # 'Bob'
        game.guess()
    with pytest.raises(ValueError): # 12
        game.guess()
    assert game.guess() == 5 # 5
    with pytest.raises(ValueError): # -1
        game.guess()
    with pytest.raises(ValueError): # 21
        game.guess()
    assert game.guess() == 7 # 7
    with pytest.raises(ValueError): # None
        game.guess()
        
