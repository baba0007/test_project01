#!/usr/bin/env python3

from tkinter import *
import tkinter.messagebox as mb
import os

top_win = Tk()
top_win.geometry('800x800')

def delete_from_list():
	selected = list_domains.curselection()
	list_domains.delete(selected)

gen_lab = Label(top_win, text = 'Domain')
gen_lab.grid(row=0, column=0)

list_domains = Listbox(top_win)

list_domains.insert(1, 'google.com')
list_domains.insert(2, 'yahoo.com')
list_domains.insert(3, 'bing.com')

but_1 = Button(top_win, text='Delete From List', command = delete_from_list)
but_1.grid(row=3, column=0)

list_domains.grid(row=1, column=0)
top_win.mainloop()
