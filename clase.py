'''
class Person:
    name = ''
    age = 0
    country = ''
    def description(self):
        print('{} is {} years, and live in {}.'.format(self.name, self.age, self.country))

person1 = Person()
person1.name = 'Mustapha'
person1.age = 52
person1.country = 'Morocco'
person1.description()

person2 = Person()
person2.name = 'Sofiane'
person2.age = 34
person2.country = 'Morocco'
person2.description()
'''
#----------------------------
# or


class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def description(self):
        print('{} is {} years and is from {}.'.format(self.name, self.age, self.country))


person1 = Person('Mustapha', 52, 'Morocco')
person2 = Person('Sofiane', 34, 'Morocco')
person1.description()
person2.description()
