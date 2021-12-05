from turtle import Turtle
import random

style = ("Verdana", 30)

words = ["HARE", "TORTOISE", "RACE"]

colors = ["#C70039", "#FFC300", "#8E44AD", "#A3E4D7", "#FF00FF", "#99FF33"]


def random_color():
    return random.choice(colors)


class Food(Turtle):
    def __init__(self, location, ch):
        super().__init__()
        self.up()
        self.setposition((location[0] - 5, location[1] - 20))
        self.color(random_color())
        self.write(ch, align="center", font=style)
        self.setposition(location)
        self.hideturtle()

    def new_food(self, location, ch):
        self.clear()
        self.color(random_color())
        self.setposition((location[0] - 5, location[1] - 20))
        self.write(ch, align="center", font=style)
        self.setposition(location)
