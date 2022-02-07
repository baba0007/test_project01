def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

while True:
    print('Select Operation: ')
    print('1.Add')
    print('2.Substract')
    print('3.Multiply')
    print('4.Divide')
    print('5.Exit')
    choice = int(input('Enter choice (1/2/3/4/5):'))
    

    if choice == 1:
        num1=int(input('Enter first number :'))
        num2=int(input('Enter second number :'))
        print(f'{num1} + {num2} = {add(num1,num2)}')
    
    elif choice == 2:
        num1=int(input('Enter first number :'))
        num2=int(input('Enter second number :'))
        print(f'{num1} - {num2} = {substract(num1,num2)}')

    elif choice == 3:
        num1=int(input('Enter first number :'))
        num2=int(input('Enter second number :'))
        print(f'{num1} * {num2} = {multiply(num1,num2)}')

    elif choice == 4:
        num1=int(input('Enter first number :'))
        num2=int(input('Enter second number :'))
        print(f'{num1} / {num2} = {divide(num1,num2)}')

    elif choice == 5:
        break