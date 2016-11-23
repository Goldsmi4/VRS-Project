"""
Immune system simulator start menu
"""
from tkinter import *

startWin=Tk()           #start menu window
window=Tk()            #game window

window.withdraw()      #temporally hides game window 

def newWin():
    window.deiconify()          #exposes game window
    startWin.withdraw()         #hides start menu window

def credit():
    f=open('Credits.txt')
    t.insert(1.0, f.read)

def closeWin():
    startWin.quit()
    startWin.destroy()

firstB = Button(text='Start Game', command=newWin)      #opens game
firstB.pack()

secondB = Button(text='Credits', command=credit)        #opens credits.txt file
secondB.pack()

lastB = Button(text='Exit Game', command=closeWin)      #Closes menu window
lastB.pack()

startWin.mainloop()
