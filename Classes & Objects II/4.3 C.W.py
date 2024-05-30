import random as r
from tkinter import *
root=Tk()
class Fly():
    img =PhotoImage(file = "small_fly.png")
    def __init__(self, x, y):
        self.x = x # we do this because we want to store these values
        self.y = y
        self.obj = c.create_image(x,y, image = Fly.img)

first_fly = Fly(100,100) # first_fly's x = 100, y = 100
second_fly = Fly(200,100) # this fly's x = 200, y = 100
# this is how I can access class attributes:
a = Fly.img # by calling on the Class itself or…
b = first_fly.img # any instance of the class
print(a == b) # this is True, all flies use the same image
# this is how I can access instance attributes
c = first_fly.x # this gets the value 100 because of initialization on first line
d = second_fly.x # this gets the value 200
second_fly.x = 50 # this changes the value! Remember these are just variables

def destroy_fly(self): # a particular fly will have this called on itself
    c.delete(self.obj) # THAT FLY will have itself destroyed
    print('Got one!')

class Bug():
    def __init__(self, x, y, bug_image):
        self.x = x
        self.y = y
        self.obj = c.create_image(x,y, image = bug_image)
        c.tag_bind(self.obj, '<ButtonPress-1>', self.destroy)
    def destroy(self, event): # ignore the 'event' parameter, we will learn later
        c.delete(self.obj)
        print('Got one!')

class Fly(Bug): # Notice the Bug in brackets! Parent class goes between brackets
    img = PhotoImage(file = 'small_fly.png')
    def __init__(self, x, y):
        super().__init__(x, y, Fly.img )
class LadyBug(Bug):
    img = PhotoImage(file='small_ladybug.png')
    def __init__(self, x, y):
        super().__init__(x, y, LadyBug.img )

for i in range(10):
    Fly(r.randrange(0,400), r.randrange(0,400))
    LadyBug(r.randrange(0,400), r.randrange(0,400))
Tk.mainloop()