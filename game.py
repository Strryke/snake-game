from time import sleep
from random import randrange

from snake import Snake
from food import Food, words
from screen import Window

# Returns a location away from the Snake
# Used to make food
def generate_rand(snake):
    new_location = (randrange(-300, 300, 20), randrange(-300, 300, 20))
    if all(segment.distance(new_location) > 100 for segment in snake.segments):
        return new_location
    return generate_rand(snake)


def switch_gamestate():
    global gaming, playing
    gaming = "gaming"
    playing = True


def switch_playstate():
    global playing
    playing = not playing


def key_binds(snake):
    window.screen.onkey(snake.up, "Up")
    window.screen.onkey(snake.down, "Down")
    window.screen.onkey(snake.left, "Left")
    window.screen.onkey(snake.right, "Right")
    window.screen.onkey(switch_playstate, "space")


# game start
def game_screen():
    window.reset_screen()

    global playing
    playing = True

    images_files = {
        "TORTOISE": "./assets/tortoise.gif",
        "HARE": "./assets/hare.gif",
        "RACE": "./assets/race.gif",
        "FINAL": "./assets/final.gif",
    }

    snake = Snake()
    key_binds(snake)
    window.edge_drawing()
    window.bottom_text()
    window.word_list([])

    wordsindex, charindex = 0, 0
    word = words[wordsindex]
    completedls = []

    spelling = window.top_spelling(word, 0)

    window.show_image(images_files[word])
    food = Food(generate_rand(snake), word[charindex])

    # Game loop
    while True:
        window.screen.listen()
        if playing == True:
            snake.move()

            if snake.collide():
                playing = False
                return "dead"

            elif snake.head.distance(food) < 25:
                snake.eat()  # creates new segments

                if charindex == len(word) - 1:  # finish spelling word
                    completedls.append(word)  # add completed word to list

                    if len(completedls) == len(words):  # finish word list
                        playing = False
                        window.word_list(completedls)
                        charindex += 1
                        window.screen.update()
                        return "win"
                    else:
                        window.word_list(completedls)  # update word list
                        wordsindex += 1
                        word = words[wordsindex]  # change word
                        window.del_image()
                        window.show_image(images_files[word])  # show new image
                        charindex = 0
                        food.new_food(
                            generate_rand(snake), word[charindex]
                        )  # generate next food

                else:
                    charindex += 1
                    food.new_food(
                        generate_rand(snake), word[charindex]
                    )  # generate next food

                spelling.clear()
                spelling = window.top_spelling(
                    word, charindex
                )  # see current word spelling at the top
        window.screen.update()
        sleep(0.1)


if __name__ == "__main__":
    gaming = "welcome"
    playing = False

    window = Window()
    window.screen.onkey(switch_gamestate, "Return")

    while True:
        window.screen.listen()

        if gaming == "welcome":
            window.start_screen()

        elif gaming == "dead" or gaming == "win":
            window.end_text(gaming)
            window.screen.onkey(switch_gamestate, "Return")

        else:
            gaming = game_screen()
