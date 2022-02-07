name = 'Mustapha'
surname = 'Lab'


def f1():
    print('f1 execution.')


def f2():
    print('f2 execution.')


def f3():
    print('f3 execution.')


def calc(a, b):
    print(f'sum of {a} + {b} = {a + b}')
    print(f'sub of {a} - {b} = {a - b}')
    print(f'product of {a} * {b} = {a * b}')


a = 10
b = 20

# Directly execution:

if __name__ == '__main__':

    f1()

    f2()

    f3()

    calc(a, b)
    print(name)
    print(surname)

'''
f1()
f2()
f3()
calc(a, b)
print(name)
print(surname)
'''
