import turtle
wn = turtle.Screen()
wn.bgcolor("black")
sqar = turtle.Turtle()
sqar.color("yellow")
sqar.pensize(10)

for i in range(4):
    sqar.left(90)
    for i in range(4):
        sqar.forward(100)
        sqar.left(90)

hideturtle()
