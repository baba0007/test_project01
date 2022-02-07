# oop video 4/4
'''
class Employee:
    # class attributes:
    name = 'Ben'
    designation = 'Sales'
    salesMadeThisWeek = 6

    # Methodes:
    def hasAchievedTarget(self):
        # self is used to access the attribute of our class
        if self.salesMadeThisWeek >= 5:
            print('Target has been achieved.')
        else:
            print('Target has not been achieved')


# objects creation to access methods and attribute of the class:
employee1 = Employee()


print(employee1.name)
print(employee1.designation)
print(employee1.salesMadeThisWeek)
print(employee1.hasAchievedTarget())

employee2 = Employee()
print(employee2.name)
# employe1 and employe2 get the same name that is not a good way

numbers = [1, 2, 3, 4]
print(type(numbers))
# the numbers is an object of the class list.
numbers.append(4) # append is a method in the class list
print(numbers)
'''
# ---------------------------------
'''
# class attribute and instance attribute:
# class attribute is common to all the instances of the class
# instance attribute is specific to each instance of the class


class Employee:
    # class attribute
    numberOfWorkingHours = 40


employee1 = Employee()
employee2 = Employee()
print(employee1.numberOfWorkingHours)
print(employee2.numberOfWorkingHours)

# to change the class attribute :
Employee.numberOfWorkingHours = 45
print(employee1.numberOfWorkingHours)

employee1.name = 'baba'
employee2.name = 'dialo'
print(employee1.name)
print(employee2.name)

print('')
employee1.numberOfWorkingHours = 40
print(employee1.numberOfWorkingHours)
print(employee2.numberOfWorkingHours)
'''
# ----------------------------------------------

'''
class Employee:
    def employeeDetails(self):
        # instance attribute:
        self.name = 'baba'
        print(f'Name = {self.name}')
        self.age = 30
        print(f'Age = {self.age}')

    def printEmployeeDetails(self):
        print('Printing in another method:')
        print(f'Name = {self.name}')
        print(f'Age = {self.age}')


employee = Employee()
print(employee.employeeDetails())
print(employee.printEmployeeDetails())
'''
# ---------------------------
# static methods and instance mthods:

'''
class Employee:
    def employeeDetails(self):
        self.name = 'baba'

    def welcomeMessage(self):
        print('Welcome to our Organisation.')


employee = Employee()
employee.employeeDetails()
print(employee.name)
print(employee.welcomeMessage())
'''

# static method will replace the default self parameter if we dont use it in our methods.

'''
class Employee:
    def employeeDetails(self):
        self.name = 'baba'

    @staticmethod
    def welcomeMessage():
        print('Welcome to our Organisation.')


employee = Employee()
employee.employeeDetails()
print(employee.name)
print(employee.welcomeMessage())
'''

# video 4/4 init method:

'''
class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayEmployeeDetails(self):
        print(self.name, self.age)


employee1 = Employee('Mark', 45)
employee2 = Employee('Bob', 56)
employee1.displayEmployeeDetails()
employee2.displayEmployeeDetails()
'''

# 4/4.3 exercice (4.2 is solution):
#
'''
Write an object oriented program to create a precious stone.
Not more than 5 precious stones can be held in possession at a given point of time.
If there are more than 5 precious stones,
delete the first stone and store the new one.
'''
#######
'''
class PreciousStone:
    numberOfPreciousStones = 0
    preciousStoneCollection = []

    def __init__(self, name):
        self.name = name
        # Increment the number of preciousStones
        PreciousStone.numberOfPreciousStones += 1
        # Append the precious stone to the list if total number of stones are less than 5
        if PreciousStone.numberOfPreciousStones <= 5:
            PreciousStone.preciousStoneCollection.append(self)
        else:
            # If more than 5 stones are present, delete the first one and store the new one
            del PreciousStone.preciousStoneCollection[0]
            PreciousStone.preciousStoneCollection.append(self)

    @staticmethod
    def displayPreciousStones():
        for preciousStone in PreciousStone.preciousStoneCollection:
            print(preciousStone.name, end=' ')
        print()


preciousStoneOne = PreciousStone("Ruby")
preciousStoneTwo = PreciousStone("Emerald")
preciousStoneThree = PreciousStone("Sapphire")
preciousStoneFour = PreciousStone("Diamond")
preciousStoneFive = PreciousStone("Amber")
preciousStoneFive.displayPreciousStones()
preciousStoneSix = PreciousStone("Onyx")
# Print all the stones after deleting the first stone
preciousStoneSix.displayPreciousStones()
'''
###
# video 5/2 Abstraction and encapsulation:

