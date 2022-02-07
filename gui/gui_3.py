#!/usr/bin/env python3

#!/usr/bin/env python3

from tkinter import *

import tkinter.messagebox as mb
import os


top_win = Tk()
top_win.title('Tools')
top_win.geometry('550x550')


def run_ping():
	host = input('Enter host ip: ')
	os.system(f'ping -c 2 {host}')
	
	
def run_devicesupdate():
	os.system('python /Users/babadialo/Documents/python/wing/devicesupdate.py')
	
	
def run_chrome():
	os.system('sudo open /Applications/Google\ Chrome.app/')
	
	
#common_img = PhotoImage(width = 1, height = 1)

but_1 = Button(top_win, text='ping host', width = 10, height = 2, compound = 'c', 
	highlightbackground = 'lightgreen', foreground = 'red', font = ('Arial', 18), command = run_ping)
#but_1.place(x=5, y=2)
but_1.pack(side = LEFT, anchor = NE) # NE = Noorth eest.


#but_2_img = PhotoImage('/Users/babadialo/Documents/python/wing/gui/lightning.jpg')
but_2 = Button(top_win, text='UpdateDevices',width = 20, height = 2, highlightbackground = 'blue', command = run_devicesupdate)
#but_2.place(x=120, y=2)
but_2.pack(side = LEFT, anchor = NE)


but_3 = Button(top_win, text='chrome', width = 25, height = 2, state = DISABLED, command = run_chrome)
#but_3.place(x=305, y=2)
but_3.pack(side = LEFT, anchor = NE) # place the button better than place() method

 

top_win.mainloop()