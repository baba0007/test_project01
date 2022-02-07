'''
This module contains some builtins members, Demo examples!
'''
# -------------------------------

'''
import modules
print(modules.x)
print(modules.y)
modules.add(10, 20)
modules.product(10, 20)
'''
# ---------------------------
'''
# module aliasing: shorting the name of any module: you cannot use old module name after aliasing
import modules as m
print(m.x)
print(m.y)
m.add(20, 30)
m.product(20, 30)
# modules.add(20, 30) # will return NameError coz we are using aliasing for short name m

# importing all modules.py members without using the modules:
print('-' * 10)
from modules import x, y, add, product
print(x)
print(y)
add(20, 30)
product(20, 30)

# or
print('-' * 10)

from modules import *

print(x)
print(y)
add(20, 30)
product(20, 30)

# member aliasing:
print('-' * 10)
from modules import add as a, product as p
a(30, 40)
p(30, 40)

# various possibility of import statement:


# 1- import modile1
# 2- import module1, module2, module3, .....etc
# 3- import module1 as m1
# 4- import module1 as m1, module2 as m2, module3 as m3, ....etc
# 5- from module1 import member1
# 6- from module1 import member1, member2
# 7- from module1 import *
# 8- from module1 import member1 as m1
# 9- from module1 import member1 as m1, member2 as m2, member3 as m3
'''

# ------------------------
# module name conflict:
# incase of same member name in a module , the last one will be the winner

# print('-' * 10)
# module name conflict:
# incase of same member name in a module , the last one will be the winner in our case modul2 will be.

'''
from modul1 import *
from modul2 import *

add(10, 30)
'''

# -------------------
# to get both same member in a module to be used then:
# solution-1: if i want to choose modul1 or modul2:/
# import modul1
# import module2
# modul1.add(a, b)
# or if i want modul2:
# modul2.add(a, b)
'''
print('-' * 10)
import modul1
import modul2

modul1.add(30, 80)
modul2.add(30, 80)

# solution-2:
# from modul1 import add as a1
# from modul2 import add as a2
# a1(10,20)
# a2(10,20)

print('-' * 10)
from modul1 import add as a1
from modul2 import add as a2

a1(10, 20)
a2(10, 20)
'''
# --------------------------
# Module reloading:
'''
import modules
import time
from imp import reload

modules.add(10, 50)
print('Entering sleeping state!')
time.sleep(30)
print('Wakeup state ... trying to reload the modules.py again!!!')
reload(modules)
modules.product(10, 50)
'''

# ---------------------------
# Finding members of module by using dir():

# 1- dir() : will return list [] of all members of current module if i dont pass no argument
# 2- dir(modulename): return list of all members of specified module.
# help(): # will return documentation the module and its members.


# import modules
# import modul1
# import math


# print(dir(modules))
# print('-' * 10)
# print(dir(modul1))
# print('-' * 10)
# print(dir(math))
# print('-' * 10)
# print('help(math): ')
# print(help(math))  # will return documentation the module and its members.
# print(__doc__)
# print(dir())

# __name__ :
'''
import modules
print('This is a test module')
print(__name__)
'''

import modules
print('test module')
