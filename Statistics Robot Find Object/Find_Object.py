#imports a libraries to be used in the project
import inspect
import pickle
import random
import turtle
import time
import argparse
bag = turtle.Turtle()
targetx, targety = random.randint(1, 10), random.randint(1, 10)
t = turtle.Turtle()
#function in order to draw the bag that will be used in the project that the robot has to escape
#this is done by creating a shape for the turtle and then creating a pen to draw the bag around the turtle shape
def draw_bag(rows=10, cols=10, cellsize=7):
    bag.shape('turtle')
    bag.pen(pencolor='brown', pensize=5)
    bag.penup()
    bag.goto(-35, 35)
    bag.pendown()
    bag.right(90)
    bag.forward(70)
    bag.left(90)
    bag.forward(70)
    bag.left(90)
    bag.forward(70)
    bag.left(90)
    bag.forward(70)
    bag.left(180)

    for row in range(rows):
        bag.penup()
        bag.goto(-35, 35 - row*(cellsize))
        bag.pendown()
        bag.forward(70)

    bag.right(90)
    for col in range(cols):
        bag.penup()
        bag.goto(-35 + col*(cellsize), 35)
        bag.pendown()
        bag.forward(70)


    object_width = 5

    bag.pencolor('blue')

    bag.penup()
    bag.goto(-35 + (targetx*cellsize) - (cellsize/2) - (object_width/2), 35 - (targety*cellsize) + (cellsize/2) + (object_width/2))
    bag.pendown()

    bag.fillcolor('blue')
    bag.begin_fill()
    for i in range(4):
        bag.forward(object_width)
        bag.left(90)
    bag.end_fill()

    bag.hideturtle()

def find_rand_number_sequentially():
    t.penup()
    triesx, triesy = 1, 1
    t.goto(-35 + triesx*7 - 7/2, 35 - triesy*7 + 7/2)
    t.pendown()
    turnright = False
    while triesy < targety:
        while triesx < targetx:
            triesx = triesx +1
            t.forward(7)
            if triesx is targetx:
                turnright = True
        triesy = triesy + 1

        if turnright:
            t.right(90)
            turnright = False
        t.forward(7)
    time.sleep(2.5)
    t.clear()

def find_rand_number_randomly():
    t.penup()
    triesx, triesy = 1, 1
    t.goto(-35 + triesx*7 - 7/2, 35 - triesy*7 + 7/2)
    t.pendown()
    turnright = False
    while triesy != targety:
        while triesx != targetx:
            triesx = random.randint(1, 10)
            t.goto(-35 + triesx*7 - 7/2, 35 - triesy*7 + 7/2)
            if triesx is targetx:
                turnright = True
        triesy = random.randint(1,10)

        if turnright:
            t.right(90)
            turnright = False
        t.goto(-35 + triesx * 7 - 7 / 2, 35 - triesy * 7 - 7 / 2)
    time.sleep(2.5)
    t.clear()

def find_rand_number_using_binary():
    t.penup()
    triesx, triesy = int, int
    rowsmin, colsmin = 0, 0
    rowsmax, colsmax = 10, 10
    triesx = ((rowsmax - rowsmin)/2 + rowsmin)
    triesy = ((colsmax - colsmin)/2 + colsmin)
    t.goto(-35 + triesx * 7 - 7 / 2, 35 - triesy * 7 + 7 / 2)
    t.pendown()

    turnright = False

    while triesx != targetx:
        if triesx > targetx:
            rowsmax = triesx - 1
        if triesx < targetx:
            rowsmin = triesx + 1
        triesx = ((rowsmax - rowsmin)/2) + rowsmin
        t.goto(-35 + triesx*7 - 7/2, 35 - triesy*7 + 7/2)
        if triesx is targetx:
            turnright = True
    while triesy != targety:
        if turnright:
            t.right(90)
            turnright = False
        if triesy > targety:
            colsmax = triesy - 1
        if triesy < targety:
            colsmin = triesy + 1
        triesy = ((colsmax - colsmin)/2 + colsmin)
        t.goto(-35 + triesx * 7 - 7 / 2, 35 - triesy * 7 - 7 / 2)
    time.sleep(2.5)
    t.clear()

#function that creates the gui used and then gives the option of what function to run depending on what is input
#then it runs the called function in order to draw the bag and then run the function
#if it can not find what is being called it throws in an error and then has the program print for help and what the probelm is
if __name__ == '__main__':
    turtle.setworldcoordinates(-70., -70., 70., 70.)

    draw_bag()
    find_rand_number_sequentially()
    find_rand_number_randomly()
    find_rand_number_using_binary()

    turtle.mainloop()