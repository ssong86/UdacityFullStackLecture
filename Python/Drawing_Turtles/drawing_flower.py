#drawing a flower
import turtle 


def draw_petal(flower_ob):
    flower_ob.penup()
    flower_ob.setpos(0,100)
    flower_ob.width(10)
    flower_ob.shape("arrow")
    flower_ob.color("yellow")
    flower_ob.pendown()
    #draw parallelogram
    for i in range(0,2):
        flower_ob.forward(100)
        flower_ob.right(60)
        flower_ob.forward(100)
        flower_ob.right(120)

def draw_stamen(flower_ob):
    #draw stamen with multiple circles
    flower_ob.setpos(0,0)
    flower_ob.width(10)
    flower_ob.color("brown")
    flower_ob.circle(100)

    flower_ob.penup()
    flower_ob.setpos(0,25)
    flower_ob.pendown()
    flower_ob.circle(75)

    flower_ob.penup()
    flower_ob.setpos(0,50)
    flower_ob.pendown()
    flower_ob.circle(50)

    flower_ob.penup()
    flower_ob.setpos(0,75)
    flower_ob.pendown()
    flower_ob.circle(25)

def draw_leaf(flower_ob):
    #draw a stalk and leafs
    flower_ob.penup()
    flower_ob.setpos(0,-72)
    flower_ob.pendown()
    flower_ob.color("green")
    flower_ob.right(90)
    flower_ob.forward(150)
    flower_ob.left(150)
    flower_ob.forward(100)
    flower_ob.right(60)
    flower_ob.forward(100)
    flower_ob.right(120)
    flower_ob.forward(100)
    flower_ob.right(60)
    flower_ob.forward(200)
    flower_ob.right(60)
    flower_ob.forward(100)
    flower_ob.right(120)
    flower_ob.forward(100)
    flower_ob.right(60)
    flower_ob.forward(100)

    
        

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("skyblue")

    myflower = turtle.Turtle()
    myflower.speed(10)
    
    for i in range(0,36):
        draw_petal(myflower)
        myflower.right(10)

    draw_stamen(myflower)
    draw_leaf(myflower)

    window.exitonclick()




draw_flower()
