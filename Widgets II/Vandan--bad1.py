from tkinter import *
root = Tk()
root.title('Painting')
root.geometry('300x200')
root.resizable(True, True)


T = Text(root, width=50, height = 20, background= 'black', foreground='white')
T.insert('1.0', 'Enter ur goddam birthday(YYYY-MM-DD)\n')
words_on_line_1 = T.get('1.0', 'end')
print(words_on_line_1)
T.pack()


var = IntVar()
scalebar = Scale(root, variable = var, bg = 'red', tickinterval=10000000,
resolution = 1, orient = HORIZONTAL, from_ = 1000000000, to = 9999999999)
scalebar.pack()
root.mainloop()

listvar = StringVar(value = ('James', 'Michael', 'Robert', 'John', 'David', 'William', 'Richard', 'Joseph', 'Thomas', 'Thomas','Other'))
listbox = Listbox(root, listvariable = listvar, height = 10,selectmode='extended')
if listbox == 'Other':
    print('LOL UR NAME IS NOT COMMON HAHAHAHHA')
listbox.pack()
