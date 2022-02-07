# Types of methods:

# 1- instance method
# 2- class method
# 3- static method

'''
class Student:
    def __init__(self, name, marks):
        self.name = name  # instance variable
        self.marks = marks  # instance variable

    def display(self):  # instance method
        print(f'Hi {self.name}.')
        print(f'Your Marks are {self.marks}.')

    def grade(self):
        if self.marks >= 60:
            print('You got first Grade.')

        elif self.marks >= 50:
            print('You got second Grade')

        elif self.marks >= 35:
            print('You got the third Grade.')

        else:
            print('You are Failed')


n = int(input('Enter number of students: '))
for i in range(n):
    name = input('Enter name of student: ')
    marks = int(input('Enter marks: '))

    t = Student(name, marks)
    t.display()
    t.grade()
    print()
'''

# ----------------------------------------
# Setter and Getter Method: are type of instance method.
# we can set and get the values of instance variables by using setter and getter methods.

# setter method (also known as mutator method): to set value to instance variables:

# syntax: for student Marks for example:

'''
def setMarks(self, marks):
    self.marks = marks

# getter method (known as accessor method) , is we wnat to get instance variables values:
# syntax:


def getMarks(self):
    return self.marks

# Example:


class Student:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks


n = int(input('Enter number of student: '))
students = []
for i in range(n):
    s = Student()
    name = input('Enter name: ')
    marks = int(input('Enter marks: '))
    s.setName(name)
    s.setMarks(marks)
    students.append(s)
    print()

# getting datato be printed:
for s in students:
    print(f'Hello {s.getName()}.')
    print(f'Your Marks are: {s.getMarks()}')
    print()
'''

# ------------------
# class methods:

# ex1:

'''
class Test:
    x = 10

    @classmethod
    def m1(cls):
        print(cls.x)


Test.m1()
print()
# ex2:


class Bird:
    wings = 2

    @classmethod
    def fly(cls, name):
        #cls.name = name
        print('{} flying with {} wings.'.format(name, cls.wings))


Bird.fly('Parrot')
Bird.fly('Eagle')

print()
# Program to track number of objects created for a class :


class Test:
    count = 0  # static variable

    def __init__(self):  # constructor
        Test.count = Test.count + 1

    @classmethod
    def getNoOfObects(cls):  # class method
        print('The number of Objects created:', cls.count)


Test.getNoOfObects()
t1 = Test()
t2 = Test()
t3 = Test()
t4 = Test()
Test.getNoOfObects()
'''

# -------------------
# instance methods vs class methods:

# instance variable    staic variable
# instance variables&  only static variable
# static variables
# No decorator         @classmethod
# self                 cls
# object reference,    object reference or class name to call,
# to call instance,    class method, but recommended class name.
# method


# ------------------------
# Static methods and demo: we dont use self, or cls
# if we dont use instance variable neither static variable means we are talking about static method:
'''
# syntax:
class Test:
    @staticmethod
    def m1():
        pass


Test.m1()  # calling of the static method, we can use also object reference


# ex:
class mustaphamath():

    @staticmethod
    def add(a, b):
        print(f'The sum: {a}+{b} = {a+b}')

    @staticmethod
    def product(a, b):
        print(f'The product: {a}*{b} = {a*b}')

    @staticmethod
    def average(a, b):
        print(f'The average: {a+b}/2 = {(a + b) / 2}')


mustaphamath.add(12, 10)
mustaphamath.product(12, 10)
mustaphamath.average(12, 10)
'''

# --------------------------
# instance method vs class method vs Static method
# instance variable ---> instance method ----> self
# static variable ----> class method ---> cls ---> @calssmethod
# no instance , no static variable ----> static method ---> @staticmethod

# ex1
'''
class Test:
    def m1():
        print('some method.')


t = Test()
t.m1() # TypeError: m1() takes 0 positional arguments but 1 was given , coz we did not use self variable
'''

# ex2:

'''
class Test:
    def m1(x):  # instance method coz we use x and we can use self
        print('some method.')


t = Test()
t.m1()
# t.m1(10) # invalid
'''

# ex3:
'''
# in this method we are not using any decorator and we are are calling it with class name Test.m1() ==> it is static method


class Test:
    def m1():
        print('some method.')


Test.m1()
'''

# ex 4:

# we are not using any decorator and we are using an argument

'''
class Test:
    def m1(x):
        print('some method.')


#Test.m1()  # TypeError: m1() missing 1 required positional argument: 'x'
Test.m1(10)
'''

# -----------
# Accessing Members of one class inside another class:

'''
class Employee:
    def __init__(self, eno, ename, esal): #constructor
        self.eno = eno
        self.ename = ename
        self.esal = esal

    def display(self): # instance method
        print('Employee Number is', self.eno)
        print('Employee Name', self.ename)
        print('Employee esal', self.esal)


class Manger:
    def updateEmpSal(emp):
        emp.esal = emp.esal + 10000
        emp.display()


emp = Employee(101, 'baba', 45000)
Manger.updateEmpSal(emp)
'''
# -----------------------------------------------------
# inner classes: class inside another class:
# without existing one type of object, if there is no chance of existing another type of object, then we should go for inner classes:


class University:  # Outer class
    class Department:  # Inner class
        pass
# Department cannot exist without University.


class Car:  # Outer class
    class Engine:  # Inner class
        pass

# Engine cannot exist without Car.


class Head:  # Outer class
    class Brain:  # Inner class
        pass

# without Head , brain will not exist ==> that is wht we use Inner class
# without Outer classes , there is ni chance to go for Inner classes.

# Advantages of Inner Classes:
# 1- it improves modularity of the application.
# 2- it imporoves security of the application.

# Demo program to define and use inner classes:


'''
class Outer:
    def __init__(self):
        print('Outer object Creation.')

    class Inner:
        def __init__(self):
            print('Inner object Creation.')

        def m1(Self):
            print('Inner class method.')


# calling m1 method: first create outer object then inner object dat require outer object then call inner method m1().
# o = Outer()
# i = o.Inner()
# i.m1()

# or

# i = Outer().Inner()
# i.m1()

# or
Outer().Inner().m1()
'''
# ---------
# Nesting of Inner Classes:

# ex1: instance method

'''
class Outer:
    def __init__(self):
        print('Outer class object creation.')

    class Inner:
        def __init__(Self):
            print('Inner class object creation.')

        class InnerInner:
            def __init__(self):
                print('InnerInner class object creation.')

            def m1(self):
                print('Nested Inner class method.')


o = Outer()
i = o.Inner()
ii = i.InnerInner()
ii.m1()

# or
# Outer().Inner().InnerInner().m1()
'''


# ex2: @staticmethod
'''
class Outer:
    def __init__(self):
        print('Outer class object creation.')

    class Inner:
        def __init__(Self):
            print('Inner class object creation.')

        class InnerInner:
            def __init__(self):
                print('InnerInner class object creation.')

            @staticmethod
            def m1():
                print('Nested Inner static method.')


# to call static method m1() , class InnerInner is not required (optionel):
Outer().Inner().InnerInner().m1()
# or
print('-' * 10)
Outer().Inner().InnerInner.m1()
'''

# Nesting of Inner Classes Demo-Program-2:

'''
class Human:
    class Head:  # Inner class of Human
        def talk(self):
            print('Talking...')

        class Brain:
            def think(self):  # Inner class of Head
                print('Thinking...')


#human = Human()
#head = human.Head()
# head.talk()
#brain = head.Brain()
# brain.think()

# or
Human().Head().talk()
Human().Head().Brain().think()
'''
# -----------------------------------

