#!/usr/bin/env python
def square():
    print('You choosed to print SQUARE Pattern...')
    n = int(input('Enter No of Rows: '))
    for i in range(n):
        print('* ' * n)


def right_angle_triangle():
    print('You choosed to print Right Angled Triangle Pattern....')
    n = int(input('Enter No of Rows: '))
    for i in range(n):
        for j in range(i + 1):
            print('*', end=' ')
        print()


def pyramid():
    print('You choosed to print pyramid Pattern...')
    n = int(input('Enter No of Rows: '))
    for i in range(n):  # 0,1,2,3
        print((' ' * (n - i - 1)) + ('* ') * (i + 1))


def diamond():
    print('You choosed to print Diamond Pattern...')
    n = int(input('Enter n Value: '))
    for i in range(n):  # 0,1,2,3
        print(' ' * (n - i - 1) + '* ' * (i + 1))
    for i in range(n - 1):  # 0,1,2
        print(' ' * (i + 1) + '* ' * (n - i - 1))
