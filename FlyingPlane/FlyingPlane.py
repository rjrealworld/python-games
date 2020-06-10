import turtle
import math
import random
import pygame

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
player.color("lightblue")
player.shape("turtle")
player.penup()
player.speed(0)

#Creat the score variable
score = 0

#Create goals
maxGoals = 6
goals = []
for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))

#Create enemies
maxEnemies = 2
enemies = []
for count in range(maxEnemies):
    enemies.append(turtle.Turtle())
    enemies[count].color("green")
    enemies[count].shape("circle")
    enemies[count].penup()
    enemies[count].speed(0)
    enemies[count].setposition(random.randint(-300, 300), random.randint(-300, 300))

#Set speed variable
speed = 1

#Sound
pygame.init()
bounce_sound = pygame.mixer.Sound("bounce1.wav")
def bounce():
    pygame.mixer.Sound.play(bounce_sound)

pygame.mixer.music.load("Mission - AShamaluevMusic.mp3") 
pygame.mixer.music.play(-1, 0.0) #-1 means music will go on infinitely

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

def scoreBoard():
    mypen.undo()
    mypen.penup()
    mypen.hideturtle()
    mypen.setposition(-180, -30)
    scorestring = "Use arrows to control.\nPress q to exit." 
    mypen.write(scorestring, False, align="left", font=("Arial",30, "normal"))
    wn.tracer()
    turtle.listen()

def endGame():
    wn.bye()

def gameOver():
    player.hideturtle()
    for count in range(maxGoals):
        goals[count].hideturtle()
    for count in range(maxEnemies):
        enemies[count].hideturtle()
    mypen.undo()
    mypen.penup()
    mypen.hideturtle()
    mypen.setposition(-55, -15)
    scorestring = "Score: %s\n"%score 
    write = mypen.write(scorestring, False, align="left", font=("Arial",30, "normal"))
    turtle.ontimer(write, 5000)

#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")
turtle.onkey(scoreBoard, "Return")
turtle.onkey(endGame, "q")

while True:
    player.forward(speed)

    #Boundary checking
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)

    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)

    #Move the enemies
    for count in range(maxEnemies):
        enemies[count].forward(2)

        #Enemy checking
        if enemies[count].xcor() > 290 or enemies[count].xcor() < -290:
            enemies[count].right(180)

        if enemies[count].ycor() > 290 or enemies[count].ycor() < -290:
            enemies[count].right(180)

        if isCollision(player, enemies[count]):
            bounce()
            gameOver()
            quit()

    #Move the goal
    for count in range(maxGoals):
        goals[count].forward(2)

        #Goal checking
        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(180)

        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)

        #Collision checking
        if isCollision(player, goals[count]):
            goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
            goals[count].right(random.randint(0, 360))
            bounce()
            score += 1

			#Draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring = "Score: %s\tPress Enter for help" %score
            mypen.write(scorestring, False, align="left", font=("Arial",14, "normal"))

delay = raw_input("Press q to finish.")
