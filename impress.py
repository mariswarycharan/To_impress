from cgitb import text
import turtle
#name = input("enter your crush name :")
a = turtle.Turtle()
b = turtle.Screen()
b.bgcolor("purple")

a.hideturtle()
#a.speed(0)

a.begin_fill()
a.fillcolor("red")
a.right(90)

a.up()
a.forward(190)
a.down()

a.left(90)
a.left(45)
a.forward(200)
a.circle(150,180)
a.right(90)
a.circle(150,180)
a.forward(300)
a.left(90)
a.forward(300)


a.end_fill()


a.up()
a.forward(250)
a.left(45)
a.forward(50)
a.right(60)

a.down()

a.begin_fill()

a.fillcolor("black")
a.forward(-350)
a.left(90)
a.forward(5)
a.right(90)
a.forward(350)
a.left(90)
a.forward(10)
a.right(135)
a.forward(15)
a.right(90)
a.forward(15)
a.right(120)
a.forward(8)

a.end_fill()

a.right(105)
a.forward(-200)


a.up()
a.forward(-405)
a.down()

a.begin_fill()

a.forward(-250)
a.left(90)
a.forward(5)
a.right(90)
a.forward(250)

a.end_fill()

a.left(60)

a.up()
a.forward(210)
a.right(90)
a.forward(150)
a.down()

a.write( "I        LOVE     YOU ", font=("ALGERIAN",40),align="center")

a.up()
a.right(90)
a.forward(100)
a.left(90)
a.down()

# a.write("Hai",font=("ALGERIAN",35),align="center")

a.up()
a.right(90)
a.forward(50)
a.left(90)
a.down()

a.write("",font=("ALGERIAN",25),align="center")

a.up()
a.right(90)
a.forward(50)
a.left(90)
a.down()

# a.write("Hai",font=("ALGERIAN",35),align="center")










turtle.mainloop()
