# video 07/136
# https://www.w3schools.com/python/python_ref_dictionary.asp
# print(int('0b11000000', 2))
# print(bin(192))

'''
username = input('Enter your username: ')
password = input('Enter password: ')
password1 = len(password) * ('*')
print(f'{username} your password {password1} is {len(password)} characters long.')
'''
# -------------------------------------------
'''
# to hide password
from getpass import getpass
password = getpass(prompt='Enter password: ')
password1 = len(password) * '*'
print(f'The lenght of your password is {len(password)} characters long.')

# print('The lenght of you password is: {}'.format(len(password)))
'''
# -----------------------------------------------
'''
from covid import Covid
covid = Covid()
cases = covid.get_status_by_country_name(input('Enter Country name: '))
# print(type(cases))
print(f'Numbers of keys is: {len(cases)}: ')
print('Numbers of Confirmed cases: {}'.format(cases['confirmed']))
for x in cases:  # x is key, cases[x] is value
    print(f'{x}: {cases[x]}')
'''
# -------------------------------------
'''
lis = ['a', 'c', 'b', 'd', 'e', 'd', 'g', 'f']
print(lis.index('a', 0, 4))  # print(lis.index('a', start, stop))
# print(lis.index('a', 1, 4)) # will return ValueError coz 'a' not in list starting from 1 to 4

print(lis.count('d'))
lis.sort()
print(f'lis = {lis}')
lis2 = lis.copy()
print(f'lis2 = {lis2}')
print(sorted(lis2))
# ------------------
lis.sort()
lis.reverse()
print(lis)
'''
# ---------------------
# list unpacking:
'''
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)
'''
# ------------------------------------
'''
# covid-19 checkup:
from covid import Covid
covid = Covid()
cases = covid.get_status_by_country_name(input('Enter Country name: '))
# print(type(cases))

print('*' * 30)
print('Keys' + '\t\t ' + 'Values')
print('*' * 30)

# print(f'Numbers of keys is: {len(cases)}: ')
for x in cases:  # x is key, cases[x] is value
    print(f'{x}: \t {cases[x]}')
'''
# -----------------------------------
# covid-19 checkup:
'''
from covid import Covid
covid = Covid()
cases = covid.get_status_by_country_name(input('Enter Country name: '))
# print(type(cases))

print('*' * 30)
print('Keys' + '\t\t\t ' + 'Values')
print('*' * 30)

for k, v in cases.items():  # x is key, cases[x] is value
    print(f'{k}: \t\t {v}')
    # print(k, '\t', v)
'''
# ------------------------------------
'''
# https://www.w3schools.com/python/python_ref_dictionary.asp

dict = {
    'a': [1, 2, 3],
    'b': 'Hello',
    'c': 3
}
print(dict['a'])
print(dict['a'][2])
'''
# ------------------------------
'''
my_list = [
    {
        'a': [1, 2, 3],
        'b': 'Hello',
        'c': 3
    },

    {
        'a': [4, 5, 6],
        'b': 'Bello',
        'c': 48
    }

]
print(my_list[0]['a'])
print(my_list[0]['a'][0])
print(my_list[1]['b'])
'''
# -------------------------------
'''
d = {}
d['name'] = 'baba'
d['age'] = 52
print('d =', d)
# --------------------------
user = dict(name='baba')
user['age'] = 52
user['Gender'] = 'Male'
print('user =', user)
# ------------------------------
d3 = user.copy()
print('d3 =', d3)
# -------------------------------
print('Gender' in user)
print('Gender' in user.keys())
print('Gender' in user.values())
print('Gender' in user.items())
print(('Gender', 'Male') in user.items())
# user.clear()
print(user)
# user.pop('Gender')
print(user)
# will remove the last item not always it can remove any one so, be careful.
# user.popitem()
print(user)
user.update({'age': 55})
user.update({'size': '100cm'})
print(user)
'''
# ----------------------------------
# Tuple: immutable, only 2 methods are available for tuples : count() and index()
'''
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])
print(5 in my_tuple)
x, y, z, *other = my_tuple
print(x)
print(y)
print(z)
print(other)
print(my_tuple.count(1))
print(my_tuple.index(1))
print(len(my_tuple))
'''
# ----------------------------------
# sets:anordered, no duplicate
'''
my_set = {1, 2, 3, 4, 5, 6, 6}
print(my_set)
my_set.add(100)
my_set.add(2)  # will not be added coz no duplicating is sets
print(my_set)
# print(my_set[0])  # no indexing are supported by sets
print(1 in my_set)
print(len(my_set))
print(list(my_set))
x = list(my_set)
x.append(200)
print(x)
new_set = my_set.copy()
print('new_set =', new_set)
my_set.clear()
print(my_set)

school = {'Bobby', 'Tammy', 'Jammy', 'Sally', 'Danny'}
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']
print('The absent student was: ', school.difference(attendance_list))
'''
# -----------------------------------
'''
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
# print(my_set.difference(your_set))
# my_set.discard(5)
# print(my_set)
# my_set.difference_update(your_set)
# print(my_set)
print(my_set.intersection(your_set))
# print(my_set & your_set)

print(my_set.isdisjoint(your_set))
print(my_set.union(your_set))
# or print(my_set | your_set)
print(my_set.issubset(your_set))  # is my_set a subset of your_set
print(my_set.issuperset(your_set))
print(your_set.issuperset(my_set))  # does your_set include all my_set
'''
# ----------------------------
'''
import colorama as i
import termcolor as t

i.init()
print(t.colored('Hello world', 'blue', 'on_yellow'))
'''
# ------------------------------
# Teneary Operator:
# condition_if_true if condition else condition_if_false
'''
is_friend = True
can_message = 'message allowed' if is_friend else 'not allowed message'
print(can_message)

# Short Circuiting:
is_friend = False
is_User = True
print(is_friend and is_User)

if is_friend or is_User:
    print('Best friend forever.')

if is_friend and is_User:
    print('Best friend forever.')
else:
    print('Not best friend.')
'''
# -------------------------------------
'''
is_magician = False
is_expert = True

if is_magician and is_expert:
    print('You are a master.')

elif is_magician and not is_expert:
    print('at least you are getting there.')

elif not is_magician:
    print('You need magic powers.')
'''
# -----------------------------------
'''
# is compare memory location
print(True == 1)  # True
print('' == 1)  # False
print([] == 1)  # False
print(10 == 10.0)  # True
print([] == [])  # True
print()
print(True is 1)  # False
print([] is [])  # False
print(10 is 10)  # True
'''
# ----------------------------------
'''
numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
even = [i for i in numbers if i % 2 == 0]
odd = [i for i in numbers if i % 2 != 0]
print(f'even = {even}')
print(f'odd = {odd}')
'''
# ---------------------------------
'''
user = {
    'name': 'baba',
    'age': 52,
    'gender': 'male'
}
for k, v in user.items():
    print(k,':', v)
'''
# ---------------------------------
'''
# counter : calculate the sum of the list:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('sum =', sum(my_list))
sum = 0
for item in my_list:
    sum = sum + item
print('sum =', sum)
'''
# --------------------------
'''
# range()
sum = 0
for i in range(101):
    sum = sum + i
print(sum)
'''
# ------------------
'''
for _ in range(0, 10, 2):
    print(list(range(10)))
'''
# ------------------------
# enumerate():
'''
for i, char in enumerate('hello'):  # will return the index and the item of it.
    print(char, i)
'''
# wap that tell you what is the index of the number 50 in a range:
'''
for i, char in enumerate(list(range(100))):
    # print(i, char)
    if char == 50:
        print(f'index of {char} is {i}')
        # break # to not continue till 99
'''
# -------------------------------
# while loop:
'''
i = 0
while i < 10:
    print(i)
    i += 1
else:
    print('Done!')
'''
# -----------------------
'''
my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)
print()
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
'''
# ------------------------
'''
while True:
    response = input('say something: ')
    if response == 'bye':
        break
'''
# ----------------------------------------
'''
# exercice:
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
i = 0
fill = '#'
empty = ' '
while i < 3:
    for row in picture:
        for pixel in row:
            if pixel == 0:
                print(empty, end='')
            else:
                print(fill, end='')
        print('')  # for new line after evry row
    print('')
    i += 1
'''
# ---------------------------------------
'''
# check for duplicate in list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate = []
for item in some_list:
    if some_list.count(item) > 1:
        if item not in duplicate:
            duplicate.append(item)
print('duplicated items are :', duplicate)
'''
# ----------------------------------------
# Functions:

