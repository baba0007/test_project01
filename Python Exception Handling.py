# in any programming language, there are 2 types of possible errors:
# 1- Syntax Error
# 2- Runtime Error


# 1- Syntax Errors:
# the errors which occurs because of invalid syntax, such type of errors are considered as Syntax errors.
# Programmer is responsible to correct these syntax errors. Once all syntax errors are corrected, then,
# only program execution will be started.

# 2- Runtime Errors:
# Also known as Exceptions
# While executing the program, at runtime if something goes wrong because of end user input,
# memory problems, programming logic etc, then we will get Runtime errors.

# Exeption Handling concept applicable for Runtime Errors but not for Syntax Errors.


# I- Syntax error:

'''
# 1- ex:

x = 10

if x == 10  #(forgotten :)
    print('x value 10')

# 2-ex:

print 'hello there' # (forgotten ())
'''
# ------------------------------------------

# II- Runtime Error: known as exeptions:

# Ex1-
'''
x = int(input('Enter First Number: '))
y = int(input('Enter Second Number: '))
# print(f'x + y = {x+y}')
print('The Result is: ', x/y) # if i device 10/0 , becoz of zero deivision error it is Runtime Error

# so the enduser input is the raison of getting Runtime error:
# ZeroDevision Error, ValueError, FileNotFoundError,etc.... are RuntimeError
'''

'''
# Ex-2:
# becoz the file xyxy.txt does not exist i get FileNotFoung Error
f = open('xyxy.txt')
print(f.read())
'''

'''
# Ex-3:
# No error coz the file exist
f = open('ip-range.txt')
print(f.read())
'''

# -------------------------
# The 3 most important Questions about Exception Handling:
# What is an Exception ?:
# An unwanted and unexpected event that disturbs normal flow of program is called Exception.
# eg:
# ZeroDivisionError, ValueError, FileNotFoundError, etc....


# What is the main objective of Exception Handling ?:

# It is highly recommended to handle exceptions.
# The main objective of exception handling is Graceful Termination / Normal Termination of the,
# application (i.e we should not block our resources and we should not miss anything)

# What is the meaning of Exeption Handling ?:

# Exception handling does not mean repairing an exception. we have to define alternative way,
# to continue rest of the program normally.

# This way of defining alternative is nothing but exception handling.

'''

try:
    Read data from file located at london

except FileNotFoundError:
    use locale file and continue the rest of the program normally
'''

# Default Exception Handling and Exception Hierarchy:

# Abnormal Termination:

'''
print('Hello')
print(10 / 0)  # because of ZeroDivisionError the programme will stop and do not continue, coz there is no handling
print('Hi')
'''

# Every exception in python is an object.
# For every exception type the corresponding class is available.
# All exceptons in python are childclass of the python baseexception parent class
# ZeroDivisionError, OverflowError, FloatingpointError, IndexError, FileNotFoundError, etc... are child class of Exception class

# ---------------------------------
# Customized Exception Handling by using  try-except:

# 1- without try-except: Abnormal Termination coz the programme will stop at ZeroDivisionError and will not continue to next: None Graceful termination:

'''
print('Stat-1')
print(10 / 0)
print('Stat-3')
'''

# 2- with try-except: Normal termination

# syntax:

'''
try:
    Risky code ( the code which rise exception)
except:
    Handling code
'''
# -----------------------
'''
print('Stat-1')

try:
    print(10 / 0)
    print(1 / 0)
except ZeroDivisionError:
    print('10 / 0: ZeroDivisionError')
    print('1 / 0: ZeroDivisionError')

print('Stat-3')
print('-' * 10)
'''
# ---------------

# How to print Exception information to the console ? :

# Ex-1:
'''
try:
    print(10 / 0)
except ZeroDivisionError as msg:
    print('The type of exception:', type(msg))
    print('The type of exception:', msg.__class__)
    print('The exception class name:', msg.__class__.__name__)
    print('The Description of exception:', msg)

print('-' * 10)
# Ex-2:

try:
    x = int(input('Enter First Number: '))
    y = int(input('Enter Second Number: '))
    print('The Result is : ', x / y)

except BaseException as msg:
    print('The type of exception: ', type(msg))
    print('The type of exception: ', msg.__class__)
    print('The Name of exception: ', msg.__class__.__name__)
    print('The Description of exception: ', msg)
'''
# -----------------------------------
# try with multiple except blocks:
'''
# Ex-1:

try:
    x = float(input('Enter first number: '))
    y = float(input('Enter second number: '))
    print('The Result {}/{} is: '.format(x, y), x / y)

except ZeroDivisionError:
    print("Can't Divide with Zero")

except NameError:
    print('Please provide int value only')

'''
# ---------------------
'''
# Ex-2:

try:
    print(10 / 0)

except ZeroDivisionError:
    print('ZeroDivisionError')

except ArithmeticError:
    print('ArithmeticError')

# ------------
print('-' * 10)
# Ex-3:

try:
    print(10 / 0)


except ArithmeticError:
    print('ArithmeticError')

except ZeroDivisionError:
    print('ZeroDivisionError')

'''