'''
class Human:
    def __init__(self, name):
        print('Human Object Creation...')
        self.name = name
        self.head = self.Head()

    def info(self):
        print('Hello my self ', self.name)
        print('I am full busy with')
        self.head.talk()
        self.head.brain.think()

    class Head:
        def __init__(self):
            print('Head Object Creation...')
            self.brain = self.Brain()

        def talk(self):
            print('Talking...')

        class Brain:
            def __init__(self):
                print('Brain Object creation...')

            def think(self):
                print('Thinking...')


human = Human('Mustapha')
human.info()
'''
# ------------------------------------------

'''
class Human:
    def __init__(self, name):
        print('Human Object Creation...')
        self.name = name
        self.head = self.Head()

    class Head:
        def __init__(self):
            print('Head Object Creation...')
            self.brain = self.Brain()

        class Brain:
            def __init__(self):
                print('Brain Object Creation...')


human = Human('baba')
'''
# ---------------

# Inner classes Demo Program-3:

'''
class Person:
    def __init__(self, name, dd, mm, yyyy):
        print('Person Object Creation...')
        self.name = name
        self.dob = self.Dob(dd, mm, yyyy)

    def info(self):
        print(f'Name: {self.name}')
        self.dob.display()

    class Dob:  # Dob = date of birth
        def __init__(self, dd, mm, yyyy):
            print('Dob Object Creation...')
            self.dd = dd
            self.mm = mm
            self.yyyy = yyyy

        def display(self):
            print('Dob = {}/{}/{}'.format(self.dd, self.mm, self.yyyy))


p = Person('Mustapha', 1, 2, 1968)
p.info()
'''

# -------------------------------
# Nested Methods: Method inside a  method

'''
class Test:
    def m1(self):
        def calc(a, b):
            print('The sum', a + b)
            print('The Product', a * b)
            print('The difference', a - b)
            print('The average', (a + b) / 2)
            print('-' * 10)

        calc(10, 20)
        calc(100, 200)
        calc(1000, 2000)


# Test().m1()
# or
t = Test()
t.m1()
'''
# -----------------------------------
# Garbage Collection & Destructors:
# is responssable of collecting Garbage = useless objects to not take memory and then the will be program failure.
# ==> always free memory available.
# Garbage object ==> if does not contain any reference variable.

# how to enable and disable Garbage Collector
# by default Garbage Collector is enable.
# to check if Garbage Collector is enable or not we use gc module in python:

# 1- gc.isenabled() if it return True then Garbage Collector is enable. if False the it is disabled.
# 2- gc.disable() to disable Garbage Collector.
# 3- gc.enable() to enable Garbage Collector.

'''
import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())
'''

# when should we disable Garbage Collector (this is almost 0,0001% cases happen) means that most of the time Garbage is enabled:
# 1- if we have enough Memory
# 2- when we have very less objects
# then we gain more memory that Garbage Collector dont run in background.

# Destructors:
# Garbag call destructors to perfome clean up activities (like resource deallocation activities like close db connection etc.. ),
# and once done then Object will be destroyed
# Destructor is a special method and the name should be __del__
# Conclusion :
# The job of destructor is not to destroy object and it is to perform clean up activities, destroying object,
# will taken care by PVM (python virtual machine).

# ex1:
'''
import time


class Test:
    def __init__(self):  # contructor
        print('Object Initialization Activities.')

    def __del__(self):  # destructor
        print('Fulfilling last wish and performing clean up Activities. ')


t = Test()  # constructor will be executed
t = None  # destructor will be executed
time.sleep(10)
print('End of Application')
'''

# ex2:
# when a program is finishing executing the automatically destructor will be called:

'''
class Test:
    def __init__(self):  # contructor
        print('Object Initialization Activities.')

    def __del__(self):  # destructor
        print('Fulfilling last wish and performing clean up Activities. ')


t1 = Test()
t2 = Test()
print('End of Application.')
print()
'''

# -------

'''
class Test:
    def __init__(self):  # contructor
        print('Object Initialization Activities.')

    def __del__(self):  # destructor
        print('Fulfilling last wish and performing clean up Activities. ')


t1 = Test()
t2 = Test()
t1 = None
t2 = None
print('End of Application.')
'''

# Destructor Demo Programs - 2,3

'''
import time


class Test:
    def __init__(self):
        print('Constructor execution...')

    def __del__(self):
        print('Destructor execution...')

# t1, t2, t3 are reference variables:
# if the object does not contain any reference variable then Destructor execute and it will be ready for Garbage collection gc.

# ex1:


t1 = Test()
t2 = t1
t3 = t1
del t1
time.sleep(10)
print('Object not destroyed afer deleting t1.')
del t2
time.sleep(10)
print('Object not destroyed even after deleting t2.')
print('Removing last reference:')
del t3
print('End of application.')
'''

# ex2:
'''
import time


class Test:
    def __init__(self):
        print('Constructor execution...')

    def __del__(self):
        print('Destructor execution...')


l = [Test(), Test(), Test()]
print('Making List object eligible for GC:')
del l  # all object inside will be destroyed.
time.sleep(10)
print('End of application.')
print()
print('ex3: ')

# ---------------------

# ex 3:

import time


class Test:
    def __init__(self):
        print('Constructor execution...')

    def __del__(self):
        print('Destructor execution...')


l = [Test(), Test(), Test()]
time.sleep(10)
print('End of application.')
'''

# --------------------
# The 3 important interview Questions :
# 1- what is the difference between del t1 and t1 = None ?:

# del t:

'''
class Test:
    def __init__(self):
        print('Constructor')

    def __del__(self):
        print('Destructor')


t = Test()
# print(t)
del t # will remove object and reference object variable.
print('End of Application.')
# print(t) # NameError: name 't' is not defined
print()


# t = None:


class Test:
    def __init__(self):
        print('Constructor')

    def __del__(self):
        print('Destructor')


t = Test()
t = None  # t is assigned to None Object.
print('End of Application.')
print(t)
'''

# -------

# 2- how to find the number of references variables of an object ? :
'''
# ex1:
import sys


class Test:
    pass


t1 = Test()
print(sys.getrefcount(t1))  # it will be 2, t1 and self.

# ex2:
import sys


class Test:
    pass


t1 = Test()
t2 = t1
t3 = t2
t4 = t3
print(sys.getrefcount(t1))  # it will be 5: t1, t2, t3, t4 and self.

# ex3:

import sys


class Test:
    pass


t1 = Test()
t2 = t1
t3 = t2
t4 = t3
del t3, t4
print(sys.getrefcount(t1))  # it will be 3: t1, t2, and self.
'''

# ------------
# 3- what is the difference between constructor and destructor ? :
#  Constructor                                                          Destructor
#  __init__()                                                           __del__()
#  Initialisation activities(self.name, self.age .....)                 cleanup activities
# After creating object constructor will be called                      will be called just before destroying an object

# ------------------------------
# Using Members of One class inside another class: there ar 2 ways:

# 1- by using HAS-A Relationship (Composition) ==> the advantage is: Code reusability
# 2- by using IS-A Relationship (Inheritance)

'''
# ex1:
# class Car HAS-A Engine reference:


class Engine:
    def __init__(self):
        self.power = '125KW'

    def useEngine(self):
        print('Engine Specific Funcyionality.')


class Car:
    def __init__(self):
        self.engine = Engine()

    def useCar(self):
        print('Car required Engine Functionality.')
        self.engine.useEngine()
        print(self.engine.power)


c = Car()
c.useCar()
'''

