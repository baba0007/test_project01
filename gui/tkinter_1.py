#!/usr/bin/env python3

# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&index=2
# video 29:36/

from tkinter import *
import os

root = Tk()

e = Entry(root, width=50, bg='blue', fg='white', borderwidth=2)
e.pack()

# button action:

def myClick():
	myLabel = Label(root, os.system('ssh pi@11.0.0.254'))
	myLabel.pack()


# Creating buttons widgets:

myButton = Button(root, text = 'ssh to DNSserver', state = 'normal', padx = 50, pady=10, command=myClick, bg='red', fg='blue')
myButton.pack()

# run the program:
root.mainloop()

