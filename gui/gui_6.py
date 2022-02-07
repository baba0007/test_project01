#!/usr/bin/env python3

from tkinter import *
import tkinter.messagebox as mb
import os
from random import *


top_win = Tk()
top_win.geometry('700x700')

area = Canvas(top_win, width=500, height=500, bg='lightgreen')

# creating rectangle:
rec = area.create_rectangle(10, 10, 200, 200, fill='orange')
rec_1 = area.create_rectangle(20, 20, 150, 150, fill='blue')

# creating Arc:
arc = area.create_arc(30, 30, 300, 300, extent = 90, fill='red')
#--------------

# creating oval:
oval = area.create_oval(10, 10, 300, 50, fill='yellow')
# ----------


# creating lines:
for x in range(10):
	
	#line = area.create_line(10, 10, 400, 50, fill='red', width = 10)
	line = area.create_line(randrange(25, 100), randrange(25, 100),
		randrange(50, 400), randrange(200, 400))


area.grid(row=0, column=0)

top_win.mainloop()