# -----
# ex2:

'''
class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def getInfo(self):
        print(
            f'Car Name: {self.name}, Car Model: {self.model}, Car Color: {self.color}.')


class Employe:
    def __init__(self, ename, eno, car):
        self.ename = ename
        self.eno = eno
        self.car = car

    def empInfo(self):
        print('Employe Name:', self.ename)
        print('Employe eno:', self.eno)
        print('Employe Car Info: ')
        self.car.getInfo()


car = Car('Suzuki', '1,3vvt', 'Black')
e = Employe('Mustapha', 228855, car)
e.empInfo()
'''
# --------------------------

# ex3: HAS-A Relationship

# method-1:

'''
class SportsNews:
    def sportsInfo(self):
        print('Sports Information-1')
        print('Sports Information-2')
        print('Sports Information-3')
        print('Sports Information-4')


class MoviesNews:
    def moviesInfo(self):
        print('Movies Information-1')
        print('Movies Information-2')
        print('Movies Information-3')
        print('Movies Information-4')


class PoliticsNews:
    def politicsInfo(self):
        print('politics Information-1')
        print('politics Information-2')
        print('politics Information-3')
        print('politics Information-4')


class MustaphaNews:
    def __init__(self):
        self.sports = SportsNews()
        self.movies = MoviesNews()
        self.politics = PoliticsNews()

    def getTotalNews(self):
        print('Welcome to Mustapha News: ')
        self.sports.sportsInfo()
        print()
        self.movies.moviesInfo()
        print()
        self.politics.politicsInfo()


Mnews = MustaphaNews()
Mnews.getTotalNews()

'''
# method-2:

'''
class SportsNews:
    def sportsInfo(self):
        print('Sports Information-1')
        print('Sports Information-2')
        print('Sports Information-3')
        print('Sports Information-4')


class MoviesNews:
    def moviesInfo(self):
        print('Movies Information-1')
        print('Movies Information-2')
        print('Movies Information-3')
        print('Movies Information-4')


class PoliticsNews:
    def politicsInfo(self):
        print('politics Information-1')
        print('politics Information-2')
        print('politics Information-3')
        print('politics Information-4')


class MustaphaNews:
    def __init__(self, sports, movies, politics):
        self.sports = SportsNews()
        self.movies = MoviesNews()
        self.politics = PoliticsNews()

    def getTotalNews(self):
        print('Welcome to Mustapha News: ')
        self.sports.sportsInfo()
        print()
        self.movies.moviesInfo()
        print()
        self.politics.politicsInfo()


sports = SportsNews()
movies = MoviesNews()
politics = PoliticsNews()

Mnews = MustaphaNews(sports, movies, politics)
Mnews.getTotalNews()
'''

# -------------------
# Using Members of one class inside another class: 2nd method:
# 2- By inheritance (IS-A Relationship) = Parent to child Relationship:

# syntax:


class P:
    pass
    # 10 methods


class c(P):
    pass
    # 5 methods ==> class c will contains 15 methods

# advantage of inheritance:
# code Reusability
# code extendibility (in our syntax case from 10 to 15)

# Parent class has one method m1


'''
class P:
    def m1(self):
        print('Parent method.')

# class c (child will have 2 methods m1 and m2)

# 1-ex:


class C(P):
    def m2(self):
        print('Child method.')


c = C()
c.m1()
c.m2()
print('-' * 10)
# 2-ex:


class P:
    a = 10  # static variable

    def __init__(self):  # constructor
        print('Parent constructor.')
        self.b = 20  # instance variable

    def m1(self):  # instance method
        print('Parent instance method.')

    @classmethod
    def m2(cls):
        print('Parent class method.')

    @staticmethod
    def m3():
        print('Parent Static method.')


class C(P):  # all parent class codes will be inherited to child class.
    pass


c = C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()
'''

# ------------------------
# Developing Employee and Person classes with inheritance:

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eatndrink(self):
        print('Eat rize and dring cola.')


class Employee(Person):
    def __init__(self, name, age, eno, esal):
        # self.name = name # will be called from parent class Person by using super().__init__(name, age)
        # self.age = age  # will be called from parent class Person by using super().__init__(name, age)
        # or
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal

    def work(self):
        print('Coding python programs.')

    def empInfo(self):
        print('Employee Name:', self.name)
        print('Employee Age:', self.age)
        print('Employee enumber:', self.eno)
        print('Employee salary:', self.esal)


e = Employee('Mustapha', 53, 992255184, str(2000) + ' euro')
e.eatndrink()
e.work()
e.empInfo()
'''

# --------------------------------------------------
# IS-A vs HAS-A
# if we want to extend existing functionality with some extra functionality then we should go for IS-A or Inheritance.
# if we dont want to extend and just we have to use existing functionality then we should go for HAS-A or Composition.

# Employee IS-A Person and HAS-A Car

'''
class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def getinfo(self):
        print(
            f'\tCar Name: {self.name}\n\tModel: {self.model}\n\tColor: {self.color}')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eatndrink(self):
        print('Eating Rize & Drinking Cola.')


class Employee(Person):
    def __init__(self, name, age, eno, esal, car):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal
        self.car = car

    def work(self):
        print('Coding Python Programs.')

    def empinfo(self):
        print('Employee Name: ', self.name)
        print('Employee Age: ', self.age)
        print('Employee Number: ', self.eno)
        print('Employee Salary: ', self.esal)
        print('Employee Car information: ')
        self.car.getinfo()  # Employee using car Functionality


car = Car('Suzuki', 'VVT', 'Black')
e = Employee('Mustapha', 53, 88776655, '2000 euro', car)
e.eatndrink()  # Employee using Person class Functionality
e.work()
e.empinfo()
'''
# -------------------------------------
# composition vs aggregation, both are HAS-A relation:
# in composition objects are strongly associated
# in aggregation objects are weakly associated

# composition:

'''
class University:  # Top level class
    def __init__(self):
        self.dept = self.Department()

    class Department:  # Inner class
        pass


u = University()

# aggregation:


class Professor:
    pass


class Department:
    def __init__(self, professor):
        self.professor = Professor


professor = Professor()
cesdept = Department(professor)
itdept = Department(professor)
'''
# -------------------------------
# Types of Inheritance:
# 1-single inheritance
# 2-multi level inheritance
# 3-hierarchical inheritance
# 4-multiple inheritance
# 5-hybrid inheritance
# 6-cyclic inheritance

# 1- single inheritance:
# The concept of inheriting members from one class to another class is known as single inheritance.
# single Parent and single child:

'''
class P:
    def m1(self):
        print('Parent class method.')


class C(P):
    def m2(self):
        print('Child class method.')


c = C()
c.m1()
c.m2()
print()
# -------------------
# 2-Multi Level inheritance:
# The concept of inheriting members from multiple classes to single class with the concept of one after another,
# is known as multi level inheritance.


class P:
    def m1(self):
        print('Parent Method.')


class C(P):
    def m2(self):
        print('Child Method.')


class CC(C):
    def m3(self):
        print('Sub Child Method.')


c = CC()
c.m1()
c.m2()
c.m3()
print()
# ------------------------
# Hierarchical inheritance: One Parent class and Multiple Child classes:
# The concept of inheriting members from one class to multiple classes which present at same level is,
# known as hierarchical inheritance.
# One Parent but Multiple child classes and all child classes are at same level.


