# This file was created by: Antonio Santana 

'''
Goals - create images for paper and scissors
Write program so that user selects rock or paper or scissors when cliking on image...
'''

# import package
from random import randint
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os

print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the width and height for the window
WIDTH, HEIGHT = 1400, 800

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="black")



# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)

# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
# add the rock image as a shape
screen.addshape(rock_image)
# attach the rock_image to the rock_instance
rock_instance.shape(rock_image)
# remove the pen option from the rock_instance so it doesn't draw lines when moved
rock_instance.penup()
# assign vars for rock position
rock_pos_x = 0
rock_pos_y = 0

# set the position of the rock_instance
rock_instance.setpos(rock_pos_x,rock_pos_y)

# setup the rock image using the os module as rock_image
paper_image = os.path.join(images_folder, 'paper.gif')
# instantiate (create an instance of) the Turtle class for the rock
paper_instance = turtle.Turtle()
# add the rock image as a shape
screen.addshape(paper_image)
# attach the rock_image to the rock_instance
paper_instance.shape(paper_image)
# remove the pen option from the rock_instance so it doesn't draw lines when moved
paper_instance.penup()
# assign vars for rock position
paper_pos_x = 500
paper_pos_y = 0

# set the position of the rock_instance
paper_instance.setpos(paper_pos_x,paper_pos_y)





# setup the rock image using the os module as rock_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
# instantiate (create an instance of) the Turtle class for the rock
scissors_instance = turtle.Turtle()
# add the rock image as a shape
screen.addshape(scissors_image)
# attach the rock_image to the rock_instance
scissors_instance.shape(scissors_image)
# remove the pen option from the rock_instance so it doesn't draw lines when moved
scissors_instance.penup()
# assign vars for rock position
scissors_pos_x = -500
scissors_pos_y = 0

# set the position of the rock_instance
scissors_instance.setpos(scissors_pos_x,scissors_pos_y)

# instantiate a generic turtle
t = turtle.Turtle()
# instantiate a turtle for writing text
text = turtle.Turtle()
# Changes text color
text.color('grey')
text.hideturtle()

def writingpos (x,y, text):
    text.goto(x,y)
    text.write("text!", False, "left", ("Times New Roman", 36, "normal"))
# hide that turtle
t.hideturtle()

# function that passes through wn onlick
def someFunction(x, y):
    print("window geometry " + str(cv.winfo_geometry()))
    # screen.setup(WIDTH,HEIGHT,0,0)
    global playerchoice
    if x > -242 and y > -420 and x < 240 and y < 240:
        print("hitbox!")
        t.penup()
        t.goto(x, y)
        text.goto(x, y)
        # font is changed 
        text.write("rock!", False, "left", ("Times New Roman", 36, "normal"))
        playerchoice = "rock"
        # turtle.write(str(x)+","+str(y))
        # hides paper and scissors if rock is selected 
        paper_instance.hideturtle()
        scissors_instance.hideturtle()
        print(str(x)+","+str(y))
    else: 
        print("not hitbox")
        print(str(x)+","+str(y))
    
    print("window geometry " + str(cv.winfo_geometry()))
    # screen.setup(WIDTH,HEIGHT,0,0)
    if x > 257 and y > -134 and x < 700 and y < 138:
        print("hitbox!")
        text.goto(x, y)
        # changes font
        text.write("paper!", False, "left", ("Times New Roman", 36, "normal"))
        playerchoice = "paper"
        # turtle.write(str(x)+","+str(y))
        # hides rock and scissors if paper is selcted
        rock_instance.hideturtle()
        scissors_instance.hideturtle()
        print(str(x)+","+str(y))
    else: 
        print("not hitbox")
        print(str(x)+","+str(y))

    print("window geometry " + str(cv.winfo_geometry()))
    # screen.setup(WIDTH,HEIGHT,0,0)
    if x > -707 and y > -150 and x < -270 and y < 150:
        print("hitbox!")
        t.penup()
        t.goto(x, y)
        text.goto(x, y)
        # changes font
        text.write("scissors!", False, "left", ("Times New Roman", 36, "normal"))
        playerchoice = "scissors"
        # turtle.write(str(x)+","+str(y))
        # Hides rock and paper if scissors is selected 
        rock_instance.hideturtle()
        paper_instance.hideturtle()
        print(str(x)+","+str(y))
    else: 
        print("not hitbox")
        print(str(x)+","+str(y))
# onclick action runs function on turtle window using x and y coordinates
# https://docs.python.org/3/library/turtle.html#turtle.onclick

screen.onclick(someFunction)
# runs mainloop for Turtle - required to be last
screen.mainloop()

    
# String Variables 
p = "you have tied"
w = "you have won"
l = "you have lost"
rps_choices = ["rock","paper","scissors"]

#  This everything under is what will happen if "rps_game()" is run
# Asks the player their choice and asks for an input then decides the computers input
def rps_game():
    print("do you chose rock, paper, or scissors?")
   
    cpuchoice = rps_choices[randint(0,len(rps_choices)-1)] 
# group 1: Shows all the possible outcomes if player chooses rock and will print the results 

    if playerchoice == "rock":
        print ("p1 chose rock")
        if cpuchoice == "rock":
            print ("CPU chose rock") 
            print (p) #Using elif we tell the code that if it is not this move onto the next (el)if
            # text.write ("YOU HAVE TIED!", False, "left", ("Times New Roman", 36, "normal")) was my original attemot however I am unsure as to why it does not work.
            # I also attempted to display turtle images for each option however I could not debug the problem as they would flash to show up then dissapear.
          
        elif cpuchoice == "paper":
            print ("CPU chose paper") 
            print (l)
        elif cpuchoice == "scissors":
            print ("CPU chose scissors") 
            print (w) 
        

# group 2 Shows all the possible outcomes if player chooses paper and will print the results 
    elif playerchoice == "paper":
        print ("p1 chose paper")
        if cpuchoice == "rock":
            print ("CPU chose rock") 
            print (w)
        elif cpuchoice == "paper":
            print ("CPU chose paper") 
            print (p)
        elif cpuchoice == "scissors":
         print ("CPU chose scissors") 
         print (l)

        #  group 3 Shows all the possible outcomes if player chooses scissors and print the results
    elif playerchoice == "scissors":
        print ("p1 chose scissors")
        if cpuchoice == "rock":
            print ("CPU chose rock") 
            print (l)
        elif cpuchoice == "paper":
         print ("CPU chose paper") 
         print (w)
        elif cpuchoice == "scissors":
         print ("CPU chose scissors") 
         print (p)
# This will run all of the code above which is the game of rock paper scissors. 
rps_game ()

