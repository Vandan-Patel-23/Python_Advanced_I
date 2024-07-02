'''
To-Do List App - STARTER
Author:
Date:

[Project Description]

'''

'''
TODO:
1. Draw out your app on paper! Choose a colourscheme and your widget arrangement.
2. Set up your window and create your frames. (under class definitions)
3. Fill out the Classes, following the commented instructions

    Classes and other outlines are just suggestions! If you find it more complicated
    to follow this structure than make your own - go ahead and make your own or change
    the classes here!

4. Configure rows and columns (under frame and label creation)
5. Modify layout to make it look nice!
6. Test it out!
    - Ensure that progress bar resizes with window
    - Ensure that progress bar is accurate (should be 2/3 full if there are 3 items, 2 checked off)
7. Clean up your code! Check to make sure all your instance variables are actually necessary, etc.

'''

'''
EXTRAS THAT WILL BE HELPFUL:

root.winfo_width() <- returns current width of the window
[Canvas].winfo_width() <- returns current width of chosen Canvas
winfo_height() will do the same for current height
'''

from tkinter import *
root = Tk()
# Configure root here, give it a title, start size, resizability, etc.
root.title('TODO List')

class ProgressBar():
    def __init__(self):
        '''
        Customize this with the info needed to make your progress bar!
        '''
        pass

    def resize(self):
        '''
        An additional method could be useful for updating the progress bar
        when a new item is added or an item is checked/unchecked.

        This method can also handle the resizing necessary when the window
        changes size, or you can handle that seperately.

        '''
        pass


class ListItem():
    '''
    Items of this class are the entire line in your To-Do List.
    They contain the Entry (for the user to type their list item),
    the Checkbutton (created once Entry is destroyed),
    and can contain your Trashcan Button if you choose to make one.
    '''

    def __init__(self):
        # Set up any instance attributes here

        # Create a StringVar for your Entry, give it some default text
        # Create a StringVar for your Checkbutton, empty
        # Create an IntVar for your Checkbutton (to keep track of its state)

        # Create your Checkbutton   <- Could do this in replace_entry instead if you want
        # Grid your Checkbutton     <-

        # Handle event binding
        # - when Entry clicked -> default text should disappear
        # - when User is using Entry and hit Return Button -> Entry should disappear and be replaced with Checkbutton
        # - when Checkbutton is checked/unchecked -> progress bar should update

        # May need to do some row configuration here, since each ListItem is on a new row
        pass

    def clear_entry(self):
        '''
        Clears the default text out of the Entry
        '''
        pass

    def replace_entry(self):
        '''
        Destroys Entry and replaces with Checkbutton
        '''
        pass

    def checkbox_update(self):
        '''
        Update required variables when boxes are checked/unchecked, trigger progress bar change.
        '''
        pass


# Create basic necessary Frames

# Create Labels

# Create first ListItem

# Create Canvas to hold ProgressBar and ProgressBar

# Configure rows and columns - for the root, and each frame as necessary!

root.mainloop()