class P:
    def m1(self):
        print('Parent Method.')


class C1(P):
    def m2(self):
        print('Child1 Method.')


class C2(P):
    def m3(self):
        print('Child2 Method.')


c1 = C1()
c1.m1()
c1.m2()
# c1.m3() # AttributeError: 'C1' object has no attribute 'm3'
print()
c2 = C2()
c2.m1()
c2.m3()
# c2.m2() # AttributeError: 'C2' object has no attribute 'm2'
'''

# ------------------------------------
# Multiple inheritance: Multiple Parents classes and one child class:

'''
class P1:
    def m1(self):
        print('Parent1 Method.')


class P2:
    def m2(self):
        print('Parent2 Method.')


class C(P1, P2):
    def m3(self):
        print('Child Method.')


c = C()
c.m1()
c.m2()
c.m3()

# if the same method is inherited from both parent classes,
# then python will always consider the order of parent classes,
# in the declaration of the child class.
# class C(P1, P2): ==> P1 method will be considered.
# class C(P2, P1): ==> P2 method will be considered.

# Considering P1 method:


class P1:
    def m1(self):
        print('Parent1 Method.')


class P2:
    def m1(self):
        print('Parent2 Method.')


class C(P1, P2):
    def m2(self):
        print('Child Method.')


print()
c = C()
c.m1()
c.m2()
# ------------------------

# Considering P2 method:


class P1:
    def m1(self):
        print('Parent1 Method.')


class P2:
    def m1(self):
        print('Parent2 Method.')


class C(P2, P1):
    def m2(self):
        print('Child Method.')


print()
c = C()
c.m1()
c.m2()
'''
# ---------------------------

# Types of inheritance:

# 1- Hybrid inheritances: Combination of different types of inheritances:,
# combination of single, multi level, multiple and hierarchical inheritances:
# Note: in hybrid inheritance, method resolution is based on MRO algorithm.

# 2- Cyclic inheritance: not required in java or python language and not supported and will get error:
# Cyclic inheritance is the concept of inheriting members from one class to another class in cyclic way,
# is called cyclic inheritance:


'''
class A(B):
    pass


class B(A):
    pass
'''
# ---------

'''
class A(A):
    pass
'''
# -------

# Method Resolution Order (MRO) in Hybrid Inheritance Part-1:
# In Hybrid Resolution Order The method resolution,
# order is decided based on MRO algorithm.
# we can find MRO of any classy using mro() function.
# print(classname.mro())

'''
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


# it will search first in A class (__main__.A), if none is found the it will search in parent object class.
print(A.mro())
print(B.mro())  # will search in B, A, and A Parent class object.
print(C.mro())  # will search in C, A, and A Parent class object.
print(D.mro())  # will search in D, B, C, and A, and A Parent class object.

print()


class A:
    def m1(self):
        print('A class Method.')


class B(A):
    def m1(self):
        print('B class Method.')


class C(A):
    def m1(self):
        print('C class Method.')


class D(B, C):
    pass
    # def m1(self):
    #print('D class Method.')


d = D()
d.m1()

print()

# m1 method not found in D, B, C, A, Class A Prent object
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()
#d.m1() # AttributeError: 'D' object has no attribute 'm1'
'''

# ---------------------------
# Method Resolution Order (MRO) in Hybrid Inheritance Part-2:

'''
class A:
    pass


class B:
    pass


class C:
    pass


class D(A, B):
    pass


class E(B, C):
    pass


class F(D, E, C):
    pass


print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
print(E.mro())
print(F.mro())

# -------
print()


class A:
    def m1(self):
        print('A Class Method.')


class B:
    def m1(self):
        print('B Class Method.')


class C:
    def m1(self):
        print('C Class Method.')


class D(A, B):
    def m1(self):
        print('D Class Method.')


class E(B, C):
    def m1(self):
        print('E Class Method.')


class F(D, E, C):
    def m1(self):
        print('F Class Method.')


f = F()
f.m1()

# -------

print()


class A:
    pass


class B:
    def m1(self):
        print('B Class Method.')


class C:
    def m1(self):
        print('C Class Method.')


class D(A, B):
    pass


class E(B, C):
    pass


class F(D, E, C):
    pass


f = F()
f.m1()

# MRO Algorithm: known as c3 algorithm.
# Proposed by Samuel Pedroni.
# it follows DLR = Depth Left to Right.
# mro(x) = x + merge(mro(p1), mro(p2), mro(p3),...,Parentlist), we consider only immediate parents.
# we need to consider also Head Element and Tail part.
# c1,c2,c3,... are classes:
# First element is considered ad Head ==> c1 is the head.
# The rest is considered as Tail part ==> c2,c3...

# -------------------------------------
# MRO algorithm-1:
# mro(A) = A, O
# mro(B) = B, O
# mro(C) = C, O
# mro(D) = D, A, B, O
# mro(E) = E, B, C, O
# mro(F) = F + merge(mro(D), mro(E), mro(C),..., Parentslist)
# mro(F) = F + merge(DABO, EBCO, CO, DEC)
# mro(F) = F + D + merge(ABO, EBCO, CO, EC)
# mro(F) = F + D + A + merge(BO, EBCO, CO, EC) # ignore B coz it is present in the next tail list
# mro(F) = F + D + A + E + merge(BO, BCO, CO, C)
# mro(F) = F + D + A + E + B + merge(O, CO, CO, C)
# mro(F) = F + D + A + E + B + C + merge(O, O, O)
# mro(F) = FDAEBC0
# ex:


print()


class A:
    def m1(self):
        print('A Class Method.')


class B:
    def m1(self):
        print('B Class Method.')


class C:
    def m1(self):
        print('C Class Method.')


class D(A, B):
    def m1(self):
        print('D Class Method.')


class E(B, C):
    def m1(self):
        print('E Class Method.')


class F(D, E, C):
    def m1(self):
        print('F Class Method.')


f = F()
f.m1()  # will check for m1() in F first, if not found then it will serach in this order DAEBCO

print()

# MRO algorithm-1:


class A:
    def m1(self):
        print('A Class Method.')


class B:
    def m1(self):
        print('B Class Method.')


class C:
    def m1(self):
        print('C Class Method.')


class D(A, B):
    def m1(self):
        print('D Class Method.')


class E(A, C):
    def m1(self):
        print('E Class Method.')


class F(D, E):
    pass


print(F.mro())  # FDEABCO
f = F()
f.m1()  # if it does not find m1() in F then it go for D class and so one.
'''
# ------------------------------------------
# The complete story of super() function theory:

'''
class P:
    def m1(self):
        print('Parent Method.')


class C(P):
    def m2(self):
        self.m1()
        print('Child Method.')


c = C()
c.m2()

print()

# ----------


class P:
    def m1(self):
        print('Parent Method.')


class C(P):
    def m1(self):
        self.m1()
        print('Child Method.')


c = C()
# c.m1() # RecursionError: maximum recursion depth exceeded, to prevent this error and we want m1() of parent class we use:
# super()
print('RecursionError')
print()


class P:
    def m1(self):
        print('Parent Method.')


class C(P):
    def m1(self):
        super().m1()
        print('Child Method.')


c = C()
c.m1()

# if method naming conflict with the same name between child class and parent class then we use super() to call method,
# from the child class
'''

# -------------------------------
# Demo programs to describe use of super() function:

# ex-1:
'''
print('Using super(): ')
print()


