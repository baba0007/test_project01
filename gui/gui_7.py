#!/usr/bin/env python3

from tkinter import *
import tkinter.messagebox as mb
import os

top_win = Tk()
top_win.geometry('800x800')
top_win.title('Logins')

can = Canvas(top_win, width = 400, height = 400, bg = 'lightgreen')


user_name = Label(top_win, text='Username: ')
user_name.place(x = 20, y = 40)

user_pass = Label(top_win, text='Password: ')
user_pass.place(x = 20, y = 80)


submit_button = Button(top_win, text='Login')
submit_button.place(x = 20, y = 120)

# -------------------

entry_name = Entry(top_win)
entry_name.place(x = 100, y = 40)

entry_pass = Entry(top_win)
entry_pass.place(x = 100, y = 80)


can.grid(row = 0 , column = 0)
top_win.mainloop()
