# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")

def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)

def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x,y)
    window.update()
    return sprite

def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)

def draw_rectangle( color="black",x=0,y=0, width=100, height=100,):
	sprite = turtle.Turtle()
	sprite.speed(0)
	sprite.pencolor(color)
	sprite.color(color)
	sprite.penup()
	sprite.goto(x - (width*0.5), y + (height*0.5))
	sprite.pendown()
	sprite.begin_fill()
	for i in range(2):
		sprite.forward(width)
		sprite.right(90)
		sprite.forward(height)
		sprite.right(90)
	sprite.end_fill()
	sprite.hideturtle()


window = turtle.Screen()
window.tracer(0)



######################################################################
# https://en.wikipedia.org/wiki/Web_colors#Extended_colors
# Section 2 - Your code
#this is my backround because i am american
set_background("Merica")
#theese are my rectangles red white blue yellow 
draw_rectangle("red", 100, 100, 200, 200)
draw_rectangle("white", -100, 100, 200, 200)
draw_rectangle("blue", 100, -100, 200, 200)
draw_rectangle("yellow", -100, -100, 200, 200)
# my sprites relate to my hobbies and personality
s1 = create_sprite("Eagle2", 100, 100)
s2 = create_sprite("Waterpolo", -100, -100)
s3 = create_sprite("card", 100, -100)
# theese are my words my name and my counrty 
message1 = create_sprite("alien",-200,200)
message1.color("red")
message1.write("Holler",font = ("bold", 40, "normal"))
message1.hideturtle()

message1 = create_sprite("ribs",-100,50)
message1.color("blue")
message1.write("america",font = ("Arial", 40, "normal"))

######################################################################


# Section 3 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()