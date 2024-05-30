from tkinter import *
root = Tk()

title = Label(root, bg = 'black', fg = 'white', text = 'Title')
title.grid(row = 0, column = 0, columnspan= 4, sticky = 'ew')
b1 = Button(root, bg = 'red', fg = 'white', text = 'Left Button')
b2 = Button(root, bg = 'green', fg = 'white',text = 'Very Very Long Text Button')
b3 = Button(root, bg = 'blue', fg = 'white', text = 'Right Button')
b1.grid(row = 1, column = 0, sticky = 'w')
b2.grid(row = 1, column = 1, sticky = 'w')
b3.grid(row = 1, column = 2, sticky = 'w')
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)
root.mainloop()