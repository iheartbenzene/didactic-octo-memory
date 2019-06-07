import data

numlist = [1, 2, 3, 4, 5]
list_of_numbers = [x + 1 for x in range(5)]

print(numlist)
print(list_of_numbers)

numlist.reverse()
print('reversed: ', numlist)
numlist.sort()
print('sorted: ', numlist)

my_string = 'jubbles'
print('The improper way, haha: ')
for s in my_string: # because strings are lists in Python.
    print(s)
    
print('The proper way: ')
for s in list(my_string): # the proper way
    print(s)
    
lst = list(my_string)
tpl = tuple(my_string)

print('As a list = ', lst)
print('As a tuple = ', tpl)

print('The first item in the list is: ', lst[0])
lst[0] = 'foo'
print('Then overwritten by \'foo\', it becomes:', lst)

print('Compare that with the tuple: ', tpl[0])
print('Overwritten by \'bar\', it becomes: ')
try: 
    tpl[0] = 'bar'
except:
    print('Haha! Nice try but you can\'t assign items in a tuple.')

print('Now popping: ')
l7 = lst.pop()
print('This, {}, got popped off just now'.format(l7))
print('So our list is now: {}, implying that \'pop\' takes off the item at the end.'.format(lst))

lst.insert(5, 'bar')
print('Then `insert` gives: {}, at the particular index.'.format(lst))

l2 = lst.pop(2)
print('Okay, so I lied a little bit about `pop`.')
print('Check it out, {}, came off at index 2.'.format(l2))
print('So the list is now: ', lst)
lst.insert(2, 'lala')
print('The list with a new `insert`: ', lst)
del lst[2]
print('Then there\'s the `del` command...: ', lst)
print('Nothing gets assigned. Just...(T_T)')

bagels = {'jubbles': 30, 'ark': 31, 'lucy': 33}
print('bagels: ', bagels)

people = {}
people['jubbles'] = 30
print('people: ', people)
people['ark'] = bagels['ark']
print('people: ', people)
print('bagels: ', bagels)

print('bagel keys: ', bagels.keys())
print('bagel values: ', bagels.values())
print('bagel items: ', bagels.items())

for keys in bagels.keys():
    print('key = ', keys)
    
for values in bagels.values():
    print('values = ', values)
    
for k, v in bagels.items():
    print(k + ' ' + str(v))
    
for k, v in bagels.items():
    print('%s is %s, haha' % (k, v))
    
