import random as r
from tkinter import *
root = Tk()
c=Canvas(height=400, width=400, bg='white')
c.pack()


class Fruit():
    def __init__(self, x, y, Fruit_image):
        self.obj = c.create_image(x, y, image=Fruit_image)
        c.tag_bind(self.obj, '<Motion>', self.destroy)
        self.move()
    def destroy(self, event):
        c.delete(self.obj)
    def move(self):
        c.move(self.obj, 0, 2)
        root.after(25, self.move)

#BANANA CLASS
class Bananas(Fruit):
    img = PhotoImage(file='C:\\Users\\ucbra\\OneDrive\\Desktop\\UC Academy\\Vandan\\Python Advanced I\\Fruit Ninja\\bananas.png')
    def __init__(self, x, y):
        super().__init__(x, y, Bananas.img)

#COCONUT CLASS
class Coconut(Fruit):
    img = PhotoImage(file='C:\\Users\\ucbra\\OneDrive\\Desktop\\UC Academy\\Vandan\\Python Advanced I\\Fruit Ninja\\coconut.png')
    def __init__(self, x, y):
        super().__init__(x, y, Coconut.img)

#WATERMELON CLASS
class Watermelon(Fruit):
    img = PhotoImage(file='C:\\Users\\ucbra\\OneDrive\\Desktop\\UC Academy\\Vandan\\Python Advanced I\\Fruit Ninja\\watermelon.png')
    def __init__(self, x, y):
        super().__init__(x, y, Watermelon.img)

#BOMB CLASS
class Bomb():
    img = PhotoImage(file='C:\\Users\\ucbra\\OneDrive\\Desktop\\UC Academy\\Vandan\\Python Advanced I\\Fruit Ninja\\bomb.png')
    def __init__(self, x, y):
        self.obj = c.create_image(x, y, image = Bomb.img)
        c.tag_bind(self.obj, '<Motion>', self.destroy)
        self.move()
    def destroy(self, event):
        print('YOU HIT A BOMB!')
        root.quit()
    def move(self):
        c.move(self.obj, 0, 2)
        root.after(25, self.move)
'''
Create your Bomb class here.
The __init__ should
- create the bomb's Canvas Object and store it as an instance variable
- copy the given extra lines from the Fruit class comments
Give it a destroy method, but it should instead just
print out 'YOU HIT A BOMB', then quit the game using
'root.quit()' which closes our window.
Copy the move function from Fruit here too since it should also fall down the screen.
'''
fruits = ['bomb', 'coconut', 'watermelon', 'banana']
def new_fruit():
    for i in range(3):
        fruit = r.choice(fruits)
        if fruit == 'bomb':
            Bomb(r.randrange(0,400), r.randrange(0,1))
        elif fruit == 'watermelon':
            Watermelon(r.randrange(0, 400), r.randrange(0,1))
        elif fruit == 'banana':
            Bananas(r.randrange(0, 400), r.randrange(0, 1))
        else:
            Coconut(r.randrange(0, 400), r.randrange(0, 1))
    root.after(2000, new_fruit)

new_fruit()

root.mainloop()