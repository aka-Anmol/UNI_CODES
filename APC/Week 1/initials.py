import turtle

#set up reference to the turtle and the screen
anm = turtle.Turtle()
screen = turtle.Screen()

#set the screen background colour and title
screen.bgcolor("white")

#letter A
anm.pencolor("orange")
anm.penup()
anm.goto(-100, -50)
anm.pendown()

anm.goto(-50, 50)
anm.goto(0, -50)

anm.penup()   #to draw the middle part of the A
anm.goto(-25,0)
anm.pendown()

anm.goto(-75,0)
anm.penup()

#Letter K
anm.pencolor("blue")
anm.goto(50,-50)
anm.pendown()

anm.goto(50,50)

anm.penup()
anm.goto(50,0)
anm.pendown()
anm.goto(100,50)
anm.penup()
anm.goto(50,0)
anm.pendown()
anm.goto(100,-50)


