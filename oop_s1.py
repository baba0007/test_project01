#!/usr/bin/env python3.9


# The complete story of python Constructors part-1:

# Constructors is a special method in python and the name of the constructor is always: __init__
# the constructors are executed as soon as we create an object.
# The purpose of the constructor is to declare and initialize the instance variable related to object.

'''
class Test:
    def __init__(self):
        print('Contructor execution...!!!')

t1=Test()
t2=Test()
t3=Test()'''
#-----------------------------
'''
class Student:
    def __init__(self, name, rollno, marks):
        # instance variables:
        print('Creating instance variables and performing initialization...')
        self.name = name
        self.rollno = rollno
        self.marks = marks

s1 = Student('baba', 101, 50)
print(s1.name, s1.rollno, s1.marks)
s2 = Student('dialo', 130, 20)
print(s2.name, s2.rollno, s2.marks)
'''
#----------------------------------

# The complete story of python Constructors part-2:
# within class constructors functions are always optionel.
'''
class Test:
    def m1(self):
        print('Method execution...')

t = Test()
t.m1()

# ----------------
class Test1:
    def __init__(self):
        print('Constructor execution...')

t1 = Test1() # will return Construction execution...
t1.__init__() # will return Construction execution...
t1.__init__() # will return Construction execution...
t1.__init__() # will return Construction execution...

print('')
print('-'*10)

# --------------------------------
class Test2:
    def __init__(self):
        print('non-arg constructor...')

    def __init__(self, x):
        print('one-arg constructor...')

t2 = Test2(10)
# t2 = Test2() # will return: TypeError: __init__() missing 1 required positional argument: 'x'
# we got error coz python will ignore the first constructor
# in python beter to use one constructor
# and if by mistake you use 2 or more constructors with the same names (__init__), then python will choose the last constructor.
# in our cases __init__ are same name constructors

# Mini Application to explain oop (object oriented programming)

# self.title, self.hero, self.heroine are instance variables
# title, hero, heroine are local variables, also are argument variables they can be any name a, b, c or ....

print()
print('-'*10)

class movie:
    def __init__(self, title, hero, heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine

    def info(self):
        print(f'Movie name is {self.title}.')
        print(f'Movie hero name is {self.hero}.')
        print(f'Movie heroine name is {self.heroine}.')



list_movie = []
# this list_movie will be gone when the programm is executed so the print(lis_movie) will be empty.

while True:
    title = input('Enter Movie name:')
    hero = input('Enter hero name:')
    heroine = input('Enter heroine name:')

    m = movie(title, hero, heroine) # Movie Object
    list_movie.append(m)
    print('Movie added to the list_movie successfully.')
    option = input('Do you want to add another movie [Yes/No] ?: ')
    if option.lower() =='no':
        break
print()
print('All Movies information:')
print('-'*10)

for movie in list_movie:
    movie.info()
    print()


# Difference between method and constructor:

    # Method                      Contructor
    # Any name                   __init__()
    # called any no times        only once
    # we should call it,             automatically called after object creation
    # expllicitly
    # business logic inside,         self.something
    # the code

'''
# --------------------------------------

# Basic idea about types of variables instance, static and local:

# 1-instance variables:

# if the value of a variable is varied from object to object, such type of variables are called instance variables or,
# object level variable, eg: name and rollno of the student.
# Most of the times instance variables will be declared inside constructor by using self variable.

# 2-static variables:

# if the value of variable is not varied from  object to object, then it is not recommended to declare those variables as,
# instance variables, we have to declare at class level as static variables:
# eg: shool_name = 'polo'
# Most of the times, static variables should be declared within the class diectly.
# in the case of instance variables, for every object a separate copy will be created. but in the case of static variables,
# at class level only one copy will be created and shared by every object of that class.

# 3-local variables : knows as method level variables:

# to meet temporary requirements of the programmer, sometimes we can declare variables inside a method, such type of,
# variables are called local variables or method level variables.

'''
class Student:

    shool_name = 'polo'  # static variabe

    def __init__(self, name, rollno):
        self.name = name  # instance variable
        self.rollno = rollno  # instance variable

    def info(self):

        x = 3  # Local variable declared inside this method info()
        for i in range(x):  # i is local variable
            print(f'Hello {self.name}, you have {self.rollno} ')

# obj = Student('baba', 105)
# obj.info()
'''

# Type of Methods:

# 1-Instance Methods : it use self as argument
# 2-Class Methods it use cls as argument and also it use @classmethod dcorator
# 3-Static Methods = general utility method and it use @staticmethod decorator

