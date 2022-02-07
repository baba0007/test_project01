# working with math module:
# 1-factorial(x)
# 2-sqrt(x)
# 3-ceil(x)
# 4-fmod(x, y)
# 5-fabs(x), .........etc, there are a lot of function in math module.

'''
from math import *

# print(dir()) # will return list of all functions available in math module
# help(math) # will return documentation of each function

print(f'4! = {factorial(4)}')
print(f'sqrt(4) = {sqrt(4)}')
print(f'fabs(-10.6) = {fabs(-10.6)}')  # abs = absolute value ==> 10.6
print(f'fabs(10.6) = {fabs(10.6)}')  # abs = absolute value ==> 10.6
print(f'ceil(10.5) = {ceil(10.5)}')  # will return the next integer ==> 11
print(f'floor(10.5) = {floor(10.5)}')  # will return the before integer ==> 10

# calculate area of a circle:
from math import pi

# r = int(input('Enter radius: '))

r = 9
area = pi * pow(r, 2)  # pow(r, 2) = r ** 2

print(f'Circle area = {area} ')

# print(pow(4, 2))
'''

# ------------------------

#from math import *
# print(floor(fabs(-12.893)))

#from math import sqrt as sq
# print(sq(4))
'''
import math

l = [str(round(math.pi)) for i in range(1, 6)]
# print(round(math.pi))
print(f'l = {l}')  # will return 3 as a string 5 times (roud(math.pi) = 3)


# return a circle area
r = 9


def find_area():
    return math.pi * pow(r, 2)


print(f'Circle area = {find_area()}')
'''
# ----------------------------------
# working with random module:
# 1-random() function : to generate random float number between 0 and 1
# 2-uniform(begin, end): to generate random float begin < x < end
# 3-randint() : generate random integer value
# 4-randrange() :
# 5-choice()
'''
from random import *
# print(random())
print('range(): ')
for i in range(6):
    print(random())

print('-' * 10)
# ---------------
# print(uniform(5, 10))
print('uniform(5, 10)')
for i in range(6):
    print(uniform(5, 10))

# randint()
# syntax : randint(begin, end) (begin and end are inclusive)
print('-' * 10)
# print(randint(1, 20))
print('randint(1, 15): ')
for i in range(10):
    print(randint(1, 15))

# randrange(): syntax: randrange(begin, end, step) : will return from begin to end-1
# begin is optionel and default value
# step value is optionel and default value is 1
print('-' * 10)
print('randrange(5): ')
print(randrange(5))  # will return integers from 0 to 4
print('-' * 10)
print('randrange(1, 11): ')
# print(randrange(1, 11))
for i in range(5):
    print(randrange(1, 11))

print('-' * 10)
print('randrange(1,11,2): ')  # [1, 3, 5, 7, 9]
for i in range(5):
    print(randrange(1, 11, 2))

print('-' * 10)
print('randrange(0, 101, 10): ')
print(randrange(0, 101, 10))

# --------------------------
# 5-choice(): to generate random object from list, tuple, no set, string, etc...
# syntax choice(sequence): sequence should be indexeble ==> list, tuple, string, and no set
print('-' * 10)
print('choice(fuits): ')
fruits = ['Apple', 'Banana', 'Orange', 'Lemon', 'Mango']
print(choice(fruits))

print('-' * 10)
print('choice(fruits1): ')
fruits1 = ('Apple', 'Banana', 'Orange', 'Lemon', 'Mango')
print(choice(fruits1))

# fruits3 = {'Apple', 'Banana', 'Orange', 'Lemon', 'Mango'}
# print(choice(fruits3)) # TypeError: 'set' object is not subscriptable

print('-' * 10)
print('choice(alphabets): ')
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(choice(alphabets))
for i in range(5):
    print(choice(alphabets))

print('-' * 10)
print('choice((digits):')
digits = '0123456789'
for i in range(5):
    print(choice(digits))
'''
# ---------------------------------------
'''
# wap to generate 6 digit random number which can be used ad OTP
# ex1 methode:
from random import *
print('otp = ', randint(0, 9), randint(0, 9), randint(0, 9),
      randint(0, 9), randint(0, 9), randint(0, 9), sep='')

# ex2 methode:

otp = ''
for i in range(6):
    otp = otp + str(randint(0, 9))

print(f'otp = {otp}')
# print(randint(100000, 999999)) # not the best solution will not give us 0b
# print(randint(0, 999999)) # also not a good solution
'''
# ----------------------------------
# wap to generate a random password of 6 lenght where 1,3,5 characters are alphabet symbols and,
# 2,4,6 characters are digits ?
'''
from random import *

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
print('password = ', choice(alphabets), choice(digits), choice(
    alphabets), choice(digits), choice(alphabets), choice(digits), sep='')

# --------------------------------
print('-' * 10)
# if you want 10 random password:
for i in range(10):
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    print('password = ', choice(alphabets), choice(digits), choice(
        alphabets), choice(digits), choice(alphabets), choice(digits), sep='')

print('-' * 10)
# if you want that not always the password start with alphabets but also can start with digits then:

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
print('password = ', choice(alphabets + digits), choice(digits + alphabets), choice(
    alphabets + digits), choice(digits + alphabets), choice(alphabets + digits), choice(digits + alphabets), sep='')


for i in range(9):
    l = 'ABCDEFG'
    d = '0123456789'
print(choice(l + d), choice(l + d), choice(l + d), choice(l + d), sep='')

# ---------------
print('-' * 10)

opt = ''
for i in range(8):
    opt = opt + str(randint(0, 11))
print(opt)
'''

