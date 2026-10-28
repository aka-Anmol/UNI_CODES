import turtle

t = turtle.Turtle()
t.speed(5)

#CONE
t.pendown()

t.color("saddlebrown")

t.begin_fill()
t.left(120)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.end_fill()


#Semi-circle
t.penup()
t.color("pink")
t.right(120)
t.forward(100)
t.right(30)

t.pendown()
t.begin_fill()
t.circle(-50,180)
t.end_fill()


###Cone
##t.penup()
##t.goto(-70, 0)
##t.pendown()
##
##t.color("saddlebrown")
##t.fillcolor("burlywood")
##
##t.begin_fill()
##t.goto(70, 0)
##t.goto(0, -200)
##t.goto(-70, 0)
##t.end_fill()
##
##t.penup()
##t.goto(-70, 0)
##t.setheading(0)
##t.pendown()
##
##t.color("pink")
##t.fillcolor("pink")
##t.begin_fill()
##
##t.forward(140)
##
##t.circle(90, 180)
##t.right(180)
##


"""


t.circle(70, 180)
t.end_fill()

t.hideturtle()

turtle.done()
"""
"""
#Ice cream semicircle
t.penup()
t.goto(-70, 0)
t.pendown()

t.color("pink")
t.fillcolor("pink")

t.begin_fill()
t.goto(70, 0)
t.circle(70, 180)
t.end_fill()

t.hideturtle()

turtle.done()
"""

"""import turtle

t = turtle.Turtle()
t.speed(5)

# Ice cream scoop
t.penup()
t.goto(0, 100)
t.pendown()
t.color("saddlebrown")
t.fillcolor("pink")

t.begin_fill()
t.circle(80)
t.end_fill()

# Move to the top of the cone
t.penup()
t.goto(-65, 20)
t.pendown()

# Ice cream cone
t.color("saddlebrown")
t.fillcolor("burlywood")

t.begin_fill()
t.goto(65, 20)
t.goto(0, -180)
t.goto(-65, 20)
t.end_fill()

# Cone pattern - diagonal lines
t.penup()
t.goto(-50, 15)
t.pendown()
t.goto(45, -125)

t.penup()
t.goto(-25, 20)
t.pendown()
t.goto(35, -160)

t.penup()
t.goto(0, 20)
t.pendown()
t.goto(20, -180)

t.penup()
t.goto(25, 20)
t.pendown()
t.goto(-20, -160)

t.penup()
t.goto(50, 15)
t.pendown()
t.goto(-35, -125)

# More diagonal lines in the other direction
t.penup()
t.goto(-45, -30)
t.pendown()
t.goto(35, 15)

t.penup()
t.goto(-35, -70)
t.pendown()
t.goto(50, -10)

t.penup()
t.goto(-20, -115)
t.pendown()
t.goto(35, -70)

t.hideturtle()

turtle.done()
"""
