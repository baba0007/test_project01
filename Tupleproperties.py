#Tuple data structure: difference to lists is that:
#tuple are immutable we cannot change elements inside , in Lists we can that is why Lists are mutable.
#tuple use () it is optionel ,instead of [] for List:
'''
k = (10, 'durga', 20, 10)
t = 10, 'durga', 20, 10
print(k)
print(t)
print(t[0])
print(t[-1])
'''

'''
t1 = (10,20,30,40)
t1[0] = 77
print(t1) # we will get typerror coz tuple are immutable
'''
#------------------------------------
#tuple validity:
'''
t = (10,20,30) # it is a tuple
t1 = (20, 30) # it is a tuple
t2 = (10, ) # it is a tuple
t3 = (10) # it is not a tuple but an integer
print(type(t))
print(type(t1))
print(type(t2))
print(type(t3))
#-------------------------------
#all of this are tuple:
t4 = ( ) 
t5 = 10, 
t6 = 10,20,30
t7 = 10,20,30,
t8 = (10,20,30,)
print('-'*40)
print(type(t4))
print(type(t5))
print(type(t6))
print(type(t7))
print(type(t8))
'''
#--------------------------------
'''
#1-creation of tuple object:
#Empty tuple:
t = ( )
#2-single tuple:
t = (10, )
t = 10, 
#3-multi valued tuple:
t = (10, 20, 30)
t = 10,20,30,
t = (10,20,30,)
t = 10,20,30

#4-by using tuple() function:
t = tuple('anysequence')
#ex1:
l = [10,20,30]
t = tuple(l)
print(t)
print('-'*40)

t = tuple(range(1,11,2))
print(t)
print('-'*40)

t = tuple('Mustapha')
print(t)
print('-'*40)
#5-With Dynamic input :
t = eval(input('Enter tuple values: ')) #eval is used for list and tuples.
print(t)
print(type(t))
'''
#-------------------------------------------------
'''
#Accessing elements of Tuple:
#1-by using index:

t = [10,20,30,40,50,60]
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[-1])

#2-by using slice operator:
t = (10,20,30,40,50,60,70)
print(t[2:5])
print(t[::2])
'''
#-------------------------------------------------
#Mathematical operators for tuple:
'''
#1-Concatenation operator (+):
t1 = (10,20,30)
t2 = (40,50,60)
t3 = t1 + t2
print('t3 =',t3)
#t3 + 10 #will get error coz both should be tuple 

#2-Repetition operator (*):

t1 = (10,20,30)
t2 = (40,50,60)
t4 = t1 * 3 # repetition should be always between tuple and int number if not it will be returning error.
print('t4 =',t4)

t1 = (10,20)
t2 = (30,40)
t5 = t1 + t2
t6 = t3 * 3

print('t5 =',t5)
print('t6 =',t6)
'''
#------------------------------------------------------
'''
#equality operator for tuple ( == , != )
t1 = ('cat', 'Rat', 'Dog')
t2 = ('cat', 'Rat', 'Dog')
t3 = ('CAT', 'RAT', 'DOG')
t4 = ('Rat', 'Cat', 'Dog')

print(t1==t2)
print(t1==t3)
print(t1==t4)
print('-'*80)
#Relationel operator for tuple (<, >, <=, >=):
t1 = (10, 20, 30)
t2 = (30, 15, 40)
print(t1<t2)
print(t1>t2)
print('-'*40)

t1 = (10, 20, 30)
t2 = (10, 5, 70)
print(t1<t2)
print(t1>t2)
print('-'*40)

t1 = (10, 20, 30)
t2 = (10, 20, 30, 40, 50)
print(t1<t2)
print(t1>t2)
print('-'*40)
#Membership operators (in, not in):
t = (10, 20, 30)
print(10 in t)
print(50 not in t)
print(60 in t)
'''
#-------------------------------------
# Important methods / Functions for Tuple:
'''
# 1- len() function:
t =  (10, 20, 30, 40)
print('lenght of t is: ', len(t))

#2- count() method:
t = (1, 1, 2, 2, 2, 3, 3)
print(f'Number 1 is {t.count(1)} times in this tuple.')
print(f'Number 2 is {t.count(2)} times in this tuple.')
print(f'Number 3 is {t.count(3)} times in this tuple.')
print(f'Number 7 is {t.count(7)} times in the tuple.')
print('-'*40)
#3- index() method: return the first element index but not all incase of double or triple.
t = (1, 10, 20, 30, 10)
# print('Number 10 is at index: ', t.index(10))

i = 0
for x in t:
    print(f'{x} is at index {t.index(x)} and {i-len(t)}')
    i += 1
'''
#----------------------------------------
'''
# Reversing and sorting elements of tuple:
# 1-reversing:
# reverse() method not available for tuple coz tuple are immutable
t = (10, 20, 30, 40)
r = reversed(t)
t1 = tuple(r)
print('t =', t)
print('t1 =', t1)
print('-'*40)
#2-sorting acending order:
# sort() method not available for tuple:
t = (20, 5, 10, 15, 0)
l = sorted(t)
t1 = tuple(l)
print('t =', t)
print('t1 =', t1)
print('-'*40)
#desceding order :
t = (20, 5, 10, 15, 0)
l = sorted(t, reverse=True)
t2 = tuple(l)
print('t2 =', t2)
print('-'*40)
#max() and min() functions for tuple:
t = (20, 10, 0, 5, 15)
print(f'Maximum value of t is {max(t)}.')
print(f'Minimum value of t is {min(t)}.')
'''
#-------------------------------------------------
'''
# Tuple packing and unpacking:
# 1-packing:
a = 10
b = 20
c = 30
d = 40
t = (a, b, c, d)
print(type(t))
print('t =', t)
l = [a, b, c, d]
print(type(l))
print('l =', l)

#2-unpacking:
a, b, c, d = t
print(a, b, c, d)
# print('a =',str(a) +'\n', 'b =',str(b) +'\n', 'c =',c)

# a, b, c = t
# print(a, b, c) # will get error: too many values to unpack (expected 3), that why number of value should be same as variables.
# a, b, c, d, e = t
# print(a, b, c, d, e) will return error : ValueError: not enough values to unpack (expected 5, got 4)

a, *b = t
print(f'a = {a}, b = {b}')
'''
#--------------------------------------
'''
# Tuple comprehension:
t = (x * x for x in range(1, 6))
print('t =', t) # will return generator object but not tuple object. that's why comprehension is applicable only for list.
'''
#----------------------------------
'''
# difference between list and tuple:
l = [10, 20, 30, 40] # list required more memory to store data
t = (10, 20, 30, 40) # tuple required less memory to store data
# list we can access elements not speedy ==> performence low
# tuple we can access elements very easylly ==> performance high
# in a set order is not applicable and no duplicate elements are allowed.
s = {10, 20, 30, 70, 80}
s.add(55)
print(s)
#in set the objects are stored using hash code.
# linear search algorithm
# binary search algorithm
# hashing search algorithm whis is the best and quick for searching.
# list is not hashable ==> you cannot add list to the set and to dictionary.
# tuple is hashable ==> you add tuple element to the set and dictionary.

# to chack if the list and tuple are hashable or not we use the isinstance() function in the collections module:
l = [10, 20, 30]
t = (10, 20, 30)
import collections
print(isinstance(l, collections.Hashable)) # False
print(isinstance(t, collections.Hashable)) # True

# to find the hash code of the tuple:
print('t hash code is: ', hash(t))
#----------------
s = {10, 20}
l = [10, 20, 30]
t = (10, 20, 30)
# adding tuple to the set:
s.add(t)
print('s =', s)
#we cannot add list to set coz list is not hashable:
# s.add(l)
# print(s) # will return error: builtins.TypeError: unhashable type: 'list'

# adding list and tuple to dictionary:
# list will not be added coz not hashable
# tuple will be added coz it is hashable:

dict = {}
l = [10, 20, 30]
t = (10, 20, 30)
dict[t] = 'A'
print('dict =', dict)
# dict[l] = 'B'
# print(dict) # will return error : builtins.TypeError: unhashable type: 'list'
'''
#---------------------------------------
# wap to take a tuple of numbers from the keyboard and print its sum and average:
t = eval(input('Enter tuple of numbers: '))
print(f'sum = {sum(t)}')
print(f'Average = {sum(t)/len(t)}')
print('-'*40)
#or
sum = 0
for x in t:
    sum = sum + x
print(f'sum = {sum}')
print(f'Average = {sum/len(t)}')





 





