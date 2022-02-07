#!/usr/bin/env python3

from tkinter import *
import tkinter.messagebox as mb
import os

top_win = Tk()
top_win.geometry('800x800')

def sub_nl():
	name = ent_name.get()
	last_name = ent_last_name.get()
	print(f'Name: {name}')
	print(f'Last Name: {last_name}')
	print('-'*20)

def sub_ap():
	age = ent_age.get()
	pay = ent_pay.get()
	print(f'Age: {age}')
	print(f'Pay: {pay}')
	print('-'*20)

frm_1 = Frame(top_win, highlightbackground='black', highlightthickness=1)
frm_2 = Frame(top_win, highlightbackground='black', highlightthickness=1)

# Frame 1:

lab_name = Label(frm_1, text='Name').grid(row=0, column=0)
lab_last_name = Label(frm_1, text='Last Name').grid(row=1, column=0)

ent_name = Entry(frm_1)
ent_name.grid(row=0, column=1)

ent_last_name = Entry(frm_1)
ent_last_name.grid(row=1, column=1)

but_1 = Button(frm_1, text='Submit', command=sub_nl).grid(row=3, column=0)

# --------------------------------------------------------------

# Frame 2:

lab_age = Label(frm_2, text='Age').grid(row=0, column=0)
lab_pay = Label(frm_2, text='Pay').grid(row=1, column=0)

ent_age = Entry(frm_2)
ent_age.grid(row=0, column=1)

ent_pay = Entry(frm_2)
ent_pay.grid(row=1, column=1)

but_2 = Button(frm_2, text='Submit', command=sub_ap).grid(row=3, column=0)


frm_1.grid(row=0, column=0)
frm_2.grid(row=0, column=1)

top_win.mainloop()
