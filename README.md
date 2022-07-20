Built by Melvin, Chewon, Wei Ming, Gavin, Ad, Ashley

# Spelling With Snake
![image](https://user-images.githubusercontent.com/63138233/179952527-40764881-31e0-4af4-9ba8-38cdf929d0e9.png)
![image](https://user-images.githubusercontent.com/63138233/179952710-2a08e9cd-5798-40c9-aa41-64beac4e97e1.png)

### Background
We wanted to recreate our childhood game, Snake, for the younger generation to experience. Since children in this generation are often seen using electronic devices for visual entertainment, their exposure to the English language is limited and hence their learning curve for English is deteriorating. We hope to lessen the difficulty for them by creating a game that combines learning and fun together.

### Target Audience
This game is targeted at primary school children that are learning new words. Unlike the conventional way of doing spelling, this game is interactive in a way that there are pictures that give hints to them and move the snake to eat the letter. This helps to keep the children focused while learning new words. Through this game, it would not let the children feel that learning new words is a chore. In addition, the game is simple to play with and suitable for their age.

### Characteristics of target audience
They are energetic and are easily distracted thus they cannot focus on one activity. Usually foreducationalgames,theirattentionspanisveryshort. Learningnewwordsusing definitions bores them quickly and are unable to absorb new information as compared to using pictures. They are at the age whereby they are easily influenced by online platforms, thus the game without internet is safe for them to play.

### How the game might help
There are spelling tests and composition writings that upper primary students need to do. It is important for them to learn higher level of vocabulary words, since it is beneficial for their English PSLE.

Learning the spelling of new English words can be hard for most students. Current methods for learning spelling includes writing the words over and over again. Our game hopes to gamify the learning process, having a fun game to do so will motivate them to learn the words.

The students can use our program whenever they need to learn a new word before a spelling test or before an exam, helping them to memorise the spelling of a new word. Teachers can also use them to aid their teaching, especially in times of the pandemic when most of the learning are home-based.

## Main Features
- Image at the top left
- Spelling of words at the top
- Completed words at the side
- Start, pause, and restart of the game
- Snake gets longer
- Wall and self-collision
- Different end game messages, based on whether the user wins or loses.

# Documentation
This game is built using the turtle, time, random library. The bulk of the game utilises the turtle library to generate graphics.
The code is broken up into 4 parts – a main file and 3 classes (Food, Snake and Window) forming the core of the game.

## Main
The main game consists of various functions that generates random positions for the food, that changes the start of the game (with global variables playing and gaming) as well as the main game screen.

`generate_rand(snake)`
snake (object): to get the list of positions of the segments. 
Generates a random location within the frame for the letters to appear in. It also ensures that the location is not within any of the segments of the snake.


`switch_gamestate()` - 
Changes the state of the program to “gaming”, whenever the enter key is pressed

`switch_playstate()` - 
Called when the space bar is pressed, it changes the variable playing, allowing the user to pause the game and continue playing.

## Window
A class that sets up the basic elements required to introduce the players to our Snake Game.

`Window.__init__(self)` - 
Called when a window object is instantiated. Sets the screen up by giving it a title, a colour and the size.

`Window.edge_drawing()` -
(Takes in no parameters)
- Draws the frame of the screen with a green colour pen
- Creates a green coloured, square turtle object
- Starting from bottom left position (-350,-350)
- Creates a square using a for loop ,move forward by 700 before turning left, 4 times.

`Window.show_text(pos, msg)` -
pos (tuple): a 2-element tuple containing the x and y co-ordinate msg (string): the message to be displayed
Creates a turtle object assign it to text, followed by hiding it. Use the Turtle.write() method to display the text on the screen.

`Window.reset_screen()` - 
(Takes in no parameters)
Using the clearscreen() method from the TurtleScreen class to clear the screen. Called every time when the game is being played.

`Window.start_screen()` - 
(Takes in no parameters)
Displays welcome picture (containing the instructions).


## Food

`Food.__init__(location, ch)` - 
location (tuple): location to spawn the food
ch (string): a 1-character string to be displayed

`Food.new_food(location, ch)` - location (tuple): location to spawn the food
ch (string): a 1-character string to be displayed

`Snake__init__()` - 
Called when a new snake object is instantiated, creates a list called segments, calls the start_snake() method, and reassigns the colour of the first segment to orange.

`Snake.new_segment(position)`
position (tuple): the position to create the new segment
creates a new body segment by creating a white coloured square turtle object
