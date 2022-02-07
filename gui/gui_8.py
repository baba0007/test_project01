#!/usr/bin/env python3

from tkinter import *
import tkinter.messagebox as mb
import os

top_win = Tk()
top_win.geometry('800x800')

def calc_func():
	number_atm = entry_1.get()
	print_res = (int(number_atm) * 2)
	#print('Result:',print_res) # will be printed in shell
	# print inside tkinter:
	lab_2 = Label(top_win)
	lab_2['text'] = print_res
	lab_2.grid(row=1, column=2)
	
	#print('Number ATM is', number_atm)

lab_1 = Label(top_win, text = 'Number', bg = 'lightyellow')
lab_1.grid(row=0, column=0)

entry_1 = Entry(top_win)
entry_1.grid(row=0, column=1)

but_1 = Button(top_win, text = 'Calculate', highlightbackground = 'lightgreen', command = calc_func)
but_1.grid(row=1, column=1)



top_win.mainloop()
