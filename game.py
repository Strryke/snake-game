from turtle import Turtle, Screen, screensize
from time import sleep
from random import randrange
import turtle
from snake import Snake
from food import Food, words
from screen import Window

vocab = words
images_files={"TORTOISE":"tortoise.gif","HARE":'hare.gif',"RACE":'race.gif',"FINAL":'final.gif'}
completedls=[]
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


def word_list(x,ls):
    for i in range(len(ls)):
        completedword = Turtle()
        completedword.setpos(x, -(i * 40))
        completedword.color("yellow")
        completedword.hideturtle()
        completedword.write(ls[i], align="left", font=style)

def show_image(word):
    image=Turtle()
    image.up()
    image.setpos(-500,200)
    window.screen.addshape(images_files[word])
    image.shape(images_files[word])


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


def endgame(completedls,msg):
    window.reset_screen()
    word_list(0,completedls)

    show_image("FINAL") #not working :(

    text = Turtle()
    text.setpos(0, 200)
    text.hideturtle()
    text.color("white")
    text.write(f"{msg}\nClick anywhere to exit", align="center", font=style)
    switch_playstate()
    #window.screen.onkey(restart, "r")
    #window.screen.listen()

    window.screen.exitonclick()


def switch_playstate():
    global playing
    playing = not playing

'''
def restart():
    global playing, food, charindex
    window.reset()
    snake.__init__()
    playing = True
    charindex = 0
    key_binds()
    food = Food(generate_rand(), word[0])
    window.bottom_text()
'''

def key_binds():
    window.screen.onkey(snake.up, "Up")
    window.screen.onkey(snake.down, "Down")
    window.screen.onkey(snake.left, "Left")
    window.screen.onkey(snake.right, "Right")
    window.screen.onkey(switch_playstate, "space")
    #window.screen.onkey(restart, "r")


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

word = vocab[0]
show_image(word)
spelling = top_spelling(word, 0)

food = Food(generate_rand(), word[0])

key_binds()


# Game loop
while True:
    window.screen.listen()
    if playing == True:
        snake.move()

        if snake.collide():
            endgame(completedls,"GAME OVER")

        elif eat_food(snake.head, food):
            snake.eat()  # creates new segments
        
            if charindex == len(word) - 1:
                completedls.append(word)
                if len(completedls)==len(vocab):
                    endgame(completedls,"CONGRATULATIONS! YOU WIN!")
                else:
                    word_list(-400,completedls)
                    wordsindex += 1
                    word = vocab[wordsindex]
                    charindex = 0
                    food.new_food(generate_rand(), word[charindex])
                    show_image(word)

            else:
                charindex += 1
                food.new_food(generate_rand(), word[charindex])  # generate next food

            spelling.clear()
            spelling = top_spelling(
                word, charindex
            )  # see current word spelling at the top

    window.screen.update()
    sleep(0.1)
