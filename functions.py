'''
def calculate(a, b):

    print(f'{a} + {b} = {a + b}')
    print(f'{a} - {b} = {a - b}')
    print(f'{a} * {b} = {a * b}')
    print('')


a = int(input('Enter a: '))
b = int(input('Enter b: '))
print('')
calculate(a, b)
'''
# ----------------------------------------
# types of functions:
# 1-built in functions/predefined functions:
# ex:
# id(), type(), print(), input(), eval()......

# user defined functions are customized functions that user
# can self build it and use it in python:
# like the example up : calculate() function:

# syntax:

'''
def funcname(parameter):
    return


def wish():
    print('Hello how are you ?')


wish()
wish()
'''

# Function parameters:
# write a function to take name of student as input and print wish message by name:

'''
def wish(name='Amina'):
    for n in range(2):
        print('hello', name.capitalize())


wish('mustapha')
'''
# --------------------------
# write a function to take a number as input and print its square value:
'''
def square(num):
    #num = int(input('Enter a number: '))
    print(f'The square of {num} is {num**2}')


square(10)
square(109)
square(108)
'''
# --------------------------
# Return statement:
# write a function to accept 2 numbers as input and return sum:

'''
def add(a, b):
    sum = a + b
    return sum


result = add(10, 20)
print(f'{10} + {20} = {result}')

# return value of this function is saved in x.
# if in a function there is no return statement then it will return None as default like this function below
# there is no return statment that is why we got None at the end stored in x variable:


def f1():
    print('Hello')


x = f1()  # will return hello coz of the calling of the function f1()
print(x)  # will return None
'''
# ---------------------
# write a function to find factorial of given positive int value:

'''
def factorial(num):
    result = 1
    while num >= 1:
        result = result * num
        num = num - 1
    return result


# num = int(input('Enter number: '))
print(f'{3}! = {factorial(3)}')

# find factorial of multiple numbers:
for i in range(6):
    print(f'{i}! = {factorial(i)}')
'''
# --------------------------
# Returning multiple values from a function:

'''
def sum_sub(a, b):
    sum = a + b
    sub = a - b
    return sum, sub


# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# print(f'{a} + {b} = {x}')
# print(f'{a} - {b} = {y}')
# x, y = sum_sub(a, b)
x, y = sum_sub(20, 10) # x = sum = 20+10, y = sub = 20-10

print(f'{20} + {10} = {x}')
print(f'{20} - {10} = {y}')
'''
# -----------------

'''
def calc(a, b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return sum, sub, mul, div


w, x, y, z = calc(10, 20)
print(f'{10} + {20} = {w}')
print(f'{10} - {20} = {x}')
print(f'{10} * {20} = {y}')
print(f'{10} / {20} = {z}')

print('')
t = calc(10, 20)
print(type(t))
print(t)

#for x in t:
#    print(x)
'''
# --------------------
# types of arguments: there are 4 types:
# 1-positional arguments
# 2-keyword arguments
# 3-Default arguments
# 4-variable length arguments

'''
# 1-positional arguments

def sub(a, b):
    print(a - b)


sub(200, 100)  # a=200, b= 100 ==> positional arguments


def sub1(a, b=10):
    print(a - b)


sub1(30)
'''
# --------------------------
# 2-kyword arguments:
# in keyword arguments order is not required:
# number of arguments are required
# we can mix positional and keyword argument but first should be positional then keyword arguments.

'''
def sub(a, b):
    print(a - b)


sub(200, 100)  # positional argument
sub(a=200, b=100)  # pasing value by keyword (a and b are keywords)
sub(b=100, a=200)
sub(200, b=100)  # positional argument first then keyword argument ==> valid
# sub(a=200, 100) # SyntaxError: positional argument follows keyword argument coz keyword argument is first , it should be positional argumnent first then keyword argument.
'''
# ------------------------------
# 3-Default arguments:

'''
def wish(name):
    print(f'Hello {name}')

# wish() # will return error missing 1 argument
wish('Mustapha')
'''

'''
def wish(name='baba'):
    print(f'Hello {name}')


wish()  # will not return missing arguments coz it will take default value name 'baba'
wish('dialo')
'''
# ----------------------