'''
def say_hello(name):
    print('Hello', name)


name = 'Mustapha'
say_hello(name)
'''
# --------------------------
'''
# Functions:
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

fill = '#'
empty = ' '


def show_tree():
    for row in picture:
        for pixel in row:
            if pixel == 0:
                print(empty, end='')
            else:
                print(fill, end='')
        print('')  # for new line after evry row
    print('')


show_tree()
show_tree()
'''
# ----------------------------------
# parameters:

'''
def say_hello(name, emoji):

    print(f'hello {name} {emoji}')


# positional argumensts : should be in order: in this case: name then emoji:
say_hello('Mustapha', ':)')

# keyword arguments:
say_hello(emoji=':)', name='baba')
'''
# Default parameters:
'''
def say_hello(name='John', emoji=':)'):

    print(f'hello {name} {emoji}')


say_hello('dialo', ':)')
say_hello()
say_hello('Amina')
'''
# ------------------------

'''
def sum(num1, num2):
    return num1 + num2


total = sum(10, 5)
print(sum(4, total))
'''
# ----------------------
'''
def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)


total = sum(10, 20)
print(total)
'''
# -------------------------------------
'''
age = input("What is your age?: ")


def checkDriveAge():

    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


checkDriveAge()
'''
# ------------------------------
# Methods vs Functions:
'''
# s = 4


# def call():
    #'''
