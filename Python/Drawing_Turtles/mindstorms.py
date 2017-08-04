import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("pink") # creates a drawing GUI with red background color

    brad = turtle.Turtle() # drawing module
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    x=0
    for x in range (0,4): # runs from 0 to 3 (4-1)
        brad.forward(100)
        brad.right(90)
        x = x+1

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    window.exitonclick()
draw_square()
