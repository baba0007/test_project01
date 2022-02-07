# Dictionary data structure:
'''
lis = [10, 20, 30, 40]  # list
t = (10, 20, 30, 40)  # tuple
s = {10, 20, 30, 40}  # set
d = {100: 'durga', 200: 'ravi'}  # dictionary

# when should we shoose to use dictionary:
# 1-when we need key-value pairs
# 2-Duplicate keys not allowed but values if they are duplicated no probleem it is allowed
# 3-insertion order is not preserved and it is based on hash code of the keys
# 4-indexing & slicing are not allowed.
# 5-hetrogenious objects are allowd for keys and values.
# 6-is mutable (we can perform changes in both keys and values)
# 7-Dynamic (we can increase and decrease)
# 8-Syntax: d ={k1:v1, k2:v2, k3:v3}


# d = {100: 'durga', 'A': 300, 200: 'Ravi', 'B': 400, 100: 'shiva'}
# print(f'd = {d}')

# creation of dict objects:
# 1-empty dictionary:
d = {}
d = dict()

# 2-if we know data already:
d = {100: 'durga', 200: 'ravi'}

# 3-by using dict():
# ex:list of tuple
l = [(100, 'A'), (200, 'B'), (300, 'C')]
d = dict(l)
print('d = {}'.format(d))

# tuple of tuples:
lis = ((100, 'A'), (200, 'B'), (300, 'C'))
d = dict(l)
print('d = {}'.format(d))

# set of tuples:
lis = {(100, 'A'), (200, 'B'), (300, 'C')}
d = dict(l)
print('d = {}'.format(d))

# list of lists:
lis = [[100, 'A'], [200, 'B'], [300, 'C']]
d = dict(l)
print('d = {}'.format(d))

# tuple of lists
lis = ([100, 'A'], [200, 'B'], [300, 'C'])
d = dict(l)
print('d = {}'.format(d))

# set of lists wont work error : TypeError: unhashable type: 'list' , list objects are unhashable:
# l = {[100, 'A'], [200, 'B'], [300, 'C']}
# print('d = {}'.format(d))

# in case of more elements in a tuple inside a list will return ValueError:
# ValueError: dictionary update sequence element #0 has length 3; 2 is required

# -------------------------------------

lis = [(100, 'A', 300), (200, 'B'), (300, 'C')]
d = dict(l)
print('d = {}'.format(d))

# --------------------------------------
# 4-by using dynamic input:
# d = eval(input('Enter dictionary: '))
# print('d = {}'.format(d))
'''
# ----------------------------------
# how to access data from the dictionary:
'''
d = {100: 'durga', 200: 'ravi', 300: 'shiva'}
print(f'd[100] = {d[100]}')
print(f'd[200] = {d[200]}')
print(f'd[300] = {d[300]}')
# print(f'd[700] = {d[700]}')  # will return keyerror

d = {100: 'durga', 200: 'ravi', 300: 'shiva'}
key = int(input('Enter key: '))
if key in d:
    print(f'The value of {key} = {d[key]}')
else:
    print(f'The key {key} has no value.')

'''
# -------------------------------
'''
# how to add/update data in dict: syntax d[key]=value
d = {100: 'durga', 200: 'ravi'}
d[300] = 'shiva'
print(f'd = {d}')
d[100] = 'sunny'  # the value sunny will replace durga
print(f'd = {d}')

# how to delete data from dict:
d = {100: 'durga', 200: 'ravi', 300: 'shiva'}
del d[200]
print(f'd = {d}')
del d[100], d[300]
print(f'd = {d}')
'''
# ------------------------------------
# wap a program to enter name and marks into dictionary and display
# information on the screen:
'''
n = int(input('Enter number of Students: '))
d = {}
for i in range(n):
    name = input('Enter name of Student: ')
    marks = int(input('Enter marks of Student: '))
    d[name] = marks
# print(f'd = {d}')
print('*' * 30)
print('Name', '\t\t', 'Marks')
print('*' * 30)
for name in d:
    print(name, '\t\t', d[name])
'''
# ----------------------------------------
'''
# Operators for dict:
d1 = {100: 'A', 200: 'B'}
d2 = {300: 'C', 400: 'D'}
d3 = {200: 'B', 100: 'A'}
# d3 = d1 + d2
# print(d3)  # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# d4 = d1 * 3
# print(d4) # TypeError: unsupported operand type(s) for *: 'dict' and 'int'
print(f'd1 == d2: {d1 == d2}')
print(f'd1 != d2: {d1 != d2}')
print(f'd1 == d3: {d1 == d3}')
# print(d1 > d2) # TypeError: '>' not supported between instances of 'dict' and 'dict'
# print(d1 < d2) # TypeError: '<' not supported between instances of 'dict' and 'dict'

# Membership operators: applicable only for keys not values:
print(f'100 in d1: {100 in d1}')
print(f'300 in d1: {300 in d1}')
# will return False always coz membership is applicble only for keys not values.
print('A in d1: {}'.format('A' in d1))
'''
# -----------------------------------
# Important Functions/Methods for dict:
# 1-len(): will return lenght of keys in the dict: syntax: len(d)
'''
d = {100: 'A', 200: 'B'}
print(f'lenght of d is: {len(d)}')

# 2-get(): syntax: d.get(k) # incase the key is not there it will return None
d = {100: 'A', 200: 'B', 300: 'C'}
print(f'd.get(100) = {d.get(100)}')
print(f'd.get(700) = {d.get(700)}')  # will return None
# print(f'd.get(700) = {d[700]}') # will return KeyError
print(d.get(700, 'baba'))
# will return Guest instead of None if key is not available, we can use any value as default  than Guest
print('d.get(700) = {}'.format(d.get(700, 'Guest')))

# 3-update(): syntax d1.update(d2) will add all items of d2 to d1
d1 = {100: 'A', 200: 'B'}
d2 = {300: 'C', 400: 'D', 100: 'Mustapha'}
d1.update(d2)
print(f'd1 = {d1}')
'''
# ----------------------------------------
# Important Methods and functions for dict:keys(), values(), items():
# 1-keys(): syntax: k = d.keys()
'''
d = {100: 'A', 200: 'B', 300: 'C', 400: 'D'}
# print(d.keys())
print('Keys are: ')
for k in d.keys():
    print(k)
# 2-values(): syntax: v = d.values()
# print(d.values())
print('Values are: ')
for value in d.values():
    print(value)

# 3-items(): i = d.items()
# print(d.items())
for item in d.items():
    print(item)
print('*' * 30)
print('Keys' + '\t\t' + 'Values')
print('*' * 30)
for k, v in d.items():
    print(k, '\t\t',    v)
'''
# -------------------------------------
'''
# wap to get value from the dictionary for the given key ?
d = {100: 'A', 200: 'B', 300: 'C', 400: 'D'}
# d = {100: 'A', 200: 'A', 300: 'A', 400: 'D'}
# based on key finding value:
# print('d[100 =]', d.get(100))
key = int(input('Enter key: '))
if key in d:
    print(f'value = {d.get(key)}')
else:
    print('The corresponding value is not available.')

# wap to get key from the dictionary for the given value ?
value = input('Enter value: ')
available = False
for k, v in d.items():
    if v == value:
        print(f'key = {k}')
        available = True

if available == False:
    print('The corresponding key not found.')
'''
# ----------------------------------
'''
# Important Functions/methods for dict:
# 1-pop(key):
# removes item associated with specified key and returns the corresponding value:
# incase key is not available , it will returns KeyError
# d = {100: 'A', 200: 'B', 300: 'C', 400: 'D'}
# print('d.pop(300) =', d.pop(300))
# print(f'd = {d}')
# print(d.pop(700)) # will return KeyError
# d.pop(100, 'A')
# print(f'd = {d}')
# print(d.pop(300, 'Guest'))
# print(f'd = {d}')
# print(d.pop(700, 'Guest'))
# print(f'd = {d}')

# 2-popitem(): will remove one random key-value pair which we dont know which:
d = {100: 'A', 200: 'B', 300: 'C', 400: 'D'}
# print(d.popitem())
# print(d.popitem())
# print(d.popitem())
# print(d.popitem())
# print(f'd = {d}')
# print(d.popitem()) will return KeyError incase dict is empty
d.clear()
print(f'd = {d}')
'''
# ------------------------------
'''
# Important Functions/methods for dict:
d = {100: 'A', 200: 'B', 300: 'C'}
# if key is already in dict then d.setdefault will not overwrite
# if key is not available then d.setdefault will add key value to dicy:
d.setdefault(700, 'E')
d.setdefault(700, 'D')
print(d)

# Aliasing and cloning:
# 1-Aliasing: any change in both dict will affect both:
d1 = {100: 'A', 200: 'B'}
d2 = d1
d2[300] = 'C'
print(d1)
'''
# 2-Cloning: copy() any changes will not affect both:
'''
d1 = {100: 'A', 200: 'B'}
d2 = d1.copy()
d2[300] = 'C'
print(f'd1 = {d1}')
print(f'd2 = {d2}')
'''
# ------------------------------
# Important Methods and Functions for dict
'''
len()
get(key) and get(key, value)
d1.update(d2)
d.keys()
d.values()
d.items()
d.pop(key) and d.pop(key, value)
d.popitem()
d.clear()
d.setdefault(key, value)
d2 = copy(d1)
'''
# --------------------------------
# wap to take dictionary from the keyboard and print sum of values:
'''
d = eval(input('Enter dict: '))
sum = 0
for item in d.items(): # will return tuples
    sum = sum + item[1]
print(sum)
'''
# or
# d = eval(input('Enter dict: '))
# print('Sum of the values =', sum(d.values()))

