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
users = {'person1': 'role1'}
print(users['person1'])
try:
    print(users['person2'])
except:
    print('There are no users matching that name or description.')

print(users.get('person1'))
print(type(users.get('person1')))
print(users.get('person2') is None)
print(type(users.get('person2')))

user_collection = [('user1', 10), ('user2', 12), ('user3', 7),
                   ('user4', 3), ('user5', 15), ('user6', 20)]

print(user_collection)

try:
    challenges = {}
    for user, challenge in user_collection:
        challenges[user].append(challenge)
    print('challenges = ', challenges)
except:
    challenges2 = defaultdict(list)
    for user, challenge in user_collection:
        challenges2[user].append(challenge)
    print('challenges2 = ', challenges2)
    
    
words = ''' Lorem Ipsum is simply dummy text of the typsetting
and printing industry. Lorem Ipsum has been the industry's standard
for dummy text since the 1500s, when an unknown printer took a galley
of text and scrambled it to make a type specimen book. It has 
survived not only five centuries but also the leap into electronic 
typesetting, remaining essentially unchanged. It was popularized in
the 1960s with the release of Letraset sheets containing Lorem Ipsum 
passages, and more recently with desktop publishing software like Aldus
Pagemaker including versions of Lorem Ipsum.'''.split()

print(words[:5]) 

commonly_used_words = {}

for word in words:
    if word not in commonly_used_words:
        commonly_used_words[word] = 0
    commonly_used_words[word] += 1
    
for keyed, valued in sorted(commonly_used_words.items(), key = lambda x: x[1], reverse=True)[:5]:
    print(keyed, valued)
    
counted_common_words = Counter(words).most_common(5)
print(counted_common_words)