# def wish(name, msg):
#    print(f'Hello {name} {msg}')


# def wish(name='Guest', msg='Good morning.'):
#    print(f'Hello {name} {msg}')


# def wish(name, msg='Good morning.'):
#    print(f'Hello {name} {msg}')

# will return error coz after default argument we cannot take non default argument
# def wish(name='Guest', msg):
# SyntaxError: non-default argument follows default argument
#    print(f'Hello {name} {msg}')


# wish('baba', 'Good morning.')
# wish()
# wish('Amina')
# wish('zaza', 'How are you ?') # syntaxError: non-default argument follows default argument

# -4 variable length arguments: *args

'''
def f1(*n):
    print(type(n))
    print(n)
    #print('variable length argument function.')


f1()
f1(10, 20, 30)
'''
# ----------------------

'''
def sum(*n):
    total = 0
    for x in n:
        total = total + x
    print(f'sum{n} = {total}')


sum()
sum(1, 2, 3, 4)
sum(10, 20, 30, 40)
'''

# ----------------

'''
def f1(*n):
    print(n)


f1(10, 20)
f1((10, 20, 30), (40, 50, 60))
'''
# --------------------

'''
def f1(x, *y):  # x is a positional argument, *y is variable length argument and wiill return tuple
    print(x)
    print(y)
    for y1 in y:
        print(y1)


f1(10, 20, 30, 40, 50)
print('')
f1(10)
print('')
# f1() # TypeError: f1() missing 1 required positional argument: 'x'
'''

# -----------------------------

'''
def f1(*x, y):
    print(x)
    print(y)


# f1(10, 20, 30, 40, 50) # TypeError: f1() missing 1 required keyword-only argument: 'y'
f1(10, 20, 30, 40, y=50)
'''
# ------------------------------------------

'''
def f1(*x, *y): # we cannot take more than 1 variable length argument (*x) in a funcction.
    print(x)
    print(y)


f1(10, 20, 30, 40) # SyntaxError: invalid syntax,
'''
# ---------------------------
# Differences between *args and **kwargs:
# *args = variable length arguments , **kwargs = variable length keyword arguments
# f1(*n) ===> tuple will be created
# f1(**kwargs) ===> dictionary will be created

'''
def f1(*n):
    print(n)


f1()
f1(10)
f1(10, 20, 30)

print('')


def f2(**kwargs):
    print(kwargs)


f2()
f2(name='mustapha', age=52)
f2(A=10, B=20, C=30, D=40)
'''
# -------------------------------

'''
def f1(*args, **kwargs):
    print(args)
    print(kwargs)


f1(10, 20, A=40, B=50)  # will return tuple and dictionary
'''

# def f(**kwargs, *args): # will return syntax error coz after kwargs we cannot take args
#    print(args)
#    print(kwargs)


# f(A=10, B=20, 40, 50)

# ------------------------------
'''
def f1(*y, x=10):
    print(y)
    print(x)


f1(10, 20, 30, x=40)
'''
# ------------------

'''
def f(arg1, arg2, arg3=4, arg4=8):
    print(arg1, arg2, arg3, arg4)


# f()  # Error missing argument arg1 and arg2
f(3, 2)
f(10, 20, 30, 40)
f(25, 50, arg4=100)
f(arg4=2, arg1=3, arg2=4)
# f(arg3=10, arg4=20, 30, 40) # SyntaxError: positional argument follows keyword argument
# after kwargs we cannot take positional arguments arg4=20, 30, 40 (30, 40 are positional args)
# f(4, 5, arg2=6) # TypeError: f() got multiple values 5 and 6 for argument 'arg2'
# f(4, 5, arg3=5, arg5=6)  # TypeError: f() got an unexpected keyword argument 'arg5'
'''
# ---------------------------
# Types of Variables: Global and Local:
'''
a = 10  # Global Variable

def f1():
    print(a)


def f2():
    print(a)


f1()
f2()

print('-' * 10)
'''
# -------------------------------
'''
def f3():
    a = 20  # Local Variable
    print(a)


def f4():
    print(a)


f3()
f4() # NameError: name 'a' is not defined
'''

