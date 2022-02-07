#import webbrowser
#webbrowser.open(input('Enter url: '))
'''
s='ABCDEBFGHIJK'
print(s.find('x')) # will return -1 if letter not found.
print(s.find('B',1,9))
print(s.rfind('B'))
# print(s.index('z')) #will return error substring not found.
print(s.index('B'))
print(s.index('B', 3, 8))

print(s.rindex('B'))

print('-'*40)
mail = input('Enter mail address: ')
try:
    i = mail.index('@')
    print('This {} address contain @ symbol.'.format(mail))
except ValueError:
    print(f'This {mail} address do not have @ symbol.')
    

'''
#-----------------------------------------------------------------------------------------
# count() method:
'''
print('-'*40)

s2 = input('Enter string: ').upper()
l=input('Enter letter to seach: ').upper()
if l in s2:
    print(f'There is {s2.count(l)} letter {l} in {s2}.')
else:
    print(f'There is no letter {l} in {s2}.')
    
print('-'*40)    
    
s ='ABBABBABA'
print(s.count('A', 3, 100))
print('There is,', s.count('B'), 'B letters in s.')
print('There is,', s.count('BB'), 'BB couple letters in s.')

x = input('Enter letter to search: ').upper()
if x in s:
    print(f'There is {s.count(x)} letter {x} in {s}')
else:
    print(f'There is no letter {x} in {s}')

'''
#-----------------------------------------------------------
'''
s = 'BBBBB'
print(s.count('B'))
print(s.count('BB'))
print(s.count('BBB'))
'''
#-------------------------------------------------------------
'''
# how many ABC letters are in the string:
s = 'ABCABCABCA'
print(s.count('ABC'))

#to find index of all occurences:
i = s.find('ABC')
print(f'The First ABC is at index: {i}')
i=s.find('ABC', 3, 10) # will search from 3rd index to n-1 =10-1=9 and will return the 1st ABC in this segment.
print(f'The Second ABC is at index: {i}')
i = s.find('ABC', 6, 10)
print(f'The Third ABC is at index: {i}')
i = s.find('ABC', 9, 10)
print(f'The Last ABC is at index: {i}') # will return -1 coz there is no ABC from index 9 to 10.
print('Numbers of ABC available in s string is: ', s.count('ABC'))
'''
#---------------------------------------------------------
'''
s = 'ABCABCABCA'
subs = 'ABC'
i = s.find(subs)
if i == -1:
    print(f'substring {subs} not found.')
while i != -1:
    print('{} is at index {}'.format(subs, i))
    i = s.find(subs,i+len(subs),len(s)) #i+len(subs) =3 , len(s)=10 (all this mean to search ABC from 3 till end od the string)
'''
# ------------------------------------------------------------------
'''
print('-'*40)
s = input('Enter string: ')
subs = input('Enter letters to search: ')
i = s.find(subs)
if i == -1:
    print(f'substring {subs} not found.')
while i != -1:
    print('{} is at index {}.'.format(subs, i))
    i = s.find(subs,i+len(subs),len(s))
print(f'There is {s.count(subs)} times {subs} in the given string.')
'''
#or
'''
print('-'*40)
s = input('Enter string: ')
subs = input('Enter letters to search: ')
i = s.find(subs)
if i == -1:
    print(f'substring {subs} not found.')
count = 0
while i != -1:
    count += 1
    print('{} is at index {}.'.format(subs, i))
    i = s.find(subs,i+len(subs),len(s))
print(f'There is {count} times {subs} in the given string.')
'''
print('-'*40)
#Replacing string with another string: syntax: s.replace(oldstring, newstring):
# Replace very A with B in following string:
'''
s = 'ABABABA'
s1 = s.replace('A', 'B')
print(s1)
s2 = s.replace('AB', 'DC')
print(s2)
'''
#-------------------------------------------------------------
'''
print('-'*40)
s = input('Enter string: ')
s1 = s.replace(' ', ', ')
print(s1)
s2 = s.replace(' ', '')
print(s2)
#count number of spaces:
s3 = s.count(' ')
print(f'The number of spaces in the given string is {s3}.')
#or:
print(f'The number of spaces in the given string is {len(s)-len(s2)}.')
'''
#-----------------------------------------------------------------------
'''
print('-'*40)
s = 'Learning Python Is Very Difficult.'
s1 = s.replace('Difficult', 'Easy')
print(s1)

s1 = s.replace('difficult', 'Easy') # will not replace coz case sensetive.
print(s1)
'''
#------------------------------------
'''
print('-'*40)
#strings are immutable but with replace method a new object will be created:
s = 'ABABABA'
s1 = s.replace('AB', 'DC')
print(s)
print(s1)

#---------------------
print('-'*40)
s = 'ABABABA'
print(f'Before replacement s(id) is {id(s)}.')
s = s.replace('AB', 'DC')
print(f'After replacement s(id) is {id(s)}.')
print(s)
'''
#--------------------------------------
'''
# spliting of strings:will return list as result:
s = 'Durga solutions software'
l = s.split()
print(l)
#if you do not want list as result then:
for x in l:
    print(x)

#--------------------------------------
print('-'*40)
d = '01-02-1968'
l = d.split('-')
print(l)
for x in l:
    print(x)

#--------------------------------------
print('-'*40)
#joining of strings: is the opposite of string spliting:

l = ['Durga', 'Software', 'Solutions']
# joining with space operator:
s = ' '.join(l)
print(s)
#joining with , operator:
s = ', '.join(l)
print(s)
#joining with - operator:
s = '-'.join(l)
print(s)
#joining with : operator:
s = ':'.join(l)
print(s)

#-----------------------------------------
print('-'*40)
l = ['01', '02', '1968']
s = '-'.join(l)
print(s)
print('-'*40)
l = ['01', '02', '1968']
s = '/'.join(l)
print(s)
'''
#----------------------------------------------
# changing case of characters of the string:
# 1-upper()
# 2-lower()
# 3-swapcase() = if upper case then change to lowwrcase and vise versa.
# 4-title() = capitalize the first letters of a given string and all remaining words stay lower.
# 5-capitalize()
'''
s = 'Learning Python is very easy.'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())
print('-'*40)
#write a program to check wether the 2 given strings are equal or not by ignoring case.
s1 = input('Enter first string: ') # or try s1 = input('Enter first string: ').title() or .capitalize() etc...
s2 = input('Enter second string: ')
if s1 == s2:
    print('Both s1 and s2 are equal.')
else:
    print('Bothe s1 and s2 are not equal.')
'''
#-----------------------------------------------------------------------------
'''
print('-'*40)
s1 = input('Enter first string: ') # or try s1 = input('Enter first string: ').title() or .capitalize() etc...
s2 = input('Enter second string: ')
if s1.lower() == s2.lower():
    print('Both s1 and s2 are equal.')
else:
    print('Bothe s1 and s2 are not equal.')

#or

s1 = input('Enter first string: ').lower()
s2 = input('Enter second string: ').lower()
if s1 == s2:
    print('Both s1 and s2 are equal.')
else:
    print('Bothe s1 and s2 are not equal.')
'''
#-----------------------------------------------------
# Q-2:write a program to check whether provided username and password are valid or not ?
# username is not case sensitive, but password should be case sensitive.
'''
u = input('Enter Username: ')
p = input('Enter password: ')
if u.lower() == 'baba007' and p == '@Labi8621':
    print('Welcome to The Servers, your login are corrects.')
else:
    print('Please check your logins.!!!')
'''
#Q-3:write a program to convert first and last characters as upper case and remaining characters should be lower case of
# the given string:
'''
s = 'mustapha'
print(s[0].capitalize() + s[1:7] + s[7].capitalize())
#or
print('-'*40)
s = input('Enter string: ')
print(s[0].capitalize() + s[1:len(s)-1].lower() + s[-1].capitalize())
print('-'*40)
'''
#checking starting and ending part of the string:
# 1- s.startswith(substring)
# 2- s.endswith(substring)
'''
s = 'Learning Python is very easy'
print(s.startswith('Learning'))
print(s.startswith('Lea'))
print(s.startswith('lea'))
print(s.endswith('easy'))
print(s.endswith('Easy'))
'''
#-------------------------------
print('-'*40)
#-----------------------------
# checking types of characters present in the given string:

