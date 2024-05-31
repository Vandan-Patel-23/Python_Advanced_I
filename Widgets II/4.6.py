from tkinter import *

root=Tk()

listvar = StringVar(value = ('Python', 'Java', 'Javascript', 'C++'))
listbox = Listbox(root, listvariable = listvar, height = 5,selectmode='extended')
listbox.curselection()
listbox.config(state = 'disabled')
listbox.pack()

scroller = Scrollbar(root, orient = VERTICAL)
listvar = StringVar(value = (0,1,2,3,4,5,6,7,8,9,10))
listbox = Listbox(root, listvariable = listvar, height = 3,yscrollcommand=scroller.set)
scroller.config(command = listbox.yview)

# scroller.grid(row = 0, column=1, rowspan=2)
# listbox.grid( row = 0, column=0)

scroller.pack(side = RIGHT, fill = Y)
listbox.pack(side = LEFT)

textbox = Text(root, width = 50, height = 20, background = 'yellow')
textbox.insert('1.0','Type anything u want\n')
words_on_line_1 = textbox.get('1.0', 'end')
print(words_on_line_1)
textbox.pack()

var = IntVar()
scalebar = Scale(root, variable = var, bg = 'red', tickinterval=10,
resolution = 1, orient = HORIZONTAL, from_ = 50, to = 80)
scalebar.pack()
root.mainloop()