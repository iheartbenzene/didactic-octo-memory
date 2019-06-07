import csv
import random

from collections import defaultdict, namedtuple, Counter, deque
from urllib.request import urlretrieve

regular_tuple = ('name', 'role')
print(f'{regular_tuple[0]} is a {regular_tuple[1]}')

User = namedtuple('User', 'name role')
human = User(name='ted', role = 'checkerboard')
print(f'{human.name} is a {human.role}')
