import turtle
wn = turtle.Screen()
wn.bgcolor("red")
octa = turtle.Turtle()
octa.color("lime")
octa.pensize(10)

for i in range(8):
    octa.left(45)
    for i in range(8):
        octa.forward(100)
        octa.left(45)

hideturtle()
