import turtle

#set up references to the turtle and screen
bar = turtle.Turtle()
screen = turtle.Screen()

#set screen background color and title
screen.bgcolor("black")

#draw orange planet
bar.pencolor("orange")
bar.begin_fill()
bar.circle(28)
bar.fillcolor("orange")
bar.end_fill()
bar.penup()


#move to start of grey planet
bar.right(104)
bar.forward(30)
bar.left(20)

#draw grey planet
bar.pendown()
bar.pencolor("gray")#note American spellings
bar.begin_fill()
bar.circle(12)
bar.fillcolor("gray")
bar.end_fill()
bar.penup()

#move to start of red planet
bar.right(17)
bar.forward(50)
bar.left(5)

#draw planet
bar.pendown()
bar.color("red")
bar.begin_fill()
bar.circle(25)
bar.end_fill()
bar.penup()


#move to start of green planet
bar.right(-9)
bar.forward(77)
bar.left(26)

#draw green planet
bar.color("green")
bar.begin_fill()
bar.circle(22)
bar.end_fill()

#hide turtle
bar.hideturtle()

#leave window open
turtle.done()