'''
class Student:
    schoolname = 'Polo'  # static variable

    def __init__(self, name, rollno):
        self.name = name  # instance variable
        self.rollno = rollno  # instance variable

    # Instance method coz it access instance variables self.name, self.rollno, also it contain self as first argument
    def getStudentinfo(self):
        print(f'Student Name is {self.name}.')
        print(f'Student Rollno is {self.rollno}.')

    @classmethod  # decorator
    # class Method coz it access class or (static) variable, also coz it contain cls argument.
    def getSchoolinfo(cls):
        print(f'SchoolName is {cls.schoolname}.')

    @staticmethod
    def getSum(a, b):  # Static method
        sum = a + b
        return sum


t = Student('dialo', 119)
t.getStudentinfo()
t.getSchoolinfo()
print(t.getSum(10, 4))
'''
# ------------------------------------------------

# various places to declare instance variables:
# if the value of a variable is varied from object to object, such type of variables are called instance variables,
# or object level variables: eg: name and rollno of the student.

# fro every object a separate copy of instance variables will be created.

# Most of the times instance variables will be declared inside constructor by using self variable.

# we can declare instance variables in 3 places:
# 1- Inside constructor by using self variable
# 2- Inside instance method by using self.
# 3- Outside of the class by using object refeence variable.

'''
class Test:
    def __init__(self):  # constructor
        self.a = 10  # instance variable
        self.b = 20  # instance variable

    def m1(self):  # instance method
        self.c = 30  # instance variable


# 1- instance variable declared inside the constructor, a nd b will be added to object.
t = Test()

# 2- instance variable inside instance method is declared, c will be added to object.
t.m1()
# 3- declaring instance variable outside of the class, d will be added to object.
t.d = 40
# ask class how many instance variables are present and print it.
print('t dict =', t.__dict__)
# print(t.a)
# print(t.b)
# print(t.c)
t1 = Test()
t1.m1()
t1.d = 40
t2 = Test()
print('t1 dict =', t1.__dict__)
print('t2 dict =', t2.__dict__)
# ==> number of instance variables vary from object to object.
'''

# How to access instance variables ? :
# 1- inside classe by using self
# 2- outside class by using object reference.

'''
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def display(self):
        print(f'a = {self.a}')
        print(f'b = {self.b}')


print('Accessing instance variables within the class: t = Test(): ')
t = Test()
t.display()
print('-' * 10)
print('Accessing instance variable outside of the class: print(t.a) and print(t.b): ')
print('a =', t.a)
print('b =', t.b)

# * how to delete instance variables ? :
# within the class : syntax : del self.variablename -- > eg:  del self.c

# from outside of the class:
# syntax: del objectreference.variablename , eg: del t.c
# we can delete multiple instance variables : del t.a, t.b, t.c ...

print('')
print('-' * 10)


class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

    def m1(self):
        del self.a


t1 = Test()
print('t1 =', t1.__dict__)

print('Deleting instance variables within the class: ')
t1.m1()  # a will be deleted from inisde the class in instance method
print('t1 =', t1.__dict__)

print('Deleting instance variables outside the class: ')
t2 = Test()
del t2.b, t2.d  # deleting instance variables outside of the class
print('t2 =', t2.__dict__)

# The instance variables which are deleted from one object, won't be deleted from other object becoz for evry object,
# separate copy there.

print('-' * 10)
# updating instance variables:


class Test:
    def __init__(self):
        self.a = 10
        self.b = 20


t1 = Test()
t1.a = 888  # updating instance variable from 10 to 888
t1.b = 999  # updating instance variable from 20 to 999
# t1.c = 222 # to add instance variables outside the class
print('t1 =', t1.__dict__)
t2 = Test()
print('t2 = ', t2.__dict__)
'''
# ---------------------

# Various places to declare static variables:
# 1- in general and most of the time static variables should be declared within the class level:
# 2- inside constructor by using class name : eg : Test.b =20
# 3- inside instance method by using class name.
# 4- inside class method by using either cls or class name.
# 5- inside static method by using either class name.
# 6- outside of class by using classname.


# 1- ex: within class
'''
class Student:

    schoolname = 'Polo'  # static variable

    def __init__(self, name, rollno):
        self.name = name  # instance variable
        self.rollno = rollno  # instance variable


t = Student('baba', 190)
# print(t.__dict__)  # will print available instance variables of the class
# print(Student.__dict__)  # will print available static variables of the class

# 2-ex: inside constructor by using class name:


class Test:

    a = 10  # static variable

    def __init__(self):  # inside constructor by using class name:
        Test.b = 20  # static variable

    def m1(self):  # instance method coz of using self
        Test.c = 30

    @classmethod
    def m2(cls):  # class method coz of decorator and cls
        cls.d = 40  # or Test.d = 40
        Test.e = 50

    @staticmethod
    def m3():
        Test.f = 60


t = Test()  # accessing static variable within constructor.
t.m1()  # accessing static variable within instance method.
# accessing static variable within class method by using cls or class name:
Test.m2()  # or t.m2()
# accessing static variable within static method by using class name:
Test.m3()  # or t.m3()
Test.g = 70  # declaring static variable outside of class by using class name.

print(Test.__dict__)
'''

