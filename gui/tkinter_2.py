#!/usr/bin/env python3

# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&index=2
# video 37:36/

from tkinter import *
import os

root = Tk()

e = Entry(root, width=50, bg='blue', fg='white', borderwidth=2)
# e.insert(1, 'Enter a command: ')
e.pack() # pack means to put it inside our window created

# button action:

def myClick():
	
	myLabel = Label(root, os.system(e.get())) # e.get() = what you write inside the box
	myLabel.pack()
	
	
# Creating buttons widgets:
	
myButton = Button(root, text = 'Enter', state = 'normal', padx = 50, pady=10, command=myClick, bg='red', fg='blue')
button_quit = Button(root, text = 'Exit Program', command = root.quit)
#button_quit.grid(row=0)

myButton.pack()
button_quit.pack()




# run the program:
root.mainloop()

