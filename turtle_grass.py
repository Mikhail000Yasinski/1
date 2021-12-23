import turtle as tl

screen = tl.Screen()
screen.bgcolor('Bisque')

def draw_fractal(size):
    tl.speed (10000000000)
    if size >= 5:
        tl.pensize(max(size / 40, 1))
        tl.forward(size)
        tl.right(35)
        draw_fractal(size / 2)
        tl.left(110)
        draw_fractal(size / 1.5)
        tl.right(75)
        tl.penup()
        tl.backward(size)
        tl.pendown()
        
        
    else:
        tl.pensize(1)
        tl.dot()
    
size = 200

tl.delay(1) 
tl.penup()
tl.color('ForestGreen')
tl.goto(0, -size * 2)
tl.setheading(75)
tl.pendown()

draw_fractal(size)

def draw_fractal(size):
    tl.speed (10000000000)
    if size >= 5:
        tl.pensize(max(size / 40, 1))
        tl.forward(size)
        tl.left(35)
        draw_fractal(size / 2)
        tl.right(110)
        draw_fractal(size / 1.5)
        tl.left(75)
        tl.penup()
        tl.backward(size)
        tl.pendown()
        
        
    else:
        tl.pensize(1)
        tl.dot()
    
size = 200

tl.delay(3) 
tl.penup()
tl.color('ForestGreen')
tl.goto(0, -size * 2)
tl.setheading(105)
tl.pendown()

draw_fractal(size)
tl.done()