# ---------------------------------
# How to access Static variables ? :

# 1- inside constructor by using self or class name:
# 2- inside instance method by using self or class name:
# 3- inside class method by using cls or class name:
# 4- inside static method by using class name: h
# 5- outside class by using object reference or class name:

'''
class Test:
    a = 10

    def __init__(self):
        print(self.a)
        print(Test.a)

    def m1(self):
        print(self.a)
        print(Test.a)

    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)

    @staticmethod
    def m3():
        print(Test.a)


print('Accessing static variable Inside Constructor by using self or class name Test: ')
t = Test()
print('-' * 10)
print('Accessing static variable Inside Instance method by using self or class name Test: ')
t.m1()
print('Accessing static variable Inside class method by using cls or class name Test: ')
t.m2()  # or Test.m2()
print('Accessing static variable Inside static method by using class name Test: ')
t.m3()  # or Test.m3()
print('Accessing static variable outside class by using object refence or class name: ')
print(t.a)
print(Test.a)

'''

# -------------------------
# where can we modify value of static variables ? :
# we can modify it anywhere by using class name or inside class by using cls variable:
# Note: we cannot modify static variable by using self or object reference...

'''
class Test:
    a = 10

    def __init__(self):
        Test.a = 20

    def m1(self):
        Test.a = 30

    @classmethod
    def m2(cls):
        cls.a = 40
        Test.a = 50

    @staticmethod
    def m3():
        Test.a = 60


t = Test()
t.m1()  # a = 30
t.m2()  # a = 40 an d will be 50
t.m3()  # a = 60
Test.a = 70  # modifying a outside the class now a = 70
print(Test.a)
'''

# -----------------------------
# Example Programs set-1 about instance and static variables:

# 1-

'''
class Test:
    a = 10  # static variable

    def m1(self):
        self.a = 888  # instance variable


t1 = Test()
t1.m1()
print(Test.a)  # will return static variable a = 10
print(t1.a)  # will return instance variable a = 888

print('-' * 10)
# ---------------------
# 2-


class Test:
    a = 10  # static variable

    def m1(self):
        Test.a = 888  # static variable coz we are using class name Test.a but not self.a


t1 = Test()
t1.m1()
print(Test.a)  # static variable a will be updated to 888
print(t1.a)  # static variable a will be updated to 888 , coz we dont have no instance variable, priority to instance variable if it was available

print('-' * 10)
# -------------------------
# 3-


class Test:
    a = 10  # static variable

    def __init__(self):
        self.b = 20  # instance variable


t1 = Test()
t2 = Test()
print('t1: ', t1.a, t1.b)  # 10 20
print('t2: ', t2.a, t2.b)  # 10 20
t1.a = 888  # new instance variable will be added a = 888 ,
t1.b = 999  # instance variable b will be modified from 20 to 999
print('t1: ', t1.a, t1.b)
print('t2: ', t2.a, t2.b)


print('-' * 10)
# ------------------
# 4-


class Test:
    a = 10 # static variable

    def __init__(self):
        self.b = 20 # instance variable


t1 = Test()
t2 = Test()

print('t1: ', t1.a, t1.b)  # 10 20
print('t2: ', t2.a, t2.b)  # 10 20
Test.a = 888 # static variable will be modified from 10 to 888
Test.b = 999 # new static variable b will be created b = 999
print('t1: ', t1.a, t1.b)  # 888 20
print('t2: ', t2.a, t2.b)  # 888 20
print('Test: ', Test.a, Test.b)  # 888 999

'''

# -------------------------------------
# Example Programs set-2 about instance and static variables:
'''
# 1-


class Test:
    a = 10  # static variable

    def __init__(self):
        self.b = 20  # instance variable


t1 = Test()
t2 = Test()
Test.a = 888
t1.b = 999

print('t1: ', t1.a, t1.b)  # will return 888 999
print('t2: ', t2.a, t2.b)  # will return 888 20

# 2-
# -----------------------------
print('-' * 10)


class Test:
    a = 10  # static variable

    def __init__(self):  # constructor
        self.b = 20  # instance variable

    def m1(self):  # instance method
        self.a = 888  # instance variable
        self.b = 999  # instance variable


t1 = Test()
t2 = Test()
t1.m1()
print('t1: ', t1.a, t1.b)  # 888 999
print('t2: ', t2.a, t2.b)  # 10 20

# 3-
# ----------------------------
print('-' * 10)


class Test:
    a = 10

    def __init__(self):
        self.b = 20  # instance

    def m1(self):
        self.a = 888  # instance
        self.b = 999  # instance


t1 = Test()
t2 = Test()
t1.m1()
t2.m1()
print('t1: ', t1.a, t1.b)  # 888 999
print('t2: ', t2.a, t2.b)  # 888 999

# 4-
print('-' * 10)
# -------------------


class Test:
    a = 10  # static variable

    def __init__(self): # constructor
        self.b = 20  # instance variable

    @classmethod
    def m1(cls): # class method
        cls.a = 888  # static variable
        cls.b = 999  # static variable


t1 = Test()
t2 = Test()
t1.m1()
#t2.m1()
print('t1: ', t1.a, t1.b)  # 888 20
print('t2: ', t2.a, t2.b)  # 888 20
print('Test: ', Test.a, Test.b)  # 888 999
'''

