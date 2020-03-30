import random
import os
import tkinter as tk
from PIL import Image,ImageTk
from pathlib import Path



CurrentPath = str(Path().absolute())


#Creation of GUI frame
root = tk.Tk()
root.title("Dice Rolling Application")
root.iconbitmap(CurrentPath + "/Images/CND.ico")

canvas = tk.Canvas(root, height =300, width = 700)
image = ImageTk.PhotoImage(Image.open(CurrentPath + "/Images/MainBackground.jpg"))
canvas.create_image(0,0,anchor="nw",image=image)
canvas.pack()



def ValidRoll(rollData):
    #Consumes a variable. Returns True if it is a positive integer. Returns False Otherwise.
    isValid = False
    

    if isinstance(rollData, str):
        if rollData.isdigit():
            rollData = int(rollData)


    if isinstance(rollData, int):
        if rollData > 0:
            isValid = True
    
    if isValid:
        return True
    else:
        return False

def ValidMod(mod):
    try:
        int(enterMod.get())
        return True
    except:
        return False
            

def roll(sumBool):
    #Consumes a boolean. If False the array of rolled dice are displayed on the screen. If True the sum of the rolled dice array is displayed instead.
    dieRolls = []
    mod = 0

    if ValidMod(enterMod.get()):
            mod = int(enterMod.get())

    if not ValidRoll(enterSidesDice.get()):
        dieSize = "Please Enter the Number of Sides"
    else:
        dieSize = int(enterSidesDice.get())
        
    if not ValidRoll(enterNumDice.get()):
        dieNum = "Please Enter the Number of Rolls"
    else:
        dieNum = int(enterNumDice.get())

    if not sumBool and ValidRoll(dieNum) and ValidRoll(dieSize):
        i = 0
        
        while(i < dieNum):
            if(dieSize > 0):
                currRoll = random.randint(1,dieSize) + mod
                if currRoll < 1:
                    currRoll = 1
                dieRolls.append(currRoll)
            i = i + 1
        dispText = ', '.join(map(str,dieRolls))


    elif sumBool and ValidRoll(dieNum) and ValidRoll(dieSize):
        i = 0
        sum = 0

        while(i < dieNum):
            currRoll = random.randint(1,dieSize) + mod
            if currRoll < 1:
                    currRoll = 1
            sum = sum + currRoll
            dieRolls.append(currRoll)
            i = i + 1
        dispText = str(sum)
    
    else:
        dispText = "Please Fill the Required Boxes"
    
    label['text'] = dispText




#Label Creation
label1 = tk.Label(root, text = " Number of Rolls ", bg = "light grey", font = ('Helvetica', 12, 'bold'))
canvas.create_window(200, 100, window=label1)

label2 = tk.Label(root, text = "Sides on the Dice", bg = "light grey", font = ('Helvetica', 12, 'bold'))
canvas.create_window(200, 150, window=label2)

label3 = tk.Label(root, text = "   Enter Modifier   ", bg = "light grey", font = ('Helvetica', 12, 'bold'))
canvas.create_window(200, 200, window=label3)

#Entry Panels
enterNumDice = tk.Entry(root)
canvas.create_window(350, 100, window = enterNumDice)

enterSidesDice = tk.Entry(root)
canvas.create_window(350, 150, window = enterSidesDice)

enterMod = tk.Entry(root)
canvas.create_window(350, 200, window = enterMod)


#Instruction Label
label = tk.Label(root, text = "Please Fill the Required Boxes")
canvas.create_window(350, 275, window=label)


#Clickable Buttons
rollButton = tk.Button(text='Roll The Dice', command=lambda: roll(False), bg = "grey")
canvas.create_window(500, 100, window=rollButton)

rollSumButton = tk.Button(text='Roll and Sum The Dice', command=lambda: roll(True), bg = "grey")
canvas.create_window(500, 150, window=rollSumButton)




root.mainloop()