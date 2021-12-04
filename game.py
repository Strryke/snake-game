from turtle import Turtle, Screen, screensize
import time
from random import randrange
from snake import Snake
from food import Food


vocab = ["Apple", "Banana", "Cherry"]
wordsindex = 0
charindex = 0
style = ("Courier", 30, "italic")
playing = True

screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.setup(height=1.0, width=1.0)

# bottom pause text
text = Turtle()
text.setpos(0, -500)
text.hideturtle()
text.color("white")
text.write("Press space to pause", align="center", font=style)


def top_spelling(word, charindex):
    spelling = Turtle()
    spelling.setpos(0, 400)
    spelling.color("white")
    spelling.hideturtle()
    spelling.write(word[0:charindex], align="center", font=style)
    return spelling


def word_list(word):
    idk = Turtle()
    idk.setpos(-700, -(wordsindex * 40))
    idk.color("yellow")
    idk.hideturtle()
    idk.write(word, align="left", font=style)


# wall creation (chewon)
def edge_drawing():
    edge = Turtle("square")
    edge.setpos(-500, -385)
    edge.pensize(10)
    edge.shapesize(0.3)
    edge.color("green")

    for i in range(2):
        edge.forward(1000)
        edge.left(90)
        edge.forward(780)
        edge.left(90)


# Returns a location away from the Snake
# Used to make food
def generate_rand():
    new_location = (randrange(200), randrange(200))
    if all(segment.distance(new_location) > 30 for segment in snake.segments):
        return new_location
    return generate_rand()


# Check collision with food
def eat_food(head, food):
    foody = abs(head.ycor() - (food.ycor() + 20))
    foodx = abs(head.xcor() - food.xcor())

    if foody < 20 and foody > 0 and foodx > 0 and foodx < 20:
        return True


# todo
def endgame():
    # clear turtles
    # display words completed
    # press space to restart
    pass


def switch_playstate():
    global playing
    playing = not playing


# shld have a start screen here? "press space to start"

# game start
snake = Snake()
word = vocab[0]
spelling = top_spelling(word, 0)
food = Food(generate_rand(), word[0])  # create first food
edge_drawing()

# Key bindings to "talk" to the screen
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(switch_playstate, "space")

# Game loop
while playing:
    screen.listen()
    screen.update()
    snake.move()

    if snake.collide():
        switch_playstate()
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
        spelling = top_spelling(word, charindex)  # see current word spelling at the top

    time.sleep(0.1)

while not playing:  # when game is paused (todo)
    screen.listen()
    screen.update()

screen.exitonclick()
