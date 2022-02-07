#!/usr/bin/env python3

from tkinter import *
import tkinter.messagebox as mb
import os

top_win = Tk()
top_win.geometry('800x800')

def pg():
	os.system('ping -c 2 google.com')

def py():
	os.system('ping -c 2 yahoo.com')

# Menu bar:
bar = Menu(top_win)

# adding thing in the Menubar:
bar.add_command(label = 'Ping Google', command = pg)
bar.add_command(label = 'Ping Yahoo', command = py)





top_win.config(menu = bar)
top_win.mainloop()
