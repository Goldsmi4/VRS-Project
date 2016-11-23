'''
immune system simulator
simulates how the immune system interacts with foreign bodys
created with Tkinter
author: William escobar parra, Tim Goldsmith, Mathew Glaysher and Freddie Dugdale
'''
import turtle
import tkinter
import tkinter.messagebox
import random
import threading
import math


#                                                                          #
#                                                                          #
#                                                                          #
############################################################################


#Set up screen/ window 
window = turtle.Screen()
window.bgcolor("grey")
window.tracer(2) #this will skip frames, allowing program to run slightly faster


# here the turtle is created
user= turtle.Turtle()
user.shape('triangle')
user.color('red')
user.speed=0
user.penup()

#drawring boarder, preventing turtle from losing itself
borderGuide=turtle.Turtle()
borderGuide.color('white')
borderGuide.penup()
borderGuide.setpos(-350,-350)
borderGuide.pendown()
borderGuide.pensize(4)

for x in range (4):
    borderGuide.forward(700)
    borderGuide.left(90)

borderGuide.hideturtle()


#turtle speed  value is set
turtleSpeed=1

 
#wasd movement functions defined
def turnLeft():
    user.setheading(user.heading()+30)
    print(user.heading())        
def turnright():
    user.setheading(user.heading()-30)
    print(user.heading())
def speedIncrease():
    global turtleSpeed
    turtleSpeed+=1

def changeShape():
    #tried to make the user turtle cycle through shapes by pressing space, it changes once but never again
    if user.shape("circle"):
        user.reset
        user.shape("square")
        user.colour("green")
    elif user.shape("triangle"):
        user.reset
        user.shape("circle")
        user.color("green")
    elif user.shape("square"):
        user.reset
        user.shape("triangle")
        user.color("green")

        
#keyboard bindings
turtle.onkey(speedIncrease, 'w')
turtle.onkeypress(turnLeft,"a")
turtle.onkeypress(turnright,"d")
turtle.onkey(changeShape,"space")
turtle.listen()

#cloning multiple turtles 
maxPathogens=20
turtles=[]


for count in range(maxPathogens):
    
    #pathogen creation
    turtles.append(turtle.Turtle())    
    turtles[count].speed(0)
    turtles[count].penup()
    turtles[count].setposition(random.randint(-350,350),random.randint(-350,350))
    turtles[count].color("orange")
    turtles[count].shape("triangle")
#creating score board display
userScore= 0



#math calculation to calculate collision

def collisionCheck(tur1,tur2):
    
    x= math.sqrt(math.pow(tur1.xcor()-tur2.xcor(),2))
    y= math.pow(tur1.ycor()-tur2.ycor(),2)
    #pythagoras theorem,change in x coordinate squared
    #plus the change in y squared
    d=x+y
    if d<19:
        return True
    else:
        return False

       
while True:
    user.forward(turtleSpeed)
    

    #setting up x,y coordinates for boundary checking
    if user.xcor()>350 or user.xcor()<-350:
        user.right(180)
        #attempted to get the user turtle to bouce off the boundary realistically
        #if user.heading()
        
        #user.right(360 - user.heading())
        #print(user.heading())
    #boundary checking the y coordinates
    if user.ycor()>350 or user.ycor()<-350:
        user.right(180)




        #allows the movement of multiple pathogens/turtles
        
    for count in range (maxPathogens):
        turtles[count].forward(2)
            
        #setting up x,y coordinates for boundary checking
        if turtles[count].xcor()>350 or turtles[count].xcor()<-350:
            turtles[count].right(180)
                
        #boundary checking the y coordinates
        if turtles[count].ycor()>350 or turtles[count].ycor()<-350:
            turtles[count].right(180)


    #if collision occurs, this will take turtle to a random spot
        if collisionCheck(user,turtles[count]):
            if turtles[count].color("green"):
               turtles[count].setposition(random.randint(-350,350),random.randint(-350,350))                                              
               turtles[count].right(random.randint(0,360))
               userScore = userScore - 2
            else:
                turtles[count].setposition(random.randint(-350,350),random.randint(-350,350))                                              
                turtles[count].right(random.randint(0,360))#turtle will start in random location and movement every time
                turtles[count].color("green")
                turtles[count].shape("circle")
                userScore = userScore + 1
            
            
            #show user score on screen using the borderGuide turtle
            borderGuide.undo()
            borderGuide.penup()
            borderGuide.hideturtle()
            borderGuide.setposition(-300,320)
            #userScore="current score: %s" %userScore
            borderGuide.write("current score: "+ str(userScore), move=False, align="left", font=("comic", 15, "bold"))
