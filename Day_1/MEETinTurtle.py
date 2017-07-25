import turtle
#
#
#
#
#
#Everything that comes after the # is a
#comment.
#It is a note to the person reading the code.
#The computer ignores it.
#Write your code below here...
# ...and end it before the next line.


turtle.penup()
#Pick up the pen so it doesn’t
#draw
turtle.goto(-200,-100)
#Move the turtle to the
#position (-200, -100)
#on the screen
turtle.pendown()
#Put the pen down to start
#drawing
#Draw the M:
turtle.goto(-200,-100+200)
turtle.goto(-200+50,-100)
turtle.goto(-200+100,-100+200)
turtle.goto(-200+100,-100)

turtle.penup()
turtle.goto(-50,-100)
turtle.pendown()
turtle.goto(-50+75,-100)
turtle.penup()
turtle.goto (-50,-100)
turtle.pendown()
turtle.goto(-50,-100+200)
turtle.goto(-50+75,100)
turtle.penup()
turtle.goto(-50,0)
turtle.pendown()
turtle.goto(-50+75,-100+100)

turtle.penup()
turtle.goto(125,-100)
turtle.pendown()
turtle.goto(125+75,-100)
turtle.penup()
turtle.goto (125,-100)
turtle.pendown()
turtle.goto(125,-100+200)
turtle.goto(125+75,-100+200)
turtle.penup()
turtle.goto(125,0)
turtle.pendown()
turtle.goto(125+75,-100+100)

turtle.mainloop()
