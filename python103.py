import csv
import random

from collections import defaultdict, namedtuple, Counter, deque
from urllib.request import urlretrieve

regular_tuple = ('name', 'role')
print(f'{regular_tuple[0]} is a {regular_tuple[1]}')

User = namedtuple('User', 'name role')
human = User(name='ted', role = 'checkerboard')
print(f'{human.name} is a {human.role}')


# Straight forward enough, namedtuple just turns your regular tuple into an object.
# And below is dicts.
# dicts all the way down.
users = {'user1': 'role1'}
print(users['user1'])
try:
    print(users['user2'])
except:
    print('There are no users matching that name or description.')

print(users.get('user1'))
print(type(users.get('user1')))
print(users.get('user2') is None)
print(type(users.get('user2')))

user_collection = [('user1', 10), ('user2', 12), ('user3', 7),
                   ('user4', 3), ('user5', 15), ('user6', 20)]

challenges = {}
for user, challenge in user_collection:
    challenges['user'].append('challenge')

print(challenges)