# ----------------------------

# Single except block that can handle multiple different exceptions:
'''
try:
    x = float(input('Enter first number: '))
    y = float(input('Enter second number: '))
    print('The Result {}/{} is: '.format(x, y), x / y)

except(ZeroDivisionError, NameError, ValueError) as msg:
    print('exception name: ', msg.__class__.__name__)
    print('Please Provide valid input only.')
'''

# -------------

# Default Except Block & Various except block syntaxes:
# Default Except Block must be last not at the begining, coz if we put it at first we will get:
# SyntaxError: default 'except:' must be lastß

'''
try:
    x = float(input('Enter first number: '))
    y = float(input('Enter second number: '))
    print('')
    print('The Result {}/{} is: '.format(x, y), x / y)

# except ZeroDivisionError:
#    print('ZeroDivisionError: Cannot divide with zero.')

# except:
#    print('')
#    print('Default Except block: provide valide input only.')

except (ZeroDivisionError, ValueError) as msg:
    print(f'Error message: {msg.__class__.__name__}')

'''

# -----------------------------
# finally block purpose and speciality:

# Syntax:

'''
try :
    Risky code
except:
    Handling code
finally block:
    Cleaning code
'''


# ---------------------

# Ex1: if no exception
'''
try:
    print('try')
except ZeroDivisionError:
    print('except')
finally:
    print('finally')

print('-' * 5)

# Ex-2: if exception raised and handled:

try:
    print('try')
    print(10 / 0)

except ZeroDivisionError:
    print('except')

finally:
    print('finally')


print('-' * 5)

# Ex-3: Exception raised but not handled:

try:
    print('try')
    print(10 / 0)

except ValueError:
    print('except')

finally:
    print('finally')
'''

# -----------------
# finally block vs os._exit(0) : when you execute os._exit(0) , finally block wont execute.
# 0 inside exit(0) means status code: 0 ---> Normal Termination (NT), Non Zeo -----> Abnormal Termination (AT)


# Finally block meant for cleanup activities,
# related to try block. i.e whatever resources,
# we opened as the part of try block will be closed,
# inside finally clock

# Destructor meant for cleanup activities related,
# to object. what ever resources associated with,
# with the object should be deallocated inside destructor,
# which will be executed before destroying object.


'''
import os

try:
    print('try')
    os._exit(0)
    # os._exit(1000)

except ValueError:
    print('except')

finally:
    print('finally')

'''

# -------------

# Controle Flow in try-except-finally:

# Nested try-except-finally theory and demo program:


# Ex1:
'''
try:
    print('Outer try block')
    
    try:
        print('Inner try block')
    except ZeroDivisionError:
        print('Inner except block')
    finally:
        print('Inner finally block')

except:
    print('Outer except block')
    
finally:
    print('Outer finally block')        



print('-'*10)
# -----------------
    
# Ex2:
    

try:
    print('Outer try block')
    
    try:
        print('Inner try block')
        print(10/0)
    except ZeroDivisionError:
        print('Inner except block')
    finally:
        print('Inner finally block')
        
except:
    print('Outer except block')
    
finally:
    print('Outer finally block')     


print('-'*10)

#-----------------

# Ex3:

try:
    print('Outer try block')
    
    try:
        print('Inner try block')
        print(10/0)
    except ValueError:
        print('Inner except block')
    finally:
        print('Inner finally block')
        
except:
    print('Outer except block')
    
finally:
    print('Outer finally block')     
    

print('-'*10)

#--------------------------

# Ex4:

try:
    print('Outer try block')
    print(10/0)
    
    try:
        print('Inner try block')
    
    except ValueError:
        print('Inner except block')
    finally:
        print('Inner finally block')
        
except:
    print('Outer except block')
    
finally:
    print('Outer finally block')     

'''

#------------------------
'''
# Control Flow in Nested try-except-finally:

# else block with try-except-finally theory:
# syntax: try-except-else-finally:

# if-else:

x = 10

if x > 10:
    print('x > 10')
else:
    print('x is not > 10.')

print('')
print('-' * 10)

# loops:

for x in range(10):
    print(x)

else:
    print('')
    print('All items are printed.')

print('-' * 10)
print()

for x in range(10):
    if x > 5:
        break
    print(x)
else:
    print('Items are printed.')


print('')
'''

# ---------------
# else block with try-except-finally demo programs:
# else will excecute only when there is no exception:

# ex1 without exception:
'''
try:
    print('try')
except:
    print('except')
else:
    print('else')
finally:
    print('finally')


print('')
print('-'*10)
# ex2: with except:

try:
    print('try')
    print(1/0)
except:
    print('except')
else:
    print('else')
finally:
    print('finally')

print('')
print('-'*10)

'''

# ex3:
# you cannot use else without except block , coz error syntaxerror will rised:

'''
try:
    print('try')
else:
    print('else')
finally:
    print('finally')
'''

