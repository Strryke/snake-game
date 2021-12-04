from turtle import Screen, Turtle
import turtle

style = ("Verdana", 20)


class Window:
    def __init__(self):
        self.setup()
        self.edge_drawing()

    def setup(self):
        self.screen = Screen()
        self.screen.title("Snake Game")
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.setup(height=1.0, width=1.0)

    def start_screen(self):
        text = Turtle()
        text.hideturtle()
        text.up()
        text.setpos(0, 0)
        text.color("white")
        text.write("")
        turtle.bgpic("welcome.gif")

    # wall creation (chewon)
    def edge_drawing(self):
        edge = Turtle("square")
        edge.setpos(-350, -350)
        edge.pensize(10)
        edge.shapesize(0.3)
        edge.color("green")

        for i in range(4):
            edge.forward(700)
            edge.left(90)

    def reset(self):
        turtle.clearscreen()
        self.setup()
        self.edge_drawing()

    def bottom_text(self):
        # bottom pause text
        text = Turtle()
        text.up()
        text.setpos(0, -395)
        text.hideturtle()
        text.color("white")
        text.write("Press 'SPACE' to pause", align="center", font=style)
