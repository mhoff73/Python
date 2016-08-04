from turtle import *

def draw_square (side_length, color):
    fillcolor(color)
    pendown()
    begin_fill()
    for i in range(4):
        forward(side_length)
        right(90)
    end_fill()
    penup()
    forward (side_length+10)

def draw_triangle (side_length, color):
    fillcolor(color)
    pendown()
    begin_fill()
    for i in range(3):
        forward(side_length)
        right(120)
    end_fill()
    penup()
    forward (side_length+10)

side_length = 50
for i in range(2):
    draw_square(side_length, "magenta")
    draw_square(side_length, "cyan")

goto(0,50)
for i in range(2):
    draw_triangle(side_length, "cyan")
    draw_triangle(side_length, "magenta")