#1- is the string contain only alphanumeric:[a-z, A-Z, 0-9] (s.alnum())---> will return true or false
#2- is the string contain only alphabet ?: (s.isalpha())
#3- is only lowercase ? : s.islower() --> will return True or false
#4- is only uppercase ?: s.isupper()
#5- is the string contain only digit ?: s.isdigit()
#6- is only in title case (is every first character in a word is in upper case in the string)?: s.istitle()
#7- is only space in the string ?: s.isspace()
'''
print('Durga786'.isalnum())
print('Durga786'.isalpha())
print('Durga'.isdigit())
print('786786'.isdigit())
print('abc'.islower())
print('Abc'.islower())
print('abc786'.islower())
print('ABC'.isupper())
print('Durga Software Solutions'.istitle())
print('Durga software solutions'.istitle())
print('   '.isspace())
'''
#----------------------------------------------
'''
print('-'*40)
s = input('Enter String: ')
print(s.title())
print(s.isalpha())
print(s.isalnum())
print(s.istitle())
print(s.isupper())
print(s.islower())
print(s.isdigit())
print(s.isspace())
'''
# print('-'*40)
#------------------------------------------------
'''
s = input('Enter string: ')
if s.isalnum():
    print('It is alphanumeric character.')
    if s.isalpha():
        print('It is alphabet Character.')
        if s.islower():
            print('It is lower case')
        else:
            print('It is upper case.')
    else:
        print('It is digit.')
elif s.isspace():
    print('It is only space Character.')
else:
    print('It is non space special Character.')
    
'''
#--------------------------------------------------------
# string coding interview questions:
# wap=write a program to reverse a given string:
# 1- slice operator:
# by default slice step is 1
# slice step 1 or 2 or etc the string is forward direction
# slice step -1 0r -2 or etc the string is in backward direction sort of reversed.
'''
s = 'Mustapha'
print(s[:])
print(s[::1])
print(s[::-1])
print('-'*40)
s = input('Enter string: ')
print(s[::-1])
'''
#--------------------------------------------------
'''
s = input('Enter Anything: ')
r = reversed(s)
# print(type(r)) # to print the data inside the r object:
# for x in r:
#    print(x, end='')
print('')
#or
output = ''.join(r)
print(output)
'''
#----------------------------------------------------
'''
s = input('Enter anything: ')
print(s[::-1])
output = reversed(s)
r=''.join(output)
print(r)
'''
#-----------------------------------------------------
# print('-'*40)
#write a program to reverse content of the given string by using while loop:
'''
s = input('Enter string: ')
output = ''
i = len(s) - 1
while i >= 0:
    output = output + s[i]
    i = i - 1
print(output)
'''
#----------------------------------------------------------
#write a program to reverse order of the given string :
'''
s = input('Enter string: ').title()
l = s.split()
print(l)
l1 = l[::-1]
print(l1)
output = ' '.join(l1)
print(output)
'''
#OR------------------------------------------------
'''
s = input('Enter string: ').title()
l = s.split()
print(l)
output = reversed(l)
r = ' '.join(output)
print(r)
'''
#-------------------------------------------------
'''
# write a program to reverse the internal content of each word:
s = input('Enter anyting: ')
l = s.split()
print(l)
l1 = []
for word in l:
    l1.append(word[::-1])
print(l1)
output = ' '.join(l1)
print(output)
'''
#----------------------------------------------------

