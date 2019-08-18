#simple random number game showing tkinter
#the code is rather self-explanatory
from tkinter import *
import random

window = Tk()
window.title("Choose button")
window.geometry("400x300")

def insertButtons():
    buttonQuantity = 3
    global buttons
    buttons = []
    good = random.randint(0,buttonQuantity-1)
    for i in range (buttonQuantity):
        if i == good:
            buttons.append(Button(window,text = "Click me!", command = target))
        else:
            buttons.append(Button(window,text = "Click me!", command = missed))

    for i in buttons:
        i.pack(fill=BOTH, expand = YES)

def target():
    for i in buttons:
        i.destroy()
    global finalLabel
    finalLabel = Label (window, text = "You hit the target!")
    finalLabel.pack(fill = BOTH, expand = YES)
    window.after(2000, restart)

def missed():
    for i in buttons:
        i.destroy()
    global finalLabel
    finalLabel = Label (window, text = "You missed the target!")
    finalLabel.pack(fill = BOTH, expand = YES)
    window.after(2000, restart)

def restart():
    finalLabel.destroy()
    insertButtons()

insertButtons()
