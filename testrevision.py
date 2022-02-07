'''
import sys
# import os


a = sys.executable
print(a)


from requests import get

ip = get('https://api.ipify.org').text
print(f'My wan ip is: {ip}')
'''

# -----------------------

# a = input('Enter name: ')
# print(a)


# x = os.system('ping 4.2.2.2')
# print(x)

'''
import nmap as np
np.PortScanner()
'''
# ---------
'''
from guizero import App, Text
app = App(title='Hello World!!!')
app.bg = 'green'
message = Text(app, text='Welcome to the app')
app.display()
'''

# ------------------------
'''
import os


def net():
    return os.system('ping -c 2 4.2.2.2')


print(net())
'''

# --------------

'''
word = 'mustapha'


def caps(word):
    # return word.upper()
    return word.capitalize()


print(caps(word))
'''

# -------------
'''
import random
repeat = True
while repeat:
    print ("You rolled", random.randint(1, 6))
    print ("Do you want to roll again? Y/N")
    repeat = ("y" or "yes") in input().lower()
'''

# --------
# what is a method:
# it is a function which a member of a class:

'''
class C:
    def my_method(self):
        print("I am a C")


c = C()
c.my_method()  # Prints("I am a C")
'''

# -------
'''
import math

# print(dir(math))
print(math.__name__)
print(math.pi)
print(math.pow(3, 5))
# -------------

import sys

a = sys.executable
print(a)
'''

# ------------------
'''
import socket


r = input("Enter Website name: ")
try:
    # print("Ip address of " + r + (" is ") + socket.gethostbyname(r))
    print(f'ip address of {r} is: {socket.gethostbyname(r)}')
except socket.error as e:
    print("Error : {} ".format(e))


r1 = input('Enter ip: ')
try:
    print(f'Name of {r1} is: {socket.gethostbyaddr(r1)}')

except socket.error as e:
    print(f'Error: {e}')
'''

# ---------------------

# all this codes try them in the terminal python:

'''
from rich import inspect

my_list = ['foo', 'winkel']
inspect(my_list, methods=True)
'''

# ---------------------
'''
from time import sleep
from rich.console import Console

console = Console()
tasks = [f"task {n}" for n in range(1, 11)]

with console.status("[bold green]Working on tasks...") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(1)
        console.log(f"{task} complete")
'''

# ---------------------
'''
from time import sleep
from rich.progress import track

for step in track(range(10)):
    sleep(1)
    step

'''

# ----------------------
'''
from time import sleep
from rich.console import Console

console = Console()
tasks = [f'task {n}' for n in range(1, 11)]

with console.status('[bold green]Working on tasks...') as status:
    while tasks:
        task = tasks.pop(0)
        sleep(1)
        console.log(f'{task} complete')

'''

# ----------------------
'''
# must be run from the console

import typer

app = typer.Typer()

@app.command()
def hello(name: str, age: int):
    print(f'Hello There {name} !!!')
    print(f'Your Age is {age} !!!')
    
@app.command()
def goodbye():
    print('Goodbye.')
    
    
    
    
if __name__ == '__main__':
    app()
    
'''

# --------------


from rich import inspect
import subprocess
'''
results = subprocess.run(['ping', '-c', '2', '4.2.2.2'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print(results.stdout.decode('utf-8'))
'''

# to send output to a file in my case ping_out.txt:

'''
with open('ping_out.txt', 'w') as f:
    results = subprocess.run(['ping', '-c', '4', '4.2.2.2'], stdout=f, stderr=subprocess.PIPE, text=True)
    
    print(results.stdout)
f.close()
'''

# to run the command more quickly:
'''
with open('ping_out.txt', 'w') as f:
    results = subprocess.Popen(['ping', '-c', '4', '4.2.2.2'], stdout=f, stderr=subprocess.PIPE, text=True)
    
results.poll()
stdout, stderr = results.communicate()

f.close()

'''

# ------------------

'''
import math

x = math.pi
print(math.cos(x))
'''

# --------------
'''
import math

x = dir(math)
print(x)

'''

# ------------

import pretty_errors
import os
import sys


# print(sys.executable)

#print(os.system('ping -c 2 4.2.2.2'))
# print(os.popen('ls').read())
# print(os.system('ls'))


#os.system('ping -c 2 4.2.2.2 > pingg.txt')

# Current date:

'''
import subprocess

cmd = 'date'
res0 = subprocess.check_output(cmd)
x = res0.decode('utf-8')
print(f'Current date is: {x}')

print('-' * 10)


def calculate(x, y):
    return int(x) * int(y)


x = input('x: ')
y = input('y: ')

print()
print(f'{x} * {y} = {calculate(x, y)}')
'''

# -------

'''
x = int(input('Enter x: '))

if x % 2 == 0:
    print('x is pair.')
else:
    print('x is impair.')
'''
