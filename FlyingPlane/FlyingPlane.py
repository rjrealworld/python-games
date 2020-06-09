import turtle
import math
import random
import os

#setup Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("space.gif")
wn.tracer(3)

#Draw border
mypen = turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.setposition(-300, -300) #Left Bottom
mypen.pendown()
mypen.pensize(3)
for side in range (4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

#Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)

#Creat the score variable
score = 0

#Create goals
maxGaols = 6
goals = []
for count in range(maxGaols):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))

#Set speed variable
speed = 1

#Define functions
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    if speed < 8:
        speed += 1

def decreasespeed():
    global speed
    if speed > 1:
        speed -= 1

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    return (d < 20)

#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")

while True:
    player.forward(speed)

    #Boundary checking
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)
        os.system("aplay bounce.mp3&")

    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)
        os.system("aplay bounce.mp3&")

    #Move the goal
    for count in range(maxGaols):
        goals[count].forward(2)

        #Goal checking
        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(180)
            os.system("aplay bounce.mp3&")

        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)
            os.system("aplay bounce.mp3&")

        #Collision checking
        if isCollision(player, goals[count]):
            goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
            goals[count].right(random.randint(0, 360))
            os.system("aplay collision.mp3&")
            score += 1

			#Draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring = "Score: %s" %score
            mypen.write(scorestring, False, align="left", font=("Arial",14, "normal"))

delay = raw_input("Press enter to finish.")