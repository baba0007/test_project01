#!/usr/bin/env python3

from tkinter import *
import tkinter.messagebox as mb
import os

top_win = Tk()
top_win.geometry('200x200')

lab_1 = Label(top_win, text='Scrolls are weird')
lab_1.pack(side=TOP, anchor=NW)

# scrollbar creation:

scr_bar = Scrollbar(top_win)
scr_bar.pack(side=RIGHT, fill=Y)

items = Listbox(top_win, yscrollcommand=scr_bar.set)

for x in range(100):
	items.insert(END, 'Item: ' + str(x))

items.pack(side=LEFT, fill=Y) # also can use BOTH instead of Y



# connecting scrollbar with items:
scr_bar.config(command=items.yview)


top_win.mainloop()
