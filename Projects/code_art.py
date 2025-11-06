# ###############################################
# ### SETUP ###
import turtle
# ###############################################

t = turtle.Turtle()
t.penup()
t.goto(-0, -0)
t.color("purple")
t.pendown()

for i in range (500):
    t.forward(i)
    t.left(45+i)




# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
