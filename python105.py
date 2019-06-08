import random
import pytest

from unittest.mock import patch
from guess import get_random_number, Game

@patch.object(random, 'randint')
def test_get_random_number(n):
    n.return_value = 17
    assert get_random_number == 17