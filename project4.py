import turtle
t = turtle.Turtle() 
#different colors
colors = ["purple", "green", "red"]
t.speed (10)
for i in range (10000):
    #square instead of triangle
    t.color ( colors[ i % 3 ] )
    t.forward (10 + i)
    t.left (90+1)

turtle.exitonclick()