#!/usr/bin/env python3

from tkinter import *
import tkinter.messagebox as mb
import os

top_win = Tk()
top_win.geometry('800x800')


def activate_boost():
	status_10 = turbo_10.get()
	status_20 = turbo_20.get()
	
	if status_10 == 1:
		print('Boost +10 Activated')
	if status_20 == 1:
		print('Boost +20 Activated')
	if status_10 == 1 and status_20 == 1:
		print('!'*10)
		print('Alert - Danger')
		print('Lower Down Boost Levels - Just One Checkbutton.')
	if status_10 == 0 and status_20 == 0:
		print('Normal Operation.')
	
gen_lab = Label(top_win, text='Engine boost')
gen_lab.grid(row=0, column=0)

turbo_10 = IntVar()
turbo_20 = IntVar()

ch_10 = Checkbutton(top_win, text='Boost +10', variable=turbo_10)
ch_10.grid(row=1, column=0)

ch_20 = Checkbutton(top_win, text='Boost +20', variable=turbo_20)
ch_20.grid(row=2, column=0)


but_1 = Button(top_win, text='Activate Boost', command=activate_boost)
but_1.grid(row=3, column=0)




top_win.mainloop()
