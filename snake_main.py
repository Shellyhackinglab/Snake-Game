from turtle import Turtle, Screen
from snake_bar import Bar
from snake_food import Food
from snake_scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Invader Game")

bar = Bar()
food = Food()
scoreboard = Scoreboard()

#if bar.__init__().bar.distance(food) < 15:
#    food.refresh()
#    scoreboard.add_score()

screen.listen()
screen.onkey(bar.up, "Up")
screen.onkey(bar.down, "Down")
screen.onkey(bar.left, "Left")
screen.onkey(bar.right, "Right")

bar.move()

screen.exitonclick()
