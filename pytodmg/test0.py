'''
def my_function():
    print('Line 1')
    print('Line 2')
    print('Line 3')


def triple():
    my_function()
    my_function()
    my_function()


triple()
'''

# -----------

import os


def ping_something():
    x = input('Enter ip: ')
    os.system('ping -c 2 ' + x)


ping_something()
