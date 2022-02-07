#!/usr/bin/env python3

# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&index=2
# video 1:27:43/



from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Apple is best')

# puting the icone on the left up corner of the window.
root.iconbitmap('/Users/babadialo/Documents/python/wing/gui/apple.ico')


# put in the image in our program
my_image = ImageTk.PhotoImage(Image.open('/Users/babadialo/Documents/python/wing/gui/lightning.jpg'))
my_label = Label(image=my_image)
my_label.pack()

# puting the exit button.
button_quit = Button(root, text = 'Exit Program', command = root.quit)
button_quit.pack()




















root.mainloop()
