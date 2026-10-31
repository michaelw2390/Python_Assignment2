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

"""Thank you for submitting your code! Let's audit it according to the [CURRICULUM LOCKDOWN] rules and the current step: "Use a loop to draw a row of squares for a chessboard."

Here’s what I see:
- You have a loop that draws a square correctly.
- After finishing a square, you lift the pen (penup()), set the heading to 0, and move forward 100 units, which is good for moving to the right for the next square.
- However, after that, you have another block of code that draws another square (the four turtle.forward and turtle.right statements at the end of your loop). This means you are actually drawing a second square each time within the same iteration, resulting in twice as many squares per loop and incorrect positions.

You only need to draw one square per loop iteration and then move to the right, not draw a second square after moving.

Here’s a more direct hint:
- After you finish drawing the square and lift the pen, you only need to move forward by 100 (the width of a square) to get ready for the next square. You do not need to draw another square in the same iteration.
- Remove the second set of four turtle.forward/turtle.right lines.

Try removing the extra square-drawing code after turtle.penup() and just keep the movement to the right.

This was your 5th coding attempt for this step, so here's what the correct code should look like:

What do you think the next step should be?"""