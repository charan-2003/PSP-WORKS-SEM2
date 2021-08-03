import turtle
wn = turtle.Screen()
wn.bgcolor("indigo")
hexa = turtle.Turtle()
hexa.color("cyan")
hexa.pensize(10)

for i in range(6):
    hexa.left(60)
    for i in range(6):
        hexa.forward(100)
        hexa.left(60)

hideturtle()
