import random
import os
import tkinter as tk
from PIL import Image,ImageTk
from pathlib import Path



CurrentPath = str(Path().absolute())



def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def ValidRoll(sides,rolls):
    isValid1 = False
    isValid2 = False

    if type(sides) == int:
        if sides > 0:
            isValid1 = True
    if type(rolls) == int:
        if rolls > 0:
            isValid2 = True
    if isValid1 == True and isValid2 == True:
        return True
    else:
        return False



def roll():

    dieRolls = []

    if( not isInt(enterSidesDice.get()) ):
        dieSize = "Please Enter the Number of Sides"
    else:
        dieSize = int(enterSidesDice.get())
    if( not isInt(enterNumDice.get()) ):
        dieNum = "Please Enter the Number of Rolls"
    else:
        dieNum = int(enterNumDice.get())

    if ValidRoll(dieNum,dieSize):
        i = 0
        while(i < dieNum):
            if(dieSize > 0):
                currRoll = random.randint(1,dieSize)
                dieRolls.append(currRoll)
            i = i + 1
        dispText = ', '.join(map(str,dieRolls))

    else:
        dispText = "Please Enter a Positive Integer in Both Boxes"
    label['text'] = dispText


def rollSum():

    dieRolls = []
    sum = 0

    if( not isInt(enterSidesDice.get()) ):
        dieSize = "Please Enter the Number of Sides"
    else:
        dieSize = int(enterSidesDice.get())
    if( not isInt(enterNumDice.get()) ):
        dieNum = "Please Enter the Number of Rolls"
    else:
        dieNum = int(enterNumDice.get())

    if ValidRoll(dieNum,dieSize):
        i = 0
        while(i < dieNum):
            currRoll = random.randint(1,dieSize)
            sum = sum + currRoll
            dieRolls.append(currRoll)
            i = i + 1
        dispText = sum

    else:
        dispText = "Please Enter a Positive Integer in Both Boxes"
    label['text'] = dispText


root = tk.Tk()
root.title("Dice Rolling Application")
root.iconbitmap(CurrentPath + "/Images/CND.ico")

canvas = tk.Canvas(root, height =300, width = 700)
image = ImageTk.PhotoImage(Image.open(CurrentPath + "/Images/MainBackground.jpg"))
canvas.create_image(0,0,anchor="nw",image=image)
canvas.pack()


label1 = tk.Label(root, text = "Sides on the Dice", bg = "light grey", font = ('Helvetica', 12, 'bold'))
canvas.create_window(200, 100, window=label1)

label1 = tk.Label(root, text = "Number of Rolls", bg = "light grey", font = ('Helvetica', 12, 'bold'))
canvas.create_window(500, 100, window=label1)

enterSidesDice = tk.Entry(root)
canvas.create_window(200, 150, window = enterSidesDice)

enterNumDice = tk.Entry(root)
canvas.create_window(500, 150, window = enterNumDice)

label = tk.Label(root, text = "Please Enter a Positive Integer in Both Boxes")
canvas.create_window(350, 200, window=label)




    
    

rollButton = tk.Button(text='Roll The Dice', command=roll, bg = "grey")
canvas.create_window(350, 100, window=rollButton)

rollSumButton = tk.Button(text='Roll and Sum The Dice', command=rollSum, bg = "grey")
canvas.create_window(350, 150, window=rollSumButton)




root.mainloop()