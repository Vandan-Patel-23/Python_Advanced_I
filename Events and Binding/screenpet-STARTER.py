'''
Project: Screen Pet
Author:
Date

[Project Description]

'''

'''
TODO:
1. Copy over your screen pet drawing here to animate it! (Or you can make a new one if you wish)
2. Decide on at least 3 events and their corresponding actions
    EXAMPLES
    - Draw a set of closed eyes, and opened eyes. Pet blinks automatically. Pet winks if eyes clicked.
    - Draw an exaggerated smile. Pet switched mouth to smile if user moves mouse over face.
    - On activation (when window is created) Pet smiles / Any action
    - A pet's feature (ex. nose, ears) changes colour when clicked
'''

'''
HOW TO CREATE ALTERNATE VERSIONS:
1. Create a variable storing version 1, set state to NORMAL
2. Create a variable storing version 2, set state to HIDDEN
    This will create the object, but not place it on the screen.

HOW TO SWITCH BETWEEN THE VERSION:
1. Create a function that toggles
    1.1. Figure out which version is currently in use
        - do this using a global variable that keeps track of this OR
        - fetch the current state of the canvas object involved ex. if the variable for verson 1's state is HIDDEN (using c.itemcget function)
    1.2  Switch the state for the version in use to HIDDEN
    1.3  Switch the state for the other version to NORMAL - if using a global variable, change it now
2. Ensure this function is bound to the appropriate event
(EXAMPLE GIVEN - crossed and uncrossed version of eyes)

'''

'''
HOW TO MAKE ACTIONS OCCUR AUTOMATICALLY - TIMED
If you want func_a function to happen every second, in the function definition, write
root.after(1000, func_a) <- this tells the root to call this function again after 1000 milliseconds
Ensure function is called once in the main code.
(EXAMPLE GIVEN - crossing and uncrossing eyes is done automatically)

'''


from tkinter import *
root = Tk()

c = Canvas(root, width=600, height=600, bg='light blue')
crossed = False  # Starting out with uncrossed eyes
c=Canvas(root, height=600, width=600, bg='yellow')
c.create_rectangle(50, 50, 550, 550, fill="light blue",tags=('frame'))
c.create_polygon(210, 285, 188, 230, 210, 210, 260, 225, fill='brown', tags=('corossed ears'))
c.create_polygon(390, 285, 412, 230, 390, 210, 340, 225, fill='brown', tags=('crossed ears'))

c.create_polygon(210, 285, 188, 230, 210, 210, 260, 225, fill='brown')
c.create_polygon(390, 285, 412, 230, 390, 210, 340, 225, fill='brown')
c.create_polygon(390, 285, 412, 230, 405, 225, 385, 245, fill='white', tags=('inside ear'))
c.create_polygon(210, 285, 188, 230, 195, 225, 215, 245, fill='white', tags=('inside ear'))
c.create_oval(200, 200, 400, 400, fill="brown", tags=('head'))
c.create_line(300, 350, 325, 370, tags=('mouth'))
c.create_line(300, 350, 275, 370, tags=('mouth'))
c.create_oval(245, 280, 295, 330, fill='white', tags='pupil')
c.create_oval(305, 330, 355, 280, fill='white', tags='pupil')




def toggle_eyes():
    '''
    If using a global variable, include lines like this to 
    use and check that variable

    global crossed
    if not crossed:
    '''
    # This function uses the approach of checking an object's state to determine what version is currently used
    if c.itemcget(left_eye_pupil_1, 'state') == NORMAL:
        c.itemconfigure(left_eye_pupil_1, state=HIDDEN)
        c.itemconfigure(right_eye_pupil_1, state=HIDDEN)

        c.itemconfigure(left_eye_pupil_2, state=NORMAL)
        c.itemconfigure(right_eye_pupil_2, state=NORMAL)
        '''crossed = True # this is ESSENTIAL if using the global variable approach'''

    elif c.itemcget(left_eye_pupil_2, 'state') == NORMAL:
        c.itemconfigure(left_eye_pupil_2, state=HIDDEN)
        c.itemconfigure(right_eye_pupil_2, state=HIDDEN)

        c.itemconfigure(left_eye_pupil_3, state=NORMAL)
        c.itemconfigure(right_eye_pupil_3, state=NORMAL)
        '''crossed = False'''
    elif c.itemcget(left_eye_pupil_3, 'state') == NORMAL: 
        c.itemconfigure(left_eye_pupil_3, state=HIDDEN)
        c.itemconfigure(right_eye_pupil_3, state=HIDDEN)

        c.itemconfigure(left_eye_pupil_4, state=NORMAL)
        c.itemconfigure(right_eye_pupil_4, state=NORMAL)
    else:
        c.itemconfigure(left_eye_pupil_4, state=HIDDEN)
        c.itemconfigure(right_eye_pupil_4, state=HIDDEN)

        c.itemconfigure(left_eye_pupil_1, state=NORMAL)
        c.itemconfigure(right_eye_pupil_1, state=NORMAL)
    # after 1000 milliseconds, call this function again
    root.after(1000, toggle_eyes)




