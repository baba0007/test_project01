#!/usr/bin/env python3

from tkinter import *
import tkinter.messagebox as mb
import os

top_win = Tk()
top_win.geometry('800x800')


def select():
	selcted = real_var.get()
	print('Selected From Range: ', selcted)
	
	if selcted > 50:
		print('More than 50.')

real_var = IntVar()

# orient can be HORIZONTAL or VERTICAL
scale = Scale(top_win, label= 'Range', length = 200, from_ = 1, to = 200, orient=HORIZONTAL, troughcolor='red', variable=real_var)
scale.pack(anchor=CENTER)

btn_1 = Button(top_win, text='Submit', command = select)
btn_1.pack(anchor=CENTER)



top_win.mainloop()
