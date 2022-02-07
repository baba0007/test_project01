from tkinter import *
import tkinter.messagebox as mb
import os


top_win = Tk()
top_win.geometry('300x300')


def run_ping():
    host = input('Enter host ip: ')
    os.system(f'ping -c 2 {host}')


def run_devicesupdate():
    os.system('python /Users/babadialo/Documents/python/wing/devicesupdate.py')


def run_chrome():
    os.system('sudo open /Applications/Google\ Chrome.app/')


common_img = PhotoImage(width=1, height=1)

but_1 = Button(top_win, text='ping host', image=common_img, width=200, height=200, compound='c',
               bg='lightgreen', command=run_ping)
but_1.place(x=5, y=2)
