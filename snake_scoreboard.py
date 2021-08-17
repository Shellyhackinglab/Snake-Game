from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("yellow")
        self.speed(0)
        self.refresh()      

    def refresh(self):
        random_x = random.randint(-200,200) 
        random_y = random.randint(-200,200)
        self.goto(random_x,random_y)