# Docstrings:
# You need to use Return or print inside the function to get a print.
#'''
# s = 10


# print(help(call))
# print(s)

# ----------------------------
# clean code:
'''
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(is_even(7))
'''
# -----------------------
# or

'''
def is_even(num):
    if num % 2 == 0:
        return True
    return False


num = int(input('Enter Number: '))
print(f'{num} is it even ?: {is_even(num)}')
'''
# -------------------------
# or
'''

def is_even(num):
    return num % 2 == 0


num = int(input('Enter Number: '))
print(f'{num} is it even ?: {is_even(num)}')
'''
# --------------------------------
# *args **kwargs

'''
def super_func(*args):
    return sum(args)


args = 1, 2, 3, 4, 5
print(f'sum of {args} = {super_func(*args)}')
'''
# **kwargs:
'''

def super_func(*args, **kwargs):
    total = 0
    # print('kwargs =', kwargs)
    # print('args =', args)
    for items in kwargs.values():
        total = total + items
    print('total =', total)
    return sum(args) + total


args = 1, 2, 3, 4
kwargs = {'num1': 5, 'num2': 6}

print(f'{args} + {kwargs.values()} = {super_func(1, 2, 3, 4, num1=5, num2=6)}')
'''
# --------------------------------------
# wap that print the highest even in a list:
'''
def highest_even(li):
    evens = []
    for i in li:
        if i % 2 == 0:
            evens.append(i)
    return max(evens)


li = [10, 2, 3, 4, 8, 11, 40]
# li = eval(input('Enter a list: '))
print(f'The highest even number in {li} is: {highest_even(li)}')
'''
# ---------------------------------
# Scope is : what variables do i have access to ?
'''
x = 10


def some_func():
    total = 100
    print(total)


print(x)


some_func()
'''
# --------------------------------------
'''
a = 1


def confusion():
    a = 5
    return a


print('Global a =', a)
print('Local a =', confusion())
'''
# ------------------------------------
'''
a = 1


def parent():
    a = 10

    def confusion():
        return a
    return confusion()


print(parent())
print(a)
'''
# -----------------------------------
'''
total = 0


def count():
    global total
    total += 1
    return total


count()
count()
print(count())
print(count())
print(count())
print(count())
'''
# ------------------------------
# OOP = object oriented Programing
# everything in python is an object

