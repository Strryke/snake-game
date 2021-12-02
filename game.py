from turtle import Turtle, Screen
import time
from random import randrange
from snake import Snake
from food import Food

score = 0

# Screen setup
screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
text = Turtle()
text.setpos(-300,-200)
text.hideturtle()
text.color("white")
style = ('Courier', 30, 'italic')
text.write(f"Score {score}", font = style)

# Returns a location away from the Snake
# Used to make food
def generate_rand():
    new_location = (randrange(200), randrange(200))
    if all(segment.distance(new_location) > 30 for segment in snake.segments):
        return new_location
    return generate_rand()


# init snake
snake = Snake()
food = Food(generate_rand())

# Check collision with food 
def eat_food(head,food):
    global score
    if head.distance(food.pos()) < 20:
        score += 1
        text.clear()
        text.write(f"Score {score}", font = style)
        return True

# Key bindings to "talk" to the screen 
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()

# Todo
def endgame():
    global playing
    playing = False

# Game loop
playing = True
while playing:
    screen.update()
    snake.move()
    if snake.self_collide():
        endgame()
    elif eat_food(snake.head, food):
        snake.eat()
        food.new_food(generate_rand())
    time.sleep(0.1)

screen.exitonclick()