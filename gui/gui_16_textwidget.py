#!/usr/bin/env python3

from tkinter import *
import tkinter.messagebox as mb
import os


top_win = Tk()
top_win.geometry('800x800')

file = open('textwidget.txt','r')
t = Text(top_win, padx=20, pady=10, width=40, height=40, bd=10, relief=RIDGE, bg='lightyellow',
	fg='blue', selectbackground='yellow', selectforeground='black', font='verdana')

for x in file.read():
	t.insert(END, x)





file.close()
t.pack(side=TOP, anchor=NW)
top_win.mainloop()
