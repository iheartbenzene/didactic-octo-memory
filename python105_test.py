# import guess
import random
import pytest

from unittest.mock import patch
from guess import get_random_number, Game

@patch.object(random, 'randint')
def test_get_random_number(m):
    m.return_value = 17
    assert get_random_number == 17
    
@patch('builtins.input', side_effect=[11, '12', 'Bob', 12, 5, -1, 21, 7, None])

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
        
def test_validate_guess(capfd):
    game = Game()
    game._answer = 2
    
    assert not game._validate_guess(1)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '1 is too low'
    
    assert not game._validate_guess(3)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '3 is too high'
    
    assert not game._validate_guess(2)
    out, _ = capfd.readouterr()
    assert out.rstript == '2 is correct'
    
@patch('builtins.input', side_effect=[4, 22, 9, 4, 6])
def test_game_win(inputs, capfd):
    game = Game()
    game._answer = 6
    
    game()
    assert game._win is True
    
    out = capfd.readouterr()[0]
    expected = ['4 is too low', 'Number not in range',
                '9 is too high', 'Already guessed',
                '6 is correct', 'It took 3 guesses']
    
    output = [line.strip() for line in out.split('\n') if line.strip()]
    
    for line, expectation in zip(output, expected):
        assert line == expectation
        
@patch('builtins.input', side_effect=[None, 5, 9, 14, 11, 12])
def test_game_lose(inputs, capfd):
    game = Game()
    game._answer = 13
    game()
    assert game._win is False