'''
class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        if self.membership:
            self.name = name  # is an attribute
            self.age = age  # is an attribute

    def shout(self):
        print(f'My name is {self.name}')
        return '!!!!!'  # to not get None


player1 = PlayerCharacter('baba', 52)
player2 = PlayerCharacter('dialo', 45)
player1.gender = 'Male'
player2.gender = 'Female'

print(player1.name, 'is', player1.age, player1.gender)
print(player2.name, 'is', player2.age, player2.gender)

print(player1.membership)
print(player2.membership)

print(player1.shout())
print(player2.shout())
'''
# ---------------------------------------

'''
class PlayerCharacter:
    membership = True

    def __init__(self, name='anonymous', age=0):
        if age > 18:
            self.name = name  # is an attribute
            self.age = age  # is an attribute

    def shout(self):
        print(f'My name is {self.name}')
        return '!!!!!'  # to not get None


player1 = PlayerCharacter('Tom', 20)
# player2 = PlayerCharacter()
player1.gender = 'Male'
# player2.gender = 'Female'

print(player1.name, 'is', player1.age, player1.gender)
# print(player2.name, 'is', player2.age, player2.gender)

print(player1.shout())
# print(player2.shout())
'''
# -----------------------------------------
# exercise :

# Given the below class:

'''
class Cat:
    # species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
baba = Cat('baba', 3)
dialo = Cat('dialo', 4)
garlfield = Cat('garlfield', 6)

# 2 Create a function that finds the oldest cat


def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(
    f'The oldest Cat is {oldest_cat(baba.age, dialo.age, garlfield.age)} years old.')
'''
# --------------------------------------

'''
class PlayerCharacter:
    membership = True

    def __init__(self, name='anonymous', age=0):
        if age > 18:
            self.name = name  # is an attribute
            self.age = age  # is an attribute

    def shout(self):
        print(f'My name is {self.name}')
        return '!!!!!'  # to not get None

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Mustapha', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Tom', 20)
# player2 = PlayerCharacter()
player1.gender = 'Male'
# player2.gender = 'Female'

print(player1.name, 'is', player1.age, player1.gender)
# print(player2.name, 'is', player2.age, player2.gender)

print(player1.shout())
print(player1.adding_things(3, 5))
print(PlayerCharacter.adding_things(3, 5))

player3 = PlayerCharacter.adding_things(10, 25)
print(player3.age)
'''
# -------------------------------
# Review:
'''
class NameOfClass():
    class_attribute = 'value'
    def __init__(self, param1, param2):
        self.param1 = param1
        self,param2 = param2

    def method(self):
        # code
        pass # delete pass after inserting code.

    @classmethod
    def cls_method(cls, param1, param2):
        # code
        pass

    @staticmethod
    def stc_method(param1, param2):
        # code
        pass

'''
# ------------------------------------
# Encapsulation, Abstraction, inhetance, Polymorphism
'''
class PlayerCharacter():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self.name} and I am {self.age} years old.')


player1 = PlayerCharacter('baba', 52)
# print(player1.name, player1.age)

# player1.run()
player1.speak()
'''
# -----------------------------------
# Users:
# -Wizards
# -Archers
# -Orgres

'''
class User():
    def sign_in(self):
        print('logged in')

# inhetance


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 500)
# print(wizard1.sign_in())
# print(archer1.sign_in())
wizard1.attack()
archer1.attack()

# isinstance:
wizard1 = Wizard('Merlin', 50)
# True wizard1 isinstance of the class Wizard
print(isinstance(wizard1, Wizard))
# True wizard1 isinstance of User
print(isinstance(wizard1, User))
# True wizard1 isinstance of python object class
print(isinstance(wizard1, object))
'''

# Polymorphism = many forms

