import turtle

myTurtle = turtle.Turtle()
s = turtle.Screen()
myTurtle.shape("square")
s.bgcolor("black")
myTurtle.pencolor("white")
a = 0
b = 0
myTurtle.speed(0)
myTurtle.penup()
myTurtle.goto(0, 200)
myTurtle.pendown()
while True:
    myTurtle.forward(a)
    myTurtle.right(b)
    a = a + 3
    b = b + 1
    if b == 200:
        break

    myTurtle.hideturtle()

turtle.done()