# --------------------------------
'''
a = 10  # Global Variable


def f1():
    a = 20  # Local Variable
    print(a)


def f2():
    print(a)


f1()
f2()
'''
# -------------
# global keyword:
'''
a = 10  # Global Variable


def f1():
    global a
    a = 20  # will be global not local coz of global a word.
    print(a)


def f2():
    print(a)


f1()
f2()
'''
# ----------------------------------

'''
def f1():
    global a  # will let a global and available for all functions.
    a = 10  # will be global not local coz of global a word.
    print(a)


def f2():
    print(a)


f1()
f2()
'''
# --------------------------
# global keyword:
'''
a = 777


def f1():
    print(a)
    global a
    a = 999
    print(a)


# f1()  # SyntaxError: name 'a' is used prior to global declaration
# before global declaration we cannot use anything.
'''

# -----------------
'''
a = 777


def f1():
    global a
    print(a)
    a = 999
    print(a)


f1()
'''
# ------------------------
'''
a = 888


def f1():
    a = 999
    print(a)


f1()  # priority to Local variable a
'''
# -----------------------------

# in this case i want global a to be printed:
# that is why i use globals() function:
'''
a = 888
def f2():

    a = 999  # Local Variable
    print(a)
    # print(globals())  # will return dictionary.
    # print(globals().get('a')) # will return the global variable key value whichis 888
    print(globals()['a'])


f2()
'''
# ----------------------------------
# Recursive Functions:
# 1- without recursion how to find factorial:

'''
def factorial(n):
    result = 1
    while n >= 1:
        result = result * n
        n = n - 1
    return result


# n = int(input('Enter number: '))
# print(f'{n}! = {factorial(n)}')
print(factorial(4))
'''

# 2-with recursion:
# n! = n*(n-1)!
# fatorial(n) = n*factorial(n-1)

'''
def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)
    return result


n = 4
print(f'{n}! = {factorial(n)}')
print('-' * 10)
# to get factorial of a range:
print('Factorial of a range of numbers: ')
print()
for i in range(11):
    print(f'{i}! = {factorial(i)}')
'''
# --------------------------------
# Internal tracing of Recursive function execution:

'''
def factorial(n):
    print('Execution of factorial function for n:', n)
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)

    print(f'Returning factorial({n}) is: {result}')
    return result


n = 3
print(f'{n}! = {factorial(n)}')
'''
# ----------------------------
# how many times we get this fuction executed to get a factorial of a number n:
'''
count = 0


def factorial(n):
    global count
    count += 1
    print('Execution of factorial function for n', n)
    if n == 0:
        result = 1

    else:
        result = n * factorial(n - 1)

    return result

# maximum recursion is 995 , above of that will return error:
# maximum recursion depth exceeded while calling a Python object


n = 995
# n = 996 # will return error coz :maximum recursion depth exceeded while calling a Python object
print(f'{n}! = {factorial(n)}')
print(f'Number of factorial function executions = {count} Times.')
'''
# ---------------------------
# Anonymous Functions/Lambda Functions:
# NAmeless functions
# Instant use (or one time usage)

# Normal function example:

'''
def squareit(n):
    return n * n


print(squareit(4))

# lambda function:
# syntax: lambda input-arguments: expression

# s = lambda n: n*n
# print(s(4))

n = 4
def s(n): return n * n


print(f'square of {n} is {s(n)}')
print('-' * 10)
for i in range(11):
    print(f'square of {i} is {s(i)}')
'''
# --------------------
# Lambda Function to find Sum of given 2 Numbers:
'''
# s = lambda a, b: a + b
# print(s(10, 20))


def s(a, b): return a + b


print(s(10, 20))
'''
# ---------------------
# Lambda function to find biggest of given numbers:

# bigger = lambda a, b: a if a > b else b
# print(bigger(10,20))
# print(bigger(-10, -20))


# 2 input numbers:
'''
def bigger(a, b): return a if a > b else b


print(bigger(10, 20))
print(bigger(-10, -20))
'''
# ------------------
'''
# 3 input numbers:
# bigger = lambda a, b , c: a if a>b and a>c else b if b>c else c
# print(bigger(10,20,30))

def bigger(a, b, c): return a if a > b and a > c else b if b > c else c


print(bigger(10, 20, 30))
print(bigger(20, 40, 3))
'''
# ----------------------
# Function as argument to another function:
# filter(function, sequence) # sequence can be string, tuple, list or etc..
# map(function, sequence)
# reduce(function, sequence)

