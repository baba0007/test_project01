# package in general is a group of related items
# package in python is a group of related modules
# and Modules is a group of functions and classes and variables....
# __init__.py is a mandatatory for a package but from python 3.3 it is not mandatory anymore
# package also contains subpackages and each subpackage contains __init__.py
# Advantages of Packages:
# 1-Resolve naming conflict : ex: loan.homeloan.account, loan.vehicleloan.account
# 2-Unique identification of our components
# 3-Modularition
# 4-Readability
# 5-Maintability

# Demo Programs to create and use packages:
# testpckage1.py (access function f1() from modulpack1.py)--> package1 (there is modulpack1.py + __init__)--> modulpack1.py (inside is a function f1())--> __init__.py
# package contains modules and modules contains functions and variables and etc...

# examples are:

# modulpack1.py, testpackage1.py, testcompackage.py, modulcom1.py, modulcom2.py (inside subpackage durga)
# access f1() and f2() from modulcom1.py and f2() from modulcom2.py

# importance of the __init__.py: (init means initialization activity):

from compackage.modulcom1 import f1

f1()

from compackage.durga.modulcom2 import f2
f2()

# Relationship Function, Module, package and library
# Function is a group of repeatedly required lines of code.
# Module is a group of function, classes, variables saved in a python file
# package is group of related modules
# Library is a group of packages


# Need of installing a python package:
# if we want to use a package compulsory it should be available in the current working directory.we cannot use from anywhere in our system.
# to make a package available through out our system, then we have to install that package.

# how to install a package and it will called from any place in our system:
# in this example we will install package2 with calling setup() function ---- > check setup.py
# to install this scrip setup.py after creating setup.py:
# run from command line pip install .  (pip install point(.))

# methode 1:
# setup.py:
# from setuptools import setup
# setup(name = 'nameof the package', version = 'version of the package', packages = ['name of the package in a list'])