# -------------------------
# How to delete static variables:
# by using class name or cls class variable

# 1-ex

'''
class Test:
    a = 10

    @classmethod
    def m1(cls):
        # del Test.a
        del cls.a


#t = Test()
print(Test.__dict__)
# t.m1()
del Test.a  # static variable a is deleted.
print(Test.__dict__)  # static variable a is deleted after calling t.m1()


print('-' * 10)
# ------------------
# 2 ex:


class Test:
    a = 10  # staticvariable

    def __init__(self):  # constructor
        Test.b = 20  # static variable
        del Test.a

    def m1(self):  # instance method
        Test.c = 30  # static coz we are using class name to add variable Test.c
        del Test.b

    @classmethod
    def m2(cls):  # class method
        cls.d = 40  # static
        del Test.c

    @staticmethod
    def m3():  # static method
        Test.e = 50  # static
        del Test.d


t = Test()  # a will be deleted and b will be added
t.m1()  # c will be added and b will be deleted
t.m2()  # c will be deleted and d will be added
t.m3()  # d will be deleted and e will be added
del Test.e  # e will be deleted
print(Test.__dict__)
'''

# ----------------------
# deleting static variable by using object reference will get error so we cannot
# delete static variable by using object refence or self

# ex:

'''
class Test:
    a = 10


t = Test()
print(t.a)  # a is still not deleted
# del t.a  # AttributError: a, so we cannot delete static variable using object reference, we need to use class name or cls to
# delete static variable.
del Test.a
print(Test.__dict__)  # a is deleted
'''

# --------------------
# instance variable vs Static variable:

'''
class Test:
    a = 10

    def __init__(self):
        self.b = 20


t1 = Test()
t2 = Test()
Test.a = 888
t1.b = 999
print('t1: ', t1.a, t1.b)  # 888 999
print(f't2: {t2.a}, {t2.b}')  # 888 20
'''

# ------------------------------

# Local variables: hold temprary values and we dont use no cls or self or object reference or class name.
# Local variables are local for the particulair method only, and cannot be reached from outside that method.

'''
class Test:
    @staticmethod
    def average(list):  # staticmethod
        # local variable coz we did not use cls and self or object reference or class name
        result = sum(list) / len(list)
        print('The average of this list: ', result)

    @staticmethod
    def wish(name):
        for i in range(5):  # i is a Local  variable to hold temprary values
            print(f'{i}- Hello {name}.')


list1 = [10, 20, 30, 40]
Test.average(list1)
Test.wish('Mustapha')

# --------------------------
print('-' * 10)
# Local variables are local for the particulair method only, and cannot be accessed from outside that method:


class Test:
    def m1(self):
        # local variable coz we did not use cls or self or class name or object reference.
        a = 10
        print(a)

    def m2(self):
        print(a)


t = Test()
t.m1()
# t.m2() : will return NameError: name 'a' is not defined  coz a is local variable in m1 and not defined in m2:
#t.m2()

'''

# -------------------------

# Mini Bank application:


class Customer:
    '''This class developed by Me and describes bank operations'''
    bankname = 'MustaphaBank'  # static variable

    def __init__(self, name, balance=0.0):  # constructor
        self.name = name  # instance variable
        self.balance = balance  # instance variable

    def deposite(self, amount):
        self.balance = self.balance + amount
        print(f'After deposite balance is: {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient Funds... cannot perform this operation.')

        else:
            self.balance = self.balance - amount
            print(f'Balance after withdraw is: {self.balance}')


print(f'Welcome to {Customer.bankname}: ')
name = input('Enter your name: ')
c = Customer(name)

while True:
    print('d-Deposite\nw-withdraw\ne-Exit')
    option = input('Choose your option: ')
    if option.lower() == 'd':
        amount = float(input('Enter amount to deposite: '))
        c.deposite(amount)

    elif option.lower() == 'w':
        amount = float(input('Enter amount to take or withdraw: '))
        c.withdraw(amount)

    elif option.lower() == 'e':
        print('Thanks for banking.')
        break

    else:
        print('Your option is invalid... please choose a valid option.')


# -------------------------
