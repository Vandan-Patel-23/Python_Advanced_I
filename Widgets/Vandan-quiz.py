'''
Project Title:Personal Quiz
Author:Vandan
Date: Wednesday 24, 2024

[insert description of project and instructions for use]

'''


'''
TODO:
- fill out titleblock
- create at least 5 questions
    - each question requires:
        - it's own frame
        - a label to ask the question (in this frame)
        - a widget to get input (in this frame) ex. Button, Entry, RadioButton

- each question must use a different type of widget for input - Get creative!
- stylize the test to show off what you know! Use background and foreground
colours, alignment settings, images, frame padding etc. to make it appealing

'''


from tkinter import *
root = Tk()

# These lists will hold each of your StringVars (1 per question)
# and expected answers (1 per question)
# As you create your questions, append to these lists so that stringvars[i]
# is considered correct if it's value is equal to answers[i]



stringvars = []
answers = []
result = StringVar()
result.set("0") 

def set_blue():
    stringvars[4].set('blue')

def set_red():
    stringvars[4].set('red')

def check_answers():
    points = 0
    for i in range(len(answers)):
        if stringvars[i].get() == answers[i]:
            points += 1
    result.set(str(points))

# Add all your questions and widgets here
#Question 1
f= Frame(root,height=250,width=250,bg='purple')
f.pack()
L = Label(f,text='What do you call a person who gives you torture in coding class?',bg='white',fg='black', justify='center')
L.pack()
SV1 = StringVar()
a = Radiobutton(f, text='The Witch', variable=SV1, value='The Witch')
b = Radiobutton(f, text='Old Lady', variable=SV1, value='Old Lady')
c = Radiobutton(f, text='Ms.Shreya', variable=SV1, value='Ms.Shreya')
d = Radiobutton(f, text='The Computer', variable=SV1, value='The Computer')
a.pack()
b.pack()
c.pack()
d.pack()
answers.append('Ms.Shreya')
stringvars.append(SV1)

#Question 2
f1= Frame(root,height=250,width=250,bg='blue')
f1.pack()
L1 = Label(f1,text='  \t\t\tWhat is 100^2?\t\t\t  ',bg='white',fg='black', justify='center')
L1.pack()
SV2=StringVar()
SV3=StringVar()
SV4=StringVar()
SV5=StringVar()
a1 = Checkbutton(f1,text='200',fg='black',state='normal',variable=SV2,onvalue='200',offvalue='0')
b1 = Checkbutton(f1,text='10,000',fg='black',state='normal',variable=SV3,onvalue='10,000',offvalue='0')
c1 = Checkbutton(f1,text='4000',fg='black',state='normal',variable=SV4,onvalue='4000',offvalue='0')
d1 = Checkbutton(f1,text='50',fg='black',state='normal',variable=SV5,onvalue='50',offvalue='0')
a1.pack()
b1.pack()
c1.pack()
d1.pack()
answers.append('10,000')
stringvars.append(SV3)

#Question 3
f2= Frame(root,height=250,width=250,bg='orange')
f2.pack()
L2= Label(f2,text='How many laptops are there in this room?', bg='white',fg='black', justify='center')
L2.pack()
SV6 = StringVar()
E = Entry(root, textvariable = SV6, bg='orange')
E.pack()
answers.append('5')
stringvars.append(SV6)

#Question 4
f3= Frame(root,height=250,width=250,bg='red')
f3.pack()
L3= Label(f3,text='\tWhat is the sum of the numbers 1 to 100?\t\t', bg='white',fg='black', justify='center')
L3.pack()
SV7 = StringVar()
a2 = Radiobutton(f3, text='550', variable=SV7, value='550')
b2 = Radiobutton(f3, text='5500', variable=SV7, value='5500')
c2 = Radiobutton(f3, text='5050', variable=SV7, value='5050')
d2 = Radiobutton(f3, text='5005', variable=SV7, value='5005')
a2.pack()
b2.pack()
c2.pack()
d2.pack()
answers.append('5050')
stringvars.append(SV7)

#Question 5
f4= Frame(root,height=250,width=250,bg='light blue')
f4.pack()
SV8=StringVar()
L4= Label(f4,text='\tHow many countries in the world use fahrenheit?\t', bg='white',fg='black', justify='center')
L4.pack()
b= Button(f4, bg='blue',text='11', command=set_blue, state='normal')
b.pack()
b1= Button(f4, bg='red',text='20', command=set_red, state='normal')
b1.pack()
stringvars.append(SV8)
answers.append('blue')
# stringvars.append(SV9)
# stringvars.append(SV10)
# stringvars.append(SV11)


# # This submit button should be at the end of your test
# # It is meant to be clicked once the user has answered all questions
submitButton = Button(root, text='Submit Answers',
                      bg='white', command=check_answers)
submitButton.pack()
results = Label(root, textvariable=result)
results.pack()
# # This results label will display the number of questions answered correctly
# # Feel free to change up the code for submitButton and results to make
# # the test prettier and individualized!
# results = Label(root, textvariable=result)
# results.pack()

root.mainloop()
print(stringvars)
print(answers)