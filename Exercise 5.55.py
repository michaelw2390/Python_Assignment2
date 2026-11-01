# (Turtle: chessboard) Write a program to draw a chessboard, as shown in
# Figure 5.6b.

import turtle

for row in range(0,9):


    turtle.pendown()
    turtle.forward(100)

    turtle.right(90)
    turtle.forward(100)

    turtle.right(90)
    turtle.forward(100)

    turtle.right(90)
    turtle.forward(100)

    turtle.penup()
    turtle.setheading(0)

    turtle.forward(100)

    for i in range(1,9):
        turtle.right(90)
        turtle.forward(100)









turtle.done()

