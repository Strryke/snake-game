from turtle import Turtle, Screen, screensize
from time import sleep
from random import randrange
import turtle
from snake import Snake
from food import Food, words
from screen import Window

vocab = words
wordsindex = 0
charindex = 0
style = ("Verdana", 30)
playing = True


def top_spelling(word, charindex):
    spelling = Turtle()
    spelling.up()
    spelling.setpos(0, 400)
    spelling.color("white")
    spelling.hideturtle()
    spelling.write(word[0:charindex], align="center", font=style)
    return spelling


def word_list(word):
    idk = Turtle()
    idk.setpos(-450, -(wordsindex * 40))
    idk.color("yellow")
    idk.hideturtle()
    idk.write(word, align="left", font=style)


# Returns a location away from the Snake
# Used to make food
def generate_rand():
    new_location = (randrange(-300, 300, 20), randrange(-300, 300, 20))
    if all(segment.distance(new_location) > 100 for segment in snake.segments):
        return new_location
    return generate_rand()


# Check collision with food
def eat_food(head, food):
    if head.distance(food) < 25:
        return True


def endgame():
    text = Turtle()
    text.setpos(0, 0)
    text.hideturtle()
    text.color("white")
    text.write("GAME OVER\nPress 'R' to restart!", align="center", font=style)
    switch_playstate()


def switch_playstate():
    global playing
    playing = not playing


def restart():
    global playing, food, charindex
    window.reset()
    snake.__init__()
    playing = True
    charindex = 0
    key_binds()
    food = Food(generate_rand(), word[0])
    window.bottom_text()


def key_binds():
    window.screen.onkey(snake.up, "Up")
    window.screen.onkey(snake.down, "Down")
    window.screen.onkey(snake.left, "Left")
    window.screen.onkey(snake.right, "Right")
    window.screen.onkey(switch_playstate, "space")
    window.screen.onkey(restart, "r")


window = Window()

while True:
    start = False

    def start():
        global start
        start = True

    # turtle.bgpic("welcome.gif")

    window.start_screen()
    window.screen.onkey(start, "Return")
    window.screen.listen()
    if start == True:
        window.reset()
        window.bottom_text()
        break


# game start
snake = Snake()
word = vocab[0]
spelling = top_spelling(word, 0)
food = Food(generate_rand(), word[0])
key_binds()


# Game loop
while True:
    window.screen.listen()
    if playing == True:
        snake.move()

        if snake.collide():
            endgame()

        elif eat_food(snake.head, food):
            snake.eat()  # creates new segments

            if charindex == len(word) - 1:
                word_list(word)
                wordsindex += 1
                word = vocab[wordsindex]
                charindex = 0
                food.new_food(generate_rand(), word[charindex])
            else:
                charindex += 1
                food.new_food(generate_rand(), word[charindex])  # generate next food

            spelling.clear()
            spelling = top_spelling(
                word, charindex
            )  # see current word spelling at the top

    window.screen.update()
    sleep(0.1)


window.screen.exitonclick()
