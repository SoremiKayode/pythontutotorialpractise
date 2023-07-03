import turtle
import time
import random
draw = turtle.Turtle()
turtle.colormode(255)
draw.width(5)
turtle.shape("circle")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

for x in range(100):
    pos1 = random.randrange(-100, 200)
    pos2 = random.randrange(-200, 200)
    col1 = random.randrange(0, 200)
    col2 = random.randrange(0, 200)
    col3 = random.randint(0, 200)
    draw.color((col1, col2, col3), (col3, col1, col2))
    draw.penup()
    draw.begin_fill()
    draw.setpos((pos1, pos2))
    draw.pendown()
    draw.circle(30)

    draw.end_fill()

time.sleep(10)

