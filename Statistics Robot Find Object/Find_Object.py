#imports a librarie to be used in the project
import inspect
import pickle
import random
import turtle
import argparse
bag = turtle.Turtle()
chosennumber = random_target_number(targetnumber)
#function in order to draw the bag that will be used in the project that the robot has to escape
#this is done by creating a shape for the turtle and then creating a pen to draw the bag around the turtle shape
def draw_bag():
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
    bag.hideturtle()

def random_target_number():
    targetnumber = random.randrange(1, 100)
    return targetnumber

def find_rand_number_sequentially():
    targetnumber = chosennumber
    triestogetnumber = 0
    while triestogetnumber < targetnumber:
        triestogetnumber = triestogetnumber +1
    print('It took ' + triestogetnumber + ' to find the target number of ' + targetnumber)

def find_rand_number_randomly():
    targetnumber = chosennumber
    triestogetnumber = 0
    randnumber = random.randrange(1, 100)
    while randnumber != targetnumber:
        triestogetnumber = triestogetnumber +1
        randnumber = random.randrange(1, 100)
    print(' It took ' + triestogetnumber + ' to find the target number of ' + targetnumber)

def find_rand_number_using_binary():
    targetnumber = chosennumber
    triestogetnumber = 0
    highnumber = 100
    lownumber = 1
    binarynumber = 100/2
    while binarynumber != targetnumber:
        triestogetnumber = triestogetnumber +1
        if binarynumber > targetnumber:
            lownumber = binarynumber
        if binarynumber < targetnumber:
            highnumber = binarynumber
        binarynumber = (highnumber/2) + lownumber
    print('It took ' + triestogetnumber + 'to find the target number of ' + targetnumber)



#function that creates the gui used and then gives the option of what function to run depending on what is input
#then it runs the called function in order to draw the bag and then run the function
#if it can not find what is being called it throws in an error and then has the program print for help and what the probelm is
if __name__ == '__main__':