# -------------------------------------
# wap to find number of occurences of each letter present in the given string:
'''
word = input('Enter string: ')
d = {}
for ch in word:
    d[ch] = d.get(ch, 0) + 1
for k, v in d.items():
    print(f'{k} occurs {v} times')

# print(f'd = {d}')
'''
# -------------------------------
'''
word1 = 'This is a test list'.lower()
dict = {}
for ch in word1:
    dict[ch] = dict.get(ch, 0) + 1
for k, v in dict.items():
    print(f'{k} occurs {v} times.')
'''
# ---------------------------------------
# wap to find number of occurrences of each vowel present in the given string then sort the answer:
'''
word2 = 'hello there how are you ?'
vowel = ['a', 'e', 'i', 'o', 'u']
dict = {}
for ch in word2:
    if ch in vowel:
        dict[ch] = dict.get(ch, 0) + 1
print(dict)
'''
# ---------------------------
'''
# sorted answer
word2 = input('Enter String: ')
vowel = ['a', 'e', 'i', 'o', 'u']
dict = {}

for ch in sorted(word2):
    if ch in vowel:
        dict[ch] = dict.get(ch, 0) + 1
for k, v in dict.items():
    print(f'{k} occours {v} times.')
'''
# ---------------------------------
# 1-wap a program to accept student name and marks from the keyboard and creates a dictionary.
# 2-Also display student marks by taking student name as input ?
# 3-option to continue or stop.
'''
# 1-
n = int(input('Enter number of students: '))
d = {}
for i in range(n):
    name = input('Enter student name: ')
    marks = int(input('Enter marks: '))
    d[name] = marks  # will add name and marks to dictionary d.
print('')
print('Student Data Table: ')
print('*' * 30)
print('Name', '\t\t', 'Marks')
print('*' * 30)
for k, v in d.items():
    print(k, '\t\t', v)
print('')

# 2-& 3-search for student marks and option to continue or stop:

while True:
    Name = input('Enter Student name: ')

    if Name not in d:

        print('Student not found!')

    else:
        print(f'{Name} marks is: {d[Name]}')

    option = input('Do you want to find another student marks (y/n) ?: ')
    if option.lower() == 'n':
        break
print('Thanks for using This application...')
'''
# ----------------------------------------------
# Dict comprehension:
# it is applicable for list, set , dict , but not tuple