class P:
    a = 10  # static variable coz declared at class level

    # Constructor:
    def __init__(self):
        print('Parent Constructor.')

    # instance method:
    def m1(self):
        print('Parent Instance Method.')

    # class method:
    @classmethod
    def m2(cls):
        print('Parent class method.')

    # Static Method:
    @staticmethod
    def m3():
        print('Parent Static Method.')


class C(P):
    def __init__(self):
        print('Child Constructor.')

    # from child class we are calling a, m1(), m2(), m3()
    def method1(self):
        print(super().a)
        super().m1()
        super().m2()
        super().m3()
        super().__init__()  # calling parent constructor.


c = C()
c.method1()

# in the up example there is no naming conflict so we can use self instead of super(),
# coz we use super() in naming conflict:


print()
print('Using self:')
print()


class P:
    a = 10  # static variable coz declared at class level

    # Constructor:
    def __init__(self):
        print('Parent Constructor.')

    # instance method:
    def m1(self):
        print('Parent Instance Method.')

    # class method:
    @classmethod
    def m2(cls):
        print('Parent class method.')

    # Static Method:
    @staticmethod
    def m3():
        print('Parent Static Method.')


class C(P):
    def __init__(self):
        print('Child Constructor.')

    # from child class we are calling a, m1(), m2(), m3()
    def method1(self):
        print(self.a)
        self.m1()
        self.m2()
        self.m3()
        # calling parent constructor. coz constructor is in both parent and child.
        super().__init__()


c = C()
c.method1()
'''

# ex-2: without super() is long code:
'''
print()


class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def display(self):
        print('Name', self.name)
        print('Age', self.age)
        print('Height', self.height)
        print('Weight', self.weight)


class Student(Person):
    def __init__(self, name, age, height, weight, rollno, marks):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.rollno = rollno
        self.marks = marks

    def display(self):
        print('Name', self.name)
        print('Age', self.age)
        print('Height', self.height)
        print('Weight', self.weight)
        print('Rollno', self.rollno)
        print('Marks', self.marks)


s = Student('Mustapha', 53, '1.78cm', '63kg', 101, 99)
s.display()

# ex-2 with super() is shorter code:

print()


class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def display(self):
        print('Name', self.name)
        print('Age', self.age)
        print('Height', self.height)
        print('Weight', self.weight)


class Student(Person):
    def __init__(self, name, age, height, weight, rollno, marks):
        super().__init__(name, age, height, weight)
        self.rollno = rollno
        self.marks = marks

    def display(self):
        super().display()
        print('Rollno', self.rollno)
        print('Marks', self.marks)


s = Student('Mustapha', 53, '1.78cm', '63kg', 101, 99)
s.display()
'''

# --------------------

# how to call method of a particular super class:
# 1- by using : classname.methodname(self) ---> ex: B.m1(self)
# 2- by using : super(classname, self).m1()

'''
# This is multilevel inheritance
class A:
    def m1(self):
        print('A class method.')


class B(A):
    def m1(self):
        print('B class method.')


class C(B):
    def m1(self):
        print('C class method.')


class D(C):
    def m1(self):
        print('D class method.')


class E(D):
    def m1(self):
        print('E class method.')


e = E()
e.m1()

print()


class A:
    def m1(self):
        print('A class method.')


class B(A):
    def m1(self):
        print('B class method.')


class C(B):
    def m1(self):
        print('C class method.')


class D(C):
    def m1(self):
        print('D class method.')


class E(D):
    def m1(self):
        super().m1()


e = E()
e.m1()

print()
print('I want B class Method or Any other class Method: ')


class A:
    def m1(self):
        print('A class method.')


class B(A):
    def m1(self):
        print('B class method.')


class C(B):
    def m1(self):
        print('C class method.')


class D(C):
    def m1(self):
        print('D class method.')


class E(D):
    def m1(self):
        # B.m1(self)
        # A.m1(self)
        super(C, self).m1() # m1() of B class will be, coz super(C) is B.


e = E()
e.m1()
'''

# ---------------------
# super() vs parent class instance variables:
# we cannot use super() to access parent class instance variable, we should use self instead:

'''
# ex-1
class P:
    a = 888  # static variable

    def __init__(self):
        self.b = 999  # instance variable


class C(P):
    def m1(self):
        print(self.a)  # 888
        print(self.b)  # 999
        print(super().a)  # 888
        # print(super().b) # AttributeError: 'super' object has no attribute 'b'


c = C()
c.m1()

print()
# ex-2:


class P:
    a = 888

    def __init__(self):
        self.b = 999


class C(P):
    def __init__(self):
        self.b = 20

    def m1(self):
        print(self.b)
        print(self.a)


c = C()
c.m1()
'''

# --------------------------------
# From child class constructor and instance methods, we can call parent class constructors,
# instance methods, class methods and static methods by using super().

# ex1:

'''
class P:
    def __init__(self):
        print('Parent Constructor.')

    def m1(self):
        print('Parent Instance Method.')

    @classmethod
    def m2(cls):
        print('Parent Class Method.')

    @staticmethod
    def m3():
        print('Parent Static Method.')


class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

    @classmethod
    def m2(cls):
        # super().__init__()
        # super().m1()
        super().m2()
        super().m3()

    @staticmethod
    def m3():
        super().__init__()
        super().m1()
        super().m2()
        super().m3()


c = C()
print()
c.m1()
print()
# from Child class classmethod we cannot use super to call parent class constructor and parent class instance method,
# but we can access parent class static and class metods:
c.m2()
print()
# RuntimeError: super(): no arguments:
# we cannot call from child class static method Parent static class members by using super(), but indirectly we can call
# parent class static and class methods:

# c.m3()

print()


# ex2:
# from class method of child class, how to call parent class constructor and instance methods indirectly:


class P:
    def __init__(self):
        print('Parent Constructor.')

    def m1(self):
        print('Parent Instance Method.')


class C(P):
    @classmethod
    def m2(cls):
        super(C, cls).__init__(cls)
        super(C, cls).m1(cls)


C.m2()

print()

# ex-3:
# how to call Parent class static and class methods from child static method :


class P:
    @classmethod
    def m2(cls):
        print('Parent class Method.')

    @staticmethod
    def m3():
        print('Parent Static Method.')


class C(P):
    @staticmethod
    def m2():
        super(C, C).m2()
        super(C, C).m3()


C.m2()
'''

# -----------------------------------------
# Polymorphism = Many Forms

# example of polymorphism:

# OPerator Overloading:
# 10 + 20 = 20
# 'Mustapha' + 'Labib' = 'MustaphaLabib'

# another example of polymorphism:
# Method Overriding:

'''
class P:
    def marry(self):
        print('Finnish')


class C(P):
    def marry(self):
        print('Moroccan')


c = C()
c.marry()

# Related to Polymorphism:

# 1-Overloading:
# 1- Operator Overloading
# 2- Method Overloading
# 3- COnstructor Overloading

# 2- Overriding:
# 1- Method Overriding
# 2- Constructor Overriding

# 3- Pythonic Behavor:
# Duck Typing
# Easier to Ask Forgiveness than Permission (EAFP)
# Monkey Patching

# ---------------------------------------
print()
# 1-Overloading:
# 1- Operator Overloading
# 2- Method Overloading
# 3- COnstructor Overloading

# 1- Operator Overloading:
print('Plus operator: ')
# plus (+) operator:
print(10 + 20)  # Arithmetic Operator
print('Mustapha' + ' Labib')  # String Concatenation