# write a program to reverse internal content of every second word on a given string:
# s = 'one two three four five six'
'''
s = input('Enter anything: ')
l = s.split()
print(l)
l1 = []
i = 0 # i is index
while i < len(l):
    if i % 2 == 0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i += 1
output = ' '.join(l1)
print(output)
'''
#---------------------------------------------------------------
# write a program to print the characters present at even index and odd index seperately for the given string:
# s = input('Enter string: ')
# print(f'Characters at even index is: {s[0::2]}') #or s[::2]
# print(f'Characters at odd index is: {s[1::2]}')

#or
'''
s = input('Enter string: ')
i = 0 # start from 0
print('Characters at even index: ')
while i < len(s):
    print(s[i], end=' ')
    i += 2

print()

i = 1 # start from 1
print('Characters at odd index: ')
while i < len(s):
    print(s[i], end=' ')
    i += 2
print()
'''
#--------------------------------------------
# same lengt
# write a program to merge characters of 2 strings into a single string by taking characters alternatively:
# s1 = 'musta' # must be same lengt s1 and s2
# s2 = 'babaa'
'''
s1 = input('Enter s1: ')
s2 = input('Enter s2: ')
output = ''
i, j = 0, 0 # i is to track index of s1 and j to track index of s2
while i < len(s1) or j < len(s2):
    output = output + s1[i] + s2[j]
    i += 1 # increment i with 1
    j += 1 # increment j with 1
print(output)
'''
#not same lengt:
'''
s1 = input('Enter s1: ')
s2 = input('Enter s2: ')
i, j = 0, 0
output = ''
while i < len(s1) or j < len(s2):
    if i < len(s1):
        output = output + s1[i]
        i += 1
    if j < len(s2):
        output = output + s2[j]
        j += 1
print(output)
'''
#------------------------------------------------------
'''
# write a program to sort characters of the string, first alphabet symbols, followed by digits:
s = 'A1C2B68FD'
#s = input('Enter some alphanumeric string: ')
# print(sorted(s)) #will return digit first then alphabet
# print(''.join(sorted(s)))
alphabets = []
digits = []
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)

    else:
        digits.append(ch)
# print(''.join(alphabets))
# print(''.join(digits))
output = ''.join(sorted(alphabets) + sorted(digits)) # sorted function return always list.
# output = sorted(alphabets) + sorted(digits)
print(output)
'''
#-------------------------------------------------------------------------
'''
# write a program for the following requirement:
# input = a4b3c2
# output = aaaabbbcc
s = input('string where alphabet should be followed by digit: ')
output = ''
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output = output + x * d
print(output)

'''    
#-------------------------------------------------------------------------
'''
# write a program with the following requirement:
# input = a3z2b4
# output = aaabbbbzz(sorted string)

s = input('Enter string alphanumeric: ')
output = ''
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output = output + x * d
# print(output)
# print(sorted(output))
print(''.join(sorted(output)))
'''
#-----------------------------------------------------------------------------
'''
# write a program for the following requirement:
# input = aaaabbbccz
# output = 4a3b2c1z

# s = 'aaaabbbccz'
s = input('Enter string: ')
output = ''
previous = s[0]
c = 1
i = 1
while i < len(s):
    if s[i] == previous:
        c = c + 1
    else:
        output = output + str(c) + previous
        previous = s[i]
        c = 1
    if i == len(s) - 1:
        output = output + str(c) + previous
    i = i + 1
print(output)
'''
#---------------------------------------------------
# to print the alphabet order:
'''
for x in range(97, 123):
    print(chr(x), end=' ')
   
#to know an alphabet number:
print(ord('a'))
'''
#-------------------------------------------------
'''
# write a program for the following requirement:

# input: a4k3b2
# output: aeknbd

#function needed:
# ord() : to find unicode value for the given character: eg: print(ord('a'))  # 97, print(ord('A')) #65
# chr() : to find corresponding character for the given unicode value eg: print(chr(97)) # a

# s = 'a4k3b2'
s = input('Enter alphabet followed by digit string: ')
output = ''
for ch in s:
    if ch.isalpha():
        x = ch
        output = output + ch
    else:
        d = int(ch)
        newc = chr(ord(x) + d)
        # print(newc)
        output = output + newc
print(output)
'''
#----------------------------------------------------------------------------
# wap to remove dubplicate character from the given input string:
# input = AZZZBCDABBBBCCCCDDDDEEEEEF
# 1st way:
'''
# s = 'AZZZBCDABBBBCCCCDDDDEEEEEF'
s = input('Enter string: ').lower() # incase if the string has an uppercase alphabet we use lower() or upper() function
output = ''
for ch in s:
    if ch not in output:
        output = output + ch
print(output)

#2nd way:
# s = 'AZZZBCDABBBBCCCCDDDDEEEEEF'
s = input('Enter string: ').lower()
l = []
for ch in s:
    if ch not in l:
        l.append(ch)
print(''.join(l))

#3rd way: using set function but as set are without order
s = 'AZZZBCDABBBBCCCCDDDDEEEEEF'
s1 = set(s)
print(s1)
print(''.join(s1))
'''
#------------------------------------------------------------------------
# wap to find the number of each character present in the given string:
# by using count() method and list:
# s = 'ABCDXXXBBDDCCEEFFGGHHKLM'
# 1st way:
'''
s = input('Enter string: ')
l = []
for ch in s:
    if ch not in l:
        l.append(ch)
print(''.join(sorted(l)))
for ch in sorted(l):

    print(f'{ch} occurs {s.count(ch)} times.')
print('-'*40)
#2nd way:
s = 'ABCDXXXBBDDCCEEFFGGHHKLM'
# s = input('Enter string: ')
s1 = set(s)
print(s1)
for ch in sorted(s1):
    print('{} occurs {} times.'.format(ch, s.count(ch)))
'''
#------------------------------------------------------------------
# conclusion about dictionary :
'''
d = {}
d['A'] = 100
d['B'] = 200
print(d)
d['A'] = 300
print(d)
print(d['A'])
print(d.get('A'))
print(d.get('Z'))
print('-'*40)
#if the value is not then return 0 but dont return None.
print(d.get('A', 0))
print(d.get('Z', 0))
'''
#--------------------------------------------------------------------
'''
d = {}
d['A'] = 1
d['B'] = 2
d['A'] = d.get('A', 0) + 1
print(d) #will return {'A':2, 'B':2} 
'''
#---------------------------------------------------------------------
'''
d = {'A': 100, 'Z': 200, 'B': 300}
print(d.items())
for k, v in sorted(d.items()):
    print(f'key {k} has value: {v}')
for k in sorted(d.keys()):
    print(k)
for v in d.values():
    print(v)
'''
#---------------------------------------------------
'''
s = 'AADDCCCBBBBBBXXXXZZZ'
d = {}
for ch in s:
    d[ch] = d.get(ch, 0) + 1
print(d)
for k, v in sorted(d.items()):
    print(f'{k} occurs {v} times')
'''
#--------------------------------------------------
# wap for the following:
# input = 'ABAABBCA'
# output = 4A3B1C
'''
s = 'ABAABBCA'
d = {}
output = ''
for ch in s:
    d[ch] = d.get(ch, 0) + 1
    
for k, v in sorted(d.items()):
    print(f'{k} occurs {v} times.')
    output = output + str(v) + k
print('-'*40)
print(output)
'''
#---------------------------------------------------------
'''
s = input('Enter string: ')
d = {}
for ch in s:
    d[ch] = d.get(ch, 0) + 1
print(d)
for k, v in d.items():
    print(f'{k} occurs {v} times.')
output = ''
for k, v in sorted(d.items()):
    output = output + str(v) + k
print(output)
'''
#-------------------------------------------------------
# wap for the followed requirement:
# input='ABAABBCA'
# output=A4B3C1

