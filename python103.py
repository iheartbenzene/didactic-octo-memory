import csv
import random
import timeit

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

lst = list(range(10000000))
deq = deque(range(10000000))

def insert_or_delete(data_structure):
    for _ in range(10):
        index = random.choice(range(100))
        data_structure.remove(index)
        data_structure.insert(index, index)
        
# print(timeit.timeit(insert_or_delete(lst)))
# print(timeit.timeit(insert_or_delete(deq)))

# movie_data = "https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv"
movie_data = 'movie_metadata.csv'
movies_csv = 'movies.csv'
# urlretrieve(movie_data, movies_csv)

Movie = namedtuple('Movie', 'title year score')

# import pandas as pd 

def get_movie_by_director(movies_csv):
    directors = defaultdict(list)
    with open(movie_data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            
            m = Movie(title = movie, year = year, score = score)
            directors[director].append(m)
    return directors

directors = get_movie_by_director(movies_csv)
print(directors['Christopher Nolan'])

counts = Counter()
for director, movies in directors.items():
    counts[director] += len(movies)
    
print(counts.most_common(5))