'''
class User():
    def sign_in(self):
        print('logged in')

# inhetance


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')


wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 30)


def player_attack(char):
    char.attack()


# same function giving different output.
player_attack(wizard1)
player_attack(archer1)

print('')
# or
for char in [wizard1, archer1]:
    char.attack()
'''

# ---------------------
# pure function:

'''
def multiplay_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


li = [1, 2, 3, 4, 5]
print(multiplay_by2(li))
'''

# map(), filter(), zip(), reduce()
# 1- map(action, data_structure)
'''
def multiplay_by2(item):

    return item * 2


items = [1, 2, 3, 4, 5]
# print(map(multiplay_by2, li))  # to view this map we need to turn it to a list
print(list(map(multiplay_by2, items)))
'''
# ----------------
# 2-ex2:
'''
my_list = [1, 2, 3, 4, 5]
def multiplay_by2(item):

    return item * 2


print(list(map(multiplay_by2, my_list)))
print(my_list)
'''
# -------------------------------
# filter():
'''
my_list = [1, 2, 3, 4, 5]


def only_odd(item):
    return item % 2 != 0


print('new_odd_list =', list(filter(only_odd, my_list)))
# print(list(map(multiplay_by2, my_list)))
print(f'my_list = {my_list}')

# ex2:
lis = ['Mustapha', 'Labib', 'Amina', 'Sofiane', 'Driss']


def first_letter(item):
    return item[0] == 'D'


print(list(filter(first_letter, lis)))
#-----------------

print(list(map(lambda i: i**2, range(10))))
print(list(filter(lambda i: i % 2 == 0, range(10))))

#-----------------------


# -------------------------------
# zip():

my_list = [1, 2, 3, 4]
your_list = [10, 20, 30]
their_list = ['A', 'B', 'C']
print(list(zip(my_list, your_list, their_list)))
'''
# ----------------------------
'''
# reduce():
from functools import reduce
# in this example we reduce our list to one number using accumulator function:
my_list = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


# we can use any acc 0 or 1 or 2 or .....
print(reduce(accumulator, my_list, 0))
'''
# ----------------------------------
'''
# exercices solutions:
from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capita(item):
    return item.upper()


print(list(map(capita, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def over_50(item):
    return item > 50


print(list(filter(over_50, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
my_numbers = [5, 4, 3, 2, 1]
scores = [73, 20, 65, 19, 76, 100, 88]


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, (my_numbers + scores)))
'''
# --------------------------------
'''
# lambda expressions: video 138
# syntax: lambda param: action(param)

from functools import reduce
my_list = [1, 2, 3]


# def multiply_by2(item):
#    return item * 2


# print(list(map(multiply_by2, my_list)))
# multipy each item in my_list with 2
print(list(map(lambda item: item * 2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))  # return odd numbers
print(reduce(lambda acc, item: acc + item, my_list))
'''
# -------------------------------
# lambda video 7/139
# Exxercices:

# 1- square our list with lambda expression:
# Normal function:

'''
my_list = [5, 4, 3]


def square():
    my_list1 = []
    for item in my_list:
        my_list1.append(item**2)

    print(my_list1)


square()
'''
# ------------------------------------
'''
# 1-square:
my_list = [5, 4, 3]
print('new_list =', list(map(lambda item: item**2, my_list)))


# 2- list sorting with lambda based in the second element of the tuple:
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print('sorted a by second tuple element: ', a)
'''
# -------------------
'''
# list, set, dict comprehension:
my_list = []
for char in 'hello':
    my_list.append(char)
print(my_list)

# list, comprehension:
# syntax : [variable for variable in iterable]
my_list = [char for char in 'hello']
print(my_list)

print('')
my_list2 = [num ** 2 for num in range(100)]
print('my_list2 =', my_list2)

print('')
# keep only even numbers from my_list2:
my_list3 = [num ** 2 for num in range(100) if num % 2 == 0]
print('my_list3 =', my_list3)
'''
# -------------------------------
'''
# set, dictionary comprehension:
my_set = {char for char in 'hello'}
print('my_set =', my_set)

print('')
my_set1 = {num ** 2 for num in range(100) if num % 2 == 0}
print('my_set1 =', my_set1)

print('')
my_dict1 = {x: x**2 for x in range(10)}
print('my_dict1', my_dict1)

simple_dict = {'a': 1, 'b': 2}
my_dict2 = {k: v * 2 for k, v in simple_dict.items()}
my_dict3 = {k: v * 2 for k, v in simple_dict.items() if v % 2 == 0}
my_dict4 = {x: x * 2 for x in [1, 2, 3]}
print('my_dict2 =', my_dict2)
print('my_dict3 =', my_dict3)
print('my_dict4 =', my_dict4)
'''
# ----------------------------------------
'''
# Exercices:
# use list comprehension to print duplicate items:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate = list(
    set([item for item in some_list if some_list.count(item) > 1]))
print(duplicate)
'''
# ----------------------------------------
# video 8/144
# Decorators: gives more power to the function

