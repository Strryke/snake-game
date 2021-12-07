from turtle import Screen, Turtle
import turtle

style = ("verdana", 10)


class Window:
    def __init__(self):
        self.screen = Screen()
        self.screen.title("Snake Game")
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.setup(height=1.0, width=1.0)
        self.screen.screensize(1000, 1200)

    # wall creation
    def edge_drawing(self):
        edge = Turtle("square")
        edge.up()
        edge.setpos(-350, -350)
        edge.down()
        edge.pensize(10)
        edge.shapesize(0.3)
        edge.color("green")

        for i in range(4):
            edge.forward(705)
            edge.left(90)

    def show_text(self, pos, message):
        style = ("verdana", 25)
        text = Turtle()
        text.hideturtle()
        text.up()
        text.setpos(pos[0], pos[1])
        text.color("white")
        text.write(message, align="center", font=style)
        return text

    def reset_screen(self):
        turtle.clearscreen()
        self.__init__()
        self.screen.update()

    def start_screen(self):
        self.show_text((0, 0), "")
        turtle.bgpic("welcome.gif")

    def end_text(self, msg):
        if msg == "win":
            self.show_text(
                (0, 200), "Congratulations! You won!\n\n Press 'Enter' to restart! :)"
            )
        if msg == "dead":
            self.show_text((0, 200), ":( You died!\n\n Press 'Enter' to restart! :)")

    def word_list(self, ls):
        self.show_text((500, 200), "Completed Words:")

        for i in range(len(ls)):
            self.show_text((500, 170 - (i * 25)), f"{i+1}. {ls[i].capitalize()}")

    def top_spelling(self, word, charindex):
        return self.show_text((0, 380), word[0:charindex])

    def bottom_text(self):
        self.show_text((0, -395), "Press 'SPACE' to pause")

    ###
    def show_image(self, image):
        self.image = Turtle()
        self.image.up()
        self.image.setpos(-500, 200)
        self.screen.addshape(image)
        self.image.shape(image)

    def del_image(self):
        self.image.hideturtle()
