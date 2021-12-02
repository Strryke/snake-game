from turtle import Turtle

class Food(Turtle):
    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.up()
        self.color("green")
        self.setposition(location)
        
    def new_food(self, location):
        self.setposition(location)
    
