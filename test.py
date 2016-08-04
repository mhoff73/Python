from turtle import *

def pentagram (side_length):
    pencolor("red")
    pendown()
    fillcolor("black")
    begin_fill()
    for i in range(5):
        forward(side_length)
        right(144)
    end_fill()

pentagram(50)
