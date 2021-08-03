import turtle
wn = turtle.Screen()
wn.bgcolor("gray")
octa = turtle.Turtle()
octa.color("navy")
octa.pensize(10)

for i in range(7):
    octa.left(51.42)
    for i in range(7):
        octa.forward(100)
        octa.left(51.42)

