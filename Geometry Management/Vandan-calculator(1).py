'''
Calculator Builder - Starter Code
Author:Vandan
Date: May 23, 2024

[Project Description]

'''
"""
TODO:
SETUP
1. Draw out your calculator on paper - think about what buttons should be included and how to arrange them
    MUST INCLUDE: 0,1,2,3,4,5,6,7,8,9,+,-,*,/, CLEAR, =, DEL (or DELETE or BACKSPACE)
    OPTIONAL: any buttons you choose, like on OFF button linked to root.quit()
2. From this drawing determine what row and column each button should be placed in
3. Pick out a colour-scheme so that your design is attractive

CODING
1. Create a Label that uses the 'expression' StringVar as its textvariable
2. Customize the CalcButton class so that creating your Buttons is easy and standardized
    2.1 Add more parameters to the __init__ function so your buttons can be created inside it
    2.2 Set the 'command' for your Buttons to be 'self.onClick' so that you can use the premade functions
3. Create a Label that uses the 'expression' StringVar as its textvariable - this is the top of the calculator where the expression appears
4. Create your Buttons using the CalcButton class. Some buttons you may want to create without it, especially if they have special commands.
    4.1 Your '=' button, for example, should have its command set to the 'evaluate' function instead
    4.2 Your 'CLEAR' button should have its command set to the 'clear' function

"""


from tkinter import *
root = Tk()
expression = StringVar()
root.title('Calcuator')


class CalcButton():
    def __init__(self, frame, char, bgcol, fgcol, row, col, command=None):  # add extra parameters
        
        # this should be the character on the button, like '2' or '+' as a one character string
        self.char = char

        if command == None:
            command = self.onClick

        self.obj = Button(frame, text=char, bg=bgcol, fg=fgcol, relief='raised', command=command)  # create your Button and store it as the 'obj' instance variable
        self.obj.grid(row=row, column=col, sticky='news')
        # are there any other pieces of information a button should store?

    def onClick(self):
        """
        This function simply adds this buttons character to the expression
        """
        expression.set(expression.get() + self.char)


def clear():
    """
    Clears the expression.
    """
    expression.set('')


def delete():
    """
    Removes the last character in expression.
    """
    expression.set(expression.get()[:-1])

def evaluate():
    """
    Calls the built-in function 'eval' which will evaluate a string according to Pythons evauation rules.
    Replaces the existing expression with the result of evaluating the expression.
    strip() removes any trailing whitespace (spaces or newline characters) since eval does not like them.
    Examples:
    eval('3+4') -> '7'
    eval('3 - 3 + 3 + 56') -> '59'              # spaces between numbers are optional
    eval('-2 * 6') -> '-12'                     # do not use 'x' for multiplication, must be '*'
    """
    expression.set(str(eval(expression.get().strip())))

# Create your frames and label here
mainframe=Frame(root, bg='grey', padx=10, pady=15)
mainframe.grid(row=0, column=0, rowspan=4, columnspan=4, sticky='news')

F1 = Label(mainframe, bg='white', fg='black', textvariable=expression,justify='right', relief='sunken', width=mainframe.winfo_width())
F1.grid(row=0, column=0, columnspan=5, sticky='news')

F2 = Frame(mainframe, bg='light grey', relief='flat', padx=5, pady=5)
F2.grid(row=1, column=0, columnspan=4, sticky='ew')

F3 = Frame(mainframe, bg='light grey', relief='flat', padx=5, pady=5)
F3.grid(row=2, column=0, rowspan=4, columnspan=4, sticky='news')


CalcButton(F3, '7', 'orange', 'white', 0, 0)
CalcButton(F3, '8', 'orange', 'white', 0, 1)
CalcButton(F3, '9', 'orange', 'white', 0, 2)
CalcButton(F3, '4', 'orange', 'white', 1, 0)
CalcButton(F3, '5', 'orange', 'white', 1, 1)
CalcButton(F3, '6', 'orange', 'white', 1, 2)
CalcButton(F3, '3', 'orange', 'white', 2, 0)
CalcButton(F3, '2', 'orange', 'white', 2, 1)
CalcButton(F3, '1', 'orange', 'white', 2, 2)
CalcButton(F3, '0', 'orange', 'white', 3, 0)
CalcButton(F3, '.', 'red', 'white', 3, 1)
CalcButton(F3, '=', 'red', 'white', 3, 2, command=evaluate)
CalcButton(F3, '+', 'red', 'white', 3, 3)
CalcButton(F3, '-', 'red', 'white', 2, 3)
CalcButton(F3, '*', 'red', 'white', 1, 3)
CalcButton(F3, '*', 'red', 'white', 0, 3)
CalcButton(F2, 'OFF', 'dark grey', 'black', 0, 0, command=root.quit)
CalcButton(F2, 'CLR', 'dark grey', 'black', 0, 1, command=clear)
CalcButton(F2, 'DEL', 'dark grey', 'black', 0, 2, command=delete)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(1, weight=1)

for i in range(3):
    mainframe.rowconfigure(i, weight=1)
    mainframe.columnconfigure(i, weight=1)

F2.rowconfigure(0, weight=0)
for i in range(3):
    F2.columnconfigure(i, weight=1)
for i in range(4):
    F3.rowconfigure(i, weight=1)
    F3.columnconfigure(i, weight=1)
root.mainloop()