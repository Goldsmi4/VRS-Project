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
    f.insert(1.0, f.read)       #currently broken (doesnt display file)
    
    
    
    root.mainloop()



def closeWin():
    startWin.quit()
    startWin.destroy()

firstB = Button(text='Start Game', command=newWin)
firstB.pack()

secondB = Button(text='Credits', command=credit)
secondB.pack()

lastB = Button(text='Exit Game', command=closeWin)
lastB.pack()

startWin.mainloop()
