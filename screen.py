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
        self.screen.screensize(1000, 1200)

    # wall creation (chewon)
    def edge_drawing(self):
        edge = Turtle("square")
        edge.up()
        edge.setpos(-350, -350)
        edge.down()
        edge.pensize(10)
        edge.shapesize(0.3)
        edge.color("green")

        for i in range(4):
            edge.forward(700)
            edge.left(90)

    def start_screen(self):
        text = Turtle()
        text.hideturtle()
        text.up()
        text.setpos(0, 0)
        text.color("white")
        text.write("")
        turtle.bgpic("welcome.gif")

    def reset_screen(self):
        turtle.clearscreen()
        self.__init__()
        self.word_list([])
        self.bottom_text()
        self.screen.update()

    def word_list(self, ls):
        text = Turtle()
        text.up()
        text.color("white")
        text.setpos(500, 200)
        text.write(
            "Completed Words:", align="center", font=("Verdana", 25, "underline")
        )
        text.hideturtle()

        for i in range(len(ls)):
            completedword = Turtle()
            completedword.up()
            completedword.color("white")
            completedword.setpos(450, 170 - (i * 20))
            completedword.hideturtle()
            completedword.write(
                f"{i+1}. {ls[i].capitalize()}", align="left", font=("Verdana", 20)
            )

    def bottom_text(self):
        # bottom pause text
        text = Turtle()
        text.up()
        text.setpos(0, -395)
        text.hideturtle()
        text.color("white")
        text.write("Press 'SPACE' to pause", align="center", font=style)

    def show_image(self, image):
        self.image = Turtle()
        self.image.up()
        self.image.setpos(-500, 200)
        self.screen.addshape(image)
        self.image.shape(image)

    def del_image(self):
        self.image.hideturtle()