# ex4:
'''
print('')
print('-'*10)

f = None
try:
    f = open('ping_out.txt', 'r')

except:
    print('some problem while locating/opening file')

else:
    print('file opened successfully')
    print('The Contents of the file: ')
    print('#'*20)
    print(f.read())

finally:
    if f is not None:
        f.close()


# -------

# ex5:
        
print('-'*10)

f = None
try:
    f = open('ping_.txt', 'r')
    
except:
    print('some problem while locating/opening file')
    
else:
    print('file opened successfully')
    print('The Contents of the file: ')
    print('#'*20)
    print(f.read())
    
finally:
    if f is not None:
        f.close()

'''

# Various possible combinations of try-except-finally:

# we cannot use only try alone we get syntaxerror , so we should use except and if not we use atleast finally:
# also we cannot use only except block alone we get syntaxError we need to associated with try:
# also else should be associated with try and except block to not get syntaxError:
# also finally should be associated with try and except block to not get syntaxError:

'''
# SyntaxError
try:
    print('try')
'''
    
'''
# SyntaxError
except:
    print('except')
'''

'''
# SyntaxError
else:
    print('else')
'''

'''
# SyntaxError
finally:
    print('finally')
'''

'''
# valid code:
try:
    print('try')

except:
    print('except')
'''

'''
# Syntaxerror coz else without except wont work and return syntaxerror
try:
    print('try')
else:
    print('else')
'''
    
'''
# Valid code
try:
    print('try')
finally:
    print('finally')
'''

'''
# SynatxError: becoz else has come first, so it should be except first then else
try:
    print('try')
else:
    print('else')
except:
    print('except')
finally:
    print('finally')
'''

'''
# SyntaxError: coz except is required
try:
    print('try')
else:
    print('else')
finally:
    print('finally')
'''

'''
#Valid code:
try:
    print('try')
except:
    print('except')
else:
    print('else')
finally:
    print('finally')

'''

'''
#Valid code
try:
    print('try')
except:
    print('except')
try:
    print('try')
finally:
    print('finally')
'''

'''
#SynatxError
try:
    print('try')
except('except')
try:
    print('try')
else:
    print('else')
    
'''

'''
#Valid code: try block can be associated with multiple except blocks:
try:
    print('try')
except xxx:
    print('except-1')
except yyy:
    print('except-2')

'''

'''
#SyntaxError: more than on else block in try block will result in Syntaxerror
try:
    print('try')
except:
    print('except')
else:
    print('else-1')
else:
    print('else-2')
'''
    
'''
#Synatxerror: not possible to associate multiple finally block in a try block:
try:
    print('try')
except:
    print('except')
finally:
    print('finally-1')
finally:
    print('finally-2')

'''

'''
#valid code: else is associated to if but not to try block: 
try:
    print('try')
except:
    print('except')
if 10 > 20:
    print('if')
else:
    print('else')
'''

'''
#SynatxError: no independent statment should be between try and except:
try:
    print('try')
print('Hello.')
except:
    print('except')
'''
    
'''    
#SyntaxError: invalid syntax
try:
    print('try')
except xxx:
    print('except-1')
print('Hello')
except yyy:
    print('except-2')

'''

'''
#SyntaxError: invalid syntax:no independent statment should be between else and except:
try:
    print('try')
except:
    print('except')
print('Hello.')
else:
    print('else')
'''
    
'''    
#SynatxError: no independent statment should be between finally and except:
try:
    print('try')
except:
    print('except')
print('Hello')
finally:
    print('finally')
'''
    

'''
#Validcode:
try:
    try:
        print('inner try')
    except:
        print('inner except')
    finally:
        print('inner finally')

except:
    print('outer except')

'''

'''
#ValidCode:
try:
    print('try')
except:
    try:
        print('inner try')
    except:
        print('inner except')

'''

'''
#ValidCode
try:
    print('try')
except:
    print('except')
else:
    try:
        print('try')
    finally:
        print('finally')
    
'''

'''
#ValidCode
try:
    print('try')
except:
    print('except')
finally:
    try:
        print('try')
    except:
        print('except')
'''
        
'''
#SyntaxError: inner try without except block or finally will result to SynatxError:
try:
    try:
        print('inner try')
except:
    print('except')
'''

'''
#ValidCode:
try:
    try:
        print('try')
    finally:
        print('finally')
except:
    print('except')
'''
    
#Conclusion:
#whenever we are writing try block, compulsory we should write except or finally blocks.
#try without except or finally is always invalid.

#whenever we are writing except block, compulsory try block should be there.
#except without try is always invalid.

#whenever we are writing finally block, compulsory try block should be there.
#finally without try is always invalid.

#whenever we are writing else block, compulsory except block should be there.
#else without except is always invalid.

#in try-except-else-finally order is important.

# we can write multiple except bloks for the same try block, but we cannot write multiple else blocks, and finally blocks.

# Types of Exceptions-Predefined and User Defined:

