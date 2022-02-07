#!/usr/bin/env python3

from tkinter import *
import tkinter.messagebox as mb
import os

top_win = Tk()
top_win.geometry('800x800')


def selected():
	selected = real_stuff.get()
	#print(selected)
	#output['text'] = selected
	output.config(text=selected)
	
	if selected == 1:
		print('Selected: Python at position', selected)
	if selected == 2:
		print('Selected: C++ at position', selected)
	if selected == 3:
		print('Selected: Perl at position', selected)
	
	

lab_1 = Label(top_win, text='Select only one').pack(anchor=W)
real_stuff = IntVar()

rad_1 = Radiobutton(top_win, text='Python', variable=real_stuff, value=1, command=selected)
rad_1.pack(anchor=W)

rad_2 = Radiobutton(top_win, text='C++', variable=real_stuff, value=2, command=selected)
rad_2.pack(anchor=W)

rad_3 = Radiobutton(top_win, text='Perl', variable=real_stuff, value=3, command=selected)
rad_3.pack(anchor=W)


output = Label(top_win, text='You selected: ')
output.pack(anchor=W)




top_win.mainloop()