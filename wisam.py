import turtle

wissam = turtle.Turtle()
zouidi = turtle.Screen()

zouidi.bgcolor('black')
wissam.hideturtle()
wissam.goto(0,-10)

wissam.pensize(3)
wissam.color('red')
wissam.begin_fill()
wissam.left(140)
wissam.forward(180)
wissam.circle(-90,200)
wissam.setheading(60)
wissam.circle(-90,200)
wissam.forward(178)
wissam.end_fill()

wissam.penup()
wissam.goto(-75,130)
wissam.pendown()
wissam.color('white')
wissam.write("Love You",font=("Calibri",30,"bold"))

wissam.penup()
wissam.goto(-180,-50)
wissam.pendown()
wissam.color('white')
wissam.write("Programming By Wissam Zouidi",font=("Calibri",20,"bold"))

turtle.done()