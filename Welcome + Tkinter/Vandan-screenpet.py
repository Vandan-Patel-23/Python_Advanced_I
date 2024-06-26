from tkinter import *
root = Tk()
c=Canvas(root, height=600, width=600, bg='yellow')
c.create_rectangle(50, 50, 550, 550, fill="light blue",tags=('frame'))
c.create_polygon(210, 285, 175, 200, 260, 225, fill='brown',outline='black', tags=('ears'))
c.create_polygon(390, 285, 425, 200, 340, 225, fill='brown',outline='black', tags=('ears'))
c.create_polygon(390, 285, 425, 200, 385, 245, fill='white',outline='black', tags=('inside ear'))
c.create_polygon(210, 285, 175, 200, 215, 245, fill='white',outline='black', tags=('inside ear'))
c.create_oval(200, 200, 400, 400, fill="brown", tags=('head'))
c.create_line(300, 350, 325, 370, tags=('mouth'))
c.create_line(300, 350, 275, 370, tags=('mouth'))
c.create_oval(245, 280, 295, 330, fill='white', tags='pupil')
c.create_oval(305, 330, 355, 280, fill='white', tags='pupil')
c.create_oval(290, 330, 310, 350, fill='pink', tags='nose')
c.create_oval(260, 300, 290, 330, fill='black')
c.create_oval(310, 300, 340, 330, fill='black')
c.pack()
root.mainloop()