# ---------------------------------
# filter() : used to filter objects from the given sequence: syntax: filter(function, sequence)
'''
# output of filet will be always <= that the input

# without filter()
# print even number
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def iseven(n):

    if n % 2 == 0:
        return True

    else:
        return False


l1 = []
for n in li:
    if iseven(n):
        l1.append(n)
print('Even numbers: ')
print(f'l1 = {l1}')

# with filter():

def iseven(n):

    if n % 2 == 0:
        return True

    else:
        return False


l1 = list(filter(iseven, li))
print(f'l1 = {l1}')

# filter() with lambda:
# l1 = list(filter(lambda n: True if n % 2 == 0 else False, li))
# or
l1 = list(filter(lambda n: n % 2 == 0, li))

print(f'l1 = {l1}')

# odd number:
print('')
print('Odd numbers: ')
l2 = list(filter(lambda n: n % 2 != 0, li))
print(f'l2 = {l2}')
'''
# ---------------------------
# filter() more examples:
'''
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# only even number:
even = list(filter(lambda n: n % 2 == 0, l))
odd = list(filter(lambda n: n % 2 != 0, l))
print(f'even = {even}')
print(f'odd = {odd}')

# print number that are divisable by 3 and odd at the same time:
odd3 = list(filter(lambda n: n % 3 == 0 and n % 2 != 0, l))
print(f'odd3 = {odd3}')

# ex 2:
# print heroines that start with k:
heroines = ['Katrinakaif', 'Kareenakapoor',
            'Anushka', 'Deepika', 'Sunnyleone', 'Mallika']
heroinesk = list(filter(lambda name: name[0] == 'k'.capitalize(), heroines))
print(heroinesk)

# name which length is divisable by 5:
heroines5 = list(filter(lambda name: len(name) % 5 == 0, heroines))
print(heroines5)

# name which length is odd:
heroinesodd = list(filter(lambda name: len(name) % 2 != 0, heroines))
print(heroinesodd)
'''
# ------------------------
# map(): syntax: map(function, sequence)
# square of each element in the list:
# input and output of the map() should be equal.

'''
# without map():

l = [1, 2, 3, 4, 5]


def sqrt(n):
    return n * n


for i in l:
    print(sqrt(i), end=' ')

print('')
print('-' * 10)
# with map():

l = [1, 2, 3, 4, 5]
l1 = list(map(sqrt, l))
print(f'l1 = {l1}')

print('-' * 10)
# map() with lambda:
l = [1, 2, 3, 4, 5]
l2 = list(map(lambda n: n * n, l))
print(f'l2 = {l2}')

# ----------------------
print('-' * 10)
# ex3: 2 arguments:

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [5, 10, 15, 20, 25]

l3 = list(map(lambda x, y: x * y, l1, l2))  # extra elements will be ignored.
print(f'l3 = {l3}')
'''
# ------------------------
'''
l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5, 6, 7, 8]
l3 = [4, 5, 6, 7, 8, 7]
print('-' * 10)
l4 = list(map(lambda x, y, z: x + y + z, l1, l2, l3))
print(f'l4 = {l4}')  # extra elements will be ignored
'''
# ---------------
'''
x = 2
for i in range(x):
    x = x - 2
    print(x)
'''
# reduce(): syntax: reduce(function, sequence)

# filter() if input elements are 10 then output is <= 10 elements
# map()  if input elements are 10 then output is = 10 elements
# reduce() if input elements are 10 then output is = 1 element

# ex : reduce all the sum of all numbers in this list to a single value.
'''
from functools import reduce

l = [10, 20, 30, 40, 50]
result = reduce(lambda x, y: x + y, l)
result1 = reduce(lambda x, y: x * y, l)
print(f'result = {result}')
print(f'result1 = {result1}')

# Find the Sum of First 100 Numbers by using reduce() function ?

res = reduce(lambda x, y: x + y, range(101))
print(f'res = {res}')
'''
# -------------------------