# Normal pupils - the tags here haven't been used in this example but they may be helpful for other events
left_eye_pupil_1 = c.create_oval(260, 300, 290, 330, fill='black', tags=('eye', 'pupil', 'uncrossed'), state=HIDDEN)
right_eye_pupil_1 = c.create_oval(310, 300, 340, 330, fill='black', tags=('eye', 'pupil', 'uncrossed'), state=HIDDEN)

# Crossed eye pupils
left_eye_pupil_2 = c.create_oval(245, 290, 275, 320, fill='black', tags=('eye', 'pupil', 'crossed'), state=HIDDEN)
right_eye_pupil_2 = c.create_oval(305, 290, 335, 320, fill='black', tags=('eye', 'pupil', 'crossed'), state=HIDDEN)

left_eye_pupil_3 = c.create_oval(255, 280, 285, 310, fill='black', tags=('eye', 'pupil', 'crossed'), state=HIDDEN)
right_eye_pupil_3 = c.create_oval(315, 280, 345, 310, fill='black', tags=('eye', 'pupil', 'crossed'), state=HIDDEN)

left_eye_pupil_4 = c.create_oval(265, 290, 295, 320, fill='black', tags=('eye', 'pupil', 'crossed'), state=HIDDEN)
right_eye_pupil_4 = c.create_oval(325, 290, 355, 320, fill='black', tags=('eye', 'pupil', 'crossed'), state=HIDDEN)

toggle_eyes()  # function must be called once in the main code to start the automatic process


def toggle_ears():
    if c.itemcget(left_ear, 'state') == NORMAL:
        c.itemconfigure(left_ear, state=HIDDEN)
        c.itemconfigure(right_ear, state=HIDDEN)
        c.itemconfigure(right_white_thing,state=HIDDEN)
        c.itemconfigure(left_white_thing,state=HIDDEN)
        c.itemconfigure(a,state=NORMAL) 
        c.itemconfigure(b,state=NORMAL)        
    else:
        c.itemconfigure(left_ear, state=NORMAL)
        c.itemconfigure(right_ear, state=NORMAL)
        c.itemconfigure(right_white_thing,state=NORMAL)
        c.itemconfigure(left_white_thing,state=NORMAL) 
        c.itemconfigure(a,state=HIDDEN) 
        c.itemconfigure(b,state=HIDDEN)  

    root.after(1000, toggle_ears)

left_ear = c.create_polygon(188, 230, 175, 200, 210, 210, fill='brown', state=NORMAL)
right_ear = c.create_polygon(412, 230, 425, 200, 390, 210, fill='brown', state=NORMAL)

a = c.create_polygon(188, 230, 200, 260, 210, 210, fill='brown', state=HIDDEN)
b = c.create_polygon(412, 230, 400, 260, 390, 210, fill='brown', state=HIDDEN)

left_white_thing = c.create_polygon(188, 230, 175, 200, 195, 225, fill='white', state=NORMAL)
right_white_thing = c.create_polygon(405, 225, 425, 200, 412, 230, fill='white',state=NORMAL)

toggle_ears()

def blush (event): # this will be called when event happens
    event.widget.itemconfigure('a', fill = 'pink')
a1=c.create_oval(290, 330, 310, 350, fill='pink', tags=('a'))
a2= c.create_oval(240, 330, 270, 360, fill='brown', outline='brown', tags=('a'))
a3= c.create_oval(340, 330, 370, 360, fill='brown', outline='brown', tags=('a'))
c.tag_bind('a','<Enter>', blush)

def something(event):
    event.widget.itemconfigure('a', fill = 'brown')
    c.create_oval(290, 330, 310, 350, fill='pink')
c.tag_bind('a','<Leave>', something)

root.after(1000, blush)

c.pack()
root.mainloop()