# s = 'ABAABBCA'
'''
s = input('Enter string: ')
d = {}
output = ''
for ch in s:
    d[ch] = d.get(ch, 0) + 1
print(d.items())
for k, v in sorted(d.items()):
    output = output + k + str(v)
print(output)
'''
#------------------------------------------------------
# wap to find number of occurences of each vowel present in a given string:
'''
s = input('Enter string to search for vowel: ')
v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
d = {}
for ch in s:
    if ch in v:
        d[ch] = d.get(ch, 0) + 1
print(d)
for k, v in sorted(d.items()):
    print(f'{k} is a vowel and occurs {v} times.')
'''
#optionel:
# output = ''
# for k, v in sorted(d.items()):
#    output = output + k + str(v)
# print(output)
# ---------------------------------------------------------
# wap to check whether the 2 given strings are anagrams or not:
# anagrams mean same content no problem the characters positions:
# s1 = 'listen'
# s2 = 'silent'
'''
s1 = input('Enter string one: ')
s2 = input('Enter string s2: ')

if sorted(s1) == sorted(s2):
    print('Strings s1 and s2 are anagrams.')
else:
    print('Strings s1 and s2 are not anagrams.')
'''
#----------------------------------------------------------------
# wap to check whether the given string is palindrome or not ?
# means if original string and its reversed string are equal:
# s = 'level'
# print(s[::-1])
# s = 'eye'
# print(s[::-1])
'''
s = input('Enter string: ')
if s == s[::-1]:
    print('String is palindrome.')
else:
    print('String is not palindrome.')
    
'''
#----------------------------------------------------------
# wap to generate words from the given input strings by taking characters alternatively:
# inputs:
# s1 = 'abcdefg'
# s2 = 'xyz'
# s3 = '12345'
# output: ax1, by2, cz3, d4, e5, f, g
'''
s1 = 'abcdefg'
s2 = 'xyz'
s3 = '12345'
i = j = k = 0
while i < len(s1) or j < len(s2) or k < len(s3):
    output = ''
    if i < len(s1):
        output = output + s1[i]
        i += 1
    if j < len(s2):
        output = output + s2[j]
        j += 1
    if k < len(s3):
        output = output + s3[k]
        k += 1
    print(output)
#or
# will work only if all strings have same number of characters:
print('-'*40)
s1 = input('Enter string: ')
s2 = input('Enter string: ')
s3 = input('Enter string: ')
i = j = k = 0
output = ''
while i < len(s1) or j < len(s2) or k < len(s3):
        output = s1[i] + s2[j] + s3[k]
        i += 1
        j += 1
        k += 1
        print(output)

'''
#----------------------------------------------------------------
































    














































