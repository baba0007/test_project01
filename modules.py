# Modules:
# This file modules.py is an example of a module.
# any .py file in python is a module.

'''This is a test __doc__ demo provides explanation of built in members!!'''

x = 888
y = 999


def add(a, b):
    print('The Sum is:', a + b)


def product(a, b):
    print('The product is:', a * b)


class A:
    pass

# ---------------------
# Module aliasing: shorting the name of any module
# aliasing our module modules.py:
# import modules as m

# ---------------------------------
# member aliasing: check test2modules.py file

# module name conflict:
# incase of same member name in a module , the last one will be the winner
# to get both same member in a module to be used then:
# solution-1: if i want to choose modul1 or modul2:/
# import modul1
# import module2
# modul1.add(a, b)
# or if i want modul2:
# modul2.add(a, b)

# solution-2:
# from modul1 import add as a1
# from modul2 import add as a2
# a1(10,20)
# a2(10,20)

# ------------------------------

# Reloading a module:
# the reload function is inside the module imp
# reload is used that after calling the modules.py in our file and we are updating our file will reload it after the sleep time.
# to not getting error Name module not defined.

# --------------------------
# finding members of module by using dir():
# will return list of members of the current module modul1.py and also will return other members python default.

# difference between dir() and help():
# will return documentation the module and its members.

# Extra Members added by python interpreter for every module:

# __doc__, __file__, __name__, __package__, __loader__, __annotations__, __builtins__, __cached__, __spec__

# Group of function is a module
# Group of modules is a package

# 1- __doc__ : it is one of the member of this module


'''
print(dir())
print(__doc__)

# 2- __file__:
import os
print(f'file name: {__file__}')
print(f'file absolute path: {os.path.abspath(__file__)}')
print(f'Directory name: {os.path.dirname(os.path.abspath(__file__))}')
'''
# Special Variable: __name__ Part1:
# print(__name__)

if __name__ == '__main__':
    print('Direct execution!')
else:
    print('Indirect execution!')

# Special Variable: __name__ Part2:
