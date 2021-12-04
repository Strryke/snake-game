from turtle import Turtle
style = ('Courier', 30, 'italic')

class Food(Turtle):
    def __init__(self, location,ch):
        super().__init__()
        self.setposition(location)
        self.color("green")
        self.write(ch,align='center', font = style)
        self.up()
        self.hideturtle()
        
    def new_food(self, location,ch):
        self.setposition(location)
        self.clear()
        self.write(ch, align='center', font = style)