'''
def hello():
    print('hellooooo')


greet = hello()
del hello
print(greet)
# hello() # will return NameError: name 'hello' is not defined (coz we deleted the hello())
'''

# -------------------------------

'''
def hello(func):
    func()


def greet():
    print('still here !')


a = hello(greet)
print(a)
'''
# Hight Order Function:

'''
def greet(func):
    func()


def greet2():
    def func():
        return 5
    return func
'''
# ----------------------------------
# Writing own Decorator Pattern

'''
def my_decorator(func):
    def wrap_func():
        print('*********')
        func()
        print('*********')
    return wrap_func


@my_decorator
def hello():
    print('hellooooo')


@my_decorator
def bye():
    print('See ya later.!')


hello()
bye()

# hello2 = my_decorator(hello)
# hello2()
'''
# --------------------
'''

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*********')
        func(*args, **kwargs)
        print('*********')
    return wrap_func


@my_decorator
def hello(greeting='hi there', emoji=':('):
    print(greeting, emoji)


# hello('hiiiiiii', ':)')
hello()
'''
# ---------------------------
'''
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'it tooked {t2-t1} s.')
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 5


long_time()
'''
# -----------------------------------
# Exercice:
'''
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
'''
# -------------------------------
# video 9/150:
# Error handling: TypeErrot, name error , etc.........
# ---------------------------------------

# video 9/151:
'''
while True:
    try:
        age = int(input('What is your age ?: '))
        print(10 / age)
    except ValueError:
        print('Please enter a number: ')
    except ZeroDivisionError:
        print('Please Enter age higher than 0.')

    else:
        break
'''
# ----------------------------------
# video 9/152:

'''
def sum(a, b):
    try:
        return a + b
    except TypeError as err:
        print(f'Please enter numbers!!!: {err}')

    finally:
        print('Ok i am done.!')


print(sum('1', 2))
'''
# -------------------
'''
while True:
    try:
        age = int(input('What is your age ?: '))
        print(10 / age)
        raise ValueError('Something is wrong!')
    except ZeroDivisionError:
        print('Please Enter number higher than 0')

'''
# ---------------------------
# video 10/155
# Generators:
# range(100)
# list(range(100))
# range hier is a generator
# everything that is generator is iterable
# and not any iterable is generator
# ex: range is a generator and list is an iterable

'''
def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = make_list(10)
print('my_list =', my_list)
'''

# ---------------------
'''
def generator_function(num):
    for i in range(num):
        yield i   # yield pauze the function and goes one by one

for item in generator_function(100):
    print(item)
'''
# -------------------------

'''
def generator_function(num):
    for i in range(num):
        yield i * 2


g = generator_function(100)
# 0
next(g) # 1
next(g) # 2
next(g) # 3
next(g) # 4
print(next(g))
'''

# ----------------------------------

'''
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator) * 2)
        except StopIteration:
            break


special_for([1, 2, 3])
'''
# ----------------------

'''
class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)
for i in gen: # looping throw the generator
    print(i)
'''

