import turtle

window = turtle.Screen()


def thing(turtle):
    turtle.forward(100)
    turtle.right(65)
    turtle.forward(20)
    turtle.right(65)
    turtle.forward(20)
    turtle.right(65)
    turtle.forward(100)

def moreThings(turtle,numberThings):
    for number in range (0,numberThings):
        thing(turtle)


if __name__ == '__main__':
    myTurtle = turtle.Turtle()
    myTurtle.color("indigo")
    thing(myTurtle)
    moreThings(myTurtle,23)
    window.exitonclick()