from tkinter import *
root = Tk()

root.title('Painting!')
root.geometry('300x300')
root.resizable(True, True)

mainframe = Frame(root)
mainframe.grid(row=3, column=3, columnspan=3, rowspan=3, sticky='news')

# mainframe.rowconfigure(2, weight = 1,pad=400)
# mainframe.columnconfigure(2, weight = 1,pad=400)

#1

L1= Label(mainframe, bg='light grey',text='Enter your Birthday')
L1.pack(fill=X)
# L1.grid(row=0,column=0,sticky='news')

L2= Label(mainframe, bg='dark grey',text='Enter your Name:')
L2.pack(fill=X)
# L2.grid(row=0,column=1,sticky='news')

L3= Label(mainframe, bg='light grey',text='Enter your Phone Number:')
L3.pack(fill=X)
# L3.grid(row=0,column=2,sticky='news')

listvar = StringVar(value = ('01','02','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'))
listbox = Listbox(mainframe, listvariable = listvar, height = 5, selectmode='extended')
listbox.curselection()
listbox.config(state = 'disabled')


for i in range(3):
    mainframe.rowconfigure(i, weight=1)
    mainframe.columnconfigure(i, weight=1)
root.mainloop()