print()
# star(*) operator:
print('star operator: ')
print(10 * 20)
print('Mustapha ' * 3)

print()


class Book:
    def __init__(self, pages):
        self.pages = pages


b1 = Book(100)
b2 = Book(200)

# between 2 Book objects we cannot apply directly + operator
# print(b1 + b2)  # TypeError: unsupported operand type(s) for +: 'Book' and 'Book'

# to use + operator between 2 Book Objects we have to use __add__() magic method:

print()


class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        total_pages = self.pages + other.pages
        return total_pages


b1 = Book(100)
b2 = Book(200)
b3 = Book(500)
print(b1 + b2)  # 300
print(b1 + b3)  # 600
print(b2 + b3)  # 700
# TypeError: unsupported operand type(s) for +: 'int' and 'Book'
#print(b1 + b2 + b3)
'''

# -------------------------------
#        Operator and                 Corresponding Magic Methods:
# + (corresponding magic method) ===> __add__(self, other)
# - (corresponding magic method) ===> __sub__(self, other)
# * (corresponding magic method) ===> __mul__(self, other)
# / (corresponding magic method) ===> __div__(self, other)
# // (corresponding magic method) ===> __floordiv__(self, other)
# % (corresponding magic method) ===> __mod__(self, other)
# ** (corresponding magic method) ===> __pow__(self, other)
# += (corresponding magic method) ===> __iadd__(self, other)
# -= (corresponding magic method) ===> __isub__(self, other)
# *= (corresponding magic method) ===> __imul__(self, other)
# /= (corresponding magic method) ===> __idiv__(self, other)
# //= (corresponding magic method) ===> __ifloordiv__(self, other)
# %= (corresponding magic method) ===> __imod__(self, other)
# **= (corresponding magic method) ===> __ipow__()
# < (corresponding magic method) ===> __lt__(self, other)
# <= (corresponding magic method) ===> __le__(self, other)
# > (corresponding magic method) ===> __gt__(self, other)
# >= (corresponding magic method) ===> __ge__(self, other)
# == (corresponding magic method) ===> __eq__(self, other)
# != (corresponding magic method) ===> __ne__()

# Overloading > and <= operators for Students class objects:

'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


s1 = Student('baba', 100)
s2 = Student('dialo', 200)
# TypeError: '>' not supported between instances of 'Student' and 'Student'
# print(s1 > s2)

# to avoid this TypeError we need to use Corresponding magic method:


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        # (s1 = self.marks, s2 = other.marks),  we are comparing marks
        return self.marks > other.marks

    def __le__(self, other):
        return self.marks <= other.marks


# is 100 > 200 ? False
s1 = Student('baba', 100)
s2 = Student('dialo', 200)
s3 = Student('Mustapha', 50)
print(s1 > s2)  # False
print(s1 > s3)  # True

# no need to implement __lt__() , it will automatically done in this case coz of using __gt__()
print(s1 < s2)  # True
print(s1 < s3)  # False
print(s1 <= s2)  # True
print(s1 <= s3)  # Flase

# no need to implement __ge__() , it will automatically done in this case coz of using __le__()
print(s1 >= s3)  # True
print(s2 >= s3)  # True
'''

# Program to overload multiplication operator to work Employee objects:

'''
class Employee:
    def __init__(self, name, salaryPerday):
        self.name = name
        self.salaryPerday = salaryPerday
    # Magic Method implementation:

    def __mul__(self, other):
        return self.salaryPerday * other.workingdays


class TimeSheet:
    def __init__(self, name, workingdays):
        self.name = name
        self.workingdays = workingdays

    def __mul__(self, other):
        return self.workingdays * other.salaryPerday


e = Employee('Mustapha', 100)
t = TimeSheet('Mustapha', 20)
print(f'Salary This Month: {e*t}€')
print(f'Salary This Month: {t*e}€')
'''

# -----------------------
# Importance of __str__() method:

# without __str__() method:

'''
class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks


s1 = Student('Mustapha', 101, 95)
s2 = Student('baba', 102, 98)
print(s1)
print(s2)


# ---------------
# with __str__() method
print()


class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def __str__(self):
        return self.name


s1 = Student('Mustapha', 101, 95)
s2 = Student('baba', 102, 98)
print(s1)
print(s2)

# -------------------


class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def __str__(self):
        return f'Name: {self.name}, rollno: {self.rollno}, marks: {self.marks}'


s1 = Student('Mustapha', 101, 95)
s2 = Student('baba', 102, 98)
print(s1)
print(s2)
'''

# -------------------------------------------
# Overloading of + oprator for Nesting Requirements:

'''
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages


b1 = Book(100)
b2 = Book(200)
b3 = Book(500)

print(b1 + b2)
print(b2 + b3)
print(b1 + b3)
# print(b1 + b2 + b3) # TypeError: unsupported operand type(s) for +: 'int' and 'Book', we need to apply :


print()


class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)

    def __str__(self):
        return 'The Total Book pages is: {}'.format(self.pages)


b1 = Book(100)
b2 = Book(200)
b3 = Book(500)
b4 = Book(600)

print(b1 + b2)
print(b2 + b3)
print(b1 + b3)
print(b1 + b2 + b3)
print(b1 + b2 + b3 + b4)

print()

print()


class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        print('add method executed...')
        return Book(self.pages + other.pages)

    def __str__(self):
        return 'The Total Book pages is: {}'.format(self.pages)

    def __mul__(self, other):
        print('mul method executed...')
        return Book(self.pages * other.pages)


b1 = Book(100)
b2 = Book(200)
b3 = Book(500)
b4 = Book(600)
print(b1 + b2 * b3 + b4)
print(b1 * b2 + b3 * b4)
'''

# --------------------------------

# Method Overloading: same method name but diiferent arguments types: supported in java but not in python,
# in python only the last method will be considered:

'''
class Test:
    def m1(self):
        print('non-arg method')

    def m1(self, x):
        print('one-arg method')

    def m1(self, x, y):
        print('two-arg method')


t = Test()
# t.m1() # TypeError: m1() missing 2 required positional arguments: 'x' and 'y'
# t.m1(10) # TypeError: m1() missing 1 required positional argument: 'y'
t.m1(10, 20)
'''

# ---------------------------------------
'''
# why python won't support Method Overloading:


class Test:
    def m1(self, x):
        # print(f'{x} is a : {type(x)}')
        print('{}-argument method'.format(x.__class__.__name__))


t = Test()
t.m1(10)
t.m1(10.3)
t.m1('baba')

'''
# --------------------------------------
# how to define a method with variable number of arguments:

# 3 arguments declaration:

'''
class Test:
    def m1(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            print('Three-argument-method')

        elif a is not None and b is not None:
            print('Two-argument-method')

        elif a is not None:
            print('One-argument-method')

        else:
            print('No-argument-method')


t = Test()
t.m1()
t.m1(10)
t.m1(10, 20)
t.m1(10, 20, 30)
# t.m1(10, 20, 30, 40) # TypeError: m1() takes from 1 to 4 positional arguments but 5 were given

print('')
# Many arguments declaration:


class Test:
    def m1(self, *args):
        print('Variable length arguments.')


t = Test()
t.m1()
t.m1(10)
t.m1(10, 20)
t.m1(10, 20, 30)
t.m1(10, 20, 30, 40, 50, 60)

print('')
# Demo program:


class Test:
    def sum(self, *args):
        total = 0
        for x in args:
            total = total + x
        #print(f'The Sum of {args} = {total}')
        print(f'The Sum = {total}')


t = Test()
t.sum()
t.sum(10)
t.sum(10, 20)
'''

