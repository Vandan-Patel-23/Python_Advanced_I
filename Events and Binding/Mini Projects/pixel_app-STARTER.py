'''
Pixel Art Application
Author:
Date:

[Project Description]

Read through the WHOLE FILE before beginning.
The comments explain the project and guide you.
There will be a 'TODO' anywhere there is a section of code for you to fill in.


'''
from tkinter import *

root = Tk()
root.title('Pixel Art')
root.geometry('600x700')

# Variables
X_PIX = 20
Y_PIX = 20
PIX_SIZE = int(400 / X_PIX)
COLOUR = 'BLACK'
PIXEL_GRID = [[0 for _ in range(X_PIX)] for _ in range(Y_PIX)]
LINES_ON = True

class Pixel():
    def __init__(self, x1, y1):
        self.fill = COLOUR
        self.outline_colour = 'white'
        x2, y2 = x1 + PIX_SIZE, y1 + PIX_SIZE
        # Create a rectangle (pixel) on the canvas
        self.obj = c.create_rectangle(
            x1, y1, x2, y2, fill=self.fill, outline='white')

    def fill_colour(event):
        # Change the color of the selected pixel
        chosen_pixel = c.find_closest(event.x, event.y)[0]
        c.itemconfig(chosen_pixel, fill=COLOUR)
        # If grid lines are off, update the outline to match the fill color
        if not LINES_ON:
            c.itemconfigure(chosen_pixel, outline=COLOUR)


    def outline(self, show_lines):
        if show_lines:
            c.itemconfig(self.obj, outline='white')
        else:
            clr = c.itemcget(self.obj, 'fill')
            c.itemconfig(self.obj, outline=clr)

class ColourButton():
    def __init__(self, parent, colour):
          self.colour = colour
          self.Button = Button(parent, bg=colour, command=self.update)
     
    def update(self):
          global COLOUR
          COLOUR = self.colour

def draw_grid():
    global PIXEL_GRID
    for row in range(Y_PIX):
        for col in range(X_PIX):
            PIXEL_GRID[row][col] = Pixel(col * PIX_SIZE, row * PIX_SIZE)


def toggle_lines():
    global LINES_ON
    LINES_ON = not LINES_ON
    for row in PIXEL_GRID:
        for p in row:
            p.outline(LINES_ON)

def clear_pixels():
    for row in PIXEL_GRID:
        for p in row:
            c.delete(p.obj)

############### MAIN CODE ###############




# PIXEL_GRID is a global variable that will be updated so it always reflects the current state of the grid


menu_bar = Frame(root)
menu_bar.pack(fill=X)

width_label = Label(menu_bar, text='Width:')
width_label.pack(side=LEFT)
width_entry = Entry(menu_bar)
width_entry.pack(side=LEFT)
width_entry.insert(0, str(X_PIX))

height_label = Label(menu_bar, text='Height:')
height_label.pack(side=LEFT)
height_entry = Entry(menu_bar)
height_entry.pack(side=LEFT)
height_entry.insert(0, str(Y_PIX))

def set_dimensions():
    # Set the new dimensions and redraw the grid
    global X_PIX, Y_PIX
    X_PIX = int(width_entry.get())
    Y_PIX = int(height_entry.get())
    clear_pixels()
    draw_grid()

set_dimensions_button = Button(menu_bar, text='Set Dimensions', command=set_dimensions)
set_dimensions_button.pack(side=LEFT)

toggle_lines_button = Button(menu_bar, text='Toggle Grid Lines', command=toggle_lines)
toggle_lines_button.pack(side=LEFT)

clear_button = Button(menu_bar, text='Clear', command=clear_pixels)
clear_button.pack(side=LEFT)

colour_bar = Frame(root)
colour_bar.pack(side=TOP,fill=X)
colours=['red','orange','yellow','green','blue','purple','white','grey','brown','black','pink']

# This loops over the list, creating and placing colour buttons
for colour in colours:
    x = ColourButton(colour_bar, colour)
    x.Button.pack(side=LEFT)


c=Canvas(root, width=400, height=400, bg=COLOUR)
c.pack()
draw_grid()
c.bind('<B1-Motion>', Pixel.fill_colour)

root.mainloop()