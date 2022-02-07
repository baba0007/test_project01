#!/usr/bin/env python3

from tkinter import *
import tkinter.messagebox as mb
import os

# window inside window with buttons:

top_win = Tk()
top_win.geometry('500x500')
top_win.title('Main Window')

def net_window():
	net_win = Toplevel()
	net_win.geometry('300x300')
	
	
	but_google = Button(net_win, text = 'ping google', command = ping_google)
	but_google.pack(side = LEFT, anchor = NW)
	
	net_win.mainloop()

def ping_google():
	os.system('ping -c 3 google.com')
	

def chrome_window():
	chrome_window = Toplevel()
	chrome_window.geometry('300x300')
	
	but_chrome = Button(chrome_window, text = 'open chrome', command = open_chrome)
	but_chrome.pack(side = LEFT, anchor = NW)
	
	
	chrome_window.mainloop()


def open_chrome():
	os.system('sudo open /Applications/Google\ Chrome.app/')

but_prim = Button(top_win, text = 'Net Window', command = net_window)
but_prim.pack(side = LEFT, anchor = NW)


but_prim_chrome = Button(top_win, text = 'Run Chrome', command = chrome_window)
but_prim_chrome.pack(side = LEFT, anchor = NW)

top_win.mainloop()