from tkinter import *
root = Tk()
root.title('Painting!')
root.geometry('300x200')
root.resizable(True, True)

T = Text(root, width=50, height = 20)
T.insert('1.0', 'EnTeR uR gOdDaM bIrThDaY(YYYY-MM-DD):\nEnTeR yOuR nAmE:\nEnTeR yOuR pHoNe NuMbEr:')
words_on_line_1 = T.get('1.0', 'end')
print(words_on_line_1)
T.pack()
root.mainloop()