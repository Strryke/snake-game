from turtle import Turtle
from time import sleep
from random import randrange
from snake import Snake
from food import Food, words
from screen import Window

vocab = words
images_files = {
    "TORTOISE": "tortoise.gif",
    "HARE": "hare.gif",
    "RACE": "race.gif",
    "FINAL": "final.gif",
}
completedls = []
wordsindex = 0
charindex = 0
style = ("Verdana", 30)
playing = True


def top_spelling(word, charindex):
    spelling = Turtle()
    spelling.up()
    spelling.setpos(0, 380)
    spelling.color("white")
    spelling.hideturtle()
    spelling.write(word[0:charindex], align="center", font=style)
    return spelling


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


def endgame(completedls, msg):
    switch_playstate()
    # window.show_image(images_files["FINAL"])
    # window.image.setpos(0, 0)
    text = Turtle()
    text.up()
    text.setpos(0, 200)
    text.hideturtle()
    text.color("White")
    text.write(f"{msg}\nPress 'R' to reset the game", align="center", font=style)


def switch_playstate():
    global playing
    playing = not playing


def restart():
    global playing, food, charindex
    window.reset_screen()
    snake.__init__()
    playing = True
    charindex = 0
    key_binds()
    food = Food(generate_rand(), word[0])
    window.bottom_text()
    window.show_image(images_files[word])
    window.update()


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

    window.start_screen()
    window.screen.onkey(start, "Return")
    window.screen.listen()

    if start == True:
        window.reset_screen()
        break


# game start
snake = Snake()
window.edge_drawing()
window.bottom_text()
window.word_list([])

word = vocab[0]
window.show_image(images_files[word])
spelling = top_spelling(word, 0)

food = Food(generate_rand(), word[0])

key_binds()


# Game loop
while True:
    window.screen.listen()
    if playing == True:
        snake.move()

        if snake.collide():
            endgame(completedls, "GAME OVER")

        elif eat_food(snake.head, food):
            snake.eat()  # creates new segments

            if charindex == len(word) - 1:
                completedls.append(word)
                if len(completedls) == len(vocab):
                    endgame(completedls, "CONGRATULATIONS! YOU WIN!")
                else:
                    window.word_list(completedls)
                    wordsindex += 1
                    word = vocab[wordsindex]
                    charindex = 0
                    food.new_food(generate_rand(), word[charindex])
                    window.del_image()
                    window.show_image(images_files[word])

            else:
                charindex += 1
                food.new_food(generate_rand(), word[charindex])  # generate next food

            spelling.clear()
            spelling = top_spelling(
                word, charindex
            )  # see current word spelling at the top

    window.screen.update()
    sleep(0.1)
