'''
Paint App Project
Author:
Date:

[Project Description]
 
'''

from tkinter import *

''''
Your window has been created for you.
TODO:
- create your frame
- create your canvas

'''
root = Tk()
root.title('Paint')

'''
This project will use some global variables.
COLOUR represents the current colour being used, and
SIZE is the current size of the paintbrush.
'''
COLOUR = 'black'
SIZE = 10

class ColourButton():
     '''
     A ColourButton is the class for the buttons at the
     top of the screen that change the brush colour.
     '''
     def __init__(self, parent, colour):
          '''
          This is the function called when creating a ColourButton.
          TODO:
          - fill in the line indicated below.
          '''
          self.colour = colour
          self.Button = #FILL IN
     
     def update(self):
          '''
          This is the method that is the command for a ColourButton.

          When a ColourButton is pressed, it must ONLY change the global COLOUR
          variable to be this ColourButton's colour attribute/
          TODO:
          - fill in this function. It should be 2 lines.
          '''
          pass
     
def draw_circle(event):
    '''
    This function is called whenever the user is dragging their mouse on the
    canvas. Use the canvas method 'createoval' to draw a circle there.
    Remember to refer to your global variables to draw the correct circle.
    TODO:
    - finish this function (should be 1-2 lines)
    '''
    
def clear_canvas():
    '''
    This function is called whent the user presses the CLEAR button.
    It must clear all drawings from the canvas.
    TODO:
    - finish this function (1 line)
    '''

#################### MAIN CODE #########################

'''
Here we first are making the ColourButtons. We will do this in a quick
and expandable way using a list. Add all the colours you want buttons for
to the list 'colours'.
The for loop will create the ColourButton objects.
TODO:
- add at least 4 more colours to the colours list
'''

colours = ['red']
for i in range(len(colours)):
    x = ColourButton(colours[i])
    x.Button.grid(row=0, column=i)

'''
Next create the CLEAR button and the width slider.

TODO:
- complete the code fragments below
'''
clear_button = # FILL IN
clear_button.grid(row = 0, column = i + 1)

SIZE = IntVar() # We are using the global variable as the int var so it is always updated
scalebar = # Fill in - there are many ways to do this
scalebar.grid(row = 0, column = i + 2)

'''
TODO:
- bind the event of mouse button held down while moving ON THE CANVAS to the draw_circle function
- bind the letter q to quitting the program
- mainloop!
'''
