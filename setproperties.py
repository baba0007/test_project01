# set Data structure:
# 1-Duplicatae are not allowed
# 2-Order is not applicable
# 3-indexing and slicing are not applicable
# 4- set={10,20,30}, list=[10,20,30], tuple = (10,20,30), dict = {'musta':52, 'simo':39, 'khad':47}
# 5-Heterogeneous objects are allowed
# 6-it is mutable
# 7-union, intersection, difference.
'''
s = {} # empty is for dict but not for the set
print(type(s))

# to create empty set:
s = set()
s.add(10)
s.add('Z')
s.add('A')
s.add(20)
s.add(20)
print('s =', s)
# print(s[0]) # will return error set object not supporting indexing
# print(s[1:3]) # will return error set object is not subscriptable
'''
#--------------------
'''
# creation of set object:
# 1-empty set:
s = {} # by default empty set is dictionary
s = set()
# by using set() function
l = [10, 20, 30, 40] # list
s = set(l)
print('s =', s)

s = set(range(0, 101, 10))
print('s =', s)


s = set('apple')
print('s =', s) # no dubble elements in set and no order.

# s = set(input('Enter set values: '))
# or
s = eval(input('Enter set values: ')) # example of input {1,2,3,4}
print('s =', s)
print(type(s))
'''
#----------------------------------
# Mathematical operators for set:
# s1 = {10, 20, 30}
# s2 = {30, 40, 50}
# s3 = s1 + s2
# s4 = s1 * s2
# print('s3 =', s3) # will return unsupported operand type(s) for +: 'set' and 'set'
# print('s4 =', s4) # will return unsupported operand type(s) for *: 'set' and 'set'
# + and * operators are not applicable for the set.
''''
s1 = {10, 20, 30}
s2 = {30, 10, 20}
print(s1 == s2)
print(s1 != s2)
'''
#----------------------
# Relationel operators for set: will return always False
'''
s1 = {10, 20, 30}
s2 = {20, 10, 5, 6, 7}
print(s1 > s2)
print(s1 < s2)
print(s1 >= s2)
print(s1 <= s2)
'''
# membership operators in not in:
'''
s = {10, 20, 30, 40}
print(10 in s)
print(50 in s)
print(50 not in s)
'''
#---------------------------------
# important methods and functions for set:
# len(), add(), and update()
# 1-len(): return number of elements present in the set:
'''
s = {10, 20, 30, 40}
print('lenght of s =', len(s))

# 2-add(): is like append() in the list and add() method take only one argument:
s = {10, 20, 30, 40}
s.add(50)
# s.add(60, 70, 80) # will return : builtins.TypeError: set.add() takes exactly one argument (3 given)
print(f's = {s}')

# update() is used to add multiple items in the set:
# items should be iterable like set, tuple, string
# ex: s.update(s1)
# ex: s.update(s1, s2, s3) #you can add as much as you want , it should be not individuel

s = {10, 20}
l = [30, 40]
s.update(l)
# s.update(10) # return error ('int' object is not iterable) coz 10 is not iterable item , should be list ot tuple or string or any iterable item
print('s =', s)
s.update(range(1, 6), 'bamco')
print('s =', s)
'''
# ---------------------------------
'''
# removing elements from set:
# 1-remove():
s = {10, 20, 30, 40}
s.remove(30)
print(f's = {s}')
# 2- s.remove(50) # will return KeyError : means that if remove does not find the element to remove it will return error
# discard(): if you find the element remove it if you dont find dont do nothing just discard:
s = {10, 20, 30, 40}
s.discard(30)
print(f's = {s}')
s.discard(50)  # 50 is not present and it will discard any error
print(f's = {s}')
# 3-pop(): will remove some random elemnts:
s = {10, 20, 30, 40}
s.pop()
s.pop()
print(f's = {s}')

# if the set is empty then after using pop() it will return KeyError from an empty set.
# 4-clear(): will empty all the set:
s = {10, 20, 30, 40}
print(f's = {s}')
s.clear()
print(f's = {s}')
'''
# ---------------------------------
'''
# set specific methods for mathematical operations:
# 1-union():
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}
s3 = s1.union(s2)
# or
# s3 = s1 | s2
print(f's3 = {s3}')

# 2-intersection(): return common elements between s1 and s2(use intersection() or &)
# print('s3 = {}'.format(s1.intersection(s2)))
# or
print('s3 = {}'.format(s1 & s2))

# 3-difference(): return elements present in s1 but not in s2
print('s3 = {}'.format(s1.difference(s2)))
# or
# print('s3 = {}'.format(s1 - s2))

# 4-symmetric-difference(): elements present in s1 but not in s2 and vise versa:
print('s3 = {}'.format(s1.symmetric_difference(s2)))
# or
# print('s3 = {}'.format(s1 ^ s2))
'''
# -----------------------------------
'''
# Aliasing and cloning and comprehension of set:
# 1-Aliasing: any changes in s1 or s2 will affect both
s1 = {10, 20, 30}
s2 = s1  # aliasing
s1.pop()
print(f's1 = {s1}')
print(f's2 = {s2}')

# 2-cloning: copy() --> will create a new independent object not affected by any changes of s1:
s1 = {10, 20, 30}
s3 = s1.copy()  # cloning
s1.pop()
print(f's1 = {s1}')
print(f's3 = {s3}')

# 3-set comprehension:
s = {x**2 for x in range(1, 6)}
print(f's = {s}')

s = {2**x for x in range(1, 6)}
print(f's = {s}')
'''
# -----------------------------------
# wap to eliminate duplicates present in the list:
# 1-ex:
'''
l = [10, 10, 20, 30, 10, 20, 30]
s = set(l)
print(f's = {s}')
l1 = list(s)
print(f'l1 = {l1}')

# 2-ex:
l = [10, 10, 20, 30, 10, 20, 30]
l1 = []
for x in l:
    if x not in l1:
        l1.append(x)
print(f'l1 = {l1}')
'''
# --------------------------------
# wap to print different vowels present in the given word:

word = input('Enter a word: ')
s = set(word)
v = {'a', 'e', 'i', 'o', 'u'}
for x in s:
    if x in v:
        print(f'Vowels present in this word are : {sorted(x)}')

# or
result = s.intersection(v)  # or result = s & v
print(f'Vowels present in this word are : {result}')
# to sort the letters:
print(f'Sorted vowels present in this word are : {sorted(result)}')
