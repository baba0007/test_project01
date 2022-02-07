#!/usr/bin/env python3

from tkinter import *
import tkinter.messagebox as mb
import os


top_win = Tk()
top_win.geometry('300x300')


def run_ping():
	os.system('ping -c 2 4.2.2.2')


def run_calc():
	os.system('sudo open /Applications/Numi.app/')


def run_chrome():
	os.system('sudo open /Applications/Google\ Chrome.app/')
	

but_1 = Button(top_win, text='ping host', command = run_ping)
but_1.place(x=5, y=2)

but_2 = Button(top_win, text='Numi', command = run_calc)
but_2.place(x=70, y=2)

but_3 = Button(top_win, text='chrome', command = run_chrome)
but_3.place(x=150, y=2)


top_win.mainloop()