'''
class Library:
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print()
        print('Available Books: ')
        print()
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print()
            print('You have now borrowed the book')
            self.availableBooks.remove(requestedBook)
        else:
            print()
            print('Sorry the book is not available in our list.')

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print('You have returned the book. Thank you!')


class Customer:
    def requestBook(self):
        print()
        print('Enter the name of the book you like to borrow: ')
        self.book = input()
        return self.book
        print()

    def returnBook(self):
        print()
        print('Enter the name of the book you are returning: ')
        self.book = input()
        return self.book
        print()


library = Library(['Python for Beginners',
                   'Java for advanced', 'C++ for intermediate'])
customer = Customer()

while True:
    print()
    print('Enter 1 to display the available books: ')
    print('Enter 2 to request a book: ')
    print('Enter 3 to return a book: ')
    print('Enter 4 to exit: ')
    print()

    userChoise = int(input())
    if userChoise is 1:
        library.displayAvailableBooks()
    elif userChoise is 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoise is 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoise is 4:
        quit()
'''
# --------------------------
# singleInheritance:

'''
class Apple:
    manufacturer = 'Apple Inc.'
    contactWebsite = 'www.apple.com/contact'

    def contactDetails(self):
        print('To contact us, log on to', self.contactWebsite)


class MacBook(Apple):
    def __init__(self):
        self.yearOfManufacture = 2017

    def manufactureDetails(self):
        print(
            f'This Macbook is manufactured in the year {self.yearOfManufacture} by {self.manufacturer}')


macBook = MacBook()
macBook.manufactureDetails()
macBook.contactDetails()
'''
# -------------------------------
# video 6/2
# MultipleInheritance:

'''
class OperatingSystem:
    multitasking = True
    name = 'Mac OS'


class Apple:
    website = 'www.apple.com'
    name = 'Apple'


class MacBook(OperatingSystem, Apple):
    def __init__(self):
        if self.multitasking is True:
            print(
                f'This is a multitasking system. visit {self.website} for more details')
            print(f'Name: {self.name}') # wiil print Mac os coz OeratingSystem class is first then Apple second , if Apple is first then it will print Apple


macBook = MacBook()
'''
# ----------------------------
# video 6/3
# Multilevelinheritance:

'''
class MusicalInstruments:
    numberOfMajorKeys = 12


class StringInstruments(MusicalInstruments):
    typeOfWood = 'Tonewood'


class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfStrings = 6
        print(
            f'This guitar consists of {self.numberOfStrings} strings. It is made of {self.typeOfWood} and it can play {self.numberOfMajorKeys} keys.')


guitar = Guitar()
'''

# -------------------------------
# video 6/4
# Public, Protected and private naming conventions in python:
# Public ==> memberName
# Protected ==> _memberName
# Private ==> __memberName

'''
class Car:
    numberOfWheels = 4  # Public attribute
    _color = 'Black'  # Protected attribute
    __yearOfManufacture = 2017  # Private attribute (_Car___yearOfManufacture)


class Bmw(Car):
    def __init__(self):
        print('Protected attribute color: ', self._color)


car = Car()
print('Public attribute numberOfWheels: ', car.numberOfWheels)
bmw = Bmw()
# print('Private attribute yearOfManufacture: ', car.__yearOfManufacture)
print('Private attribute yearOfManufacture: ', car._Car__yearOfManufacture)
'''
# --------------------------------
# video 7/1