# -------------------------------------

'''
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(21):
    print(x)
'''
# ---------------------------

'''
def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


print(fib2(100))
'''

# ------------------------
# Modules
# video 11/164
'''
import random
# print(random)
# help(random)
# print(dir(random))  # shows all the methods available inside the random module

# print(random.random()) will return numbers between 0 and 1
# print(random.randint(1, 10))  # will return numbers between 1 and 10
# print(random.choice([1, 2, 3, 4, 5]))  # will return a choice between 1 and 5
my_list = [1, 2, 3, 4, 5, 6]
random.shuffle(my_list)  # will deorder the list
print(my_list)
'''
# ------------------------
'''
from random import shuffle
my_list = [1, 2, 3, 4, 5, 6, 7]
shuffle(my_list)
print(my_list)
'''
# --------------------------
'''
# run it in terminal: python3 pythondeveloper.py Mustapha Amina
import sys
# 0 is for the file name , 1 is for mustapha , 2 is for amina and so on.
first = sys.argv[1]
last = sys.argv[2]
print(f'Hi {first} and {last}')
'''
# -------------------------------
'''
from random import randint

answer = randint(1, 10)

print(answer)

i = 0
while i < 3:
    for i in range(3):
        try:

            guess = int(input('Guess a number between 1~10: '))
            if 0 < guess < 11:
                if guess == answer:
                    print('You Win !!!!')
                    break

            else:
                print('Please Enter a number between 1~10: ')

        except ValueError:
            print('Please Enter a number: ')
    i += 1
print('Your guesses are finished, try another time!!!')
'''

# ---------------------------
# video 11/169
'''
import pyjokes
joke = pyjokes.get_joke('en', 'neutral')
print(joke)
'''
# ----------------
# from collections import Counter, defaultdict, OrderedDict

'''
li = [1, 2, 3, 4, 5, 6, 6, 7, 7]
sentence = 'Hei there how are you.'
# will return count number of each element in list or tuple or ... as dict:
print(Counter(li))
for k, v in Counter(li).items():
    print(f'{k}: {v}x')
print('-' * 4)
print('')
for k1, v1 in Counter(sentence).items():
    print(f'{k1}: {v1}x')
'''
# ----------------------
'''
dict = {'A': 1, 'B': 2}
print(dict['A'])
print(dict['B'])
# print(dict['C']) # will return KeyError coz dont exist.

print('-' * 10)
# dict = defaultdict({'A': 1, 'B': 2})
# int will resolve the collable error.
dict = defaultdict(int, {'A': 1, 'B': 2})
print(dict['A'])
print(dict['B'])
print(dict['C'])

print('-' * 10)
# will return the value 5 to the key C that does not exist. lambda:5 is a collable object.
dict = defaultdict(lambda: 5, {'A': 1, 'B': 2})
print(dict['C'])

print('-' * 10)
dict = defaultdict(lambda: 'Does not exist', {'A': 1, 'B': 2})
print(dict['C'])
'''
# --------------
'''
d = {'c': 100}
d['a'] = 1
d['b'] = 2

d2 = {'c': 100}
d2['b'] = 2
d2['a'] = 1

print(d2 == d)

print('-' * 10)

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d['b'] = 2
d['a'] = 1

print(d2 == d)
'''
# -------------
# video 11/172
'''
import datetime
print(datetime.time(5, 45, 2))
print(datetime.date.today())
'''
# ---------------
'''
from array import array

arr = array('i', [1, 2, 3])
print(arr)
print(arr[0])
'''
# ------------------
# video 12/174
# debugging:
# we can import pdb a module debugger to help us debuggin issues:
# use help commnand inside pdb
# use ctrl + alt + B
# we can see what is num1 and num2
'''
import pdb


def add(num1, num2):
    pdb.set_trace()
    t = 4 * 5
    return num1 + num2


add(4, 'kbamaro')
'''
# -------------
'''
def add(num1, num2):
    return num1 + num2


print(add(4, 5))
'''
# -----------------------
# video 13/175 part2