# ------------------------------------
# Constructor Overloading:

# Constructor overloading is not possible in Python.
# if we are trying to declare multiple constructor then PVM will always consider last constructor.

'''
class Test:
    def __init__(self):
        print('no-arg constructor')

    def __init__(self, x):
        print('one-arg construcor')

    def __init__(self, x, y):
        print('two-arg constructor')


#t = Test()
#t = Test(10)
t = Test(10, 20)

print('')
# How to define a constructor with variable number or arguments:

# 3 arguments:


class Test:
    def __init__(self, a=None, b=None, c=None):
        print('Constructor 0/1/2/3 argument')


t = Test()
t = Test(10)
t = Test(10, 20)
t = Test(10, 20, 30)
# t = Test(10, 20, 30, 40) # TypeError: __init__() takes from 1 to 4 positional arguments but 5 were given

print('')
# Multiple arguments:


class Test:
    def __init__(self, *args):
        print('Constructor 0/1/2/3 argument')


t = Test()
t = Test(10)
t = Test(10, 20)
t = Test(10, 20, 30)
t = Test(10, 20, 30, 40, 50, 60, 70)

# we discussed:
                                    #Python        #Java
# 1- Operator Overloading             yes             no
# 2- Method Overloading               no              yes
# 3- Constructor Overloading          no              yes
'''

# ---------------------------------------------------
# Method Overriding and Constructor Overriding:

# 1- Method Overriding:

'''
class Parent:
    def property(Self):
        print('Land + Gold + Cash + Power')

    def marry(self):
        print('Women')


class Child(Parent):
    pass


c = Child()
c.property()
c.marry()

print('')


class Parent:
    def property(Self):
        print('Land + Gold + Cash + Power')

    # Method Overridden
    def marry(self):
        print('Normal Women')


class Child(Parent):
    # Class Method overriding
    def marry(self):
        print('Beautiful Women')


c = Child()
c.property()
c.marry()

print('')

# to call both methods from Parent and Child class :
# in our example want to marry 2 womens:


class Parent:
    def property(Self):
        print('Land + Gold + Cash + Power')

    # Method Overridden
    def marry(self):
        print('Normal Women')


class Child(Parent):
    # Class Method overriding
    def marry(self):
        super().marry()
        print('Beautiful Women')


c = Child()
c.property()
c.marry()

print('')
# Constructor Overriding:


class Parent:
    def __init__(self):
        print('Parent Constructor')


class Child(Parent):
    pass


c = Child()

# -------------------------------


class Parent:
    def __init__(self):
        print('Parent Constructor')

# Constructor Overriding:


class Child(Parent):
    def __init__(self):
        print('Child Constructor')


c = Child()


print('')
# Calling both Constructor Parent and Child :


class Parent:
    def __init__(self):
        print('Parent Constructor')


class Child(Parent):
    def __init__(self):
        super().__init__()
        print('Child Constructor')


c = Child()
'''

# Overriding Demo program:

'''
class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def display(self):
        print('Name: ', self.name)
        print('Age: ', self.age)
        print('Height: ', self.height)
        print('Weight: ', self.weight)


class Employee(Person):
    def __init__(self, name, age, height, weight, eno, esal):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.eno = eno
        self.esal = esal

    def display(self):
        print('Name: ', self.name)
        print('Age: ', self.age)
        print('Height: ', self.height)
        print('Weight: ', self.weight)
        print('Eno: ', self.eno)
        print('Esal: ', self.esal)


e = Employee('Mustapha', 54, 178, 60, 228855, 2000)
e.display()

print('-' * 10)
# code reducity and simplicity:


class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def display(self):
        print('Name: ', self.name)
        print('Age: ', self.age)
        print('Height: ', self.height)
        print('Weight: ', self.weight)


class Employee(Person):
    def __init__(self, name, age, height, weight, eno, esal):
        super().__init__(name, age, height, weight)
        self.eno = eno
        self.esal = esal

    def display(self):
        super().display()
        print('Eno: ', self.eno)
        print('Esal: ', self.esal)


e = Employee('Mustapha', 54, 178, 60, 228855, 2000)
e.display()
'''

# -----------------------------------
# Polymorphism: give flexibility to the programmer:
# 1-Overloading:
# Operator (+)
# Method and Constructor Overloading not supported in python

# 2-Overriding:
# Method and Constructor Overriding supported in python.

# -------------------------------------
# Abstract Method and Abstract Class and interface:
# Abstract method has declaration but no implementation:
# child class will provide implementation:
# in python we can declare abstract method by using,
# @abstractmethod decorator:
# abstractmethod decorator is present in abc module.
# taht is why we need to import abc module.

'''
# Abstract method:

from abc import abstractmethod
class vehicle:

    @abstractmethod
    def getNoOfwheels(self):
        pass


# Abstract Class: Not fully implemented: Partially implemented class:
# ABC = Abstract Base Class: ABC class is in abc module:
# Every abstract class in python should be child class of ABC class which is present in abc module:
# Child class are responsible to provide implementation for parent class abstract methods:

# Abstract Class:

from abc import abstractmethod, ABC
class vehicle(ABC):

    @abstractmethod
    def getNoOfwheels(self):
        pass


class Bus(vehicle):
    def getNoOfwheels(self):
        return 6


class Auto(vehicle):
    def getNoOfwheels(self):
        return 3

# Parent class, we cannot create object coz it is not complete : not implemented:


b = Bus()
print(b.getNoOfwheels())

a = Auto()
print(a.getNoOfwheels())
'''
# -----------------------
# The most important Conclusions:
# if a class contains at least one abstract method and if we are extending ABC class,
# then instantiation (object creation) is not possible.
# For Abstract class with abstract methods, instantiation (object creation) is not possible


# This is not Abstract class it is normal class:
'''
class Test:
    pass


t = Test()

# This is Abstract class but does not contain abstract method:

from abc import *


class Test(ABC):
    pass


t = Test()
'''
# ----------------------------------
# Abstract Class with abstract methos ==> we cannot create object ==> we get error:
# TypeError: Can't instantiate abstract class Test with abstract method m1

'''
from abc import *


class Test(ABC):
    @abstractclassmethod
    def m1(self):
        pass


t = Test()
'''
# ---------------------------------------
# Normal class with abstractmethod:
'''
from abc import *


class Test:
    @abstractclassmethod
    def m1(self):
        pass


t = Test()

# case 2:
# if we are creating child class for abstract class, then for every abstract method of,
# parent class compulsory we should provide implementation in the child class,
# otherwise childclass is also abstract and we cannot create object for child class.

from abc import *

# Abstract class contain abstract method


class Test(ABC):
    @abstractclassmethod
    def m1(self):
        pass

# child class of parent class Test


class SubTest(Test):
    pass


# we cannot create object for child class: TypeError: Can't instantiate abstract class SubTest with abstract method m1,
# becoz we did not implment in child class implementation (method) for parent class abstract method
s = SubTest()
'''

# ---------------------------------------
# case3:

'''
from abc import *


class Test(ABC):
    @abstractclassmethod
    def m1(self):
        pass

    @abstractclassmethod
    def m2(self):
        pass


class SubTest(Test):
    def m1(self):
        print('m1 method implementation')


# TypeError: Can't instantiate abstract class SubTest with abstract method m2
# we cannot create child class object becoz it does not contain abstract method m2, it contain only m1 and it should be both
s = SubTest()
s.m1()
'''

