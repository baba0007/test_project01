#collection:
# List, Set, Tuple, Dict
# 1-List data structure:
'''
l = []
l.append(10)
l.append('Mustapha')
l.append(10)
print(l)
l[0] = 77
print(l)
'''
#creation of list object:
'''
l = input('Enter list: ') # will return string that is why we need to use eval to return list from input.
# return string
print(l)
print(type(l))
'''
#-----------------------------
# print('-'*40)
'''
l = eval(input('Enter list: ')) # will return list
print(l)
'''
#----------------------------
'''
# ex1:
l = list('Musta') #convert string to list
print(l)
#ex2:
l = list(range(0, 10, 2)) #convert range or tuple to list
print(l)
'''
#----------------------------
'''
s = 'Learning python is easy.'
print(list(s))
print(s.split()) # split also is used to convert string to list.
'''
#---------------------------------
# Accessing elements of a list:
# 1-by using index:
'''
l = [10, 20, 30, 40]
print(l[0])
print(l[-1])
'''
# 2-by using slice operator:
# list = [begin, end, step]
# if step is +ve => we move forward direction from begin to end-1
# if step is -ve => we move backward direction from begin to end+1

# l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(l[2:7]) # return [30,40,50,60,70]
# print(l[2:7:2]) # return [30,50,70]
# print(l[4::2]) # return [50,70,90]
# print(l[8:2:-2]) # return [90,70,50]
# print(l[4:100]) # return [50,60,70,80,90,100]
# print(l[4:0:2]) # will return emty list [] , coz end is 0 in forward direction.
# print(l[::1])
# print(l[::-1])
# ---------------------------------------------------
# traversing elements of the list:
# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1-by using while loop:
# i = 0
'''
while i < len(l):
    print(l[i])
    i += 1
print('-'*40)
# 2-by using for loop:
for x in l:
    print(x)
'''
#print only even number:
'''
print('Even Numbers are: ')
for x in l:
    if x % 2 == 0:
        print(x)
print('Odd Numbers are: ')
for x in l:
    if x % 2 != 0:
        print(x)
'''
#to print elements of list index wise:
'''
l = [10, 20, 30, 40, 50]
i = 0
while i < len(l):
    print('The element at +ve index {} and at -ve index {} is {}.'.format(i, i-len(l), l[i]))
    i += 1
print('-'*40)
i = 0
for x in l:
    print(f'{x} is at index {l.index(x)} and {i-len(l)}') # l.index(x)=+ve index , i-len(l)=-ve index
    i += 1
'''
#-----------------------------------------------------------
# Mathematical operators for list:
# 1-concatination operator (+) only lists can be continated:
'''
l1 = [10, 20, 30]
l2 = [40, 50, 60]
l3 = l1 + l2
l4 = l2 + [70]
print('l3 =', l3)
print('l4 =', l4)
'''
# 2-repetition operator (*) work only if list is * with integer:
'''
l1 = [10, 20]
l2 = l1 * 2
print(l2)
'''
#-------------
'''
l1 = [10, 20]
l2 = [30, 40]
l3 = l1 + l2
print('l3 =', l3)
l4 = l3 * 3
print('l4 =', l4)
'''
#---------------------------------------
# Equality operators for list object (== , !=):
'''
l1 = ['Dog', 'Cat', 'Rat']
l2 = ['Dog', 'Cat', 'Rat']
l3 = ['DOG', 'CAT', 'RAT']
l4 = ['Cat', 'Rat', 'Dog']

print(l1==l2)
print(l1==l3)
print(l1==l4)
print(l1!=l4)
'''
#Relationals (<, <=, >, >=):
'''
l1 = [10, 20, 30, 40]
l2 = [50, 60]
print(l1<l2) # 10<50 ==> True
print(l1<=l2) # 10<=50 ==> True
print(l1>l2) #  10>50 ==> False
print(l1>=l2) #  10>=50 ==> False

l3 = [10, 20, 30]
l4 = [10, 20, 6]
print(l3<l4) # 30<6 ==> False
print(l3<=l4) # 30<=6 ==> False
print(l3>l4) # 30>6 ==> True
print(l3>=l4) # 30>=6 ==> True

l5 = ['Ramba', 'Ramya']
l6 = ['Roja', 'Sunny']
print(l5<l6) # a<o => True
print(l5<=l6) # a<=o => True
print(l5>l6) # a>o => False
print(l5>=l6) # a>=o => False
'''
#Membership operator (in , not in):
'''
l1 = [10, 20, 30, 40]
print(10 in l1)
print(50 not in l1)
print(70 in l1)
'''
#-------------------------
'''
#important methods and functions for lists:
l=[10,20]
print(len(l)) #len is a function built in python
l.append(30) #append is a method and is applicable only for list.
print(l)
sorted(l) #sorted is a function built in python  
print('-'*40)
l2=[10,20,10,20,30,20,40]
#we will call count method which is only specific for list:
print(l2.count(10))
print(l2.count(20))
print(l2.count(50)) #will return 0
print('-'*40)
l3=[1,2,1,2,3,4]
print(l3.index(1)) #will return the first index of the first asked elements.
print(l3.index(2))
#print(l3.index(5))#will return error
print('-'*40)
l4=[1,2,2,2,3,3]
x=int(input('Enter number to find on the list: '))
if x in l4:
    print(f'{x} is at index {l4.index(x)}')
else:
    print(f'{x} is not available in the list.')
'''
#----------------------------------------
'''
l=[1,2,3,4]
print(len(l))
x=int(input('Enter number: '))
if x in l:
    print('{} is at index {}'.format(x, l.index(x)))
else:
    print(f'{x} does not exist.')
'''
#-----------------------------------------
#manipulating elements of a list:
#1- l.append() : append is a method: will add elements to the last position.
'''
l=[]
l.append(10)
l.append(20)
l.append(30)
print('l =',l)
print('-'*40)
#wap that add numbers from 1 to 100 divisable by 10 in a empty list:
l1=[]
for x in range(101):
    if x%10==0:
        l1.append(x)
print('l1 =',l1)
'''
print('-'*40)
#---------------------------
'''
#2-insert(): will add elements to a specific position. syntax: l.insert(index,elements)
l=[10,20,30,40]
l.insert(1,15)
print(l)
l.insert(100,99) #will add the elements to last position ecoz the index 100 is greater than maximum index 3
l.insert(-100,990) #will add elements the first position coz index -100 is less than minimum index -4
print(l)
'''
#--------------------------------
#3-extend(): to add all elements of given sequence to the list:
#syntax: l1.extend(l2) -> all elements of l2 will be added to l1.
'''
order1=['chiken', 'meat', 'apple']
order2=['kf', 'ko', 'rc']
order1.extend(order2)
print(order1)
print('-'*40)

l1=[10,20,30]
l2=[40,50]
l1.append(l2)
print('l1 =',l1)
print('lengte of l1 is :',len(l1))
l1.extend(l2)
print('l1 =',l1)
print('lengte of l1 is :',len(l1))
'''
print('-'*40)
#---------------------------
'''
l1=[10,20,30]
l1.append('ABC')
print(l1)
print('lengte of l1 is :',len(l1))

l1.extend('ABC')
print(l1)
print('lengte of l1 is :',len(l1))
'''
#------------------------------
#4-remove() method.
#-sytanx : l.remove(x)
'''
l=[10,20,10,20,40]
l.remove(40)
print(l)
l.remove(10) #will remove the first number 10 , incase of multiple same number the first one will be removed.
print(l)
#l.remove(50) #will return valueerror
#print(l)

l=[1,2,3,4,5,6]
print('berfore removel l = ', l)
x=int(input('Enter number to remove: '))

if x in l:
    l.remove(x)
    print('after removel l =', l)
else:
    print(f'{x} not available in the list.')

print('-'*40)
'''
#---------------------------------
#5-remove all occurrences:
'''
l=[1,1,1,1,2,2,2,3,3]
print(f'before remove l = {l}')
x=int(input('Enter number to remove: '))
while True:
    if x in l:
        l.remove(x)
    else:
        break
print(f'after remove l = {l}')
'''
#------------------------------
#6-pop(): syntax : l.pop()  to remove last elements.
'''
l=[10,20,30]
print(l.pop())
print(l)
print(l.pop())
print(l.pop())
print('l =',l) # will return empty list.
#if i use pop() again in a empty list then it will return Indexerror pop from empty list.
'''
#6-1 pop(index) : will remove element in a specified position.
'''
l=[10,20,30,40]
l.pop(1)
print('l =',l)
#index not present in the list: l.pop(100) will return Indexerror out of range.
'''
#7-clear() : to remove all elements in a list.
'''
l=[10,20,30,40]
l.clear() #will empty list
print('l =',l)
'''
#------------------------------------------
#Ordering elements of list: reversing , sorting:
#1-Reversing order of the list:
#syntax reverse method: l.reverse() only applicable for list.
'''
l=[10,20,30,40]
print('Before reverse l =',l)
l.reverse()
print('After reverse l =',l)
#2-reversed(): is a function inside python applicable for string, tuple, string 
l1=[10,20,30,40]
r=reversed(l1) #this r object need to be converted to list to get a return
#print(r) #will return <list_reverseiterator object at 0x7f8c364809d0>
print(list(r))

#incase of string or tuple or ...
s='hello'
print('Before reverse s =',s)
x=reversed(s)
print('After reverse s =',''.join(list(x))) #for string we need to convert to list and joining all to get a normal return.
#or
x=reversed(s)
for e in x:
    print(e,end='')
print('')
'''
#--------------------------------------------
#3-sorting elements of a list:
#3-1 sort() : syntax : l.sort() used only for list.
# for numbers it is Asceding order
# for strings it is alphabetical order
#ex1:
'''
l=[20,5,15,0,10]
print('l before sorting =',l)
l.sort()
print(f'l after sorting = {l}')

l1=['Banana', 'Cat', 'Apple']
print(f'l1 before sorting = {l1}')
l1.sort()
print(f'l1 after sorting = {l1}')
'''

