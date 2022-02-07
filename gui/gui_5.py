#!/usr/bin/env python3

from tkinter import *
import tkinter.messagebox as mb
import os

top_win = Tk()
top_win.geometry('600x600')


# combination place, pack but grid not possible will return error.
# so you can use pack and place no problem but not with grid will conflict with pack.
# and it is better to use only one option or place or grid or pack.

shape = Canvas(top_win, width = 200, height = 200, bg = 'red')
shape.place(x=100, y=100)

shape_2 = Canvas(top_win, width = 200, height = 200, bg = 'orange')
shape_2.pack(side=BOTTOM, anchor=SW)

shape_3 = Canvas(top_win, width = 200, height = 200, bg = 'green')
#shape_3.grid(row=2, column=2)


# ---------------

'''
# with place:

shape = Canvas(top_win, width = 200, height = 200, bg = 'red')
shape.place(x=100, y=100)

shape_2 = Canvas(top_win, width = 200, height = 200, bg = 'orange')
shape_2.place(x=160, y=160)

shape_3 = Canvas(top_win, width = 200, height = 200, bg = 'green')
shape_3.place(x=190, y=190)
'''

# ----------------
'''
# with pack:

shape = Canvas(top_win, width = 200, height = 200, bg = 'red')
shape.pack(side=TOP, anchor = NW)

shape_2 = Canvas(top_win, width = 200, height = 200, bg = 'orange')
shape_2.pack(side=RIGHT, anchor=NE)


shape_3 = Canvas(top_win, width = 200, height = 200, bg = 'green')
shape_3.pack(side=BOTTOM, anchor=NW)
'''
#- -----------

'''
# with grid:

shape = Canvas(top_win, width = 200, height = 200, bg = 'red')
shape.grid(row = 0, column = 0)

shape_2 = Canvas(top_win, width = 200, height = 200, bg = 'orange')
shape_2.grid(row = 1, column = 1)


shape_3 = Canvas(top_win, width = 200, height = 200, bg = 'green')
shape_3.grid(row = 2, column = 2)
'''




top_win.mainloop()