# -------------------------
# case4:
'''
from abc import *


class Test(ABC):
    @abstractclassmethod
    def m1(self):
        pass

    @abstractclassmethod
    def m2(self):
        pass


class SubTest(Test):
    def m1(self):
        print('m1 method implementation')

    def m2(Self):
        print('m2 method implementation')


s = SubTest()
s.m1()
s.m2()

# ----------------------------
print('')
# case5:

from abc import *


class Test(ABC):
    def m1(self):
        print('Non-abstract method')

    @abstractclassmethod
    def m2(self):
        pass


class SubTest(Test):
    def m2(self):
        print('m2 method implementation')


s = SubTest()
s.m1()
s.m2()
'''
# -----------------------------------
# Interfaces in Python: Contains only abstract methods:
# An abstract class can contains both abstract and non-abstract methods,
# if an abstract class contains only abstract methods, such type of abstract class is nothing but interface.
# 100% pure abstract class is nothing but interface.
# interface simply acts as Service Requirement Specification(SRS).

'''
from abc import *

# This is Abstract class but not interface:


class Test(ABC):
    def m1(self):
        print('Hi')

    @abstractclassmethod
    def m2(self):
        pass

# Interface: coz it contains only abstract methods:


class Test(ABC):
    @abstractclassmethod
    def m1(Self):
        pass

    @abstractclassmethod
    def m2(self):
        pass

# what is the purpose of interface ?:


from abc import *


class CollegeAutomation(ABC):
    @abstractclassmethod
    def m1(self):
        pass

    @abstractclassmethod
    def m2(self):
        pass

    @abstractclassmethod
    def m3(self):
        pass

# DurgaSOftImpl:


class DurgaSoftImpl(CollegeAutomation):
    def m1(self):
        print('m1 method implementation.')

    def m2(self):
        print('m2 method implementation.')

    def m3(self):
        print('m3 method implementation.')


d = DurgaSoftImpl()
d.m1()
d.m2()
d.m3()
'''

# -----------------------

# Interface vs Abstract class vs Concrete class:

# Interface is like a plan for a building to buil.
# Abstract Class (Partially implemented class) is like Partially Constructed building.
# Concrete Class (Fully implemented class) is like Fully Constructed Buiding.

'''
from abc import *


# Interface:
class CollegeAutomation(ABC):
    @abstractclassmethod
    def m1(self):
        pass

    @abstractclassmethod
    def m2(self):
        pass

    @abstractclassmethod
    def m3(self):
        pass

# Partially completed Class ==> Abstract Class


class AbsClass(CollegeAutomation):
    def m1(self):
        print('m1 method implementation.')

    def m2(self):
        print('m2 method implementation.')

# Fully Completed Class ==> Concrete Class:


class ConcreteClass(AbsClass):
    def m3(self):
        print('m3 method implementation.')

# can create Object only in Concrete Class not interface or Abstract class:

c = ConcreteClass()
c.m1()
c.m2()
c.m3()
'''
# ------------------------------------
# Public, Private, and Protected Members:

# if a member(either method or variable) is public, then  we can access that member from anywhere,
# either within the class or from outside the class

# by default every member present in python class is public. Hence we can access from anywhere either within,
# the class or from outside of the class.

# ex1:

'''
class Test():
    def __init__(self):
        self.x = 10

    def m1(self):
        print('Public Method.')

    # accessing members within the class:
    def m2(self):
        print(self.x)
        self.m1()


# accessing members within (from inside the class )the class
t = Test()
t.m2()

print('')
# accessing members outside of the class
print(t.x)
t.m1()
'''

# Private Members: means we can access only within the class not from outside the class:
# if a member is private then we can access that member only with in the class and from,
# outside of the class we cannot access.

# we can declare a member as private explicit by prefixing with two underscore symbols.

# x = 10 ==> public variable
# __x = 10 ==> private variable

'''
class Test:
    def __init__(self):
        self.__x = 10  # private variable

    def __m1(self):  # Private method cannot be called from outside the class
        print('Private Method.')

    def m2(self):  # Public Method can be called from outside the class.
        print(self.__x)
        self.__m1()

# calling from inside the class:


t = Test()
t.m2()

# calling Private variable and method ,from outside the class: we cannot and we will get:
# AttributeError: 'Test' object has no attribute '__x',
# AttributeError: 'Test' object has no attribute '__m1'

# print(t.__x)
# t.__m1()

print('')
# if we use Name Mangling then we can access Private Variable and Method from outside the class:
# __x ==> _Test__x

# Name Mangling and Accessing Private members from outside of the class:
# Name mangling will be happened for the private variables.
# Hence every private variable name will be changed to new name.

# __variableName == > _ClassName__VariableName
# Hence we can access private variable from outside of the class as follows:
# print(objectreference._classname__variablename):

print(t._Test__x)
t._Test__m1()
'''

# Protected Members:
# you can access protected members within the class, but outside of the class only within the child class:

# x = 10 public ==> variable
# __x = 10 private ==> variable
# -x = 10 protected ==>  variable

'''
class Test:
    def __init__(self):
        self._x = 10  # protected variable

    def m1(self):
        print(self._x)


class SubTest(Test):
    def m2(self):
        print(self._x)


# from within the class:
t = SubTest()
t.m1()
t.m2()
# outside of the class:
print('')
t = Test()
print(t._x)
t.m1()
'''

# Data hiding: outside persons cannot access directly like email authentication and the advantage is security:
# that outsider does not access our data:
'''
class Account:
    def __init__(self, initial_balance):
        self.balance = initial_balance

a = Account(1000)
print(a.balance)

# hiding the data: we put the balance variable as private == > __.balance
# and we cannot access the variable balance  coz it is private.

class Account:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

#a = Account(1000)
#print(a.__balance)
# AttributeError: 'Account' object has no attribute '__balance'

# we can access the balance data by using method:

class Account:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def getBalance(self):
        # validation, authentication
        return self.__balance

a = Account(1000)
print(a.getBalance())
'''

# Abstraction: partial information but not complete (hiding internal implementation):
# like the ATM bank (when taking money and we dont know what happening behind the scene when taking money):
# How to implement Abstraction:
# By using Gui (using Tkinter) Screens, API's we can implement abstraction.
# advandage of Abstraction:
# 1- security
# 2- Enhacement
# 3- Maintainability, modularity

# Encapsulation: it is binding mechanism or grouping mecanism of,
# data (example: variables),and correscponding behavor(methods) into a single unit,
# every python class is an example of encapsulation.
# like a medical caplsule grouping medecine inside
# Encapsulation = data hiding + abstraction

# class Student:
#   Data: Name, Rollno, Marks, age
#   Behavor: read(), write(), walk()

# ex:

'''
class Account:
    def __init__(self, initial_balance):
        # hiding data (buy using underscore __)
        self.__balance = initial_balance

    # Abstraction
    # get hiding data

    def getBalance(self):
        # validation | authentication
        return self.__balance

    def deposit(self, amount):
        # validation | authentication
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        # validation | authentication
        pass

# advantages of Encapsulation:
# Security
# Enhacement easy
# Maintainability
# Mobility
'''

# The Three Pillars of OOPs:
# 1- Inheritance : used for code reusability and extendability
# 2- Polymorphism (overloading, overriding...) : used for flexibility (if we want to use the same code)
# 3- Encapsulation (data hoding + abstraction(what happening behind the seenes like in the ATM banks when you want to take money for example)): used for security pupose.
