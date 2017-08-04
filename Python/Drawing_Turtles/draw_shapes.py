import turtle

def draw_shapes(shapes):
    window = turtle.Screen()
    window.bgcolor("pink")
    
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    
    if shapes == 'square':
        for x in range (0,4):
            brad.forward(100)
            brad.right(90)
            x=x+1
    if shapes == 'circle':
        brad.circle(100)

    if shapes == 'triangle':
        for y in range (0,3):
            brad.forward(60)
            brad.left(120)
            y=y+1

    window.exitonclick()
    
#draw_shapes('square')
#draw_shapes('circle')
draw_shapes('triangle')
        