# ------------------------------
# wap to generate fake employee data for database testing part1+2:
# Employee Name, Employee Number, Employee Salary, Employee City, Employee Mobile Number, Designation:

# 1- the Name should contains 3 to 10 characters
# 2-First of the Name character should be upper case and remaining characters be lower case.
# 3-Employee number should starts with 'e-' followeed by 4 digits eg: e-1234
# 4-Employee salary should be float value from 10000 to 50000
# 5-Employee city should be from : ['Hyderabad', 'Chennai', 'Bangalore', 'Pune', 'Delhi', 'Mumbai']
# 6-Mobile number shoulds exactly 10-dgits where first number should be 6 to 9, no restriction on
# remaining digits eg: 9848098480
# 7-Employee Designation should be from :
# ['Software Engineer', 'Senior Software Engineer', 'Team Lead', 'Project Lead', 'Project Manager']


from random import *

alphabets = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
cities = ['Casablanca', 'Rabat', 'El-jadida', 'Taza', 'Oujda', 'Mohammadia']
designations = ['Software Enginner',
                'Senior Software Engineer', 'Team Lead', 'Project Manager']

# Name


def get_fake_name():
    name = choice(alphabets).upper()
    n = randint(2, 9)
    for i in range(n):
        name = name + choice(alphabets)
    return name

# Employee Number = eno


def get_fake_eno():
    eno = 'e-'
    for i in range(4):  # 4 digits should be after e-
        eno = eno + choice(digits)
    return eno


def get_fake_salary():
    esal = uniform(10000, 500000)
    return esal


def get_fake_city():
    city = choice(cities)
    return city


def get_fake_mno():
    #mno = choice('6789')
    # 2 digits are token the rest 8 digits that's why range(8) = 10 digits for a phone num
    mno = '06'
    for i in range(8):
        mno = mno + choice(digits)
    return mno


def get_fake_designation():
    designation = choice(designations)
    return designation


def get_fake_emp_data():
    print('Employee Name: ', get_fake_name())
    print('Employee Number: ', get_fake_eno())
    # :{:.2f} to let only the digits after the point.
    print('Employee Salary: {:.2f}'.format(get_fake_salary()))
    print('Employee City: ', get_fake_city())
    print('Employee Mobile Number: ', get_fake_mno())
    print('Employee Designation: ', get_fake_designation())


'''
# check test3.py
if __name__ == '__main__':
    get_fake_emp_data()
'''

'''
for i in range(10):
    get_fake_emp_data()
    print() # to add blank line between each data.
'''

# print(get_fake_name())
# print(get_fake_eno())