#descending order: we can sort and then reverse but it is long so we use:
'''
l=[20,5,15,0,10]
print('Before reverse sorting l =',l)
l.sort(reverse=True)
print('Reverse sorted l =',l)
'''
#--------
'''
l=['Mango', 'Banana', 'Apple']
l.sort(reverse=False)
print('Normal sorting l =',l)
l.sort(reverse=True)
print('Descend sorting l =',l)
'''
#------------
'''
l=[40, 20, 'A', 'B']
#we cannot use sorting : l.sort() , coz elements are not same type , it should be same type elements.
#--------------
#3-2 sorted() : python built in function applicable for list tuple string ...and return always a list.
l1=[20,10,40,30]
l2=sorted(l1)
print('l1 =',l1)
print('l2 =',l2)

s='BCAD'
s2=sorted(s)
print('s2 =',s2)

tup=(3,2,1,4)
tup2=sorted(tup)
print('tup2 =',tup2)
'''
#-----------------------------------
#aliasing and cloning of list objects:
#aliasing is the process of duplicating the existing list and any change is made will affect both objects.
'''
l1=[10,20,30,40]
l2=l1
l1[1]=77
print('l1 =',l1)
print('l2 =',l2)
print(f'l1 id is : {id(l1)}')
print(f'l2 id is : {id(l2)}')
print(l1 is l2)
print('-'*40)
'''
#---------------------------------------------------
'''
#cloning : the change will affect only one object:
#1-using slice operator
l1=[10,20,30,40]
l2=l1[::] #new object will be created.
print(l1 is l2) # will return False coz != id.
print(id(l1))
print(id(l2))
l1[1]=77
print(l1)
print(l2)
print(id(l1))
print(id(l2))
#2-using copy() method , any change does not affect the new object.
l1=[10,20,30,40]
l2=l1.copy()
l1[1]=88
print(l1)
print(l2) #will not be affected by the change.
'''
#-------------------------------------------
#4-Nested lists: list inside another list:
'''
l=[10,20,[30,40]]
print(l[0])
print(l[1])
print(l[2])
print(l[2][0])
print(l[2][1])
'''
#--------------------------------------------
'''
#4-1 Nested list as Matrix:
l=[[10,20,30],[40,50,60],[70,80,90]]
print(l)
print('Elements as row wise: ')
for x in l:
    print(x)
print('Elements Matrix style: ')
for x in l:
    for y in x:
        print(y, end=' ') # we use end='' to not go to the next line.
    print() #to go to the next row to printed in new line.
'''
#-----------------------------------------------
#5-1 List Comprehension and Applications Part-1:
#creating a list normal way:
'''
l=[]
for x in range(1,11):
    l.append(x)
print('l =',l)
'''
#List Comprehension way:
#----------------------------------------------
'''
#creating list from 1 to 10:
l1 = [x for x in range(1,11)]
print('l1 =',l1)
#creating list of even numbers from a range of (0,21)
l2= [x for x in range(21) if x%2==0]
print('l2 =',l2)
#create a list of square values from a range 1 to 10:
l3 = [x**2 for x in range(1,11)]
print('l3 =',l3)
#create a list of 2 power x where x is in range(1,6)
l4 = [2**x for x in range(1,6)]
print('l4 =',l4)
#create a list from 1 to 100 which are dividebal by 10:
l5 = [x for x in range(1,101) if x%10==0]
print('l5 =',l5)
'''
#5-2 List Comprehension and Applications Part-2:
'''
#create a list with elements present in l1 but not in l2:
l1 = [10,20,30,40]
l2 = [30,40,50,60]
l3 = [x for x in l1 if x not in l2 ]
print('l3 =',l3)
#create list with elements present in both l1 and l2:
l4 = [x for x in l1 if x in l2]
print('l4 =',l4)

#create list where is the first Character of each string in list l5:
l5 = ['Balaica', 'Nag', 'Venki', 'Chiru']
l6 = [ word[0] for word in l5]
print('l6 =',l6)

#in this string all the alphabets are present.
#create Nested list with each list have number of words from words list.
s='the quick brown fox jumps over the lazy dog.'
words = s.split()
print('wordrs =',words)
l7 = [[word.upper(), len(word)] for word in words]
print('l7 =', l7)
'''
#-------------------------------------------------------------
#6-Program to find unique vowels present in the given word:
#1-ex:
vowels = ['a','e','i','o','u']
s = input('Enter string : ')
result = []
for ch in s:
    if ch in vowels:
        if ch not in result:
            result.append(ch)
print(f'The vowels present are {result} and the total of vowels is : {len(result)} ')
print('-'*40)
#2-ex
vowels = ['a','e','i','o','u']
s = input('Enter string : ')
result = []
for ch in vowels:
    if ch in s:
        result.append(ch)

print(f'The vowels present are {result} and the total of vowels is : {len(result)} ')
print('-'*40)
#3-list Comprehension:

vowels = ['a','e','i','o','u']
s = input('Enter string : ')
result = [ch for ch in vowels if ch in s]
print('Vowels present in the given string are {} and the total is {}.'.format(result, len(result)))



    




       


                