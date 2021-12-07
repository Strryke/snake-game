import turtle
import time
from random import randrange, choices

START = [(0, 0), (-20, 0), (-40, 0)]

# Snake setup
class Snake:
    def __init__(self):
        self.segments = []
        self.start_snake()
        self.head = self.segments[0]
        self.head.color("orange")

    def new_segment(self, position):
        new = turtle.Turtle("square")
        new.up()
        new.color("white")
        new.goto(position)
        self.segments.append(new)

    # Initialisation of snake (3 squares)
    def start_snake(self):
        for position in START:
            self.new_segment(position)

    def collide(self):
        # self collide
        for segment in self.segments[1:]:
            if self.head.distance(segment.pos()) < 10:
                return True

        # wall collision
        if (
            self.head.ycor() <= -330
            or self.head.ycor() >= 330
            or self.head.xcor() <= -340
            or self.head.xcor() >= 340
        ):
            return True

    # Movement of snake. Last part will go to 2nd last part,
    # 2nd last part goes to 3rd last
    # Head moves last
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].setpos(self.segments[i - 1].pos())
        self.head.forward(20)

    # Adds a new square to the position of the last segment
    def eat(self):
        position = self.segments[-1].pos()
        self.new_segment(position)

    # Key bindings
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