# list comprehension:
# l = [x * x for x in range(1, 6)]
# print('l =', l)

# dict comprehension:
'''
d1 = {x: x * x for x in range(1, 6)}  # x is the key and x*x is the value
print(f'd1 = {d1}')

d2 = {x: 2**x for x in range(1, 6)}
print(f'd2 = {d2}')
'''
# ----------------------------------------
'''
# Merging of collections:
# 1-List merging:
l1 = [10, 20]
l2 = [30, 40]
l3 = l1 + l2
print(f'l3 = {l3}')
# second way of merging which is common for dicts anf sets and tuples
l4 = [*l1, *l2]
print(f'l4 = {l4}')

print('')
# 2-Tuple merging:
t1 = (10, 20)
t2 = (30, 40)
t3 = t1 + t2
print(f't3 = {t3}')

# second way:
t4 = (*t1, *t2)
print(f't4 = {t4}')
print('')

# set merging:
try:
    s1 = {10, 20}
    s2 = {30, 40}
    s3 = s1 + s2
except:
    print("+ operator not applicable for the set: TypeError")

# second way:
s1 = {10, 20}
s2 = {30, 40, 10}  # set eliminate duplication.
s3 = {*s1, *s2}
print(f's3 = {s3}')
print('')
# dict merging:
try:

    d1 = {100: 'A', 200: 'B'}
    d2 = {300: 'C', 400: 'D', 100: 'baba'}
    d3 = d1 + d2
except:
    print('+ operator not supported by merging dictionary: TypeError')

# second way
d4 = {**d1, **d2}
print(f'd4 = {d4}')
'''
# ------------------------------------------------
# Nested Collections: Collection inside another collection like dictionary inside list and so ....
# List of Tuple is a nested collection:
# 1 -
'''
l1 = [(10, 20, 30), (40, 50, 60)]
print(l1[0][1])
print(l1[1][2])

# 2-
d = {'cars': ('skoda', 'suzuki', 'polo'),
     'mobiles': ('Samsung', 'Iphone', 'Nokia')}
print(d['cars'][0])
print(d['mobiles'][2])
print(d.get('cars')[2])

print('')
# display all mobiles:
for mobile in d['mobiles']:
    print(mobile)
'''
# --------------------------------------
# Implementation of supermarket by using dict:
'''
supermarket = {'store1': {'name': 'Durga General Store',
                          'items': [{'name': 'soop', 'quantity': 20},
                                    {'name': 'brush', 'quantity': 30},
                                    {'name': 'pen', 'quantity': 40}]
                          },

               'store2': {'name': 'Sunny Book Store',
                          'items': [{'name': 'python', 'quantity': 100},
                                    {'name': 'django', 'quantity': 200},
                                    {'name': 'java', 'quantity': 300}]
                          }
               }

# 1 -print of store1:
print('Name of Store1 is: ', supermarket['store1']['name'])
# print('Name of Store1 is: ', supermarket.get('store1')['name'])
# print('Name of Store1 is: ', supermarket.get('store1').get('name'))
print('')
# 2- print all items present in store1:
print('Name of items in Store1 are: ')
for dict in supermarket['store1']['items']:
    print(dict['name'])

print('')
# how many django book are available in store2:
print('Numbers of django books in store2: ')
print(supermarket['store2']['items'][1]['quantity'])

# or:
for dict in supermarket['store2']['items']:
    if dict['name'] == 'django':
        print(dict['quantity'])
'''
# ----------------------------------
'''
# home inventory example:
print('Home inventory: ')
n = 4
d = {}
for i in range(n):
    name = input('Enter Expense: ')
    marks = int(input('Enter price: '))
    d[name] = marks  # will add name and marks to dictionary d.
print('')
print(f'd = {d}')
print('')
print('Home Inventory: ')
print('*' * 30)
print('Expense', '\t', 'Price')
print('*' * 30)
for k, v in d.items():
    print(k, '\t\t', v)
print('')


while True:
    Name = input('Enter Expense name: ')

    if Name not in d:
        print('Expense not foud')

    else:
        print(f'{Name} price is {d[Name]}')

    option = input('Do you want to continue ? (yes/no): ')
    if option.lower() == 'no':
        break
print('')
print('Thanks for using our Application.')
'''
# ----------------------------------------------
# list inside set and dictionary:
# list is unhashable
# set is hashable that is why we cannot add list in set
# tuple us hashable , we cannot add list in
# dictionary key is hashable , we cannot add list in
'''
s = {(10, 20, 30)}  # can add tuple inside set coz both are hashable.
print('s =', s)
# s = {(10, 20, 30), [40, 50, 60]} # will return TypeError unhashable type: 'list'
# d = {(10, 20): 'iteme1', [30, 40]: 'iteme2'} # TypeError: unhashable type list , in dict kkey should be hashable.
d1 = {(10, 20): 'iteme1'}
print(f'd1 = {d1}')

# value as list is no problem even it is unhashable, but key should not be a list.
d2 = {(10, 20): 'item1', (30, 40): [50, 60]}
print(f'd2 = {d2}')
'''
