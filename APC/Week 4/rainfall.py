#output the charts for teh seasons
import turtle
t = turtle.Turtle()

#tuples for season and the size and color
bar = [
    (120, "green"),
    (80, "yellow"),
    (150, "orange"),
    (100, "blue")
]


#for the horizontal bar at the bottom
t.pendown()
t.goto(-220,0)
t.penup()

for height, colour in bar:
    
    
    #colouring in the bar
    t.fillcolor(colour)
    t.begin_fill()

    #drawing the bars outline
    t.pendown()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(height)

    #finishing the bar 
    t.right(90)
    t.forward(50)
    
    #finish colouring in the bar
    t.end_fill()

    #moving to the next bar
    t.left(180)
    t.forward(60)


    
