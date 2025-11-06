import turtle
t = turtle.Turtle() 

colors = ["red", "black", "blue"]
t.speed (10)
for i in range (10000):
    t.color ( colors[ i % 3 ] )
    t.forward (100 + i)
    t.left (120+1)

turtle.exitonclick()