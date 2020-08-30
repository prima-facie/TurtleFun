import turtle
colors = ["blue", "red"]
myTurtle = turtle.Pen()
turtle.bgcolor("black")
myTurtle.speed(0)
for i in range(400):
    myTurtle.pencolor(colors[i % 2])
    myTurtle.width(i / 100)
    myTurtle.forward(i - 20)
    myTurtle.left(60)

turtle.done()
